"""P4 repo 引擎測試。"""
from __future__ import annotations

import unittest
from datetime import datetime, timezone

from collectors.repo_engine import (
    RepoEngine,
    RepoQuotaError,
    link_papers_to_repos,
    paper_seed_entries,
    paper_seed_map,
    select_repos,
)
from collectors.repo_parse import RepoCandidate
from collectors.repo_sources import SourceStats
from core.models import RepoItem


def _item(
    full_name: str,
    *,
    stars: int = 100,
    paper: str = "",
    updated: str = "2026-11-20T00:00:00Z",
    quality: int = 6,
    language: str = "Python",
) -> RepoItem:
    return RepoItem(
        full_name=full_name,
        html_url=f"https://github.com/{full_name}",
        description="AI repo for testing",
        stars=stars,
        language=language,
        updated_at=datetime.fromisoformat(updated.replace("Z", "+00:00")),
        paper_url=paper,
        paired_paper=paper,
        readme_excerpt="This repository implements an AI model for testing purposes. " * 3,
        quality_score=quality,
        quality_flags=["implementation_signals"] if quality >= 5 else [],
        sections={"what": "what" * 20, "tech": "tech" * 20, "architecture": "arch" * 20},
    ).validate()


class RepoSelectionTests(unittest.TestCase):
    def test_select_prefers_paired(self):
        items = [
            _item("a/one", stars=10),
            _item("b/two", stars=500, paper="https://arxiv.org/abs/2601.01234"),
            _item("c/three", stars=400),
            _item("d/four", stars=300, paper="https://doi.org/10.1/x"),
            _item("e/five", stars=200),
            _item("f/six", stars=100),
        ]
        sel = select_repos(items, 5, max_per_source=2, min_paired=2)
        self.assertEqual(len(sel.items), 5)
        self.assertGreaterEqual(sel.report["paired"], 2)

    def test_select_quota_error(self):
        with self.assertRaises(RepoQuotaError):
            select_repos([_item("a/one")], 2, min_paired=0)

    def test_select_prefers_quality_over_raw_stars(self):
        items = [
            _item("a/awesome-list", stars=50000, quality=1, language=""),
            _item("b/real-impl", stars=200, quality=7),
            _item("c/another-impl", stars=150, quality=6),
        ]
        sel = select_repos(items, 2, max_per_source=5, min_paired=0)
        names = {item.full_name for item in sel.items}
        self.assertIn("b/real-impl", names)
        self.assertIn("c/another-impl", names)
        self.assertNotIn("a/awesome-list", names)


class PairingTests(unittest.TestCase):
    def test_paper_seed_map_extracts_github(self):
        papers = [
            {"title": "P1", "url": "https://arxiv.org/abs/2601.1", "code_url": "https://github.com/org/repo"},
            {"title": "P2", "url": "https://arxiv.org/abs/2601.2", "code_url": ""},
        ]
        seeds = paper_seed_map(papers)
        self.assertEqual(list(seeds.keys()), ["org/repo"])
        self.assertEqual(seeds["org/repo"]["paper_title"], "P1")

    def test_link_papers_to_repos_writes_back(self):
        papers = [
            {"title": "P1", "url": "https://arxiv.org/abs/2601.01234", "code_url": "https://github.com/org/repo1", "paired_repo": ""},
            {"title": "P2", "url": "https://doi.org/10.1/x", "code_url": "", "paired_repo": ""},
        ]
        repos = [
            _item("org/repo1", paper=""),
            _item("org/repo2", paper="https://doi.org/10.1/x"),
        ]
        report = link_papers_to_repos(papers, repos)
        self.assertEqual(papers[0]["paired_repo"], "org/repo1")
        self.assertEqual(papers[1]["paired_repo"], "org/repo2")
        self.assertEqual(report["papers_paired"], 2)

    def test_paper_seed_entries_is_idempotent(self):
        paper = {
            "title": "Paper title",
            "url": "https://arxiv.org/abs/2601.01234v1",
            "code_url": "https://github.com/org/repo",
            "doi": "",
            "arxiv_id": "2601.01234",
            "source": "arXiv",
        }
        once = paper_seed_entries([paper])[0]
        twice = paper_seed_entries([once])[0]
        for key in ("repo", "paper_url", "paper_title", "arxiv_id", "source"):
            self.assertEqual(twice[key], once[key], key)

    def test_link_papers_to_repos_canonical_arxiv_id(self):
        papers = [{
            "title": "P1",
            "url": "http://arxiv.org/abs/2601.01234v1",
            "code_url": "",
            "paired_repo": "",
            "doi": "",
            "arxiv_id": "",
        }]
        repos = [_item("org/repo1", paper="https://arxiv.org/abs/2601.01234")]
        report = link_papers_to_repos(papers, repos)
        self.assertEqual(papers[0]["paired_repo"], "org/repo1")
        self.assertEqual(report["papers_paired"], 1)


