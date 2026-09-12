import re
import time
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime
import requests


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

            title = title_elem.text if title_elem is not None else ""
            title = " ".join(title.split())

            link = link_elem.text if link_elem is not None else ""
            pdf_url = link.replace("/abs/", "/pdf/") + ".pdf" if "/abs/" in link else link

            raw_desc = desc_elem.text if desc_elem is not None else ""
            # 去除 HTML 標籤與 arXiv 特殊前綴
            clean_desc = re.sub(r"<.*?>", "", raw_desc)
            if "Abstract:" in clean_desc:
                clean_desc = clean_desc.split("Abstract:", 1)[1]
            abstract = " ".join(clean_desc.split())

            authors = creator_elem.text if creator_elem is not None else ""
            if not authors:
                authors = "arXiv Researcher"

            papers.append({
                "title": title,
                "authors": authors,
                "published": today_str,
                "abstract": abstract,
                "url": link,
                "pdf_url": pdf_url,
            })

            if len(papers) >= count:
                break

        print(f"[arXiv Collector] 透過 RSS 成功獲取 {len(papers)} 篇論文")
        return papers
    except Exception as e:
        print(f"[arXiv Collector] RSS 抓取失敗: {e}")
        return []


def collect_papers(query: str, count: int = 5, category: str = "cs.AI", max_retries: int = 2) -> list[dict]:
    """檢索 arXiv 論文：優先使用 API 查詢，失敗或超時時自動由官方 RSS 備援"""
    print(f"[arXiv Collector] 正在檢索論文：{query} (目標: {count} 篇)")
    encoded_query = urllib.parse.quote(query)
    url = (
        f"https://export.arxiv.org/api/query?"
        f"search_query={encoded_query}&"
        f"sortBy=submittedDate&"
        f"sortOrder=descending&"
        f"max_results={count}"
    )

    headers = {
        "User-Agent": "DailyNewsPaperAgent/1.0 (mailto:daily_agent@nkust.edu.tw; academic bot)",
        "Accept": "application/atom+xml",
    }

    response = None
    for attempt in range(max_retries):
        try:
            time.sleep(3)
            response = requests.get(url, headers=headers, timeout=25)
            if response.status_code == 200:
                break
            elif response.status_code == 429:
                print(f"[arXiv Collector] 遭遇速率限制 (429)，等待 5 秒後重試...")
                time.sleep(5)
        except Exception as e:
            time.sleep(2)

    papers = []
    if response and response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            entries = root.findall("atom:entry", ns)

            for entry in entries:
                title_elem = entry.find("atom:title", ns)
                summary_elem = entry.find("atom:summary", ns)
                published_elem = entry.find("atom:published", ns)
                id_elem = entry.find("atom:id", ns)

                title = title_elem.text if title_elem is not None else ""
                title = " ".join(title.split())

                abstract = summary_elem.text if summary_elem is not None else ""
                abstract = " ".join(abstract.split())

                published = published_elem.text if published_elem is not None else ""
                if published and "T" in published:
                    published = published.split("T")[0]

                paper_id = id_elem.text if id_elem is not None else ""

                author_elems = entry.findall("atom:author/atom:name", ns)
                authors = [a.text for a in author_elems if a.text]
                authors_str = ", ".join(authors[:5])
                if len(author_elems) > 5:
                    authors_str += " et al."

                pdf_url = ""
                for link_elem in entry.findall("atom:link", ns):
                    if link_elem.attrib.get("title") == "pdf":
                        pdf_url = link_elem.attrib.get("href", "")
                        break
                if not pdf_url and paper_id:
                    pdf_url = paper_id.replace("/abs/", "/pdf/") + ".pdf"

                papers.append({
                    "title": title,
                    "authors": authors_str or "未知作者",
                    "published": published,
                    "abstract": abstract,
                    "url": paper_id,
                    "pdf_url": pdf_url,
                })

                if len(papers) >= count:
                    break
        except Exception as e:
            print(f"[arXiv Collector] 解析 Atom 失敗: {e}")

    # 若 API 抓取少於目標數量，由 RSS 自動補齊
    if len(papers) < count:
        rss_papers = collect_papers_rss(category, count=count - len(papers))
        papers.extend(rss_papers)

    print(f"[arXiv Collector] 最終成功獲取 {len(papers)} 篇論文")
    return papers[:count]
