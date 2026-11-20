"""P1 一鍵自我檢查：不連網、不呼叫 iAI，驗證核心骨架與安全機制。

用法：
    python scripts/p1_selfcheck.py

檢查項目：
1. 時效窗邊界（14 天含頭、逾期拒絕、未來容差）
2. schema 與每日配額（10/5/5/1、跨域 ≥3、海事 ≥1）
3. 快取寫入／讀取／TTL
4. 日誌遮罩（金鑰不得落檔）
5. run manifest 產出
"""
from __future__ import annotations

import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.cache import FileCache  # noqa: E402
from core.logging_utils import reset_logger, setup_logger  # noqa: E402
from core.manifest import RunManifest  # noqa: E402
from core.models import DailyBundle, NewsItem, PaperItem, RepoItem, TechArchItem  # noqa: E402
from core.paths import ensure_day_tree  # noqa: E402
from core.security import redact_secrets  # noqa: E402
from core.timewin import is_within_window, local_today  # noqa: E402

NOW = datetime.now(timezone.utc)
TARGET_DATE = local_today()
CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> None:
    CHECKS.append((name, passed, detail))
    print(f"[{'PASS' if passed else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


def days_ago(days: float) -> datetime:
    return NOW - timedelta(days=days)


def build_bundle() -> DailyBundle:
    news = [
        NewsItem(
            title=f"AI 技術新聞 {i}",
            url=f"https://example.com/news/{i}",
            source="SelfCheck",
            published_at=days_ago(1),
            domains=["general"],
            summary="自我檢查用資料",
        )
        for i in range(7)
    ]
    news.append(
        NewsItem(
            title="海事 AI 船舶安全",
            url="https://example.com/news/maritime",
            source="SelfCheck",
            published_at=days_ago(2),
            domains=["maritime"],
            is_maritime=True,
            summary="海事應用",
        )
    )
    news.append(
        NewsItem(
            title="醫療 AI 影像診斷",
            url="https://example.com/news/medical",
            source="SelfCheck",
            published_at=days_ago(3),
            domains=["medical"],
            summary="醫療應用",
        )
    )
    news.append(
        NewsItem(
            title="AI 資安防禦",
            url="https://example.com/news/security",
            source="SelfCheck",
            published_at=days_ago(4),
            domains=["cybersecurity"],
            summary="資安應用",
        )
    )

    papers = [
        PaperItem(
            title=f"Paper {i}",
            url=f"https://arxiv.org/abs/2601.0123{i}",
            source_name="arXiv",
            source_tier=3,
            published_at=days_ago(5 + i),
            parse_level="abstract",
            code_url="https://github.com/example/repo" if i < 3 else "",
        )
        for i in range(5)
    ]
    repos = [
        RepoItem(
            full_name=f"example/repo{i}",
            html_url=f"https://github.com/example/repo{i}",
            updated_at=days_ago(i),
            paper_url="https://arxiv.org/abs/2601.01230" if i < 2 else "",
        )
        for i in range(5)
    ]
    tech = TechArchItem(
        name="Transformer 架構",
        principle="以自注意力機制處理序列資料。" * 10,
        applications_maritime="船舶航跡預測與港埠調度。" * 10,
        applications_medical="醫學影像與臨床文本分析。" * 10,
        reference_urls=["https://arxiv.org/abs/1706.03762"],
    )
    return DailyBundle(
        date=TARGET_DATE.isoformat(),
        news=news,
        papers=papers,
        repos=repos,
        tech=tech,
    )


def main() -> int:
    manifest = RunManifest(TARGET_DATE.isoformat())

    with manifest.stage("time_window"):
        check("14 天邊界（含頭）", is_within_window(days_ago(14), 14, now=NOW))
        check("超過 14 天被拒", not is_within_window(days_ago(14.1), 14, now=NOW))
        check("未來 2 天被拒", not is_within_window(NOW + timedelta(days=2), 14, now=NOW))

    with manifest.stage("schema_and_quota"):
        bundle = build_bundle()
        quotas = bundle.validate(now=NOW)
        check("10 新聞 / 5 論文 / 5 專案 / 1 技術架構", True)
        check("跨域 ≥3", quotas["cross_domain_ok"], f"跨域 {quotas['cross_domain']}")
        check("海事 ≥1", quotas["maritime_ok"], f"海事 {quotas['maritime']}")
        check("論文×專案配對統計", quotas["paired_papers"] == 3 and quotas["paired_repos"] == 2,
              f"論文 {quotas['paired_papers']}／專案 {quotas['paired_repos']}")
        manifest.counts = {
            "news": len(bundle.news),
            "papers": len(bundle.papers),
            "repos": len(bundle.repos),
            "tech": 1,
        }
        manifest.quotas = quotas

    with manifest.stage("cache"):
        with tempfile.TemporaryDirectory() as tmp:
            cache = FileCache(tmp, default_ttl=60)
            cache.set_json("demo", {"ok": True})
            check("快取讀寫", cache.get_json("demo") == {"ok": True})
            cache.set_json("expired", 1, ttl=0)
            time.sleep(0.01)
            check("快取 TTL", cache.get_json("expired") is None)

    with manifest.stage("logging"):
        with tempfile.TemporaryDirectory() as tmp:
            logger = setup_logger("p1_selfcheck", log_dir=tmp, console=False)
            secret = "sk-" + "S1" * 12
            logger.info("key=%s", secret)
            log_text = (Path(tmp) / "run.log").read_text(encoding="utf-8")
            reset_logger("p1_selfcheck")
            check("日誌不落金鑰", secret not in log_text and "****" in log_text)

    with manifest.stage("paths"):
        with tempfile.TemporaryDirectory() as tmp:
            paths = ensure_day_tree(tmp, TARGET_DATE)
            check("當日目錄建立（週資料夾/日期/assets/每日匯報）", all(p.is_dir() for p in paths.values()))

    with manifest.stage("security"):
        redacted = redact_secrets("Bearer abcdefghijklmnop")
        check("Bearer token 遮罩", "abcdefghijklmnop" not in redacted)

    passed = sum(1 for _, ok, _ in CHECKS if ok)
    total = len(CHECKS)
    manifest.finish("ok" if passed == total else "failed")
    manifest.notes["selfcheck"] = {"passed": passed, "total": total}
    path = manifest.save()
    print(f"\n[P1] 自我檢查：{passed}/{total} 通過")
    print(f"[P1] Manifest：{path}")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
