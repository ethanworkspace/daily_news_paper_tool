"""論文內容解析：Atom/JSON/XML 對映、HTML 全文抽取、GitHub 連結偵測、IF 指標格式化。"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime
from html import unescape
from html.parser import HTMLParser
from typing import Any
from urllib.parse import urljoin, urlsplit

from collectors.news_parse import strip_html
from core.dedupe import extract_arxiv_id, normalize_doi
from core.timewin import parse_datetime

ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
GITHUB_RE = re.compile(
    r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)(?:[/?#][^\s\"'<>)]*)?",
    re.IGNORECASE,
)
DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_ABS_RE = re.compile(
    r"arxiv\.org/(?:abs|pdf|html)/([0-9]{4}\.[0-9]{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7}(?:v\d+)?)",
    re.IGNORECASE,
)

_SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "canvas", "header", "footer", "nav", "form"}
_BLOCK_TAGS = {
    "p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6",
    "tr", "td", "th", "blockquote", "section", "article", "pre", "hr",
}
_HEADING_TAGS = {"h1", "h2", "h3", "h4"}
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


@dataclass
class PaperCandidate:
    title: str
    url: str
    source_name: str = ""
    source_tier: int = 3
    published_at: datetime | None = None
    authors: list[str] = field(default_factory=list)
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
    fulltext_url: str = ""
    fulltext_excerpt: str = ""
    parse_level: str = "metadata"
    extra: dict[str, Any] = field(default_factory=dict)


class _FullTextExtractor(HTMLParser):
    def __init__(self, max_length: int = 40000) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0
        self.max_length = max_length
        self._length = 0
        self._stop = False

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        if self._stop:
            return
        tag = tag.lower()
        if tag in _SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth:
            return
        if tag in _HEADING_TAGS:
            self.parts.append("\n## ")
        elif tag in _BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in _SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
        elif tag in _BLOCK_TAGS and not self._skip_depth and not self._stop:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth or self._stop or not data:
            return
        self.parts.append(data)
        self._length += len(data)
        if self._length >= self.max_length:
            self._stop = True


def extract_text_from_html(raw: object, max_length: int = 40000) -> str:
    if not raw:
        return ""
    text = str(raw)
    if "<" not in text:
        text = unescape(text)
        text = _CONTROL_CHARS.sub(" ", text)
        return " ".join(text.split())[:max_length]
    parser = _FullTextExtractor(max_length=max_length)
    try:
        parser.feed(text)
        parser.close()
        text = "".join(parser.parts)
    except Exception:  # noqa: BLE001
        text = re.sub(r"<[^>]*>", " ", text)
    text = unescape(text)
    text = _CONTROL_CHARS.sub(" ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = "\n".join(line.strip() for line in text.splitlines()).strip()
    return text[:max_length]


def extract_pdf_document(raw: bytes | bytearray | None, **kwargs):
    """PDF 全文萃取（委派 collectors.pdf_text：pypdf + fontTools + RapidOCR）。"""
    from collectors.pdf_text import extract_pdf_document as _extract

    return _extract(raw, **kwargs)


def extract_text_from_pdf(
    raw: bytes | bytearray | None,
    max_length: int = 300000,
    max_pages: int | None = None,
    *,
    ocr: bool = True,
) -> str:
    """從 PDF bytes 萃取全文文字；預設不限頁數，掃描頁可自動 OCR。失敗回傳空字串。"""
    return extract_pdf_document(raw, max_length=max_length, max_pages=max_pages, ocr=ocr).text


def extract_github_urls(text: object) -> list[str]:
    if not text:
        return []
    urls: list[str] = []
    seen: set[str] = set()
    for match in GITHUB_RE.finditer(str(text)):
        owner, repo = match.group(1), match.group(2).rstrip(".")
        if repo.lower().endswith(".git"):
            repo = repo[:-4]
        if owner.lower() in {"topics", "collections", "features", "sponsors", "marketplace", "settings", "orgs"}:
            continue
        url = f"https://github.com/{owner}/{repo}"
        key = url.lower()
        if key not in seen:
            seen.add(key)
            urls.append(url)
    return urls


def first_github_url(text: object) -> str:
    urls = extract_github_urls(text)
    return urls[0] if urls else ""


def extract_pdf_urls(html: object, *, base_url: str = "") -> list[str]:
    """從 HTML 中找出可能的 PDF 連結（meta citation_pdf_url / a[href*pdf] / .pdf）。"""
    if not html:
        return []
    text = str(html)
    urls: list[str] = []
    seen: set[str] = set()

    def add(raw: str) -> None:
        value = (raw or "").strip().replace("&amp;", "&")
        if not value or value.lower().startswith(("javascript:", "mailto:", "data:")):
            return
        if base_url:
            value = urljoin(base_url, value)
        try:
            parts = urlsplit(value)
        except Exception:
            return
        if parts.scheme not in {"http", "https"} or not parts.netloc:
            return
        norm = parts._replace(fragment="").geturl()
        if norm.lower() in seen:
            return
        seen.add(norm.lower())
        urls.append(norm)

    for m in re.finditer(r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)["\']', text, re.IGNORECASE):
        add(m.group(1))
    for m in re.finditer(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url["\']', text, re.IGNORECASE):
        add(m.group(1))
    for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', text, re.IGNORECASE | re.DOTALL):
        href = m.group(1)
        label = re.sub(r"<[^>]+>", " ", m.group(2) or " ")
        label = " ".join(label.split()).lower()
        href_low = href.lower()
        if ".pdf" in href_low or "pdf" in label or "download" in label:
            add(href)
    for m in re.finditer(r'https?://[^\s"\'<>]+\.pdf(?:\?[^\s"\'<>]*)?', text, re.IGNORECASE):
        add(m.group(0))
    return urls[:12]


def extract_doi(text: object) -> str:
    if not text:
        return ""
    match = DOI_RE.search(str(text))
    return normalize_doi(match.group(0)) if match else ""


def arxiv_id_from_text(text: object) -> str:
    if not text:
        return ""
    found = extract_arxiv_id(text)
    if found:
        return found
    match = ARXIV_ABS_RE.search(str(text))
    return extract_arxiv_id(match.group(1)) if match else ""


def parse_authors(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        parts = re.split(r",|\band\b|;|\n", value)
        return [p.strip() for p in parts if p.strip()][:20]
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            if isinstance(item, str):
                out.append(item.strip())
            elif isinstance(item, dict):
                name = item.get("name") or item.get("display_name") or item.get("raw_author_name") or ""
                if not name:
                    given = item.get("given", "")
                    family = item.get("family", "")
                    name = f"{given} {family}".strip()
                if name:
                    out.append(str(name).strip())
            if len(out) >= 20:
                break
        return [x for x in out if x]
    return []


def format_impact_factor(summary_stats: dict | None, source_name: str = "") -> tuple[str, str]:
    """回傳 (impact_factor文字, 來源說明)。使用 OpenAlex 免費指標，不冒充 JCR IF。"""
    stats = summary_stats or {}
    parts: list[str] = []
    citedness = stats.get("2yr_mean_citedness")
    h_index = stats.get("h_index")
    i10 = stats.get("i10_index")
    if citedness not in (None, ""):
        try:
            parts.append(f"2yr_mean_citedness={float(citedness):.2f}")
        except (TypeError, ValueError):
            parts.append(f"2yr_mean_citedness={citedness}")
    if h_index not in (None, ""):
        parts.append(f"h_index={h_index}")
    if i10 not in (None, ""):
        parts.append(f"i10_index={i10}")
    if not parts:
        return ("N/A", "")
    label = f"{', '.join(parts)} (OpenAlex)"
    origin = f"OpenAlex source summary_stats{': ' + source_name if source_name else ''}"
    return label, origin


def parts_non_na(value: str) -> bool:
    return bool(value) and value.strip().upper() != "N/A" and not value.strip().startswith("N/A (")


def _venue_has(text: str, token: str) -> bool:
    token = token.lower().strip()
    if not token:
        return False
    # 單字 "science" 太寬泛（會命中 applied/measurement/computer science 等），需特判為期刊 Science
    if token == "science":
        if not re.search(r"(?<![a-z])science(?![a-z])", text):
            return False
        excluded = (
            "applied science", "computer science", "measurement science", "materials science",
            "environmental science", "data science", "information science", "life science",
            "food science", "animal science", "plant science", "soil science", "sport science",
            "social science", "political science", "cognitive science", "management science",
            "decision science", "health science", "veterinary science", "earth science",
            "marine science", "surface science", "space science", "forensic science",
            "engineering science", "pharmaceutical science", "advance",  # science advances -> tier2
        )
        return not any(x in text for x in excluded)
    # "nature" 也可能出現在 "nature communications" 等子刊，但 TIER1 目標為 Nature 本刊；
    # 子刊多在其他層級，這裡保守比對獨立出現且非已知子刊詞時才可能命中（實務上 TIER1 多為頂刊名）
    if token == "nature":
        if not re.search(r"(?<![a-z])nature(?![a-z])", text):
            return False
        # 常見 Nature 子刊/衍生刊名保留給一般處理（多數仍屬高品質，若需細分可擴充 TIER2）
        return "human behaviour" not in text
    if " " in token:
        return token in text
    return bool(re.search(rf"(?<![a-z0-9]){re.escape(token)}(?![a-z0-9])", text))


def venue_tier(journal: str = "", venue: str = "", source_name: str = "") -> int:
    from config import TIER1_VENUES, TIER2_VENUES

    text = f"{journal} {venue} {source_name}".lower()
    if any(_venue_has(text, token) for token in TIER1_VENUES):
        return 1
    if any(_venue_has(text, token) for token in TIER2_VENUES):
        return 2
    if "arxiv" in text or "biorxiv" in text or "medrxiv" in text or "preprint" in text:
        return 3
    return 2


def canonical_venue(journal: str = "", venue: str = "", url: str = "") -> str:
    """回傳較適合顯示的期刊/會議名稱；避免將 arXiv 等 preprint 誤標為期刊。"""
    preprint_tokens = ("arxiv", "biorxiv", "medrxiv", "preprint")
    for c in (str(journal or "").strip(), str(venue or "").strip()):
        low = c.lower()
        if not c or any(token in low for token in preprint_tokens):
            continue
        return c
    low_url = (url or "").lower()
    if "biorxiv.org" in low_url:
        return "bioRxiv preprint"
    if "medrxiv.org" in low_url:
        return "medRxiv preprint"
    if "arxiv.org" in low_url:
        return "arXiv preprint"
    for c in (str(journal or "").strip(), str(venue or "").strip()):
        if c:
            return c
    return ""


def _atom_text(elem: ET.Element | None) -> str:
    if elem is None:
        return ""
    try:
        return ET.tostring(elem, encoding="unicode", method="text").strip()
    except Exception:  # noqa: BLE001
        return (elem.text or "").strip()


def parse_arxiv_atom(content: bytes) -> list[PaperCandidate]:
    if not content:
        return []
    if b"<!entity" in content[:8192].lower():
        return []
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return []
    papers: list[PaperCandidate] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        title = " ".join(_atom_text(entry.find("atom:title", ATOM_NS)).split())
        if not title:
            continue
        abs_url = _atom_text(entry.find("atom:id", ATOM_NS))
        arxiv_id = arxiv_id_from_text(abs_url)
        published = parse_datetime(
            _atom_text(entry.find("atom:published", ATOM_NS)) or _atom_text(entry.find("atom:updated", ATOM_NS))
        )
        abstract = " ".join(_atom_text(entry.find("atom:summary", ATOM_NS)).split())
        comment = _atom_text(entry.find("arxiv:comment", ATOM_NS))
        doi = normalize_doi(_atom_text(entry.find("arxiv:doi", ATOM_NS)) or extract_doi(abs_url))
        authors = [
            " ".join(_atom_text(name).split())
            for name in entry.findall("atom:author/atom:name", ATOM_NS)
            if " ".join(_atom_text(name).split())
        ][:20]
        pdf_url = ""
        for link in entry.findall("atom:link", ATOM_NS):
            href = (link.attrib.get("href") or "").strip()
            if link.attrib.get("title") == "pdf" or href.endswith(".pdf") or "/pdf/" in href:
                if "/pdf/" in href and not href.endswith(".pdf"):
                    href = href + ".pdf"
                pdf_url = href
            elif not abs_url and link.attrib.get("rel") == "alternate":
                abs_url = href
        if not pdf_url and abs_url and "/abs/" in abs_url:
            pdf_url = abs_url.replace("/abs/", "/pdf/") + ".pdf"
        code_url = first_github_url(f"{comment}\n{abstract}")
        papers.append(
            PaperCandidate(
                title=title,
                url=abs_url or (f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else ""),
                source_name="arXiv",
                source_tier=3,
                published_at=published,
                authors=authors,
                abstract=abstract,
                pdf_url=pdf_url,
                code_url=code_url,
                doi=doi,
                arxiv_id=arxiv_id,
                journal="arXiv",
                venue=canonical_venue(journal="", venue="arXiv preprint", url=abs_url),
                impact_factor="N/A (preprint)",
                impact_factor_source="arXiv preprint (not peer-reviewed journal/conference)",
                fulltext_url=(f"https://arxiv.org/html/{arxiv_id}" if arxiv_id else ""),
                parse_level="abstract" if abstract else "metadata",
            )
        )
    return papers


def rebuild_inverted_abstract(inv: Any) -> str:
    if not inv or not isinstance(inv, dict):
        return ""
    try:
        size = 1 + max(pos for positions in inv.values() for pos in positions)
        arr = [""] * size
        for word, positions in inv.items():
            for pos in positions:
                if 0 <= pos < size:
                    arr[pos] = str(word)
        return " ".join(w for w in arr if w)
    except Exception:  # noqa: BLE001
        return ""


def parse_openalex_work(work: dict, *, source_stats_cache: dict[str, dict] | None = None) -> PaperCandidate | None:
    if not isinstance(work, dict):
        return None
    title = " ".join(str(work.get("title") or work.get("display_name") or "").split())
    if not title:
        return None
    doi = normalize_doi(work.get("doi") or (work.get("ids") or {}).get("doi") or "")
    arxiv_id = arxiv_id_from_text((work.get("ids") or {}).get("arxiv") or work.get("id") or "")
    primary = work.get("primary_location") or {}
    best = work.get("best_oa_location") or {}
    source = primary.get("source") or best.get("source") or {}
    journal = str(source.get("display_name") or "")
    venue = journal
    source_id = str(source.get("id") or "")
    stats = (source_stats_cache or {}).get(source_id) or source.get("summary_stats") or {}
    impact_factor, impact_source = format_impact_factor(stats if isinstance(stats, dict) else {}, journal)
    if source.get("type") == "repository" and not parts_non_na(impact_factor):
        impact_factor = "N/A (repository/preprint)"
        impact_source = impact_source or "Repository source has no journal impact factor"

    url = primary.get("landing_page_url") or best.get("landing_page_url") or doi or work.get("id") or ""
    if doi and not str(url).startswith("http"):
        url = f"https://doi.org/{doi}"
    pdf_url = best.get("pdf_url") or primary.get("pdf_url") or ""
    oa_url = (work.get("open_access") or {}).get("oa_url") or ""
    fulltext_url = best.get("landing_page_url") or oa_url or url
    authors = [a.get("author", {}).get("display_name", "") for a in (work.get("authorships") or [])]
    authors = [str(a).strip() for a in authors if str(a).strip()][:20]
    abstract = rebuild_inverted_abstract(work.get("abstract_inverted_index"))
    cited = int(work.get("cited_by_count") or 0)
    published = parse_datetime(work.get("publication_date") or work.get("publication_year"))

    locations = work.get("locations") or []
    for loc in locations:
        landing = str(loc.get("landing_page_url") or "")
        if not arxiv_id and "arxiv.org" in landing:
            arxiv_id = arxiv_id_from_text(landing)
        if not pdf_url and loc.get("pdf_url"):
            pdf_url = str(loc.get("pdf_url") or "")

    display_venue = canonical_venue(journal=journal, venue=venue, url=str(url))
    src_name = journal or display_venue or ("arXiv" if arxiv_id else "OpenAlex")

    candidate = PaperCandidate(
        title=title,
        url=str(url),
        source_name=src_name,
        source_tier=venue_tier(journal=journal, venue=display_venue, source_name=source.get("type", "")),
        published_at=published,
        authors=authors,
        abstract=abstract,
        pdf_url=str(pdf_url or ""),
        doi=doi,
        arxiv_id=arxiv_id,
        journal=journal,
        venue=display_venue,
        impact_factor=impact_factor,
        impact_factor_source=impact_source,
        cited_by_count=cited,
        fulltext_url=str(fulltext_url or ""),
        parse_level="abstract" if abstract else "metadata",
        extra={"openalex_id": work.get("id", ""), "source_id": source_id},
    )
    if arxiv_id:
        journal_text = f"{journal} {display_venue}".lower()
        source_type = str(source.get("type") or "").lower()
        is_preprint_source = (
            source_type == "repository"
            or "arxiv" in journal_text
            or "biorxiv" in journal_text
            or "medrxiv" in journal_text
        )
        if is_preprint_source or not journal:
            candidate.source_tier = 3
            if not candidate.venue or "arxiv" in candidate.venue.lower():
                candidate.venue = "arXiv preprint"
            if candidate.impact_factor in ("", "N/A"):
                candidate.impact_factor = "N/A (preprint)"
                candidate.impact_factor_source = "preprint (not peer-reviewed journal/conference)"
    return candidate


def parse_semantic_scholar_paper(paper: dict) -> PaperCandidate | None:
    if not isinstance(paper, dict):
        return None
    title = " ".join(str(paper.get("title") or "").split())
    if not title:
        return None
    external = paper.get("externalIds") or {}
    doi = normalize_doi(external.get("DOI") or external.get("doi") or "")
    arxiv_id = arxiv_id_from_text(external.get("ArXiv") or external.get("arxiv") or "")
    year = paper.get("year")
    pub_date = paper.get("publicationDate") or (f"{year}-01-01" if year else None)
    published = parse_datetime(pub_date)
    authors = [a.get("name", "") for a in (paper.get("authors") or []) if isinstance(a, dict)]
    authors = [str(a).strip() for a in authors if str(a).strip()][:20]
    journal_obj = paper.get("journal") or {}
    journal = ""
    if isinstance(journal_obj, dict):
        journal = str(journal_obj.get("name") or "")
    elif isinstance(journal_obj, str):
        journal = journal_obj
    venue = str(paper.get("venue") or journal or "")
    display_venue = canonical_venue(journal=journal, venue=venue, url=str(paper.get("url") or ""))
    pdf_url = ""
    if isinstance(paper.get("openAccessPdf"), dict):
        pdf_url = str(paper["openAccessPdf"].get("url") or "")
    url = str(paper.get("url") or "")
    if not url and doi:
        url = f"https://doi.org/{doi}"
    if not url and arxiv_id:
        url = f"https://arxiv.org/abs/{arxiv_id}"
    abstract = " ".join(str(paper.get("abstract") or "").split())
    cited = int(paper.get("citationCount") or 0)
    code_url = first_github_url(f"{abstract}\n{url}")
    preprint_venue = any(
        token in f"{journal} {display_venue}".lower()
        for token in ("arxiv", "biorxiv", "medrxiv", "preprint")
    )
    peer_reviewed = bool(display_venue or journal) and not preprint_venue
    impact = "N/A" if peer_reviewed else "N/A (preprint)"
    impact_source = "" if peer_reviewed else "preprint (not peer-reviewed journal/conference)"
    return PaperCandidate(
        title=title,
        url=url,
        source_name=(journal if peer_reviewed and journal else display_venue) or "Semantic Scholar",
        source_tier=venue_tier(journal=journal, venue=display_venue) if peer_reviewed else 3,
        published_at=published,
        authors=authors,
        abstract=abstract,
        pdf_url=pdf_url,
        code_url=code_url,
        doi=doi,
        arxiv_id=arxiv_id,
        journal=journal,
        venue=display_venue,
        impact_factor=impact,
        impact_factor_source=impact_source,
        cited_by_count=cited,
        fulltext_url=pdf_url or url,
        parse_level="abstract" if abstract else "metadata",
    )

def parse_pubmed_xml(content: bytes) -> list[PaperCandidate]:
    if not content:
        return []
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return []
    papers: list[PaperCandidate] = []
    for article in root.findall(".//PubmedArticle"):
        title_el = article.find("MedlineCitation/Article/ArticleTitle")
        title = " ".join("".join(title_el.itertext()).split()) if title_el is not None else ""
        if not title:
            continue
        pmid = (article.findtext("MedlineCitation/PMID", "") or "").strip()
        journal = " ".join((article.findtext("MedlineCitation/Article/Journal/Title", "") or "").split())
        year = article.findtext("MedlineCitation/Article/Journal/JournalIssue/PubDate/Year", "") or ""
        medline_date = article.findtext("MedlineCitation/Article/Journal/JournalIssue/PubDate/MedlineDate", "") or ""
        month = (article.findtext("MedlineCitation/Article/Journal/JournalIssue/PubDate/Month", "") or "01").strip()
        day = (article.findtext("MedlineCitation/Article/Journal/JournalIssue/PubDate/Day", "") or "01").strip()
        if not year and medline_date:
            m = re.search(r"(19|20)\d{2}", medline_date)
            year = m.group(0) if m else ""
        published = None
        if year:
            month_map = {
                "jan": "01", "feb": "02", "mar": "03", "apr": "04", "may": "05", "jun": "06",
                "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12",
            }
            month_key = month[:3].lower()
            month_num = month.zfill(2) if month.isdigit() else month_map.get(month_key, "01")
            day_num = day.zfill(2) if day.isdigit() else "01"
            published = parse_datetime(f"{year}-{month_num}-{day_num}")
            if published is None:
                published = parse_datetime(medline_date or year)

        abstract_parts = []
        for at in article.findall("MedlineCitation/Article/Abstract/AbstractText"):
            label = at.attrib.get("Label", "")
            text = " ".join("".join(at.itertext()).split())
            if text:
                abstract_parts.append(f"{label}: {text}" if label else text)
        abstract = " ".join(abstract_parts)

        authors: list[str] = []
        for author in article.findall("MedlineCitation/Article/AuthorList/Author"):
            last = author.findtext("LastName", "") or ""
            fore = author.findtext("ForeName", "") or author.findtext("Initials", "") or ""
            coll = author.findtext("CollectiveName", "") or ""
            name = coll or f"{fore} {last}".strip()
            if name:
                authors.append(name)
        authors = authors[:20]

        doi = ""
        for aid in article.findall(".//ELocationID"):
            if aid.attrib.get("EIdType") == "doi":
                doi = normalize_doi(aid.text or "")
        if not doi:
            for aid in article.findall("PubmedData/ArticleIdList/ArticleId"):
                if aid.attrib.get("IdType") == "doi":
                    doi = normalize_doi(aid.text or "")

        pmc_id = ""
        for aid in article.findall("PubmedData/ArticleIdList/ArticleId"):
            if aid.attrib.get("IdType") == "pmc":
                pmc_id = (aid.text or "").strip()
        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else (f"https://doi.org/{doi}" if doi else "")
        pdf_url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc_id}/" if pmc_id else ""

        papers.append(
            PaperCandidate(
                title=title,
                url=url,
                source_name=journal or "PubMed",
                source_tier=venue_tier(journal=journal),
                published_at=published,
                authors=authors,
                abstract=abstract,
                pdf_url=pdf_url,
                doi=doi,
                journal=journal,
                venue=journal,
                impact_factor="N/A",
                impact_factor_source="",
                cited_by_count=0,
                fulltext_url=pdf_url or url,
                parse_level="abstract" if abstract else "metadata",
                extra={"pmid": pmid, "pmc_id": pmc_id},
            )
        )
    return papers
