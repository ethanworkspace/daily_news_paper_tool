import re
import urllib.parse
import xml.etree.ElementTree as ET
import requests
from config import GOOGLE_CSE_API_KEY, GOOGLE_CSE_CX


def clean_html(raw_html: str) -> str:
    """去除 HTML 標籤並整理空白"""
    if not raw_html:
        return ""
    clean_text = re.sub(r"<.*?>", "", raw_html)
    return " ".join(clean_text.split())


def search_news_google_cse(query: str, num: int = 5) -> list[dict]:
    """使用 Google Custom Search JSON API 搜尋新聞"""
    if not GOOGLE_CSE_API_KEY or not GOOGLE_CSE_CX:
        return []

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_CSE_API_KEY,
        "cx": GOOGLE_CSE_CX,
        "q": query,
        "num": num,
        "sort": "date",
    }
    try:
        response = requests.get(url, params=params, timeout=12)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            results = []
            for item in items[:num]:
                results.append({
                    "title": item.get("title", "").strip(),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", "").strip(),
                    "source": item.get("displayLink", "Google Search"),
                    "date": item.get("snippet", "")[:30],
                })
            return results
    except Exception as e:
        print(f"[News Collector] Google CSE API 查詢失敗: {e}，切換為 Google News RSS")
    return []


def search_news_google_rss(query: str, num: int = 5) -> list[dict]:
    """使用 Google News RSS 搜尋最新繁體中文新聞（無需 API key，即時且穩定）"""
    encoded_query = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            return []

        root = ET.fromstring(response.content)
        items = root.findall(".//item")
        results = []

        for item in items:
            title_elem = item.find("title")
            link_elem = item.find("link")
            pubdate_elem = item.find("pubDate")
            desc_elem = item.find("description")
            source_elem = item.find("source")

            title = title_elem.text if title_elem is not None else ""
            link = link_elem.text if link_elem is not None else ""
            pub_date = pubdate_elem.text if pubdate_elem is not None else ""
            raw_desc = desc_elem.text if desc_elem is not None else ""
            source = source_elem.text if source_elem is not None else "Google News"

            snippet = clean_html(raw_desc)
            if not snippet:
                snippet = title

            results.append({
                "title": title.strip(),
                "link": link.strip(),
                "snippet": snippet.strip(),
                "source": source.strip(),
                "date": pub_date.strip(),
            })

            if len(results) >= num:
                break

        return results
    except Exception as e:
        print(f"[News Collector] Google News RSS 查詢失敗: {e}")
        return []


def collect_news(query: str, count: int = 5) -> list[dict]:
    """收集 5 篇新聞，優先嘗試 Google CSE，失敗或未設定時自動切換至 Google News RSS"""
    print(f"[News Collector] 正在搜尋新聞：{query} (目標: {count} 篇)")
    results = search_news_google_cse(query, count)
    if not results:
        results = search_news_google_rss(query, count)
    print(f"[News Collector] 成功獲取 {len(results)} 篇新聞")
    return results[:count]
