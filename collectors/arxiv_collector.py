import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
import requests

ARXIV_NS = {"arxiv": "http://arxiv.org/schemas/atom"}
GITHUB_RE = re.compile(
    r"https?://(?:www\.)?github\.com/([A-Za-z0-9_.\-]+)/([A-Za-z0-9_.\-]+)", re.IGNORECASE
)


def _extract_github_url(text: str) -> str:
    """從論文 Comments/Abstract 中擷取 GitHub 專案根網址 (回傳空字串表示無)"""
    if not text:
        return ""
    match = GITHUB_RE.search(text)
    if not match:
        return ""
    owner, repo = match.group(1), match.group(2)
    return f"https://github.com/{owner}/{repo}".rstrip("/.")


def _build_paper(title, authors, published, abstract, paper_id, pdf_url, comment="") -> dict:
    project_url = _extract_github_url(comment) or _extract_github_url(abstract)
    return {
        "title": title,
        "authors": authors,
        "published": published,
        "abstract": abstract,
        "comment": " ".join(comment.split()) if comment else "",
        "project_url": project_url,
        "url": paper_id,
        "pdf_url": pdf_url,
    }


def _prioritize_github(papers: list[dict], count: int) -> list[dict]:
    """排序策略：優先保留含有 GitHub 專案連結的論文，其次再補一般論文"""
    with_github = [p for p in papers if p.get("project_url")]
    without_github = [p for p in papers if not p.get("project_url")]
    return (with_github + without_github)[:count]


def collect_papers_rss(category: str, count: int = 5) -> list[dict]:
    """使用 arXiv 官方即時 RSS 來源抓取最新論文（極速、高可用、無 429 限制）"""
    print(f"[arXiv Collector] 正在從 arXiv RSS ({category}) 獲取最新論文...")
    url = f"https://rss.arxiv.org/rss/{category}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            return []

        root = ET.fromstring(response.content)
        items = root.findall(".//item")
        papers = []
        today_str = datetime.now().strftime("%Y-%m-%d")

        for item in items:
            title_elem = item.find("title")
            link_elem = item.find("link")
            desc_elem = item.find("description")
            creator_elem = item.find("{http://purl.org/dc/elements/1.1/}creator")

            title = (title_elem.text or "").strip() if title_elem is not None else ""
            link = (link_elem.text or "").strip() if link_elem is not None else ""

            # 跳過 arXiv 維護期產生的空殼項目（標題/連結為空）
            if not title or not link or ("arxiv.org" not in link):
                continue

            title = " ".join(title.split())
            pdf_url = link.replace("/abs/", "/pdf/") + ".pdf" if "/abs/" in link else link

            raw_desc = desc_elem.text if desc_elem is not None else ""
            clean_desc = re.sub(r"<.*?>", "", raw_desc)
            if "Abstract:" in clean_desc:
                clean_desc = clean_desc.split("Abstract:", 1)[1]
            abstract = " ".join(clean_desc.split())

            authors = creator_elem.text if creator_elem is not None else ""
            if not authors:
                authors = "arXiv Researcher"

            paper = _build_paper(title, authors, today_str, abstract, link, pdf_url)
            papers.append(paper)

            if len(papers) >= count * 10:
                break

        papers = _prioritize_github(papers, count)
        print(f"[arXiv Collector] 透過 RSS 成功獲取 {len(papers)} 篇論文")
        return papers
    except Exception as e:
        print(f"[arXiv Collector] RSS 抓取失敗: {e}")
        return []


def collect_papers(query: str, count: int = 5, category: str = "cs.AI", max_retries: int = 5) -> list[dict]:
    """檢索 arXiv 論文：優先使用 API 查詢，並優先挑選含 GitHub 專案連結的論文。
    遭遇 429 速率限制時以指數退避重試（尊重 Retry-After），失敗或超時時自動由官方 RSS 備援。"""
    print(f"[arXiv Collector] 正在檢索論文：{query} (目標: {count} 篇，優先含 GitHub 專案)")
    pool_size = min(max(count * 5, 15), 100)
    encoded_query = urllib.parse.quote(query)
    url = (
        f"https://export.arxiv.org/api/query?"
        f"search_query={encoded_query}&"
        f"sortBy=submittedDate&"
        f"sortOrder=descending&"
        f"max_results={pool_size}"
    )

    headers = {
        "User-Agent": "DailyNewsPaperAgent/1.0 (mailto:daily_agent@nkust.edu.tw; academic bot)",
        "Accept": "application/atom+xml",
    }

    response = None
    for attempt in range(max_retries):
        if attempt > 0:
            backoff = 3 * (2 ** (attempt - 1))  # 3,6,12,24...
            time.sleep(backoff)
        try:
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                break
            elif response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                wait = int(retry_after) if retry_after and retry_after.isdigit() else 3 * (2 ** attempt)
                print(f"[arXiv Collector] 遭遇速率限制 (429)，等待 {wait} 秒後重試...")
                time.sleep(wait)
        except Exception:
            time.sleep(2)

    papers = []
    if response and response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
            entries = root.findall("atom:entry", {"atom": "http://www.w3.org/2005/Atom"})

            for entry in entries:
                title_elem = entry.find("atom:title", {"atom": "http://www.w3.org/2005/Atom"})
                summary_elem = entry.find("atom:summary", {"atom": "http://www.w3.org/2005/Atom"})
                published_elem = entry.find("atom:published", {"atom": "http://www.w3.org/2005/Atom"})
                id_elem = entry.find("atom:id", {"atom": "http://www.w3.org/2005/Atom"})
                comment_elem = entry.find("arxiv:comment", ARXIV_NS)

                title = title_elem.text if title_elem is not None else ""
                title = " ".join(title.split())

                abstract = summary_elem.text if summary_elem is not None else ""
                abstract = " ".join(abstract.split())

                comment = comment_elem.text if comment_elem is not None else ""

                published = published_elem.text if published_elem is not None else ""
                if published and "T" in published:
                    published = published.split("T")[0]

                paper_id = id_elem.text if id_elem is not None else ""

                author_elems = entry.findall("atom:author/atom:name", {"atom": "http://www.w3.org/2005/Atom"})
                authors_list = [a.text for a in author_elems if a.text]
                authors_str = ", ".join(authors_list[:5])
                if len(author_elems) > 5:
                    authors_str += " et al."

                pdf_url = ""
                for link_elem in entry.findall("atom:link", {"atom": "http://www.w3.org/2005/Atom"}):
                    if link_elem.attrib.get("title") == "pdf":
                        pdf_url = link_elem.attrib.get("href", "")
                        break
                if not pdf_url and paper_id:
                    pdf_url = paper_id.replace("/abs/", "/pdf/") + ".pdf"

                papers.append(_build_paper(
                    title, authors_str or "未知作者", published,
                    abstract, paper_id, pdf_url, comment,
                ))
        except Exception as e:
            print(f"[arXiv Collector] 解析 Atom 失敗: {e}")

    # 排序：優先含 GitHub 專案的論文
    papers = _prioritize_github(papers, count)

    # 若 API 抓取少於目標數量，由 RSS 自動補齊
    if len(papers) < count:
        rss_papers = collect_papers_rss(category, count=count - len(papers))
        papers.extend(_prioritize_github(rss_papers, count - len(papers)))

    github_count = sum(1 for p in papers[:count] if p.get("project_url"))
    print(f"[arXiv Collector] 最終成功獲取 {len(papers)} 篇論文 (含 GitHub 專案: {github_count} 篇)")
    return papers[:count]