class FakeSources:
    def __init__(self):
        self.search_calls: list[tuple[str, dict]] = []
        self._repos = {
            "org/maritime": RepoCandidate(
                full_name="org/maritime",
                html_url="https://github.com/org/maritime",
                description="Maritime AI vessel detection with deep learning",
                stars=120,
                language="Python",
                topics=["maritime", "ai", "pytorch"],
                updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
                readme_text=(
                    "# Maritime AI\n\n## Overview\nAutonomous vessel detection.\n\n"
                    "## Installation\npip install maritime-ai\n\n"
                    "## Architecture\nSensor -> model -> alert\n\n"
                    "## Usage\npython -m maritime.run\n"
                ) + ("Details. " * 80),
            ),
            "org/awesome-ai": RepoCandidate(
                full_name="org/awesome-ai",
                html_url="https://github.com/org/awesome-ai",
                description="A curated list of awesome AI papers and resources",
                stars=9000,
                language="",
                topics=["awesome", "papers", "ai"],
                updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
                readme_text="# Awesome AI\n\nA collection of papers and resources.\n\n- Paper 1\n- Paper 2\n",
            ),
        }

    def search_repos(self, query, *, per_page=20, pushed_after="", min_stars=0, sort="updated", order="desc"):
        self.search_calls.append((query, {
            "per_page": per_page,
            "pushed_after": pushed_after,
            "min_stars": min_stars,
            "sort": sort,
            "order": order,
        }))
        st = SourceStats("github_search", found=len(self._repos), fetched=len(self._repos))
        return list(self._repos.values()), st

    def get_repo(self, full_name):
        return self._repos.get(full_name)

    def enrich_repo(self, repo, *, refresh=False):
        from collectors.repo_parse import build_repo_sections, clean_readme, extract_paper_urls

        repo.readme_excerpt = clean_readme(repo.readme_text)
        repo.paper_urls = extract_paper_urls(repo.readme_text + " " + repo.description)
        repo.sections = build_repo_sections(repo)
        return repo


