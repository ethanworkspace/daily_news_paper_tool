import re
import time
import xml.etree.ElementTree as ET
import requests

from config import MAILTO_CONTACT, SEMANTIC_SCHOLAR_API_KEY

SCHOLAR_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}
GOOGLE_BLOCK_PATTERNS = [
    "unusual traffic",
    "not a robot",
    "Enable JavaScript",
    "enablejs",
    "captcha",
    "challenge platform",
    "sorry",
]

PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def _norm_title(title: str) -> str:
    return re.sub(r"\W+", "", (title or "").lower())


def _match_keywords(text: str, keywords: list[str]) -> bool:
    if not keywords:
        return True
    lower_text = (text or "").lower()
    return any(kw in lower_text for kw in keywords)


def _paper_relevance_score(title: str, abstract: str, keywords: list[str]) -> int:
    """論文對題計分：標題命中 3 分，摘要命中 1 分。回傳 0 表示不符合主題"""
    if not keywords:
        return 1
    score = 0
    if any(kw in (title or "").lower() for kw in keywords):
        score += 3
    if any(kw in (abstract or "").lower() for kw in keywords):
        score += 1
    return score


def _dedupe(papers: list[dict], seen: set | None = None) -> list[dict]:
    if seen is None:
        seen = set()
    out = []
    for p in papers:
        key = _norm_title(p.get("title"))
        if key and key not in seen:
            seen.add(key)
            out.append(p)
    return out


def _shrink_authors(authors: list) -> str:
    if not authors:
        return "未知作者"
    text = ", ".join(authors)
    if len(authors) > 5:
        text = ", ".join(authors[:5]) + " et al."
    return text


def _safe_json(response, label):
    try:
        return response.json()
    except Exception:
        print(f"[Scholar Collect] {label} 回傳非 JSON，略過此來源")
        return None


# ------------------------- Google Scholar (HTML 爬蟲，備援性質) -------------------------
def search_google_scholar(query: str, count: int = 5, patience: int = 1) -> list[dict]:
    """嘗試 Google Scholar 一般搜尋。Google 對自動化爬蟲有嚴格限制
    (robots.txt 明禁 /scholar、可能回 429/CAPTCHA)，
    被阻擋時請呼叫端自動改用其他來源，不回傳假資料。"""
    print("[Scholar Collect] 嘗試 Google Scholar ...")
    for _ in range(max(patience, 1)):
        time.sleep(3)
        try:
            response = requests.get(
                "https://scholar.google.com/scholar",
                params={"q": query, "hl": "zh-TW", "start": 0},
                headers=SCHOLAR_HEADERS,
                timeout=15,
            )
        except Exception as e:
            print(f"[Scholar Collect] Google Scholar 請求失敗: {e}")
            return []

        if response.status_code not in (200, 201):
            print(f"[Scholar Collect] Google Scholar 被阻擋 (HTTP {response.status_code})，改用後續來源。")
            return []

        lowered = response.text.lower()
        if any(pat in lowered for pat in GOOGLE_BLOCK_PATTERNS):
            print("[Scholar Collect] Google Scholar 出現驗證頁/阻擋頁，改用後續來源。")
            return []

        papers = _parse_scholar_html(response.text)
        if papers:
            print(f"[Scholar Collect] Google Scholar 成功取得 {len(papers)} 篇")
            return _dedupe(papers)[:count]
        print("[Scholar Collect] Google Scholar 未解析到結果，改用後續來源。")
        return []


