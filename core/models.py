"""資料模型與驗證（不依賴第三方套件，維持零新增依賴）。

所有項目在進入撰寫／產檔前都必須先 `validate()`：
- 必需欄位、長度上限
- URL 僅允許公開的 http/https（重用 core.security 的 SSRF 靜態檢查）
- 領域標籤白名單、來源層級、解析程度
- 每日 bundle 的數量、時效、跨域配額（跨域 ≥3、海事 ≥1）
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any

from config import NEWS_MAX_AGE_DAYS, PAPER_MAX_AGE_DAYS, REPO_MAX_AGE_DAYS
from core.dedupe import paper_identity_keys
from core.security import UnsafeURLError, assert_public_http_url
from core.timewin import end_of_day_utc, is_future, is_within_window, parse_datetime

DOMAINS = ("maritime", "cybersecurity", "medical", "electronics", "robotics", "general")
DOMAIN_LABELS = {
    "maritime": "海洋事務",
    "cybersecurity": "資訊安全",
    "medical": "醫療",
    "electronics": "電子技術",
    "robotics": "機器人（具身智慧）",
    "general": "通用 AI",
}
CROSS_DOMAIN = tuple(d for d in DOMAINS if d != "general")
SOURCE_TIERS = (1, 2, 3)
PARSE_LEVELS = ("fulltext", "abstract", "metadata")
NEWS_DOMAINS_MIN = 3
MARITIME_MIN = 1

_REPO_NAME = re.compile(r"^[A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+$")


class SchemaError(ValueError):
    """資料不符合 schema。"""


def _fail(path: str, message: str) -> None:
    raise SchemaError(f"{path}: {message}")


def _text(path: str, value: object, *, required: bool = True, max_len: int = 500, min_len: int = 0) -> str:
    if value is None:
        if required:
            _fail(path, "為必填")
        return ""
    if not isinstance(value, str):
        _fail(path, f"必須是字串（收到 {type(value).__name__}）")
    text = value.strip()
    if required and not text:
        _fail(path, "不可為空")
    if len(text) > max_len:
        _fail(path, f"長度 {len(text)} 超過上限 {max_len}")
    if text and len(text) < min_len:
        _fail(path, f"長度 {len(text)} 低於下限 {min_len}")
    return text


def _url(path: str, value: object, *, required: bool = True) -> str:
    if value is None or (isinstance(value, str) and not value.strip()):
        if required:
            _fail(path, "為必填 URL")
        return ""
    try:
        return assert_public_http_url(str(value))
    except UnsafeURLError as exc:
        _fail(path, str(exc))
    raise AssertionError("unreachable")


def _datetime(path: str, value: object, *, required: bool = True) -> datetime | None:
    if value is None or (isinstance(value, str) and not value.strip()):
        if required:
            _fail(path, "為必填日期")
        return None
    parsed = parse_datetime(value)
    if parsed is None:
        _fail(path, f"無法解析日期：{value!r}")
    return parsed


def _int(path: str, value: object, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        try:
            value = int(str(value))
        except (TypeError, ValueError):
            _fail(path, "必須是整數")
    if value < minimum:
        _fail(path, f"不可小於 {minimum}")
    return int(value)


@dataclass
class NewsItem:
    title: str
    url: str
    source: str = ""
    published_at: datetime | None = None
    language: str = ""
    country: str = ""
    ai_focus: str = ""
    domains: list[str] = field(default_factory=list)
    is_maritime: bool = False
    summary: str = ""
    key_point: str = ""

    def __post_init__(self) -> None:
        if self.is_maritime and "maritime" not in self.domains:
            self.domains.append("maritime")

    def validate(self) -> "NewsItem":
        self.title = _text("news.title", self.title, max_len=300)
        self.url = _url("news.url", self.url)
        self.source = _text("news.source", self.source, required=False, max_len=120)
        self.published_at = _datetime("news.published_at", self.published_at)
        self.language = _text("news.language", self.language, required=False, max_len=32)
        self.country = _text("news.country", self.country, required=False, max_len=32)
        self.ai_focus = _text("news.ai_focus", self.ai_focus, required=False, max_len=120)
        self.summary = _text("news.summary", self.summary, required=False, max_len=4000)
        self.key_point = _text("news.key_point", self.key_point, required=False, max_len=300)
        if not isinstance(self.domains, list) or not self.domains:
            _fail("news.domains", "至少需要一個領域標籤")
        for index, domain in enumerate(self.domains):
            if domain not in DOMAINS:
                _fail(f"news.domains[{index}]", f"未知領域：{domain!r}")
        self.domains = list(dict.fromkeys(self.domains))
        return self


@dataclass
class PaperItem:
    title: str
    url: str
    source_name: str = ""
    source_tier: int = 2
    published_at: datetime | None = None
    authors: list[str] = field(default_factory=list)
    afflictions: list[str] = field(default_factory=list)
    abstract: str = ""
    pdf_url: str = ""
    code_url: str = ""
    doi: str = ""
    arxiv_id: str = ""
    journal: str = ""
    venue: str = ""
    impact_factor: str = ""
    impact_factor_source: str = ""
    cited_by_count: int = 0
    fulltext_excerpt: str = ""
    fulltext_source: str = ""
    fulltext_kind: str = ""  # pdf/pdf+ocr/html/abstract/metadata
    fulltext_pages: int = 0
    ocr_pages: int = 0
    parse_level: str = "metadata"
    paired_repo: str = ""
    sections: dict[str, str] = field(default_factory=dict)

    def validate(self, *, require_sections: bool = False, min_section_chars: int = 0) -> "PaperItem":
        self.title = _text("paper.title", self.title, max_len=500)
        self.url = _url("paper.url", self.url)
        self.source_name = _text("paper.source_name", self.source_name, max_len=160)
        if self.source_tier not in SOURCE_TIERS:
            _fail("paper.source_tier", f"必須是 {SOURCE_TIERS}")
        self.published_at = _datetime("paper.published_at", self.published_at)
        if not isinstance(self.authors, list):
            _fail("paper.authors", "必須是字串陣列")
        self.authors = [_text(f"paper.authors[{i}]", a, max_len=200) for i, a in enumerate(self.authors)]
        if not isinstance(self.afflictions, list):
            _fail("paper.afflictions", "必須是字串陣列")
        self.afflictions = [_text(f"paper.afflictions[{i}]", a, max_len=300) for i, a in enumerate(self.afflictions)]
        self.abstract = _text("paper.abstract", self.abstract, required=False, max_len=20000)
        self.pdf_url = _url("paper.pdf_url", self.pdf_url, required=False)
        self.code_url = _url("paper.code_url", self.code_url, required=False)
        self.doi = _text("paper.doi", self.doi, required=False, max_len=200)
        self.arxiv_id = _text("paper.arxiv_id", self.arxiv_id, required=False, max_len=64)
        self.journal = _text("paper.journal", self.journal, required=False, max_len=300)
        self.venue = _text("paper.venue", self.venue, required=False, max_len=300)
        self.impact_factor = _text("paper.impact_factor", self.impact_factor, required=False, max_len=120)
        self.impact_factor_source = _text("paper.impact_factor_source", self.impact_factor_source, required=False, max_len=200)
        self.cited_by_count = _int("paper.cited_by_count", self.cited_by_count)
        self.fulltext_excerpt = _text("paper.fulltext_excerpt", self.fulltext_excerpt, required=False, max_len=400000)
        self.fulltext_source = _url("paper.fulltext_source", self.fulltext_source, required=False)
        self.fulltext_kind = _text("paper.fulltext_kind", self.fulltext_kind, required=False, max_len=32)
        self.fulltext_pages = _int("paper.fulltext_pages", self.fulltext_pages)
        self.ocr_pages = _int("paper.ocr_pages", self.ocr_pages)
        if self.parse_level not in PARSE_LEVELS:
            _fail("paper.parse_level", f"必須是 {PARSE_LEVELS}")
        self.paired_repo = _text("paper.paired_repo", self.paired_repo, required=False, max_len=200)
        self.sections = _validate_sections(
            "paper.sections", self.sections, ("background", "method", "results", "limitations"),
            require_sections=require_sections, min_chars=min_section_chars,
        )
        return self


@dataclass
class RepoItem:
    full_name: str
    html_url: str
    description: str = ""
    stars: int = 0
    forks: int = 0
    language: str = ""
    license_name: str = ""
    topics: list[str] = field(default_factory=list)
    updated_at: datetime | None = None
    created_at: datetime | None = None
    paper_url: str = ""
    paired_paper: str = ""
    readme_text: str = ""
    readme_excerpt: str = ""
    quality_score: int = 0
    quality_flags: list[str] = field(default_factory=list)
    sections: dict[str, str] = field(default_factory=dict)

    def validate(self, *, require_sections: bool = False, min_section_chars: int = 0) -> "RepoItem":
        self.full_name = _text("repo.full_name", self.full_name, max_len=200)
        if not _REPO_NAME.match(self.full_name):
            _fail("repo.full_name", "必須是 owner/name 格式")
        self.html_url = _url("repo.html_url", self.html_url)
        self.description = _text("repo.description", self.description, required=False, max_len=2000)
        self.stars = _int("repo.stars", self.stars)
        self.forks = _int("repo.forks", self.forks)
        self.language = _text("repo.language", self.language, required=False, max_len=64)
        self.license_name = _text("repo.license_name", self.license_name, required=False, max_len=64)
        if not isinstance(self.topics, list):
            _fail("repo.topics", "必須是字串陣列")
        self.topics = [_text(f"repo.topics[{i}]", t, max_len=64) for i, t in enumerate(self.topics)]
        self.updated_at = _datetime("repo.updated_at", self.updated_at)
        self.created_at = _datetime("repo.created_at", self.created_at, required=False)
        self.paper_url = _url("repo.paper_url", self.paper_url, required=False)
        self.paired_paper = _text("repo.paired_paper", self.paired_paper, required=False, max_len=300)
        self.readme_text = _text("repo.readme_text", self.readme_text, required=False, max_len=200000)
        self.readme_excerpt = _text("repo.readme_excerpt", self.readme_excerpt, required=False, max_len=20000)
        self.quality_score = _int("repo.quality_score", self.quality_score)
        if self.quality_score > 10:
            _fail("repo.quality_score", "不可大於 10")
        if not isinstance(self.quality_flags, list):
            _fail("repo.quality_flags", "必須是字串陣列")
        self.quality_flags = [_text(f"repo.quality_flags[{i}]", f, max_len=32) for i, f in enumerate(self.quality_flags)]
        self.sections = _validate_sections(
            "repo.sections", self.sections, ("what", "tech", "architecture"),
            require_sections=require_sections, min_chars=min_section_chars,
        )
        return self


@dataclass
class TechArchItem:
    name: str
    principle: str
    applications_maritime: str
    applications_medical: str
    reference_urls: list[str] = field(default_factory=list)
    rationale: str = ""
    applications_general: str = ""
    limitations: str = ""
    related_news: list[str] = field(default_factory=list)
    related_papers: list[str] = field(default_factory=list)
    related_repos: list[str] = field(default_factory=list)
    image_path: str = ""

    def validate(self, *, min_application_chars: int = 0) -> "TechArchItem":
        self.name = _text("tech.name", self.name, max_len=200)
        self.principle = _text("tech.principle", self.principle, min_len=min_application_chars, max_len=6000)
        self.applications_maritime = _text(
            "tech.applications_maritime", self.applications_maritime, min_len=min_application_chars, max_len=6000
        )
        self.applications_medical = _text(
            "tech.applications_medical", self.applications_medical, min_len=min_application_chars, max_len=6000
        )
        if not isinstance(self.reference_urls, list) or not self.reference_urls:
            _fail("tech.reference_urls", "至少需要一個參考連結")
        self.reference_urls = [
            _url(f"tech.reference_urls[{i}]", u) for i, u in enumerate(self.reference_urls)
        ]
        self.rationale = _text("tech.rationale", self.rationale, required=False, max_len=1200)
        self.applications_general = _text(
            "tech.applications_general", self.applications_general, required=False, max_len=6000
        )
        self.limitations = _text("tech.limitations", self.limitations, required=False, max_len=6000)
        for name in ("related_news", "related_papers", "related_repos"):
            values = getattr(self, name)
            if not isinstance(values, list):
                _fail(f"tech.{name}", "必須是字串陣列")
            setattr(self, name, [_text(f"tech.{name}[{i}]", v, max_len=300) for i, v in enumerate(values)])
        self.image_path = _text("tech.image_path", self.image_path, required=False, max_len=300)
        return self


def _validate_sections(
    path: str,
    sections: dict[str, str],
    required_keys: tuple[str, ...],
    *,
    require_sections: bool,
    min_chars: int,
) -> dict[str, str]:
    if sections is None:
        sections = {}
    if not isinstance(sections, dict):
        _fail(path, "必須是物件")
    cleaned: dict[str, str] = {}
    for key, value in sections.items():
        if key not in required_keys:
            _fail(f"{path}.{key}", f"未知區段（允許：{', '.join(required_keys)}）")
        cleaned[key] = _text(f"{path}.{key}", value, required=False, max_len=20000)
    if require_sections:
        missing = [k for k in required_keys if not cleaned.get(k)]
        if missing:
            _fail(path, f"缺少區段：{', '.join(missing)}")
        for key in required_keys:
            if len(cleaned[key]) < min_chars:
                _fail(f"{path}.{key}", f"內容長度 {len(cleaned[key])} 低於下限 {min_chars}")
    return cleaned


@dataclass
class DailyBundle:
    date: str
    news: list[NewsItem] = field(default_factory=list)
    papers: list[PaperItem] = field(default_factory=list)
    repos: list[RepoItem] = field(default_factory=list)
    tech: TechArchItem | None = None
    warnings: list[str] = field(default_factory=list)

    def validate(
        self,
        *,
        now: datetime | None = None,
        require_counts: bool = True,
        require_sections: bool = False,
        require_quotas: bool = True,
        min_section_chars: int = 0,
        allow_stale: bool = False,
    ) -> dict[str, Any]:
        parsed_date = parse_datetime(self.date)
        if parsed_date is None:
            _fail("bundle.date", f"必須是 YYYY-MM-DD，收到 {self.date!r}")
        reference = now or end_of_day_utc(parsed_date.date())

        for index, item in enumerate(self.news):
            try:
                item.validate()
            except SchemaError as exc:
                raise SchemaError(f"news[{index}] → {exc}") from exc
        for index, item in enumerate(self.papers):
            try:
                item.validate(require_sections=require_sections, min_section_chars=min_section_chars)
            except SchemaError as exc:
                raise SchemaError(f"papers[{index}] → {exc}") from exc
        for index, item in enumerate(self.repos):
            try:
                item.validate(require_sections=require_sections, min_section_chars=min_section_chars)
            except SchemaError as exc:
                raise SchemaError(f"repos[{index}] → {exc}") from exc
        if self.tech is not None:
            try:
                self.tech.validate(min_application_chars=min_section_chars if require_sections else 0)
            except SchemaError as exc:
                raise SchemaError(f"tech → {exc}") from exc

        future_items = (
            [f"news:{n.title}" for n in self.news if is_future(n.published_at, now=reference)]
            + [f"papers:{p.title}" for p in self.papers if is_future(p.published_at, now=reference)]
            + [f"repos:{r.full_name}" for r in self.repos if is_future(r.updated_at, now=reference)]
        )
        if future_items:
            _fail("bundle.future", f"不得包含晚於報告日的資料：{future_items[:3]}")

        if require_counts:
            from config import DAILY_NEWS_COUNT, DAILY_PAPER_COUNT, DAILY_REPO_COUNT

            if allow_stale:
                # backfill 模式：允許部分不足，但必須明確記錄
                if len(self.news) < DAILY_NEWS_COUNT:
                    self.warnings.append(f"quota_shortfall:news:{len(self.news)}/{DAILY_NEWS_COUNT}")
                if len(self.papers) < DAILY_PAPER_COUNT:
                    self.warnings.append(f"quota_shortfall:papers:{len(self.papers)}/{DAILY_PAPER_COUNT}")
                if len(self.repos) < DAILY_REPO_COUNT:
                    self.warnings.append(f"quota_shortfall:repos:{len(self.repos)}/{DAILY_REPO_COUNT}")
                if self.tech is None:
                    self.warnings.append("quota_shortfall:tech:0/1")
            else:
                _expect_count("news", len(self.news), DAILY_NEWS_COUNT)
                _expect_count("papers", len(self.papers), DAILY_PAPER_COUNT)
                _expect_count("repos", len(self.repos), DAILY_REPO_COUNT)
                if self.tech is None:
                    _fail("tech", "每日必須有 1 篇 AI 技術架構")

        freshness = {
            "news_stale": [
                n.title for n in self.news
                if not is_within_window(n.published_at, NEWS_MAX_AGE_DAYS, now=reference)
            ],
            "papers_stale": [
                p.title for p in self.papers
                if not is_within_window(p.published_at, PAPER_MAX_AGE_DAYS, now=reference)
            ],
            "repos_stale": [
                r.full_name for r in self.repos
                if not is_within_window(r.updated_at, REPO_MAX_AGE_DAYS, now=reference)
            ],
        }
        if not allow_stale:
            for key, values in freshness.items():
                if values:
                    _fail("bundle.freshness", f"{key} 超過時效窗：{values[:3]}")

        cross_domain = sum(
            1 for n in self.news if any(d in CROSS_DOMAIN for d in n.domains)
        )
        maritime = sum(1 for n in self.news if n.is_maritime or "maritime" in n.domains)
        paired_seed = sum(1 for p in self.papers if p.code_url or p.paired_repo)
        paper_keys = [
            paper_identity_keys(str(p.url))
            | paper_identity_keys(str(getattr(p, "doi", "") or ""))
            | paper_identity_keys(str(getattr(p, "arxiv_id", "") or ""))
            for p in self.papers
        ]
        repo_keys = [
            paper_identity_keys(str(r.paper_url or r.paired_paper or ""))
            for r in self.repos
        ]
        all_repo_keys = set().union(*repo_keys) if repo_keys else set()
        all_paper_keys = set().union(*paper_keys) if paper_keys else set()
        paired_actual = sum(1 for keys in paper_keys if keys & all_repo_keys)
        repo_paired_actual = sum(1 for keys in repo_keys if keys & all_paper_keys)
        repo_paired_seed = sum(1 for r in self.repos if r.paper_url or r.paired_paper)
        quotas = {
            "news_total": len(self.news),
            "cross_domain": cross_domain,
            "maritime": maritime,
            "paired_papers": paired_actual,
            "paired_papers_seed": paired_seed,
            "paired_repos": repo_paired_actual,
            "paired_repos_seed": repo_paired_seed,
            "cross_domain_ok": cross_domain >= NEWS_DOMAINS_MIN,
            "maritime_ok": maritime >= MARITIME_MIN,
            "stale_backfill": bool(allow_stale),
        }
        if require_quotas:
            if not quotas["cross_domain_ok"]:
                _fail("bundle.quotas", f"跨域新聞需 ≥{NEWS_DOMAINS_MIN}，目前 {cross_domain}")
            if not quotas["maritime_ok"]:
                _fail("bundle.quotas", f"海事新聞需 ≥{MARITIME_MIN}，目前 {maritime}")
        return quotas


def _expect_count(name: str, actual: int, expected: int) -> None:
    if actual != expected:
        _fail(f"bundle.{name}", f"需 {expected} 筆，目前 {actual} 筆")


def empty_bundle(day: date | str) -> DailyBundle:
    return DailyBundle(date=day.isoformat() if isinstance(day, date) else str(day))
