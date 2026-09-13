import requests
from config import GITHUB_TOKEN


def _relevance_score(name: str, topics: list[str], description: str, keywords: list[str]) -> int:
    """相關性計分：名稱/主題標籤命中 3 分，描述命中 1 分。回傳 0 表示不符合主題"""
    if not keywords:
        return 1
    primary = f"{name} {' '.join(topics)}".lower()
    score = 0
    if any(kw in primary for kw in keywords):
        score += 3
    if any(kw in (description or "").lower() for kw in keywords):
        score += 1
    return score


def collect_repos(query: str, count: int = 3, keywords: list[str] | None = None) -> list[dict]:
    """使用 GitHub REST API 搜尋熱門/最新開源專案，並以主題關鍵字嚴格過濾"""
    print(f"[GitHub Collector] 正在搜尋專案：{query} (目標: {count} 個, 過濾關鍵字: {keywords})")
    url = "https://api.github.com/search/repositories"
    pool_size = max(count * 8, 30)
    params = {
        "q": query,
        "per_page": pool_size,
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

        # 依主題關鍵字嚴格過濾：名稱/主題標籤命中(primary)優先，描述命中僅在不足時補位
        scored = []
        primary = []
        secondary = []
        if keywords:
            for item in items:
                score = _relevance_score(
                    item.get("name", ""),
                    item.get("topics", []) or [],
                    item.get("description") or "",
                    keywords,
                )
                if score >= 3:
                    primary.append(item)
                elif score == 1:
                    secondary.append(item)
            skipped = len(items) - len(primary) - len(secondary)
            print(f"[GitHub Collector] 關鍵字過濾：{len(items)} -> 主命中 {len(primary)} + 描述補位 {len(secondary)} (剔除 {skipped} 個)")
            primary.sort(key=lambda x: x.get("stargazers_count", 0), reverse=True)
            secondary.sort(key=lambda x: x.get("stargazers_count", 0), reverse=True)
            matched = primary[:count]
            if len(matched) < count:
                matched += secondary[: count - len(matched)]
        else:
            items.sort(key=lambda x: x.get("stargazers_count", 0), reverse=True)
            matched = items

        repos = []
        for item in matched[:count]:
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