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
    parser.add_argument("--backfill-from", default="", help="回補起始日期 YYYY-MM-DD")
    parser.add_argument("--backfill-to", default="", help="回補結束日期 YYYY-MM-DD，預設今天")
    parser.add_argument("--dry-run", action="store_true", help="僅列出將執行/缺檔日期，不實際跑")
    parser.add_argument("--allow-stale", action="store_true", help="回補模式：放寬新聞/論文/repo 時效窗，manifest 會標註 stale_backfill")
    return parser


def run_agent(target_date: str | None = None, no_push: bool = True, no_ai: bool = False, force: bool = False, allow_stale: bool = False) -> dict:
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
        allow_stale=allow_stale,
    )


def _daterange(start: str, end: str | None):
    from datetime import datetime, timedelta
    s = datetime.strptime(start, "%Y-%m-%d").date()
    e = datetime.strptime(end, "%Y-%m-%d").date() if end else datetime.now().date()
    if e < s:
        s, e = e, s
    cur = s
    while cur <= e:
        yield cur.isoformat()
        cur += timedelta(days=1)


def main() -> int:
    args = build_parser().parse_args()
    if args.backfill_from:
        dates = list(_daterange(args.backfill_from, args.backfill_to or None))
        summary = {"mode": "backfill", "from": args.backfill_from, "to": args.backfill_to or datetime.now().strftime("%Y-%m-%d"), "dates": len(dates), "results": []}
        for d in dates:
            if args.dry_run:
                summary["results"].append({"date": d, "status": "dry_run"})
                continue
            r = run_daily_pipeline(target=d, news_count=args.news, paper_count=args.papers, repo_count=args.repos, write=not args.no_write, push=args.push, use_ai=not args.no_ai, force=args.force, allow_stale=args.allow_stale)
            summary["results"].append({"date": d, "status": r.get("status"), "files": len(r.get("files", [])), "warnings": r.get("warnings", [])[:3], "stale_backfill": r.get("allow_stale", False)})
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        bad = [r for r in summary["results"] if r.get("status") not in {"ok","skipped_existing","dry_run"}]
        return 1 if bad else 0

    report = run_daily_pipeline(
        target=args.date or None,
        news_count=args.news,
        paper_count=args.papers,
        repo_count=args.repos,
        write=not args.no_write,
        push=args.push,
        use_ai=not args.no_ai,
        force=args.force,
        allow_stale=args.allow_stale,
    )
    print(json.dumps({
        "status": report.get("status"),
        "date": report.get("date"),
        "files": len(report.get("files", [])),
        "quotas": report.get("quotas", {}),
        "pairing": report.get("pairing", {}),
        "paired_actual": report.get("paired_actual"),
        "paired_seed": report.get("paired_seed"),
        "warnings": report.get("warnings", []),
        "ai": report.get("ai", {}),
        "report_path": report.get("report_path"),
        "manifest": report.get("manifest"),
    }, ensure_ascii=False, indent=2))
    return 0 if report.get("status") in {"ok", "skipped_existing"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