class RepoEngineTests(unittest.TestCase):
    def test_collect_filters_collection_repos(self):
        engine = RepoEngine(
            sources=FakeSources(),
            queries=[{"query": "maritime ai", "hint": "maritime", "min_stars": 0}],
            max_per_source=5,
            max_age_days=30,
            min_paired=0,
            min_quality_score=2,
            exclude_collections=True,
            enrich_limit=5,
        )
        sel = engine.collect(1, now=datetime(2026, 11, 21, tzinfo=timezone.utc))
        self.assertEqual(len(sel.items), 1)
        self.assertEqual(sel.items[0].full_name, "org/maritime")
        self.assertGreaterEqual(sel.items[0].quality_score, 5)
        self.assertGreaterEqual(sel.report.get("collections_excluded", 0), 1)

    def test_collect_uses_paper_seed(self):
        sources = FakeSources()
        sources._repos["org/paired"] = RepoCandidate(
            full_name="org/paired",
            html_url="https://github.com/org/paired",
            description="Implementation for a medical AI paper",
            stars=40,
            language="Python",
            topics=["medical", "pytorch"],
            updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
            readme_text="# Paired\n\n## Install\npip install paired\n\n## Usage\npython -m paired.run\n" + ("x " * 300),
        )
        engine = RepoEngine(
            sources=sources,
            queries=[],
            max_per_source=5,
            max_age_days=30,
            min_paired=1,
            min_quality_score=2,
            enrich_limit=5,
        )
        sel = engine.collect(
            1,
            now=datetime(2026, 11, 21, tzinfo=timezone.utc),
            paper_seeds=[{"repo": "org/paired", "paper_url": "https://arxiv.org/abs/2601.01234", "paper_title": "P"}],
        )
        self.assertEqual(sel.items[0].full_name, "org/paired")
        self.assertEqual(sel.items[0].paper_url, "https://arxiv.org/abs/2601.01234")

    def test_collect_insufficient_raises(self):
        engine = RepoEngine(
            sources=FakeSources(),
            queries=[{"query": "maritime ai", "hint": "maritime", "min_stars": 0}],
            max_per_source=5,
            max_age_days=30,
            min_paired=0,
            min_quality_score=2,
            enrich_limit=5,
        )
        with self.assertRaises(RepoQuotaError):
            engine.collect(3, now=datetime(2026, 11, 21, tzinfo=timezone.utc))

    def test_discover_repo_requires_literal_paper_id(self):
        sources = FakeSources()
        sources._repos["org/paper"] = RepoCandidate(
            full_name="org/paper",
            html_url="https://github.com/org/paper",
            description="Implementation of a maritime AI paper",
            stars=12,
            language="Python",
            topics=["ai", "maritime"],
            updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
            readme_text="Implementation for arXiv:2601.01234. Install with pip install paper.",
        )
        sources._repos["org/title-only"] = RepoCandidate(
            full_name="org/title-only",
            html_url="https://github.com/org/title-only",
            description="Maritime AI paper implementation",
            stars=8,
            language="Python",
            topics=["ai", "maritime"],
            updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
            readme_text="Similar title but no paper identifier or link is mentioned here.",
        )
        engine = RepoEngine(sources=sources, queries=[], min_quality_score=0)
        found = engine._discover_repo_for_paper(
            {
                "repo": "",
                "paper_url": "https://arxiv.org/abs/2601.01234v1",
                "paper_title": "Maritime AI paper implementation",
                "arxiv_id": "",
                "doi": "",
            },
            reference=datetime(2026, 11, 21, tzinfo=timezone.utc),
        )
        self.assertIsNotNone(found)
        self.assertEqual(found.full_name, "org/paper")
        self.assertTrue(sources.search_calls)
        query, kwargs = sources.search_calls[0]
        self.assertIn("in:readme", query)
        self.assertEqual(kwargs["per_page"], 20)
        self.assertEqual(kwargs["sort"], "updated")

    def test_discover_repo_rejects_title_only_match(self):
        sources = FakeSources()
        sources._repos = {
            "org/title-only": RepoCandidate(
                full_name="org/title-only",
                html_url="https://github.com/org/title-only",
                description="Maritime AI paper implementation",
                stars=8,
                language="Python",
                topics=["ai", "maritime"],
                updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
                readme_text="Similar title but no paper identifier or link is mentioned here.",
            )
        }
        engine = RepoEngine(sources=sources, queries=[], min_quality_score=0)
        found = engine._discover_repo_for_paper(
            {
                "repo": "",
                "paper_url": "",
                "paper_title": "Maritime AI paper implementation",
                "arxiv_id": "",
                "doi": "",
            },
            reference=datetime(2026, 11, 21, tzinfo=timezone.utc),
        )
        self.assertIsNone(found)

    def test_seed_survives_enrich_error(self):
        class EnrichFailSources(FakeSources):
            def enrich_repo(self, repo, *, refresh=False):
                raise RuntimeError("boom")

        sources = EnrichFailSources()
        sources._repos["org/paired"] = RepoCandidate(
            full_name="org/paired",
            html_url="https://github.com/org/paired",
            description="Implementation for a medical AI paper",
            stars=40,
            language="Python",
            topics=["medical", "pytorch"],
            updated_at=datetime(2026, 11, 20, tzinfo=timezone.utc),
            readme_text="# Paired\n\n## Install\npip install paired\n",
        )
        engine = RepoEngine(
            sources=sources,
            queries=[],
            min_paired=1,
            min_quality_score=2,
            enrich_limit=5,
            allow_stale=True,
        )
        sel = engine.collect(
            1,
            now=datetime(2026, 11, 21, tzinfo=timezone.utc),
            paper_seeds=[{
                "repo": "org/paired",
                "paper_url": "https://arxiv.org/abs/2601.01234",
                "paper_title": "P",
                "arxiv_id": "",
                "doi": "",
            }],
        )
        self.assertEqual(sel.items[0].full_name, "org/paired")
        self.assertTrue(sel.items[0].extra.get("is_paper_seed"))
        self.assertIn("enrich_error", sel.items[0].extra)


if __name__ == "__main__":
    unittest.main()
