"""論文蒐集引擎：多來源彙整 → 去重 → 時效/品質篩選 → IF 補強 → 內容抓取 → 配額選文。"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Iterable

from config import (
    PAPER_FULLTEXT_MAX_CHARS,
    PAPER_MAX_AGE_DAYS,
    PAPER_MAX_PER_SOURCE,
    PAPER_MIN_PAIRED,
    PAPER_QUERIES,
)
from collectors.news_engine import is_ai_related
from collectors.paper_parse import PaperCandidate, extract_github_urls, first_github_url
from collectors.paper_sources import PaperSources
from core.dedupe import Deduper, is_similar_title, make_keys, normalize_doi
from core.models import PaperItem, SchemaError
from core.timewin import is_within_window, now_utc, to_utc


class PaperQuotaError(RuntimeError):
    def __init__(self, message: str, report: dict):
        super().__init__(message)
        self.report = report


@dataclass
class PaperSelection:
    items: list[PaperItem]
    report: dict = field(default_factory=dict)
    rejected: list[dict] = field(default_factory=list)


def _published_key(item: PaperItem) -> datetime:
    return item.published_at or datetime.min.replace(tzinfo=timezone.utc)


def candidate_to_item(candidate: PaperCandidate) -> PaperItem:
    code_url = candidate.code_url or first_github_url(f"{candidate.abstract}\n{candidate.fulltext_excerpt}")
    paired_repo = ""
    if code_url:
        m = __import__("re").search(r"github\.com/([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", code_url, __import__("re").IGNORECASE)
        if m:
            paired_repo = m.group(1).rstrip(".")
    extra = candidate.extra if isinstance(candidate.extra, dict) else {}
    return PaperItem(
        title=candidate.title,
        url=candidate.url,
        source_name=candidate.source_name or candidate.journal or candidate.venue or "unknown",
        source_tier=int(candidate.source_tier or 3),
        published_at=candidate.published_at,
        authors=list(candidate.authors or []),
        abstract=candidate.abstract or "",
        pdf_url=candidate.pdf_url or "",
        code_url=code_url or "",
        doi=normalize_doi(candidate.doi) if candidate.doi else "",
        arxiv_id=candidate.arxiv_id or "",
        journal=candidate.journal or "",
        venue=candidate.venue or "",
        impact_factor=candidate.impact_factor or "N/A",
        impact_factor_source=candidate.impact_factor_source or "",
        cited_by_count=int(candidate.cited_by_count or 0),
        fulltext_excerpt=candidate.fulltext_excerpt or candidate.abstract or "",
        fulltext_source=str(extra.get("fulltext_source", "") or ""),
        fulltext_kind=str(extra.get("fulltext_kind", "") or ("abstract" if candidate.abstract else "metadata")),
        fulltext_pages=int(extra.get("fulltext_pages") or 0),
        ocr_pages=int(extra.get("ocr_pages") or 0),
        parse_level=candidate.parse_level or ("abstract" if candidate.abstract else "metadata"),
        paired_repo=paired_repo,
    )


def select_papers(
    items: Iterable[PaperItem],
    count: int,
    *,
    max_per_source: int = PAPER_MAX_PER_SOURCE,
    min_paired: int = 0,
) -> PaperSelection:
    """依「配對優先 → 來源層級/新近度/引用數 → 來源分散」選文。"""
    ordered = sorted(
        items,
        key=lambda item: (
            1 if (item.code_url or item.paired_repo) else 0,
            -int(item.source_tier or 3),
            _published_key(item),
            int(item.cited_by_count or 0),
        ),
        reverse=True,
    )
    selected: list[PaperItem] = []
    remaining = list(ordered)
    per_source: Counter[str] = Counter()
    relaxed = False

    def eligible(item: PaperItem) -> bool:
        key = (item.source_name or "unknown").lower()
        return max_per_source <= 0 or per_source[key] < max_per_source

    def take(predicate) -> bool:  # noqa: ANN001
        nonlocal relaxed
        for index, item in enumerate(remaining):
            if predicate(item) and eligible(item):
                remaining.pop(index)
                selected.append(item)
                per_source[(item.source_name or "unknown").lower()] += 1
                return True
        for index, item in enumerate(remaining):
            if predicate(item):
                remaining.pop(index)
                selected.append(item)
                per_source[(item.source_name or "unknown").lower()] += 1
                relaxed = True
                return True
        return False

    while len(selected) < count:
        paired = sum(1 for item in selected if item.code_url or item.paired_repo)
        # 先確保有配對候選（若池中存在）
        if paired < min_paired and take(lambda item: bool(item.code_url or item.paired_repo)):
            continue
        # 盡量優先 tier 1/2
        if take(lambda item: int(item.source_tier or 3) <= 2):
            continue
        if take(lambda _item: True):
            continue
        break

    paired = sum(1 for item in selected if item.code_url or item.paired_repo)
    report = {
        "pool_size": len(ordered),
        "selected": len(selected),
        "target": count,
        "paired": paired,
        "paired_ok": paired >= min_paired,
        "per_source": dict(per_source),
        "tiers": dict(Counter(str(item.source_tier) for item in selected)),
        "parse_levels": dict(Counter(item.parse_level for item in selected)),
        "relaxed_caps": relaxed,
    }
    if len(selected) < count:
        raise PaperQuotaError(f"論文數量不足：{len(selected)}/{count}", report)
    return PaperSelection(items=selected, report=report)


class PaperEngine:
    def __init__(
        self,
        *,
        sources: PaperSources | None = None,
        queries: list[dict] | None = None,
        max_per_source: int = PAPER_MAX_PER_SOURCE,
        max_age_days: int = PAPER_MAX_AGE_DAYS,
        min_paired: int = PAPER_MIN_PAIRED,
        enrich_fulltext: bool = True,
        enrich_limit: int = 8,
        fulltext_max_chars: int = PAPER_FULLTEXT_MAX_CHARS,
        allow_stale: bool = False,
    ) -> None:
        self.sources = sources or PaperSources()
        self.queries = PAPER_QUERIES if queries is None else queries
        self.max_per_source = max_per_source
        self.max_age_days = max_age_days
        self.min_paired = min_paired
        self.enrich_fulltext = enrich_fulltext
        self.enrich_limit = enrich_limit
        self.fulltext_max_chars = fulltext_max_chars
        self.allow_stale = allow_stale

    def collect(self, count: int = 5, *, now: datetime | None = None) -> PaperSelection:
        reference = now or now_utc()
        from_date = (reference - timedelta(days=self.max_age_days)).date().isoformat()
        to_date = reference.date().isoformat()
        year_filter = f"{reference.year - 1}-{reference.year}"

        raw_candidates: list[PaperCandidate] = []
        source_stats: dict[str, dict] = {}

        def add_stats(name: str, st) -> None:  # noqa: ANN001
            entry = source_stats.setdefault(name, {"found": 0, "fetched": 0, "errors": 0})
            entry["found"] += getattr(st, "found", 0)
            entry["fetched"] += getattr(st, "fetched", 0)
            entry["errors"] += getattr(st, "errors", 0)
            if getattr(st, "error", ""):
                entry["error"] = st.error

        for query in self.queries:
            q = str(query.get("query", "")).strip()
            if not q:
                continue
            # arXiv
            papers, st = self.sources.search_arxiv(q, max_results=12)
            raw_candidates.extend(papers)
            add_stats("arxiv", st)
            # OpenAlex
            papers, st = self.sources.search_openalex(q, per_page=15, from_date=from_date, to_date=to_date)
            raw_candidates.extend(papers)
            add_stats("openalex", st)
            # PubMed (對醫療/生醫查詢較有價值，但安全起見都跑；結果再篩)
            papers, st = self.sources.search_pubmed(q, retmax=10)
            raw_candidates.extend(papers)
            add_stats("pubmed", st)
            # Semantic Scholar（選用，429/不可用時不影響整體）
            papers, st = self.sources.search_semantic_scholar(q, limit=10, year=year_filter)
            raw_candidates.extend(papers)
            add_stats("semantic_scholar", st)

        items, rejected = self._filter_and_dedupe(raw_candidates, reference)

        # 內容抓取與 GitHub 偵測（優先處理排名前面的候選）
        if self.enrich_fulltext:
            items.sort(
                key=lambda item: (
                    1 if (item.code_url or item.paired_repo) else 0,
                    -int(item.source_tier or 3),
                    _published_key(item),
                ),
                reverse=True,
            )
            for item in items[: self.enrich_limit]:
                try:
                    # 轉成 candidate-like enrich target
                    candidate = PaperCandidate(
                        title=item.title,
                        url=item.url,
                        arxiv_id=item.arxiv_id,
                        abstract=item.abstract,
                        fulltext_url=item.pdf_url or item.url,
                        fulltext_excerpt=item.fulltext_excerpt,
                        parse_level=item.parse_level,
                        code_url=item.code_url,
                        extra={"pmc_id": ""},
                    )
                    # 嘗試從 URL 推斷 pmc id
                    if "/pmc/articles/" in (item.pdf_url or item.url):
                        import re as _re
                        m = _re.search(r"/articles/(PMC\d+)", (item.pdf_url or item.url))
                        if m:
                            candidate.extra["pmc_id"] = m.group(1)
                    enriched = self.sources.enrich_fulltext(candidate, max_chars=self.fulltext_max_chars)
                    if enriched.fulltext_excerpt:
                        item.fulltext_excerpt = enriched.fulltext_excerpt
                        item.parse_level = enriched.parse_level
                        item.fulltext_source = str((enriched.extra or {}).get("fulltext_source", "") or item.fulltext_source)
                        item.fulltext_kind = str((enriched.extra or {}).get("fulltext_kind", "") or item.fulltext_kind)
                        item.fulltext_pages = int((enriched.extra or {}).get("fulltext_pages") or item.fulltext_pages)
                        item.ocr_pages = int((enriched.extra or {}).get("ocr_pages") or item.ocr_pages)
                    if enriched.code_url and not item.code_url:
                        item.code_url = enriched.code_url
                        import re as _re
                        m = _re.search(r"github\.com/([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)", item.code_url, _re.IGNORECASE)
                        if m:
                            item.paired_repo = m.group(1).rstrip(".")
                except Exception as exc:  # noqa: BLE001 - 單篇失敗不影響
                    rejected.append({"title": item.title[:160], "reason": f"enrich_error:{type(exc).__name__}", "source": item.source_name})

        # 最終以 min_paired=目標值嘗試選取；不足則放寬並記錄 warning
        try:
            selection = select_papers(items, count, max_per_source=self.max_per_source, min_paired=self.min_paired)
        except PaperQuotaError as exc:
            # 若是配對不足但數量夠，select_papers 不會因配對丟錯；此處主要是數量不足
            exc.report.setdefault("sources", source_stats)
            exc.report.setdefault("raw_count", len(raw_candidates))
            exc.report.setdefault("unique_items", len(items))
            exc.report.setdefault("rejected_counts", dict(Counter(r["reason"] for r in rejected)))
            raise
        if selection.report.get("paired", 0) < self.min_paired:
            selection.report["paired_warning"] = (
                f"配對論文不足目標：{selection.report.get('paired', 0)}/{self.min_paired}"
            )

        selection.rejected = rejected
        selection.report["sources"] = source_stats
        selection.report["raw_count"] = len(raw_candidates)
        selection.report["unique_items"] = len(items)
        selection.report["rejected_counts"] = dict(Counter(r["reason"] for r in rejected))
        return selection

    def _filter_and_dedupe(
        self, candidates: list[PaperCandidate], reference: datetime
    ) -> tuple[list[PaperItem], list[dict]]:
        deduper = Deduper()
        kept: list[PaperItem] = []
        rejected: list[dict] = []

        for cand in candidates:
            if not cand.title or not cand.url:
                rejected.append({"title": (cand.title or "")[:160], "reason": "missing_title_or_url", "source": cand.source_name})
                continue
            published = cand.published_at
            if published is None:
                # 無日期：對 arXiv/預印本保守捨棄；避免把舊文當新文
                rejected.append({"title": cand.title[:160], "reason": "no_date", "source": cand.source_name})
                continue
            published = to_utc(published)
            if not self.allow_stale and not is_within_window(published, self.max_age_days, now=reference):
                rejected.append({"title": cand.title[:160], "reason": "stale", "source": cand.source_name})
                continue

            text = f"{cand.title} {cand.abstract} {cand.journal} {cand.venue}".strip()
            if not is_ai_related(text):
                rejected.append({"title": cand.title[:160], "reason": "not_ai", "source": cand.source_name})
                continue

            try:
                item = candidate_to_item(cand)
                item.validate()
            except SchemaError as exc:
                rejected.append({"title": cand.title[:160], "reason": f"invalid: {exc}", "source": cand.source_name})
                continue

            keys = make_keys(url=item.url, title=item.title, doi=item.doi, arxiv_id=item.arxiv_id)
            if not deduper.add(*keys):
                rejected.append({"title": cand.title[:160], "reason": "duplicate", "source": cand.source_name})
                continue
            if any(is_similar_title(item.title, other.title) for other in kept):
                rejected.append({"title": cand.title[:160], "reason": "similar_title", "source": cand.source_name})
                continue

            kept.append(item)

        return kept, rejected


def collect_daily_papers(count: int = 5, *, now: datetime | None = None) -> PaperSelection:
    return PaperEngine().collect(count, now=now)
