"""GitHub 專案來源抓取：GitHub API 搜尋、repo 詳情、README、paper link 偵測。"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any
from urllib.parse import quote, quote_plus

from config import GITHUB_TOKEN, REPO_HTTP_TIMEOUT, REPO_MAX_BYTES, REPO_ROBOTS_CHECK
from collectors.news_http import SafeHttpFetcher
from collectors.repo_parse import (
    RepoCandidate,
    build_repo_sections,
    clean_readme,
    decode_readme_content,
    extract_paper_urls,
    parse_github_repo_json,
)

GITHUB_API = "https://api.github.com"
RAW_GITHUB = "https://raw.githubusercontent.com"


@dataclass
class SourceStats:
    name: str
    found: int = 0
    fetched: int = 0
    errors: int = 0
    error: str = ""


class RepoSources:
    def __init__(
        self,
        *,
        fetcher: SafeHttpFetcher | None = None,
        token: str | None = None,
        robots_check: bool = REPO_ROBOTS_CHECK,
    ) -> None:
        self.fetcher = fetcher or SafeHttpFetcher(timeout=REPO_HTTP_TIMEOUT, max_bytes=REPO_MAX_BYTES)
        self.token = token if token is not None else GITHUB_TOKEN
        self.robots_check = robots_check
        self.last_error = ""

    def _headers(self, accept: str = "application/vnd.github+json") -> dict[str, str]:
        headers = {
            "Accept": accept,
            "User-Agent": "DailyAIReportBot/2.0",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _get_json(self, url: str, stats: SourceStats, *, check_robots: bool = False) -> dict | list | None:
        headers = self._headers()
        result = self.fetcher.fetch(url, check_robots=check_robots, headers=headers)
        # Fallback: env token may be expired/invalid; retry once without auth for public data.
        if not result.ok and self.token and result.status in {401, 403}:
            anon_headers = dict(headers)
            anon_headers.pop("Authorization", None)
            retry = self.fetcher.fetch(url, check_robots=check_robots, headers=anon_headers)
            if retry.ok:
                result = retry
                stats.error = f"auth_fallback:{result.status or 200}"
            else:
                if retry.status in {403, 429} or "rate limit" in str(retry.error or "").lower():
                    stats.error = (stats.error or "") + "|github_rate_limited"
        if (not result.ok) and (result.status in {403, 429} or "rate limit" in str(result.error or "").lower()):
            stats.error = (stats.error or "") + "|github_rate_limited"
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            self.last_error = stats.error
            return None
        stats.fetched += 1
        try:
            return json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            stats.errors += 1
            stats.error = "json_decode_error"
            return None

    def search_repos(
        self,
        query: str,
        *,
        per_page: int = 20,
        pushed_after: str = "",
        min_stars: int = 0,
    ) -> tuple[list[RepoCandidate], SourceStats]:
        stats = SourceStats("github_search")
        q = query.strip()
        if pushed_after:
            q = f"{q} pushed:>{pushed_after}"
        if min_stars > 0:
            q = f"{q} stars:>={min_stars}"
        url = f"{GITHUB_API}/search/repositories?q={quote_plus(q)}&sort=updated&order=desc&per_page={max(1, min(per_page, 50))}"
        data = self._get_json(url, stats, check_robots=False)
        if not isinstance(data, dict):
            return [], stats
        items = data.get("items") or []
        repos: list[RepoCandidate] = []
        for item in items:
            repo = parse_github_repo_json(item)
            if repo and not (repo.extra or {}).get("archived"):
                repos.append(repo)
        stats.found = len(repos)
        return repos, stats

    def get_repo(self, full_name: str) -> RepoCandidate | None:
        stats = SourceStats("github_repo")
        owner_repo = "/".join(part.strip("/") for part in full_name.split("/", 1))
        url = f"{GITHUB_API}/repos/{owner_repo}"
        data = self._get_json(url, stats, check_robots=False)
        if not isinstance(data, dict):
            return None
        repo = parse_github_repo_json(data)
        return repo

    def fetch_readme(self, repo: RepoCandidate) -> str:
        # 優先 GitHub API（含 base64），fallback raw
        stats = SourceStats("github_readme")
        owner_repo = repo.full_name
        api_url = f"{GITHUB_API}/repos/{owner_repo}/readme"
        data = self._get_json(api_url, stats, check_robots=False)
        if isinstance(data, dict) and data.get("content"):
            text = decode_readme_content(data)
            if text.strip():
                return text

        # fallback raw
        branch = repo.default_branch or "main"
        for name in ("README.md", "README.MD", "readme.md", "README.rst", "README.txt", "README"):
            raw_url = f"{RAW_GITHUB}/{owner_repo}/{quote(branch)}/{name}"
            result = self.fetcher.fetch(raw_url, check_robots=False)
            if result.ok and result.content:
                return result.content.decode("utf-8", errors="replace")
        return ""

    def enrich_repo(self, repo: RepoCandidate, *, refresh: bool = False) -> RepoCandidate:
        # 搜尋結果已含完整 metadata，除非缺欄位才再打一次 repo API（節省未驗證流量）
        if refresh or not repo.updated_at or not repo.default_branch:
            detailed = self.get_repo(repo.full_name)
            if detailed:
                # preserve any prefilled fields / seed pairing
                detailed.readme_text = repo.readme_text or detailed.readme_text
                detailed.paper_urls = repo.paper_urls or detailed.paper_urls
                detailed.paper_url = repo.paper_url or detailed.paper_url
                detailed.paired_paper = repo.paired_paper or detailed.paired_paper
                detailed.quality_score = repo.quality_score
                detailed.quality_flags = list(repo.quality_flags)
                detailed.extra.update(repo.extra)
                repo = detailed

        readme = repo.readme_text or self.fetch_readme(repo)
        repo.readme_text = readme
        repo.readme_excerpt = clean_readme(readme, max_length=20000)

        # paper links from description/readme/homepage
        paper_urls = []
        for source in (repo.description, repo.homepage, repo.readme_excerpt):
            for url in extract_paper_urls(source):
                if url not in paper_urls:
                    paper_urls.append(url)
        repo.paper_urls = paper_urls[:20]
        if not repo.paper_url and paper_urls:
            repo.paper_url = paper_urls[0]
            repo.paired_paper = paper_urls[0]

        if not repo.sections:
            repo.sections = build_repo_sections(repo)
        return repo
