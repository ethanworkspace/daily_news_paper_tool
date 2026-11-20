"""新聞蒐集診斷（開發用）：只跑指定領域的來源，列出候選與被排除原因。

用法：
    python scripts/news_diagnose.py --hint maritime
    python scripts/news_diagnose.py --hint medical --show 30

不會呼叫 iAI、不會寫入日報，只輸出到終端機。
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from config import NEWS_FEEDS, NEWS_QUERIES  # noqa: E402
from collectors.news_engine import NewsEngine, build_bing_news_url  # noqa: E402
from core.timewin import now_utc  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hint", default="maritime", choices=["maritime", "medical", "cybersecurity", "electronics", "robotics", "general"])
    parser.add_argument("--show", type=int, default=20)
    parser.add_argument("--no-robots", action="store_true")
    args = parser.parse_args()

    engine = NewsEngine(
        queries=[q for q in NEWS_QUERIES if q.get("hint") == args.hint],
        feeds=[f for f in NEWS_FEEDS if f.get("hint") == args.hint],
        robots_check=not args.no_robots,
    )
    reference = now_utc()
    raw = []
    stats: dict[str, dict] = {}

    for query in engine.queries:
        name = f"bing:{args.hint}"
        raw.extend(engine._fetch_feed(name, build_bing_news_url(query), query, stats))
    for feed in engine.feeds:
        name = f"rss:{feed.get('name')}"
        raw.extend(engine._fetch_feed(name, feed.get("url", ""), feed, stats))

    items, rejected = engine._filter(raw, reference)
    print(f"領域：{args.hint}｜參考時間：{reference.isoformat(timespec='minutes')}")
    print(f"原始 {len(raw)} 筆 → 合格 {len(items)} 筆")
    print("來源：")
    for name, entry in stats.items():
        print(f"  - {name}: found={entry.get('found', 0)} errors={entry.get('errors', 0)} {entry.get('error', '')}")
    print("排除原因：", dict(Counter(r["reason"] for r in rejected)))
    print("合格候選：")
    for item in items[: args.show]:
        print(f"  [{','.join(item.domains)}] {item.published_at:%Y-%m-%d} {item.title[:100]} | {item.source}")
    print("被排除（前 30）：")
    for row in rejected[:30]:
        print(f"  ({row['reason']}) {row['title'][:90]} | {row['source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
