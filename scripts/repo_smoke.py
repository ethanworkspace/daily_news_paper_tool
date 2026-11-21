"""P4 GitHub 專案 smoke：抓取/去重/時效/AI相關/品質篩選/論文配對，輸出可稽核報告。"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from collectors.repo_engine import (  # noqa: E402
    RepoEngine,
    RepoQuotaError,
    link_papers_to_repos,
    paper_seed_map,
)
from core.logging_utils import setup_logger  # noqa: E402
from core.manifest import RunManifest  # noqa: E402
from core.security import redact_secrets  # noqa: E402
from core.timewin import now_utc  # noqa: E402


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="P4 GitHub 專案 smoke test")
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--max-age-days", type=int, default=30)
    parser.add_argument("--min-quality", type=int, default=2, help="品質分數門檻（0–10）")
    parser.add_argument("--enrich-limit", type=int, default=24)
    parser.add_argument("--keep-collections", action="store_true", help="保留 Awesome/survey 等清單型專案（預設排除）")
    parser.add_argument("--paper-json", default="", help="P3 paper smoke 報告；用其 code_url 做雙向配對")
    parser.add_argument("--out", default="", help="輸出 JSON 報告路徑（預設 .system_generated/logs/repo_smoke_*.json）")
    parser.add_argument("--seed-repo", action="append", default=[], help="額外 seed repo，例如 owner/name，可重複")
    return parser


def _load_papers(path_arg: str) -> list[dict]:
    if not path_arg:
        return []
    path = Path(path_arg)
    if not path.is_absolute():
        path = Path(ROOT) / path
    if not path.exists():
        raise SystemExit(f"paper json not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    items = data.get("items") if isinstance(data, dict) else data
    if not isinstance(items, list):
        return []
    return [item for item in items if isinstance(item, dict)]


def main() -> int:
    args = _build_parser().parse_args()
    logger = setup_logger("repo_smoke")
    now = now_utc()
    papers = _load_papers(args.paper_json)
    seed_map = paper_seed_map(papers)
    for repo in args.seed_repo:
        seed_map.setdefault(repo.lower(), {"repo": repo, "paper_url": "", "paper_title": ""})

    engine = RepoEngine(
        max_age_days=args.max_age_days,
        min_quality_score=args.min_quality,
        exclude_collections=not args.keep_collections,
        enrich_limit=args.enrich_limit,
    )
    try:
        selection = engine.collect(
            args.count,
            now=now,
            seed_repos=args.seed_repo,
            paper_seeds=list(seed_map.values()),
        )
    except RepoQuotaError as exc:
        report = {
            "status": "quota_error",
            "error": redact_secrets(str(exc)),
            "report": exc.report,
        }
        out = _write_report(args.out, report)
        print(json.dumps({"status": "quota_error", "report": str(out), "detail": exc.report}, ensure_ascii=False, indent=2))
        return 2

    pairing = link_papers_to_repos(papers, selection.items)
    items = []
    for item in selection.items:
        items.append({
            "full_name": item.full_name,
            "html_url": item.html_url,
            "description": item.description,
            "stars": item.stars,
            "forks": item.forks,
            "language": item.language,
            "license_name": item.license_name,
            "topics": item.topics,
            "updated_at": item.updated_at.isoformat() if item.updated_at else "",
            "created_at": item.created_at.isoformat() if item.created_at else "",
            "paper_url": item.paper_url,
            "paired_paper": item.paired_paper,
            "quality_score": item.quality_score,
            "quality_flags": item.quality_flags,
            "readme_excerpt_len": len(item.readme_excerpt or ""),
            "sections": {k: (v[:500] + "..." if len(v) > 500 else v) for k, v in (item.sections or {}).items()},
        })

    paired = sum(1 for it in selection.items if it.paper_url or it.paired_paper)
    langs = Counter((it.language or "unknown") for it in selection.items)
    paired_ok = paired >= 3
    report = {
        "status": "ok",
        "generated_at": now.isoformat(),
        "count": len(items),
        "paired": paired,
        "paired_ok": paired_ok,
        "papers_paired": pairing["papers_paired"],
        "languages": dict(langs),
        "items": items,
        "paper_pairing": pairing,
        "papers": [
            {
                "title": paper.get("title", ""),
                "url": paper.get("url", ""),
                "code_url": paper.get("code_url", ""),
                "paired_repo": paper.get("paired_repo", ""),
            }
            for paper in papers
        ],
        "selection_report": selection.report,
        "rejected_counts": dict(Counter(r.get("reason", "unknown") for r in selection.rejected)),
        "rejected_sample": selection.rejected[:40],
    }
    if not paired_ok:
        report["paired_warning"] = f"配對專案不足目標：{paired}/3"
    out = _write_report(args.out, report)
    manifest = RunManifest(target_date=now.strftime("%Y-%m-%d"))
    manifest.notes["pipeline"] = "repo_smoke"
    manifest.source("github_search", found=selection.report.get("raw_count", 0), kept=len(items))
    for reason, count in Counter(r.get("reason", "unknown") for r in selection.rejected).items():
        manifest.warning(f"rejected:{reason}={count}")
    if not paired_ok:
        manifest.warning(f"paired_repos_below_target={paired}/3")
    manifest.add_file(out)
    manifest.finish("ok")
    manifest.save()
    logger.info(
        "repo smoke ok: %s items, paired=%s, papers_paired=%s, report=%s",
        len(items), paired, pairing["papers_paired"], out,
    )
    print(json.dumps({
        "status": "ok",
        "report": str(out),
        "count": len(items),
        "paired": paired,
        "papers_paired": pairing["papers_paired"],
        "languages": dict(langs),
    }, ensure_ascii=False, indent=2))
    return 0


def _write_report(path_arg: str, report: dict):
    if path_arg:
        path = Path(path_arg)
    else:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = Path(ROOT) / ".system_generated" / "logs" / f"repo_smoke_{stamp}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


if __name__ == "__main__":
    raise SystemExit(main())
