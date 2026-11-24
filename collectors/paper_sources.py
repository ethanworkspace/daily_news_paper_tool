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
    PAPER_OCR_DPI,
    PAPER_OCR_ENABLED,
    PAPER_OCR_MAX_PAGES,
    PAPER_OCR_MAX_SECONDS,
    PAPER_OCR_MIN_CHARS,
    PAPER_ROBOTS_CHECK,
    SEMANTIC_SCHOLAR_API_KEY,
)
from collectors.news_http import SafeHttpFetcher
from collectors.pdf_text import extract_pdf_document
from collectors.paper_parse import (
    PaperCandidate,
    extract_github_urls,
    extract_pdf_urls,
    extract_text_from_html,
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
    def search_arxiv(
        self,
        query: str,
        *,
        max_results: int = 20,
        now: datetime | None = None,
        from_date: str = "",
        to_date: str = "",
    ) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("arxiv")
        search_query = f"all:{query}"
        if from_date and to_date:
            start = from_date.replace("-", "") + "0000"
            end = to_date.replace("-", "") + "2359"
            search_query = f"{search_query} AND submittedDate:[{start} TO {end}]"
        url = (
            f"{ARXIV_API}?search_query={quote_plus(search_query)}"
            f"&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        )
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
    def search_pubmed(
        self,
        query: str,
        *,
        retmax: int = 20,
        mindate: str = "",
        maxdate: str = "",
    ) -> tuple[list[PaperCandidate], SourceStats]:
        stats = SourceStats("pubmed")
        date_params = ""
        if mindate and maxdate:
            date_params = (
                f"&datetype=pdat&mindate={quote(mindate, safe='/')}"
                f"&maxdate={quote(maxdate, safe='/')}"
            )
        esearch_url = (
            f"{PUBMED_ESEARCH}?db=pubmed&term={quote_plus(query)}&retmode=json&retmax={retmax}"
            f"&sort=date&tool=DailyAIReport&email={quote(MAILTO_CONTACT)}{date_params}"
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
    def enrich_fulltext(self, paper: PaperCandidate, max_chars: int = 300000) -> PaperCandidate:
        """抓取並解析可公開取得的論文全文：優先 HTML/PDF 全文（掃描頁自動 OCR），避免只停在摘要。"""
        candidates: list[tuple[str, str]] = []  # (url, kind)

        def add(url: str, kind: str) -> None:
            if not url:
                return
            if any(url == u for u, _ in candidates):
                return
            candidates.append((url, kind))

        def parse_pdf(content: bytes) -> tuple[str, dict]:
            doc = extract_pdf_document(
                content,
                max_length=max_chars,
                ocr=PAPER_OCR_ENABLED,
                ocr_max_pages=PAPER_OCR_MAX_PAGES,
                ocr_max_seconds=PAPER_OCR_MAX_SECONDS,
                ocr_dpi=PAPER_OCR_DPI,
                ocr_min_chars=PAPER_OCR_MIN_CHARS,
            )
            meta = {
                "kind": doc.kind,
                "pages": doc.pages,
                "ocr_pages": doc.ocr_pages,
                "font_warnings": doc.font_warnings,
                "fonttools": doc.fonttools,
                "ocr_engine": doc.ocr_engine,
                "pdf_note": doc.note,
            }
            return doc.text, meta

        # 1) arXiv：HTML > abs > PDF
        if paper.arxiv_id:
            add(f"https://arxiv.org/html/{paper.arxiv_id}", "html")
            add(f"https://arxiv.org/abs/{paper.arxiv_id}", "html")
            add(f"https://arxiv.org/pdf/{paper.arxiv_id}.pdf", "pdf")
        # 2) PMC
        pmc_id = str((paper.extra or {}).get("pmc_id") or "")
        if pmc_id:
            add(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc_id}/", "html")
        # 3) 來源提供的 fulltext/pdf/landing
        for url, kind in ((paper.fulltext_url, "auto"), (paper.pdf_url, "pdf"), (paper.url, "auto")):
            if not url:
                continue
            k = kind
            if k == "auto":
                k = "pdf" if str(url).lower().endswith(".pdf") else "html"
            add(url, k)

        best_text = ""
        best_meta: dict = {}
        for url, kind in candidates:
            result = self.fetcher.fetch(url, check_robots=self.robots_check)
            if not result.ok:
                continue
            ctype = (result.content_type or "").lower()
            is_pdf = kind == "pdf" or "pdf" in ctype or result.content[:4] == b"%PDF"
            if is_pdf:
                text, meta = parse_pdf(result.content)
            else:
                html = result.content.decode("utf-8", errors="replace")
                text = extract_text_from_html(html, max_length=max_chars)
                meta = {"kind": "html", "pages": 0, "ocr_pages": 0, "font_warnings": 0}
                # 若 landing page 文字不足，嘗試頁內 PDF 連結
                if len(text) < 1200:
                    for pdf_url in extract_pdf_urls(html, base_url=result.url or url):
                        if any(pdf_url == u for u, _ in candidates):
                            continue
                        pdf_result = self.fetcher.fetch(pdf_url, check_robots=self.robots_check)
                        if not pdf_result.ok:
                            continue
                        pdf_text, pdf_meta = parse_pdf(pdf_result.content)
                        if len(pdf_text) > len(text):
                            text = pdf_text
                            meta = pdf_meta
                            url = pdf_result.url or pdf_url
                            break
            if len(text) < 400:
                continue
            meta = dict(meta)
            meta["source"] = url
            if len(text) > len(best_text):
                best_text = text
                best_meta = meta
            # 已取得明確全文（通常遠大於摘要）即可提前結束
            if meta.get("kind") in {"pdf", "pdf+ocr"} and len(text) >= 3000:
                break
            if meta.get("kind") == "html" and len(text) >= 6000:
                break

        if best_text:
            paper.fulltext_excerpt = best_text[:max_chars]
            paper.parse_level = "fulltext"
            paper.extra["fulltext_source"] = str(best_meta.get("source", ""))
            paper.extra["fulltext_kind"] = str(best_meta.get("kind", ""))
            paper.extra["fulltext_pages"] = int(best_meta.get("pages") or 0)
            paper.extra["ocr_pages"] = int(best_meta.get("ocr_pages") or 0)
            paper.extra["font_warnings"] = int(best_meta.get("font_warnings") or 0)
            paper.extra["ocr_engine"] = str(best_meta.get("ocr_engine") or "")
            paper.extra["pdf_note"] = str(best_meta.get("pdf_note") or "")
            if not paper.code_url:
                codes = extract_github_urls(best_text)
                if codes:
                    paper.code_url = codes[0]
            return paper

    # fallback: abstract counts as parsed content if present
        if paper.abstract:
            paper.fulltext_excerpt = paper.abstract[:max_chars]
            if paper.parse_level == "metadata":
                paper.parse_level = "abstract"
        return paper
