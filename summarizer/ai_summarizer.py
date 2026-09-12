import re
import requests
from config import IAI_API_KEY, IAI_BASE_URL, IAI_MODEL


def clean_think_tags(text: str) -> str:
    """去除推理模型可能產生的 <think>...</think> 標籤"""
    if not text:
        return ""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return text.strip()


def call_iai(prompt: str, max_retries: int = 2) -> str:
    """呼叫高科 iAI API (Furen-large) 進行文字生成"""
    if not IAI_API_KEY:
        return ""

    url = f"{IAI_BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {IAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": IAI_MODEL,
        "messages": [
            {
                "role": "system",
                "content": "你是一位頂尖的 AI 科技情報分析專家。請使用繁體中文進行專業、精準、條理分明的繁體中文解說與分析。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    }

    for attempt in range(max_retries + 1):
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                data = response.json()
                choices = data.get("choices", [])
                if choices:
                    content = choices[0].get("message", {}).get("content", "")
                    cleaned = clean_think_tags(content)
                    if cleaned:
                        return cleaned
            else:
                print(f"[AI Summarizer] 呼叫失敗 (狀態碼 {response.status_code}): {response.text[:100]}")
        except Exception as e:
            print(f"[AI Summarizer] 請求例外 (第 {attempt + 1} 次): {e}")

    return ""


def summarize_news(news: dict) -> str:
    """為單篇新聞生成繁體中文深度解說"""
    prompt = f"""請針對以下科技新聞進行繁體中文專業解說（約 150-250 字），包含：
1. 【核心事件】：新聞核心重點是什麼？
2. 【技術與產業意義】：帶來哪些突破或商業/市場影響？
3. 【關鍵結論】：對未來發展的意涵。

新聞標題：{news.get('title')}
來源與日期：{news.get('source')} | {news.get('date')}
內容摘要：{news.get('snippet')}
"""
    result = call_iai(prompt)
    if not result:
        # Fallback 簡單摘錄
        return f"{news.get('snippet', '暫無摘要')}（AI 服務未響應，使用原文摘錄）"
    return result


def summarize_paper(paper: dict) -> str:
    """為單篇學術論文生成繁體中文專業解說"""
    prompt = f"""請針對以下 arXiv 學術論文進行繁體中文深度導讀（約 180-280 字），包含：
1. 【研究背景與痛點】：為了解決什麼核心問題？
2. 【核心技術與方法】：提出了什麼模型架構、演算法或理論突破？
3. 【實證效果與價值】：實驗表現如何？對該領域有何具體貢獻？

論文標題：{paper.get('title')}
作者群：{paper.get('authors')}
摘要原文：
{paper.get('abstract')}
"""
    result = call_iai(prompt)
    if not result:
        abstract_snip = paper.get('abstract', '')[:250]
        return f"{abstract_snip}...（AI 服務未響應，使用原文摘錄）"
    return result


def summarize_repo(repo: dict) -> str:
    """為單個 GitHub 專案生成繁體中文詳細介紹"""
    topics_str = ", ".join(repo.get('topics', []))
    prompt = f"""請針對以下 GitHub 開源專案進行繁體中文專業介紹與評析（約 150-250 字），包含：
1. 【專案定位】：解決什麼開發需求或提供什麼核心工具？
2. 【關鍵特性】：支援哪些亮點功能、技術棧與架構設計？
3. 【推薦場景】：推薦工程師或研究者在何種情境下採用？

專案名稱：{repo.get('full_name')}
星數與語言：⭐ {repo.get('stars')} | {repo.get('language')}
標籤：{topics_str}
專案描述：{repo.get('description')}
"""
    result = call_iai(prompt)
    if not result:
        return f"{repo.get('description', '暫無描述')}（AI 服務未響應，使用原文摘錄）"
    return result


def generate_daily_overview(topic_name: str, news_list: list, paper_list: list, repo_list: list) -> str:
    """結合今日所有新聞、論文、開源專案，生成今日總覽與趨勢洞察"""
    news_titles = "\n".join([f"- {n.get('title')}" for n in news_list])
    paper_titles = "\n".join([f"- {p.get('title')}" for p in paper_list])
    repo_names = "\n".join([f"- {r.get('full_name')} (⭐ {r.get('stars')}): {r.get('description')}" for r in repo_list])

    prompt = f"""今日主題為【{topic_name}】。
請根據今天收集到的以下資料，撰寫一份高質量的「今日技術情報總覽與洞察」（約 350-500 字，繁體中文）：

【今日新聞清單】：
{news_titles}

【今日前沿論文清單】：
{paper_titles}

【今日開源專案清單】：
{repo_names}

請結構化輸出：
1. 💡【今日核心焦點】：今日在這個主題領域最重大的動向或突破。
2. 🔬【學術與技術趨勢】：論文與開源社群展現出哪些技術演進方向（如架構、效能、落地應用）？
3. 🚀【未來應用啟示】：給相關開發者、研究者或產業人士的行動與探索建議。
"""
    result = call_iai(prompt)
    if not result:
        return f"今日彙整了關於【{topic_name}】的 5 篇重要新聞、5 篇前沿論文與 3 個優秀開源專案。各項目詳細內容請參見下方章節。"
    return result
