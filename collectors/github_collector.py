import requests
from config import GITHUB_TOKEN


def collect_repos(query: str, count: int = 3) -> list[dict]:
    """使用 GitHub REST API 搜尋熱門/最新開源專案"""
    print(f"[GitHub Collector] 正在搜尋專案：{query} (目標: {count} 個)")
    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "updated",
        "order": "desc",
        "per_page": count,
    }

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "DailyNewsAgent/1.0",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        if response.status_code == 403:
            print("[GitHub Collector] 警告：已觸發 GitHub API 速率限制。若需提高配額請於 .env 設定 GITHUB_TOKEN。")
            return []
        elif response.status_code != 200:
            print(f"[GitHub Collector] 請求失敗，狀態碼: {response.status_code}")
            return []

        data = response.json()
        items = data.get("items", [])

        # 若加了限制條件沒搜到，嘗試放寬搜尋條件 (移除 stars 限制)
        if not items and "stars:>" in query:
            relaxed_query = query.split("stars:>")[0].strip()
            params["q"] = relaxed_query
            response = requests.get(url, params=params, headers=headers, timeout=15)
            if response.status_code == 200:
                items = response.json().get("items", [])

        repos = []
        for item in items[:count]:
            updated_at = item.get("updated_at", "")
            if updated_at and "T" in updated_at:
                updated_at = updated_at.split("T")[0]

            repos.append({
                "name": item.get("name", ""),
                "full_name": item.get("full_name", ""),
                "url": item.get("html_url", ""),
                "description": item.get("description") or "暫無描述",
                "stars": item.get("stargazers_count", 0),
                "language": item.get("language") or "General",
                "topics": item.get("topics", [])[:5],
                "updated_at": updated_at,
            })

        print(f"[GitHub Collector] 成功獲取 {len(repos)} 個專案")
        return repos
    except Exception as e:
        print(f"[GitHub Collector] 查詢 GitHub 專案時發生錯誤: {e}")
        return []
