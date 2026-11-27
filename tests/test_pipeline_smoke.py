import unittest
from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory

from collectors.news_engine import NewsSelection
from collectors.paper_engine import PaperSelection
from collectors.repo_engine import RepoSelection
from core.models import NewsItem, PaperItem, RepoItem
from pipeline import DailyPipeline


class FakeNewsEngine:
    def collect(self, count, *, now=None):
        items = []
        for i in range(count):
            domain = "maritime" if i == 0 else ("cybersecurity" if i == 1 else ("medical" if i == 2 else "general"))
            items.append(NewsItem(
                title=f"News {i+1}",
                url=f"https://example.com/news/{i+1}",
                source="Example",
                published_at=now,
                language="en",
                ai_focus="AI",
                domains=[domain],
                is_maritime=(domain == "maritime"),
                summary="summary",
                key_point="impact",
            ).validate())
        return NewsSelection(items=items, report={"raw_count": count})


class FakePaperEngine:
    def collect(self, count, *, now=None):
        items = []
        for i in range(count):
            items.append(PaperItem(
                title=f"Paper {i+1}",
                url=f"https://arxiv.org/abs/2601.000{i+1}",
                source_name="arXiv",
                source_tier=1,
                published_at=now,
                abstract="abstract " * 20,
                journal="NeurIPS",
                venue="NeurIPS",
                impact_factor="N/A (conference)",
                impact_factor_source="OpenAlex",
                fulltext_excerpt="fulltext " * 100,
                parse_level="fulltext",
                fulltext_kind="html",
                code_url=f"https://github.com/org/repo{i+1}" if i < 3 else "",
                is_maritime=(i < 2),
            ).validate())
        return PaperSelection(items=items, report={"raw_count": count})


class FakeRepoEngine:
    def collect(self, count, *, now=None, paper_seeds=None):
        for seed in paper_seeds or []:
            assert seed.get("paper_url") and seed.get("paper_title"), seed
        items = []
        for i in range(count):
            seed = (paper_seeds or [{}])[i] if i < len(paper_seeds or []) else {}
            items.append(RepoItem(
                full_name=f"org/repo{i+1}",
                html_url=f"https://github.com/org/repo{i+1}",
                description="AI implementation repo",
                stars=100 + i,
                language="Python",
                topics=["ai"],
                updated_at=now,
                paper_url=seed.get("paper_url", ""),
                paired_paper=seed.get("paper_url", ""),
                paper_tier=int(seed.get("source_tier", 0) or 0),
                is_maritime=bool(seed.get("is_maritime", False)),
                readme_excerpt="readme " * 30,
                quality_score=8,
                sections={"what": "what " * 20, "tech": "tech " * 20, "architecture": "arch " * 20},
            ).validate())
        return RepoSelection(items=items, report={"raw_count": count, "seed_count": len(paper_seeds or [])})


class FakeShortRepoEngine(FakeRepoEngine):
    def collect(self, count, *, now=None, paper_seeds=None):
        selection = super().collect(count, now=now, paper_seeds=paper_seeds)
        selection.items = selection.items[: count - 1]
        selection.report["quota_shortfall"] = f"repos:{len(selection.items)}/{count}"
        return selection


class PipelineSmokeTests(unittest.TestCase):
    def test_run_writes_new_structure(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            pipe = DailyPipeline(root=root, news_engine=FakeNewsEngine(), paper_engine=FakePaperEngine(), repo_engine=FakeRepoEngine())
            report = pipe.run(target="2026-11-21", write=True, push=False, use_ai=False)
            self.assertEqual(report["status"], "ok")
            self.assertEqual(len(report["files"]), 13)
            day_dir = root / "6" / "2026-11-21"
            self.assertTrue((day_dir / "01_新聞_10篇.md").exists())
            self.assertTrue((day_dir / "04_AI技術架構_深度拆解.md").exists())
            self.assertEqual(len(list(day_dir.glob("02_論文_*.md"))), 5)
            self.assertEqual(len(list(day_dir.glob("03_專案_*.md"))), 5)
            self.assertTrue((root / "每日匯報" / "2026-11-21_每日匯報.md").exists())
            digest = (root / "每日匯報" / "2026-11-21_每日匯報.md").read_text(encoding="utf-8")
            self.assertIn("## 新聞（10）", digest)
            self.assertIn("## 論文（5）", digest)
            self.assertIn("## GitHub 專案（5）", digest)
            self.assertIn("papers_paired", report["pairing"])
            self.assertIn("top_journal_paper", report["selection_priority"])
            self.assertIn("maritime_papers>=2", report["selection_priority"])
            self.assertNotIn(
                "paired_repos_below_target=0/3 (seed_paired=0)", report["warnings"]
            )

    def test_unpaired_outputs_are_not_warnings(self):
        class UnpairedPaperEngine(FakePaperEngine):
            def collect(self, count, *, now=None):
                selection = super().collect(count, now=now)
                for item in selection.items:
                    item.code_url = ""
                    item.paired_repo = ""
                return selection

        class UnpairedRepoEngine(FakeRepoEngine):
            def collect(self, count, *, now=None, paper_seeds=None):
                selection = super().collect(count, now=now, paper_seeds=paper_seeds)
                for item in selection.items:
                    item.paper_url = ""
                    item.paired_paper = ""
                return selection

        with TemporaryDirectory() as td:
            pipe = DailyPipeline(
                root=Path(td),
                news_engine=FakeNewsEngine(),
                paper_engine=UnpairedPaperEngine(),
                repo_engine=UnpairedRepoEngine(),
            )
            report = pipe.run(target="2026-11-21", write=False, push=False, use_ai=False)
            self.assertEqual(report["status"], "ok")
            self.assertEqual(report["pairing"]["papers_paired"], 0)
            self.assertFalse(any("paired" in warning for warning in report["warnings"]))

    def test_bundle_quota_warnings_are_surfaced(self):
        with TemporaryDirectory() as td:
            root = Path(td)
            pipe = DailyPipeline(
                root=root,
                news_engine=FakeNewsEngine(),
                paper_engine=FakePaperEngine(),
                repo_engine=FakeShortRepoEngine(),
                allow_stale=True,
            )
            report = pipe.run(target="2026-11-21", write=False, push=False, use_ai=False)
            self.assertEqual(report["status"], "ok")
            self.assertIn("quota_shortfall:repos:4/5", report["warnings"])


if __name__ == "__main__":
    unittest.main()
