"""P3 論文蒐集煙霧測試（會連網抓取論文來源與公開頁面，不會呼叫 iAI）。

用法：
    python scripts/paper_smoke.py                 # 蒐集 5 篇並印出統計
    python scripts/paper_smoke.py --verify-links  # 額外檢查文章連結可達率
    python scripts/paper_smoke.py --count 5 --json-only
    python scripts/paper_smoke.py --no-enrich     # 跳過全文抓取（較快）

輸出：`.system_generated/paper_smoke.json`（不含任何金鑰）
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from collectors.news_http import SafeHttpFetcher  # noqa: E402
from collectors.paper_engine import PaperEngine, PaperQuotaError  # noqa: E402
from core.manifest import RunManifest  # noqa: E402
from core.timewin import local_today, now_utc  # noqa: E402


def item_to_dict(item) -> dict:  # noqa: ANN001
    return {
        "title": item.title,
        "url": item.url,
        "source_name": item.source_name,
        "source_tier": item.source_tier,
        "published_at": item.published_at.isoformat() if item.published_at else "",
        "authors": item.authors,
        "journal": item.journal,
        "venue": item.venue,
        "impact_factor": item.impact_factor,
        "impact_factor_source": item.impact_factor_source,
        "cited_by_count": item.cited_by_count,
        "doi": item.doi,
        "arxiv_id": item.arxiv_id,
        "code_url": item.code_url,
        "paired_repo": item.paired_repo,
        "pdf_url": item.pdf_url,
        "parse_level": item.parse_level,
        "abstract_len": len(item.abstract or ""),
        "fulltext_len": len(item.fulltext_excerpt or ""),
    }


def verify_links(items) -> dict:  # noqa: ANN001
    fetcher = SafeHttpFetcher(timeout=15, max_bytes=300_000)
    results = []
    reachable = 0
    for item in items:
        url = item.url or item.pdf_url
        if not url:
            results.append({"url": "", "status": 0, "ok": False, "error": "no_url"})
            continue
        result = fetcher.fetch(url, check_robots=False)
        if not (result.ok or 200 <= result.status < 400):
            result = fetcher.fetch(url, check_robots=False)
        status = result.status
        ok = result.ok or 200 <= status < 400
        if ok:
            reachable += 1
        results.append({"url": url, "status": status, "ok": ok, "error": result.error})
    total = len(results) or 1
    return {
        "results": results,
        "reachable": reachable,
        "total": len(results),
        "reachable_ratio": round(reachable / total, 3),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="P3 論文蒐集煙霧測試")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--verify-links", action="store_true")
    parser.add_argument("--no-enrich", action="store_true")
    parser.add_argument("--json-only", action="store_true")
    args = parser.parse_args()

    manifest = RunManifest(local_today().isoformat())
    started = datetime.now()

    engine = PaperEngine(enrich_fulltext=not args.no_enrich)
    try:
        with manifest.stage("paper_collect"):
            selection = engine.collect(args.count, now=now_utc())
    except PaperQuotaError as exc:
        print(f"[P3] 配額不足：{exc}")
        print(json.dumps(exc.report, ensure_ascii=False, indent=2))
        manifest.error("paper_collect", str(exc))
        manifest.quotas = exc.report
        manifest.finish("failed")
        manifest.save()
        out_path = ROOT / ".system_generated" / "paper_smoke.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(exc.report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        return 1

    report = dict(selection.report)
    report["items"] = [item_to_dict(item) for item in selection.items]
    report["rejected_sample"] = selection.rejected[:80]

    if args.verify_links:
        with manifest.stage("verify_links"):
            report["link_check"] = verify_links(selection.items)

    if not args.json_only:
        elapsed = (datetime.now() - started).total_seconds()
        print("=" * 90)
        print(f"[P3] 蒐集 {len(selection.items)} 篇，耗時 {elapsed:.1f}s")
        print(f"[P3] 原始 {report['raw_count']} 筆 → 去重/過濾後 {report['unique_items']} 筆")
        print(f"[P3] 配對(有 GitHub/專案) {report['paired']} 篇（目標 ≥3）{' ✅' if report.get('paired_ok') else ' ⚠️'}")
        if report.get("paired_warning"):
            print(f"[P3] 警告：{report['paired_warning']}")
        print(f"[P3] 來源層級分布：{report.get('tiers', {})}，解析層級：{report.get('parse_levels', {})}")
        print(f"[P3] 排除原因：{report.get('rejected_counts', {})}")
        print("[P3] 來源統計：")
        for name, stats in sorted(report["sources"].items()):
            print(
                f"   - {name}: found={stats.get('found', 0)} fetched={stats.get('fetched', 0)} "
                f"errors={stats.get('errors', 0)} {stats.get('error', '')}".rstrip()
            )
        print("-" * 90)
        for index, item in enumerate(selection.items, 1):
            print(f"{index}. {item.title}")
            print(f"   來源/期刊：{item.source_name} | tier={item.source_tier} | {item.published_at:%Y-%m-%d} | 解析={item.parse_level}")
            print(f"   IF/指標：{item.impact_factor}  [{item.impact_factor_source}]")
            print(f"   引用數：{item.cited_by_count} | DOI：{item.doi or '-'} | arXiv：{item.arxiv_id or '-'}")
            print(f"   連結：{item.url}")
            if item.code_url:
                print(f"   GitHub/專案：{item.code_url}")
            print(f"   摘要/全文長度：{len(item.abstract)} / {len(item.fulltext_excerpt)} chars")
        if args.verify_links:
            check = report["link_check"]
            print("-" * 90)
            print(f"[P3] 連結可達：{check['reachable']}/{check['total']}（{check['reachable_ratio']:.0%}）")
            for row in check["results"]:
                if not row["ok"]:
                    print(f"   - 失敗 {row['status']} {row.get('error','')} {row['url'][:100]}")
        print("=" * 90)

    manifest.counts = {"papers": len(selection.items), "paired": selection.report.get("paired", 0)}
    manifest.quotas = {k: v for k, v in report.items() if k not in {"sources", "items", "rejected_sample", "link_check"}}
    for name, stats in report["sources"].items():
        manifest.source(name, found=stats.get("found", 0), kept=0, errors=stats.get("errors", 0))
    manifest.finish("ok")
    manifest.save()

    out_path = ROOT / ".system_generated" / "paper_smoke.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(f"[P3] 詳細結果：{out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