def _parse_scholar_html(html: str) -> list[dict]:
    blocks = re.split(r'<div class="gs_r', html)[1:]
    papers = []
    for block in blocks:
        title_match = re.search(r'class="gs_rt[^"]*">.*?<a href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if not title_match:
            continue
        title = re.sub(r"<.*?>", "", title_match.group(2))
        title = " ".join(title.split())
        link = title_match.group(1)
        if link.startswith("/"):
            link = "https://scholar.google.com" + link
        meta_match = re.search(r'class="gs_a">(.*?)</div>', block, re.S)
        meta = re.sub(r"<.*?>", "", meta_match.group(1)) if meta_match else ""
        meta = " ".join(meta.split())
        snippet_match = re.search(r'class="gs_rs">(.*?)</div>', block, re.S)
        abstract = " ".join(re.sub(r"<.*?>", "", snippet_match.group(1)).split()) if snippet_match else ""

        year_match = re.search(r"\b(19|20)\d{2}\b", meta)
        year = year_match.group(0) if year_match else ""
        parts = [p.strip() for p in meta.split("-") if p.strip()]
        authors = parts[0] if parts else "未知作者"
        journal = " - ".join(parts[1:]).strip(" -")
        journal = re.sub(r"[,，].*$", "", journal).strip(" -")

        papers.append({
            "title": title,
            "authors": authors,
            "published": year,
            "abstract": abstract,
            "url": link,
            "pdf_url": "",
            "project_url": "",
            "journal": journal,
            "source_db": "Google Scholar",
        })
    return papers


# ------------------------- Semantic Scholar API -------------------------
def search_semantic_scholar(query: str, count: int = 5) -> list[dict]:
    print("[Scholar Collect] 嘗試 Semantic Scholar API ...")
    headers = {}
    if SEMANTIC_SCHOLAR_API_KEY:
        headers["x-api-key"] = SEMANTIC_SCHOLAR_API_KEY
    try:
        response = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": query,
                "limit": min(count, 100),
                "fields": "title,abstract,year,venue,journal,url,externalIds,openAccessPdf,authors",
            },
            headers=headers,
            timeout=25,
        )
    except Exception as e:
        print(f"[Scholar Collect] Semantic Scholar 請求失敗: {e}")
        return []
    if response.status_code != 200:
        print(f"[Scholar Collect] Semantic Scholar 回傳 HTTP {response.status_code}，改用後續來源。")
        return []
    data = _safe_json(response, "Semantic Scholar") or {}
    papers = []
    for item in data.get("data", []) or []:
        journal = item.get("journal") or {}
        journal_name = ""
        if isinstance(journal, dict):
            journal_name = journal.get("name", "")
        elif isinstance(journal, str):
            journal_name = journal
        journal_name = journal_name or item.get("venue", "")
        pdf = ""
        if item.get("openAccessPdf"):
            pdf = (item.get("openAccessPdf") or {}).get("url", "")
        year = item.get("year") or ""
        papers.append({
            "title": item.get("title", ""),
            "authors": _shrink_authors([a.get("name", "") for a in item.get("authors", []) or []]),
            "published": str(year) if year else "",
            "abstract": item.get("abstract") or "",
            "url": item.get("url", ""),
            "pdf_url": pdf,
            "project_url": "",
            "journal": journal_name,
            "source_db": "Semantic Scholar",
        })
    return _dedupe(papers)[:count]


# ------------------------- OpenAlex API -------------------------
def search_openalex(query: str, count: int = 5) -> list[dict]:
    print("[Scholar Collect] 嘗試 OpenAlex API ...")
    try:
        response = requests.get(
            "https://api.openalex.org/works",
            params={"search": query, "per-page": min(count, 50), "mailto": MAILTO_CONTACT},
            timeout=25,
        )
    except Exception as e:
        print(f"[Scholar Collect] OpenAlex 請求失敗: {e}")
        return []
    if response.status_code != 200:
        print(f"[Scholar Collect] OpenAlex 回傳 HTTP {response.status_code}，改用後續來源。")
        return []
    data = _safe_json(response, "OpenAlex") or {}
    papers = []
    for item in data.get("results", []) or []:
        title = item.get("title") or item.get("display_name") or ""
        abstract = _rebuild_inverted_abstract(item.get("abstract_inverted_index"))
        authors = _shrink_authors([
            (a.get("author") or {}).get("display_name", "") for a in item.get("authorships", []) or []
        ])
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        journal = source.get("display_name", "") or ""
        best = item.get("best_oa_location") or {}
        pdf = best.get("pdf_url") or primary.get("pdf_url") or ""
        doi = item.get("doi", "")
        papers.append({
            "title": title,
            "authors": authors,
            "published": str(item.get("publication_year") or ""),
            "abstract": abstract,
            "url": primary.get("landing_page_url") or doi or "",
            "pdf_url": pdf,
            "project_url": "",
            "journal": journal,
            "source_db": "OpenAlex",
        })
    return _dedupe(papers)[:count]


def _rebuild_inverted_abstract(inv: dict) -> str:
    if not inv:
        return ""
    try:
        size = 1 + max(p for positions in inv.values() for p in positions)
        arr = [""] * size
        for word, positions in inv.items():
            for pos in positions:
                arr[pos] = word
        return " ".join(word for word in arr if word)
    except Exception:
        return ""


# ------------------------- PubMed (E-utilities) -------------------------
def search_pubmed(query: str, count: int = 5) -> list[dict]:
    print("[Scholar Collect] 嘗試 PubMed (NCBI E-utilities) ...")
    try:
        esearch = requests.get(
            PUBMED_BASE + "/esearch.fcgi",
            params={
                "db": "pubmed",
                "term": query,
                "retmode": "json",
                "retmax": min(count, 20),
                "tool": "DailyAIReport",
                "email": MAILTO_CONTACT,
            },
            timeout=25,
        )
        if esearch.status_code != 200:
            print(f"[Scholar Collect] PubMed esearch 回傳 HTTP {esearch.status_code}")
            return []
        id_list = (esearch.json().get("esearchresult") or {}).get("idlist", [])
        if not id_list:
            return []
        time.sleep(0.35)
        efetch = requests.get(
            PUBMED_BASE + "/efetch.fcgi",
            params={"db": "pubmed", "id": ",".join(id_list), "retmode": "xml"},
            timeout=25,
        )
        if efetch.status_code != 200:
            print(f"[Scholar Collect] PubMed efetch 回傳 HTTP {efetch.status_code}")
            return []
        return _parse_pubmed_xml(efetch.content)[:count]
    except Exception as e:
        print(f"[Scholar Collect] PubMed 請求失敗: {e}")
        return []


