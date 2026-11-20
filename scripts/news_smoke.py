"""P2 新聞蒐集煙霧測試（會連網，但不會呼叫 iAI）。

用法：
    python scripts/news_smoke.py                 # 蒐集 10 篇並印出來源統計
    python scripts/news_smoke.py --verify-links  # 額外檢查文章連結可達率
    python scripts/news_smoke.py --no-robots     # 跳過 robots.txt 檢查（不建議）
    python scripts/news_smoke.py --count 10 --json-only

輸出：`.system_generated/news_smoke.json`（不含任何金鑰）
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from collectors.news_engine import NewsEngine, NewsQuotaError  # noqa: E402
from collectors.news_http import SafeHttpFetcher  # noqa: E402
from core.logging_utils import setup_logger  # noqa: E402
from core.manifest import RunManifest  # noqa: E402
from core.timewin import local_today, now_utc  # noqa: E402


def item_to_dict(item) -> dict:  # noqa: ANN001
    return {
        "title": item.title,
        "url": item.url,
        "source": item.source,
        "published_at": item.published_at.isoformat() if item.published_at else "",
        "domains": item.domains,
        "is_maritime": item.is_maritime,
        "ai_focus": item.ai_focus,
        "language": item.language,
        "country": item.country,
        "summary": item.summary,
    }


def verify_links(items) -> dict:  # noqa: ANN001
    fetcher = SafeHttpFetcher(timeout=15, max_bytes=300_000)
    results = []
    reachable = 0
    for item in items:
        result = fetcher.fetch(item.url, check_robots=False)
        if not (result.ok or 200 <= result.status < 400):
            # 第一次逾時／連線錯誤時重試一次，降低瞬時網路問題造成的誤判。
            result = fetcher.fetch(item.url, check_robots=False)
        status = result.status
        ok = result.ok or 200 <= status < 400
        blocked = status in (401, 403, 429)
        if ok:
            reachable += 1
        results.append(
            {
                "url": item.url,
                "status": status,
                "ok": ok,
                "blocked": blocked,
                "error": result.error,
            }
        )
    total = len(results) or 1
    return {
        "results": results,
        "reachable": reachable,
        "total": len(results),
        "reachable_ratio": round(reachable / total, 3),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="P2 新聞蒐集煙霧測試")
    parser.add_argument("--count", type=int, default=10)
    parser.add_argument("--verify-links", action="store_true")
    parser.add_argument("--no-robots", action="store_true")
    parser.add_argument("--json-only", action="store_true")
    args = parser.parse_args()

    logger = setup_logger("news_smoke")
    manifest = RunManifest(local_today().isoformat())
    started = datetime.now()

    engine = NewsEngine(robots_check=not args.no_robots)
    try:
        with manifest.stage("news_collect"):
            selection = engine.collect(args.count, now=now_utc())
    except NewsQuotaError as exc:
        print(f"[P2] 配額不足：{exc}")
        print(json.dumps(exc.report, ensure_ascii=False, indent=2))
        manifest.error("news_collect", str(exc))
        manifest.quotas = exc.report
        manifest.finish("failed")
        manifest.save()
        return 1

    report = dict(selection.report)
    report["items"] = [item_to_dict(item) for item in selection.items]
    report["rejected"] = selection.rejected[:300]

    if args.verify_links:
        with manifest.stage("verify_links"):
            verification = verify_links(selection.items)
        report["link_check"] = verification

    if not args.json_only:
        print("=" * 78)
        print(f"[P2] 蒐集 {len(selection.items)} 篇，耗時 {(datetime.now() - started).total_seconds():.1f}s")
        print(f"[P2] 原始 {report['raw_count']} 筆 → 去重/過濾後 {report['unique_items']} 筆")
        print(f"[P2] 跨域 {report['cross_domain']}（需 ≥3）、海事 {report['maritime']}（需 ≥1）")
        print(f"[P2] 排除原因：{report.get('rejected_counts', {})}")
        print(f"[P2] 來源統計（錯誤 != 0 代表該來源失敗，不影響其他來源）：")
        for name, stats in sorted(report["sources"].items()):
            if stats.get("found") or stats.get("errors"):
                print(f"   - {name}: found={stats.get('found', 0)} errors={stats.get('errors', 0)}")
        print("-" * 78)
        for index, item in enumerate(selection.items, 1):
            domains = ",".join(item.domains)
            print(f"{index:2d}. [{domains}] {item.title}")
            print(f"    {item.source} | {item.published_at:%Y-%m-%d %H:%M} UTC | {item.url[:110]}")
        if args.verify_links:
            check = report["link_check"]
            print("-" * 78)
            print(f"[P2] 連結可達：{check['reachable']}/{check['total']}（{check['reachable_ratio']:.0%}）")
            for row in check["results"]:
                if not row["ok"]:
                    print(f"   - 失敗 {row['status']} {row['error']} {row['url'][:100]}")
        print("=" * 78)

    manifest.counts = {"news": len(selection.items)}
    manifest.quotas = {k: v for k, v in report.items() if k not in {"sources", "items", "link_check"}}
    for name, stats in report["sources"].items():
        manifest.source(name, found=stats.get("found", 0), kept=stats.get("found", 0), errors=stats.get("errors", 0))
    manifest.finish("ok")
    out_path = ROOT / ".system_generated" / "news_smoke.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    manifest.save()
    print(f"[P2] 詳細結果：{out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
