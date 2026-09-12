import argparse
import sys
from datetime import datetime

# 確保 Windows 命令提示字元輸出 UTF-8，避免 cp950 編碼錯誤
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from config import TOPICS, BASE_DIR
from collectors.news_collector import collect_news
from collectors.arxiv_collector import collect_papers
from collectors.github_collector import collect_repos
from summarizer.ai_summarizer import (
    summarize_news,
    summarize_paper,
    summarize_repo,
    generate_daily_overview,
)
from report.markdown_generator import (
    format_report_markdown,
    save_reports,
)


def run_agent(weekday: int = None, test_mode: bool = False, custom_date: str = None):
    """執行自動化新聞匯報 Agent"""
    now = datetime.now()
    if weekday is None:
        weekday = now.weekday()  # 0: 禮拜一, 6: 禮拜日

    date_str = custom_date if custom_date else now.strftime("%Y-%m-%d")
    topic_info = TOPICS.get(weekday, TOPICS[0])

    print("=" * 60)
    print("🤖 每日 AI 科技新聞匯報 Agent 啟動")
    print(f"📅 執行日期：{date_str} ({topic_info['weekday_name']})")
    print(f"🏷️ 今日主題：【{topic_info['name']}】")
    print(f"📁 歸檔資料夾：{topic_info['folder']} & 8.每日新聞總結")
    print("=" * 60)

    news_target = 1 if test_mode else 5
    paper_target = 1 if test_mode else 5
    repo_target = 1 if test_mode else 3

    # 1. 收集資料
    print("\n【階段 1/3】開始並行收集情報資料...")
    news_items = collect_news(topic_info["news_query"], count=news_target)
    paper_items = collect_papers(
        topic_info["arxiv_query"],
        count=paper_target,
        category=topic_info.get("arxiv_category", "cs.AI"),
    )
    repo_items = collect_repos(topic_info["github_query"], count=repo_target)

    # 2. AI 智慧解說與總結
    print("\n【階段 2/3】正在使用高科 iAI (Furen-large) 進行智慧解說與專業分析...")

    print("  -> 正在逐篇解說新聞...")
    for idx, news in enumerate(news_items, 1):
        print(f"     [新聞 {idx}/{len(news_items)}] {news.get('title')[:30]}...")
        news["summary"] = summarize_news(news)

    print("  -> 正在逐篇導讀學術論文...")
    for idx, paper in enumerate(paper_items, 1):
        print(f"     [論文 {idx}/{len(paper_items)}] {paper.get('title')[:30]}...")
        paper["summary"] = summarize_paper(paper)

    print("  -> 正在逐個評析開源專案...")
    for idx, repo in enumerate(repo_items, 1):
        print(f"     [專案 {idx}/{len(repo_items)}] {repo.get('full_name')}...")
        repo["summary"] = summarize_repo(repo)

    print("  -> 正在生成今日前沿情報總覽與洞察...")
    daily_overview = generate_daily_overview(
        topic_info["name"], news_items, paper_items, repo_items
    )

    # 3. 生成與儲存報告
    print("\n【階段 3/3】正在生成 Markdown 日報並儲存至指定資料夾...")
    report_markdown = format_report_markdown(
        date_str=date_str,
        weekday_name=topic_info["weekday_name"],
        topic_name=topic_info["name"],
        daily_overview=daily_overview,
        news_items=news_items,
        paper_items=paper_items,
        repo_items=repo_items,
    )

    path1, path2 = save_reports(date_str, topic_info, report_markdown)

    print("\n" + "=" * 60)
    print("🎉 匯報生成完畢！")
    print(f"📄 已儲存至分類資料夾：{path1.relative_to(BASE_DIR)}")
    print(f"📄 已儲存至每日總結：  {path2.relative_to(BASE_DIR)}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="每日 AI 科技新聞匯報 Agent")
    parser.add_argument(
        "--weekday",
        type=int,
        choices=range(0, 7),
        default=None,
        help="手動指定星期幾 (0: 禮拜一 ~ 6: 禮拜日，預設為今日)",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="測試模式 (僅抓取各 1 筆進行快速驗證)",
    )
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help="手動指定日期字串 (格式: YYYY-MM-DD)",
    )
    args = parser.parse_args()

    run_agent(weekday=args.weekday, test_mode=args.test, custom_date=args.date)


if __name__ == "__main__":
    main()