def _parse_pubmed_xml(content: bytes) -> list[dict]:
    papers = []
    try:
        root = ET.fromstring(content)
    except Exception as e:
        print(f"[Scholar Collect] PubMed XML 解析失敗: {e}")
        return []
    for article in root.findall(".//PubmedArticle"):
        try:
            medline = article.find("MedlineCitation")
            if medline is None:
                continue
            pmid = medline.findtext("PMID", "").strip()
            title = " ".join("".join(
                (article.findtext("MedlineCitation/Article/ArticleTitle", "")
                 or "").split())) or ""

            title_text = ""
            title_elem = article.find("MedlineCitation/Article/ArticleTitle")
            if title_elem is not None:
                title_text = " ".join("".join(title_elem.itertext()).split())

            journal = " ".join((article.findtext(
                "MedlineCitation/Article/Journal/Title", "") or "").split())
            year = (article.findtext(
                "MedlineCitation/Article/Journal/JournalIssue/PubDate/Year", "")
                or article.findtext(
                "MedlineCitation/Article/Journal/JournalIssue/PubDate/MedlineDate", "")
                or "")
            year = re.sub(r"\D.*$", "", year)

            abstract_parts = []
            for at in article.findall("MedlineCitation/Article/Abstract/AbstractText"):
                label = at.get("Label", "")
                text = " ".join("".join(at.itertext()).split())
                abstract_parts.append(f"{label}: {text}" if label else text)
            abstract = " ".join(abstract_parts)

            authors = []
            for author in article.findall("MedlineCitation/Article/AuthorList/Author"):
                last = author.findtext("LastName", "") or ""
                fore = author.findtext("ForeName", "") or ""
                name = f"{fore} {last}".strip()
                if name:
                    authors.append(name)

            doi = ""
            for aid in article.findall(".//MedlineCitation/Article/ELocationID"):
                if aid.get("EIdType") == "doi":
                    doi = aid.text or ""
                    break
            if not doi:
                for aid in article.findall("PubmedData/ArticleIdList/ArticleId"):
                    if aid.get("IdType") == "doi":
                        doi = aid.text or ""
                        break

            url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}" if pmid else ""
            if not title_text:
                continue
            papers.append({
                "title": title_text,
                "authors": _shrink_authors(authors),
                "published": year,
                "abstract": abstract,
                "url": url,
                "pdf_url": "",
                "project_url": "",
                "journal": journal,
                "source_db": "PubMed",
            })
        except Exception:
            continue
    return _dedupe(papers)


# ------------------------- 多來源合併收集 -------------------------
def collect_papers_multisource(
    arxiv_query: str,
    count: int = 5,
    category: str = "cs.AI",
    word_query: str = "",
    keywords: list[str] | None = None,
    enable_google_scholar: bool = True,
) -> list[dict]:
    """依序從多個來源收集論文，去重後填滿 count 篇：
    1. arXiv (優先含 GitHub 專案連結的論文)
    2. Google Scholar (HTML，被阻擋即跳過)
    3. Semantic Scholar API
    4. OpenAlex API
    5. PubMed (適用於醫療/生醫相關主題)
    學術資料庫來源 (Google Scholar/Semantic Scholar/OpenAlex/PubMed) 會依 keywords
    嚴格過濾，確保論文符合當日主題；arXiv 本身以分類/檢索詞限縮範疇。
    """
    from collectors.arxiv_collector import collect_papers

    keywords = keywords or []

    seen: set = set()
    papers: list[dict] = []

    arxiv_papers = collect_papers(arxiv_query, count=count, category=category)
    for p in arxiv_papers:
        p["source_db"] = "arXiv"
        p.setdefault("journal", "")
    papers.extend(_dedupe(arxiv_papers, seen))
    if len(papers) >= count:
        return papers[:count]

    need = count - len(papers)
    if word_query:
        chains = []
        if enable_google_scholar:
            chains.append(search_google_scholar)
        chains += [search_semantic_scholar, search_openalex, search_pubmed]
        for fetcher in chains:
            if len(papers) >= count:
                break
            try:
                extra = _dedupe(fetcher(word_query, need * 4), seen)
            except Exception as e:
                print(f"[Scholar Collect] {getattr(fetcher, '__name__', '來源')} 執行失敗: {e}")
                extra = []
            if keywords:
                before = len(extra)
                extra = [p for p in extra if _paper_relevance_score(
                    p.get("title", ""), p.get("abstract", ""), keywords) > 0]
                extra.sort(key=lambda p: -_paper_relevance_score(
                    p.get("title", ""), p.get("abstract", ""), keywords))
                print(f"[Scholar Collect] 對題過濾：{before} -> {len(extra)} 篇")
            papers.extend(extra)

    return _dedupe(papers)[:count]