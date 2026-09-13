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
                print(f"[AI Summarizer] 呼叫失敗 (狀態碼 {response.status_code})")
        except Exception as e:
            print(f"[AI Summarizer] 請求例外 (第 {attempt + 1} 次): {e}")

    return ""


def summarize_news(news: dict) -> str:
    """為單篇新聞生成繁體中文詳細解說與總結"""
    prompt = f"""請針對以下科技新聞進行繁體中文深度解說與總結（約 250-350 字），分為：
1. 📌【事件詳細解說】：新聞核心事件是什麼？來龍去脈與關鍵數據/事實？
2. 🎯【技術與產業意義】：對技術發展、供應鏈、市場或商業帶來哪些影響？
3. ✅【總結】：用 1-2 句話總結這則新聞的關鍵重點與後續應關注方向。

新聞標題：{news.get('title')}
來源與日期：{news.get('source')} | {news.get('date')}
內容摘要：{news.get('snippet')}
"""
    result = call_iai(prompt)
    if not result:
        return f"{news.get('snippet', '暫無摘要')}（AI 服務未響應，使用原文摘錄）"
    return result


def summarize_paper(paper: dict) -> str:
    """為單篇學術論文生成繁體中文深度導讀（在做什麼/目的/架構/方法/結果/總結）"""
    github_line = f"附屬 GitHub 專案：{paper.get('project_url')}\n" if paper.get("project_url") else ""
    prompt = f"""請針對以下 arXiv 學術論文進行繁體中文深度導讀（約 400-550 字），必須完整涵蓋以下六部分：
1. 【這篇在做什麼】：研究主題與解決的核心問題。
2. 【研究目的】：作者想達成什麼目標、動機為何。
3. 【架構設計】：提出的模型/系統/框架整體架構為何？包含哪些主要模組或組成？
4. 【核心方法】：關鍵演算法、訓練方法、實驗設計或技術創新點。
5. 【實驗結果】：在哪些資料集/場景驗證？量化成效如何？與基線比較？
6. 【總結】：這篇論文的價值、限制與後續研究啟發。

{github_line}論文標題：{paper.get('title')}
作者群：{paper.get('authors')}
摘要原文：
{paper.get('abstract')}
若摘要未提供架構/方法/結果細節，請根據論文主題合理推測並標註『（推測）』。
"""
    result = call_iai(prompt)
    if not result:
        abstract_snip = paper.get('abstract', '')[:250]
        return f"{abstract_snip}...（AI 服務未響應，使用原文摘錄）"
    return result


def summarize_repo(repo: dict) -> str:
    """為單個 GitHub 專案生成繁體中文詳細介紹與評析（在做什麼/架構/方法/結果/總結）"""
    topics_str = ", ".join(repo.get('topics', []))
    prompt = f"""請針對以下 GitHub 開源專案進行繁體中文詳細介紹與評析（約 300-450 字），分為：
1. 🎯【在做什麼】：專案提供什麼功能、解決什麼問題、適合誰使用？
2. 🏗️【架構】：整體技術架構如何組成？主要模組、技術棧、依賴哪些主要元件？
3. ⚙️【方法】：核心運作方式/設計模式/使用方式為何？
4. 📊【結果】：社群採用度（stars/issues/forks）、成熟度、實際成效與口碑。
5. ✅【總結】：專案價值、適用場景與值得關注的發展方向。

專案名稱：{repo.get('full_name')}
星數與語言：⭐ {repo.get('stars')} | {repo.get('language')}
標籤：{topics_str}
專案描述：{repo.get('description')}
倉庫網址：{repo.get('url')}
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
        return f"今日彙整了關於【{topic_name}】的 {len(news_list)} 篇重要新聞、{len(paper_list)} 篇前沿論文與 {len(repo_list)} 個優秀開源專案。各項目詳細內容請參見下方章節。"
    return result


def generate_daily_summary(topic_name: str, news_list: list, paper_list: list, repo_list: list) -> str:
    """結合今日所有資訊，生成「今日匯報總結」精簡摘要（與詳細總覽互補）"""
    news_titles = "\n".join([f"- {n.get('title')}" for n in news_list])
    paper_titles = "\n".join([f"- {p.get('title')}" for p in paper_list])
    repo_names = "\n".join([f"- {r.get('full_name')} (⭐ {r.get('stars')})" for r in repo_list])

    prompt = f"""今日主題為【{topic_name}】的每日 AI 科技新聞匯報已收集完成。
請為其生成一份「今日匯報總結」，重點是「精簡」，約 150-250 字（繁體中文）：
1. 用 2-3 句話指出今日最重要的 1~2 個焦點或趨勢。
2. 點出今日資訊對相關開發者/研究者的整體參考價值。
請勿逐條重複清單細節。

【今日新聞清單】：
{news_titles}

【今日論文清單】：
{paper_titles}

【今日專案清單】：
{repo_names}
"""
    result = call_iai(prompt)
    if not result:
        return f"今日針對【{topic_name}】彙整了 {len(news_list)} 篇新聞、{len(paper_list)} 篇論文與 {len(repo_list)} 個開源專案，詳細內容請參見主題資料夾中的完整日報。"
    return result


def summarize_news_list(news_list: list) -> str:
    """針對今日新聞整體，生成一則精簡總結 (約 120-180 字)"""
    items = "\n".join([f"- {n.get('title')} ({n.get('source')})" for n in news_list])
    prompt = f"""請針對以下今日精選新聞做整體性的「新聞總結」（約 120-180 字，繁體中文）：
找出共同的產業/技術趨勢，點出最重要的 1-2 個焦點，不要逐條重複描述。

【今日新聞清單】：
{items}
"""
    result = call_iai(prompt)
    if not result:
        return f"今日共 {len(news_list)} 篇新聞，焦點集中在 AI 晶片/硬體與自動化相關動態。"
    return result


def summarize_paper_list(paper_list: list) -> str:
    """針對今日論文整體，生成一則精簡總結 (約 120-180 字)"""
    items = "\n".join([f"- {p.get('title')}" for p in paper_list])
    prompt = f"""請針對以下今日精選學術論文做整體性的「論文總結」（約 120-180 字，繁體中文）：
歸納今日論文的研究方向、共同技術主軸與最突出的突破點，不要逐條重複描述。

【今日論文清單】：
{items}
"""
    result = call_iai(prompt)
    if not result:
        return f"今日共 {len(paper_list)} 篇論文，研究方向集中於高效能架構與新型加速器設計。"
    return result


def summarize_repo_list(repo_list: list) -> str:
    """針對今日開源專案整體，生成一則精簡總結 (約 100-160 字)"""
    items = "\n".join([f"- {r.get('full_name')} (⭐ {r.get('stars')}): {r.get('description')}" for r in repo_list])
    prompt = f"""請針對以下今日精選 GitHub 開源專案做整體性的「專案總結」（約 100-160 字，繁體中文）：
歸納今日專案定位、成熟度與最值得了解的 1-2 個專案，不要逐條重複描述。

【今日專案清單】：
{items}
"""
    result = call_iai(prompt)
    if not result:
        return f"今日共 {len(repo_list)} 個開源專案，橫跨工具型與應用型專案，適合按需求選用。"
    return result
