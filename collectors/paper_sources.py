"""論文來源抓取：arXiv、OpenAlex、Semantic Scholar、PubMed，並提供 IF/全文補強。"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Iterable
from urllib.parse import quote, quote_plus

from config import (
    MAILTO_CONTACT,
    PAPER_HTTP_TIMEOUT,
    PAPER_MAX_AGE_DAYS,
    PAPER_MAX_BYTES,
    PAPER_ROBOTS_CHECK,
    SEMANTIC_SCHOLAR_API_KEY,
)
from collectors.news_http import SafeHttpFetcher
from collectors.paper_parse import (
    PaperCandidate,
    extract_github_urls,
    extract_text_from_html,
    extract_text_from_pdf,
    format_impact_factor,
    parse_arxiv_atom,
    parse_openalex_work,
    parse_pubmed_xml,
    parse_semantic_scholar_paper,
    parts_non_na,
)
from core.timewin import parse_datetime, to_utc

ARXIV_API = "https://export.arxiv.org/api/query"
OPENALEX_WORKS = "https://api.openalex.org/works"
OPENALEX_SOURCES = "https://api.openalex.org/sources"
SEMANTIC_SCHOLAR_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"
PUBMED_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


@dataclass
class SourceStats:
    name: str
    found: int = 0
    fetched: int = 0
    errors: int = 0
    error: str = ""


class PaperSources:
    def __init__(
        self,
        *,
        fetcher: SafeHttpFetcher | None = None,
        robots_check: bool = PAPER_ROBOTS_CHECK,
    ) -> None:
        self.fetcher = fetcher or SafeHttpFetcher(timeout=PAPER_HTTP_TIMEOUT, max_bytes=PAPER_MAX_BYTES)
        self.robots_check = robots_check
        self._source_stats_cache: dict[str, dict] = {}

    # ---------- helpers ----------
    def _get_json(self, url: str, stats: SourceStats, *, headers: dict[str, str] | None = None) -> dict | None:
        result = self.fetcher.fetch(url, check_robots=self.robots_check, headers=headers)
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            return None
        stats.fetched += 1
        try:
            return json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            stats.errors += 1
            stats.error = "json_decode_error"
            return None

    def _get_text(self, url: str, stats: SourceStats | None = None, *, headers: dict[str, str] | None = None) -> bytes | None:
        result = self.fetcher.fetch(url, check_robots=self.robots_check, headers=headers)
        if not result.ok:
            if stats is not None:
                stats.errors += 1
                stats.error = result.error or f"http_{result.status}"
            return None
        if stats is not None:
            stats.fetched += 1
        return result.content

    # ---------- arXiv ----------
    def search_arxiv(self, query: str, *, max_results: int = 20, now: datetime | None = None) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("arxiv")
        encoded = quote_plus(query)
        url = f"{ARXIV_API}?search_query=all:{encoded}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        # arXiv Atom API 為公開程式介面，robots 對爬蟲頁面限制不等同 API 使用政策；此處關閉 robots 以免誤擋。
        result = self.fetcher.fetch(url, check_robots=False)
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            return [], stats
        stats.fetched += 1
        papers = parse_arxiv_atom(result.content)
        stats.found = len(papers)
        return papers, stats

    # ---------- OpenAlex ----------
    def _openalex_source_stats(self, source_id: str) -> dict:
        if not source_id:
            return {}
        if source_id in self._source_stats_cache:
            return self._source_stats_cache[source_id]
        sid = source_id.rsplit("/", 1)[-1]
        if not sid:
            return {}
        url = f"{OPENALEX_SOURCES}/{sid}?select=id,display_name,issn_l,summary_stats,type"
        result = self.fetcher.fetch(url, check_robots=False)
        if not result.ok:
            self._source_stats_cache[source_id] = {}
            return {}
        try:
            data = json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            self._source_stats_cache[source_id] = {}
            return {}
        summary = (data or {}).get("summary_stats") or {}
        self._source_stats_cache[source_id] = summary if isinstance(summary, dict) else {}
        return self._source_stats_cache[source_id]

    def search_openalex(
        self, query: str, *, per_page: int = 25, from_date: str = "", to_date: str = ""
    ) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("openalex")
        filters = ["type:article|preprint|book-chapter"]
        if from_date:
            filters.append(f"from_publication_date:{from_date}")
        if to_date:
            filters.append(f"to_publication_date:{to_date}")
        params = [
            f"search={quote_plus(query)}",
            f"per-page={max(1, min(per_page, 50))}",
            f"filter={quote(','.join(filters), safe=':,|-')}",
            "select=id,ids,title,display_name,publication_date,publication_year,doi,primary_location,best_oa_location,locations,open_access,cited_by_count,authorships,abstract_inverted_index,type",
            f"mailto={quote(MAILTO_CONTACT)}",
        ]
        url = f"{OPENALEX_WORKS}?{'&'.join(params)}"
        result = self.fetcher.fetch(url, check_robots=False)
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            return [], stats
        stats.fetched += 1
        try:
            data = json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            stats.errors += 1
            stats.error = "json_decode_error"
            return [], stats
        if not data:
            return [], stats
        results = data.get("results") or []
        papers: list[PaperCandidate] = []
        for work in results:
            paper = parse_openalex_work(work, source_stats_cache=self._source_stats_cache)
            if not paper:
                continue
            # 補查期刊 IF 指標（OpenAlex summary_stats）
            source_id = str((paper.extra or {}).get("source_id") or "")
            if source_id and (paper.impact_factor in ("", "N/A") or paper.source_tier <= 2):
                src_stats = self._openalex_source_stats(source_id)
                if src_stats:
                    impact, origin = format_impact_factor(src_stats, paper.journal or paper.source_name)
                    if impact != "N/A":
                        paper.impact_factor = impact
                        paper.impact_factor_source = origin
            papers.append(paper)
        stats.found = len(papers)
        return papers, stats

    # ---------- Semantic Scholar ----------
    def search_semantic_scholar(
        self, query: str, *, limit: int = 20, year: str = ""
    ) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("semantic_scholar")
        fields = "title,year,publicationDate,venue,citationCount,externalIds,openAccessPdf,url,abstract,authors,isOpenAccess,journal"
        params = [
            f"query={quote_plus(query)}",
            f"limit={max(1, min(limit, 100))}",
            f"fields={quote(fields, safe=',')}",
        ]
        if year:
            params.append(f"year={quote(year, safe='-:')}")
        url = f"{SEMANTIC_SCHOLAR_SEARCH}?{'&'.join(params)}"
        headers = {"User-Agent": f"DailyAIReportBot/2.0 (mailto:{MAILTO_CONTACT})"}
        if SEMANTIC_SCHOLAR_API_KEY:
            headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY
        result = self.fetcher.fetch(url, check_robots=False, headers=headers)
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            return [], stats
        stats.fetched += 1
        try:
            data = json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            stats.errors += 1
            stats.error = "json_decode_error"
            return [], stats
        if not data:
            return [], stats
        papers = []
        for item in data.get("data") or []:
            paper = parse_semantic_scholar_paper(item)
            if paper:
                papers.append(paper)
        stats.found = len(papers)
        return papers, stats

    # ---------- PubMed ----------
    def search_pubmed(self, query: str, *, retmax: int = 20) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("pubmed")
        esearch_url = (
            f"{PUBMED_ESEARCH}?db=pubmed&term={quote_plus(query)}&retmode=json&retmax={retmax}"
            f"&sort=date&tool=DailyAIReport&email={quote(MAILTO_CONTACT)}"
        )
        result = self.fetcher.fetch(esearch_url, check_robots=False)
        if not result.ok:
            stats.errors += 1
            stats.error = result.error or f"http_{result.status}"
            return [], stats
        stats.fetched += 1
        try:
            data = json.loads(result.content.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            stats.errors += 1
            stats.error = "json_decode_error"
            return [], stats
        id_list = ((data.get("esearchresult") or {}).get("idlist") or [])
        if not id_list:
            stats.found = 0
            return [], stats
        efetch_url = f"{PUBMED_EFETCH}?db=pubmed&id={','.join(id_list)}&retmode=xml&tool=DailyAIReport&email={quote(MAILTO_CONTACT)}"
        content = self._get_text(efetch_url, stats, headers=None)
        # efetch 也用 API 介面，不受頁面 robots 誤擋影響
        if content is None and stats.error == "robots_disallowed":
            result = self.fetcher.fetch(efetch_url, check_robots=False)
            if result.ok:
                stats.errors = max(0, stats.errors - 1)
                stats.error = ""
                stats.fetched += 1
                content = result.content
        if content is None:
            # fallback: 直接再試一次不檢查 robots
            result = self.fetcher.fetch(efetch_url, check_robots=False)
            if result.ok:
                stats.fetched += 1
                content = result.content
            else:
                if not stats.error:
                    stats.errors += 1
                    stats.error = result.error or f"http_{result.status}"
                return [], stats
        papers = parse_pubmed_xml(content)
        stats.found = len(papers)
        return papers, stats

    # ---------- content enrichment (crawl/parse) ----------
    def enrich_fulltext(self, paper: PaperCandidate, max_chars: int = 40000) -> PaperCandidate:
        """抓取並解析可公開取得的全文/頁面內容：優先 HTML，必要時解析 PDF（pypdf）。"""
        candidates: list[tuple[str, str]] = []  # (url, kind)
        # 優先 arXiv HTML
        if paper.arxiv_id:
            candidates.append((f"https://arxiv.org/html/{paper.arxiv_id}", "html"))
            candidates.append((f"https://arxiv.org/abs/{paper.arxiv_id}", "html"))
        # PMC 頁面可直接抓 HTML
        pmc_id = str((paper.extra or {}).get("pmc_id") or "")
        if pmc_id:
            candidates.append((f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc_id}/", "html"))
        # landing/fulltext 頁面
        for url in (paper.fulltext_url, paper.url):
            if not url or url in {c[0] for c in candidates}:
                continue
            kind = "pdf" if str(url).lower().endswith(".pdf") else "html"
            candidates.append((url, kind))
        # PDF 作為補充（若 HTML 失敗或不可用）
        for url in (paper.pdf_url,):
            if not url or url in {c[0] for c in candidates}:
                continue
            candidates.append((url, "pdf"))
        if paper.arxiv_id:
            candidates.append((f"https://arxiv.org/pdf/{paper.arxiv_id}.pdf", "pdf"))

        for url, kind in candidates:
            result = self.fetcher.fetch(url, check_robots=self.robots_check)
            if not result.ok:
                continue
            ctype = (result.content_type or "").lower()
            is_pdf = kind == "pdf" or "pdf" in ctype or result.content[:4] == b"%PDF"
            if is_pdf:
                text = extract_text_from_pdf(result.content, max_length=max_chars)
                parsed_kind = "pdf"
            else:
                text = extract_text_from_html(result.content.decode("utf-8", errors="replace"), max_length=max_chars)
                parsed_kind = "html"
            if len(text) < 400:
                continue
            paper.fulltext_excerpt = text
            paper.parse_level = "fulltext"
            paper.extra["fulltext_source"] = url
            paper.extra["fulltext_kind"] = parsed_kind
            if not paper.code_url:
                codes = extract_github_urls(text)
                if codes:
                    paper.code_url = codes[0]
            return paper

        # fallback: abstract counts as parsed content if present
        if paper.abstract:
            paper.fulltext_excerpt = paper.abstract[:max_chars]
            if paper.parse_level == "metadata":
                paper.parse_level = "abstract"
        return paper
