import os
from datetime import datetime
from pathlib import Path
from config import BASE_DIR, DAILY_SUMMARY_FOLDER_NAME


def format_report_markdown(
    date_str: str,
    weekday_name: str,
    topic_name: str,
    daily_overview: str,
    news_items: list[dict],
    paper_items: list[dict],
    repo_items: list[dict],
) -> str:
    """生成結構精美、專業的每日新聞情報 Markdown 報告"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md = []
    md.append(f"# 🤖 每日 AI 科技情報日報 — {topic_name}")
    md.append(f"> 📅 **匯報日期**：{date_str} ({weekday_name})  |  🏷️ **今日主題**：`{topic_name}`  |  🕒 **生成時間**：{now_str}\n")
    md.append("---\n")

    # 今日總覽
    md.append("## 💡 今日情報總覽與深度洞察\n")
    md.append(daily_overview.strip())
    md.append("\n\n---\n")

    # 1. 新聞章節 (5 篇)
    md.append(f"## 📰 科技重點新聞 (精選 {len(news_items)} 篇)\n")
    if not news_items:
        md.append("> *今日暫無檢索到新聞資料*\n")
    for i, news in enumerate(news_items, 1):
        md.append(f"### {i}. [{news.get('title')}]({news.get('link')})")
        md.append(f"- 🌐 **來源媒體**：`{news.get('source', '新聞來源')}`")
        if news.get('date'):
            md.append(f"- 📅 **發布時間**：{news.get('date')}")
        md.append(f"- 🔗 **原文連結**：[點擊閱讀完整報導]({news.get('link')})")
        md.append("\n**🧠 AI 深度解說與產業影響**：")
        md.append(f"{news.get('summary', '').strip()}\n")

    md.append("---\n")

    # 2. 論文章節 (5 篇)
    md.append(f"## 📄 前沿學術論文 (arXiv 最新 {len(paper_items)} 篇)\n")
    if not paper_items:
        md.append("> *今日暫無檢索到論文資料*\n")
    for i, paper in enumerate(paper_items, 1):
        md.append(f"### {i}. {paper.get('title')}")
        md.append(f"- 👥 **作者群**：{paper.get('authors')}")
        md.append(f"- 📅 **提交日期**：{paper.get('published')}")
        md.append(f"- 🔗 **論文連結**：[arXiv 頁面]({paper.get('url')})  |  📥 **全文 PDF**：[直接下載]({paper.get('pdf_url')})")
        if paper.get('project_url'):
            md.append(f"- 💻 **官方 GitHub 專案**：[{paper.get('project_url')}]({paper.get('project_url')})")
        md.append("\n**🔬 AI 專業導讀與技術突破**：")
        md.append(f"{paper.get('summary', '').strip()}\n")

    md.append("---\n")

    # 3. GitHub 專案章節
    md.append(f"## 💻 熱門開源專案 (GitHub 精選 {len(repo_items)} 個)\n")
    if not repo_items:
        md.append("> *今日暫無檢索到 GitHub 專案*\n")
    for i, repo in enumerate(repo_items, 1):
        topics_badges = " ".join([f"`{t}`" for t in repo.get('topics', [])])
        md.append(f"### {i}. [{repo.get('full_name')}]({repo.get('url')})")
        md.append(f"- ⭐ **GitHub Stars**：`{repo.get('stars'):,}`  |  🛠️ **主要語言**：`{repo.get('language')}`  |  🔄 **最近更新**：{repo.get('updated_at')}")
        if topics_badges:
            md.append(f"- 🏷️ **標籤**：{topics_badges}")
        md.append(f"- 📝 **官方簡介**：*{repo.get('description')}*")
        md.append(f"- 🔗 **倉庫地址**：{repo.get('url')}")
        md.append("\n**🚀 AI 專案評析與應用建議**：")
        md.append(f"{repo.get('summary', '').strip()}\n")

    md.append("---\n")
    md.append("> 📌 *本報由 AI Agent 自動化爬取並透過高科 iAI (Furen-large) 進行智慧解說與分類整理。*")

    return "\n".join(md)


def format_summary_markdown(
    date_str: str,
    weekday_name: str,
    topic_name: str,
    daily_summary: str,
    news_summary: str,
    paper_summary: str,
    repo_summary: str,
    news_items: list[dict],
    paper_items: list[dict],
    repo_items: list[dict],
) -> str:
    """生成「今日匯報總結」Markdown：先分別對新聞/論文/專案做 AI 總結，再附重點清單"""
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md = []
    md.append(f"# 📋 今日匯報總結 — {topic_name}")
    md.append(f"> 📅 **日期**：{date_str} ({weekday_name})  |  🏷️ **今日主題**：`{topic_name}`  |  🕒 **生成時間**：{now_str}\n")
    md.append("---\n")

    md.append("## ✨ 整體總結\n")
    md.append(daily_summary.strip())
    md.append("\n\n---\n")

    # 1. 新聞總結
    md.append(f"## 📰 新聞總結\n")
    md.append(news_summary.strip())
    md.append("\n")
    if not news_items:
        md.append("> *今日暫無新聞資料*")
    else:
        md.append("**精選新聞清單：**")
        for news in news_items:
            md.append(f"- [{news.get('title')}]({news.get('link')}) — `{news.get('source', '來源')}`")

    md.append("\n---\n")

    # 2. 論文總結
    md.append(f"## 📄 論文總結\n")
    md.append(paper_summary.strip())
    md.append("\n")
    if not paper_items:
        md.append("> *今日暫無論文資料*")
    else:
        md.append("**精選論文清單：**")
        for paper in paper_items:
            author_note = f" — 作者群：{paper.get('authors')}" if paper.get('authors') else ""
            code_note = f" 💻[程式碼]({paper.get('project_url')})" if paper.get('project_url') else ""
            md.append(f"- [{paper.get('title')}]({paper.get('url')}){author_note}{code_note}")

    md.append("\n---\n")

    # 3. 專案總結
    md.append(f"## 💻 專案總結\n")
    md.append(repo_summary.strip())
    md.append("\n")
    if not repo_items:
        md.append("> *今日暫無 GitHub 專案資料*")
    else:
        md.append("**精選專案清單：**")
        for repo in repo_items:
            md.append(f"- [{repo.get('full_name')}]({repo.get('url')}) — ⭐ `{repo.get('stars'):,}` · `{repo.get('language')}`")

    md.append("\n---\n")
    md.append("> 📌 *本總結由 AI Agent 自動彙整，完整詳細日報存放於對應主題資料夾。*")

    return "\n".join(md)


def save_reports(date_str: str, topic_info: dict, full_content: str, summary_content: str) -> tuple[Path, Path]:
    """
    儲存 Markdown 報告：
    1. 完整詳細日報 → 該主題資料夾 (例如 1.LLM、RAG、Fine tune)
    2. 精簡「今日匯報總結」→ 8.每日新聞總結
    """
    # 建立檔案名稱 (檔名過濾特殊字元)
    safe_topic_name = topic_info['name'].replace("、", "_").replace(" ", "_").replace("/", "_")
    full_filename = f"{date_str}_{safe_topic_name}.md"
    summary_filename = f"{date_str}_今日匯報總結.md"

    # 1. 該主題資料夾 (完整詳細日報)
    topic_dir = BASE_DIR / topic_info["folder"]
    topic_dir.mkdir(parents=True, exist_ok=True)
    topic_file = topic_dir / full_filename
    with open(topic_file, "w", encoding="utf-8") as f:
        f.write(full_content)

    # 2. 每日新聞總結資料夾 (精簡總結)
    summary_dir = BASE_DIR / DAILY_SUMMARY_FOLDER_NAME
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_file = summary_dir / summary_filename
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary_content)

    return topic_file, summary_file
