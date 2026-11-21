import argparse
import json
import sys
from datetime import datetime

# Windows 終端 UTF-8
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from pipeline import run_daily_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="每日 AI 報告新流程（10新聞/5論文/5專案/1架構）")
    parser.add_argument("--date", default="", help="目標日期 YYYY-MM-DD，預設今天")
    parser.add_argument("--news", type=int, default=10)
    parser.add_argument("--papers", type=int, default=5)
    parser.add_argument("--repos", type=int, default=5)
    parser.add_argument("--no-write", action="store_true", help="只跑收集/驗證，不寫檔")
    parser.add_argument("--push", action="store_true", help="寫檔後 git push")
    parser.add_argument("--no-ai", action="store_true", help="停用 iAI，使用規則式 fallback")
    parser.add_argument("--force", action="store_true", help="覆寫既有當日輸出")
    return parser


def run_agent(target_date: str | None = None, no_push: bool = True, no_ai: bool = False, force: bool = False) -> dict:
    """相容舊介面：供 scheduler/run_daily 呼叫。"""
    return run_daily_pipeline(
        target=target_date,
        news_count=10,
        paper_count=5,
        repo_count=5,
        write=True,
        push=not no_push,
        use_ai=not no_ai,
        force=force,
    )


def main() -> int:
    args = build_parser().parse_args()
    report = run_daily_pipeline(
        target=args.date or None,
        news_count=args.news,
        paper_count=args.papers,
        repo_count=args.repos,
        write=not args.no_write,
        push=args.push,
        use_ai=not args.no_ai,
        force=args.force,
    )
    print(json.dumps({
        "status": report.get("status"),
        "date": report.get("date"),
        "files": len(report.get("files", [])),
        "quotas": report.get("quotas", {}),
        "pairing": report.get("pairing", {}),
        "warnings": report.get("warnings", []),
        "report_path": report.get("report_path"),
        "manifest": report.get("manifest"),
    }, ensure_ascii=False, indent=2))
    return 0 if report.get("status") == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
