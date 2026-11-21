import unittest
from datetime import datetime, timedelta, timezone

from collectors.paper_engine import PaperEngine, PaperQuotaError, candidate_to_item, select_papers
from collectors.paper_parse import PaperCandidate
from core.models import PaperItem

NOW = datetime(2026, 11, 21, 12, 0, tzinfo=timezone.utc)


def make_candidate(title: str, *, hours=2, source="arXiv", tier=3, code_url="", doi="", arxiv_id="", impact="N/A (preprint)"):
    return PaperCandidate(
        title=title,
        url=f"https://example.com/{abs(hash(title)) % 100000}",
        source_name=source,
        source_tier=tier,
        published_at=NOW - timedelta(hours=hours),
        authors=["A"],
        abstract="This paper studies a large language model for medical diagnosis.",
        pdf_url="",
        code_url=code_url,
        doi=doi,
        arxiv_id=arxiv_id,
        journal=source,
        venue=source,
        impact_factor=impact,
        impact_factor_source="test",
        cited_by_count=1,
        parse_level="abstract",
    )


def make_item(title: str, **kwargs) -> PaperItem:
    return candidate_to_item(make_candidate(title, **kwargs)).validate()


class FakeSources:
    def __init__(self, mapping=None):
        self.mapping = mapping or {}

    def search_arxiv(self, query, **kwargs):
        c = self.mapping.get(("arxiv", query), [])
        return c, type("S", (), {"name": "arxiv", "found": len(c), "fetched": 1, "errors": 0, "error": ""})()

    def search_openalex(self, query, **kwargs):
        c = self.mapping.get(("openalex", query), [])
        return c, type("S", (), {"name": "openalex", "found": len(c), "fetched": 1, "errors": 0, "error": ""})()

    def search_pubmed(self, query, **kwargs):
        c = self.mapping.get(("pubmed", query), [])
        return c, type("S", (), {"name": "pubmed", "found": len(c), "fetched": 1, "errors": 0, "error": ""})()

    def search_semantic_scholar(self, query, **kwargs):
        c = self.mapping.get(("s2", query), [])
        return c, type("S", (), {"name": "semantic_scholar", "found": len(c), "fetched": 0, "errors": 1, "error": "http_429"})()

    def enrich_fulltext(self, paper, max_chars=300000):
        paper.fulltext_excerpt = (paper.abstract or "") + "\n## Methods\nDetails here." * 30
        paper.parse_level = "fulltext"
        paper.extra["fulltext_kind"] = "pdf"
        paper.extra["fulltext_source"] = paper.pdf_url or paper.url
        return paper


class TestCandidateToItem(unittest.TestCase):
    def test_sets_if_and_pairing(self):
        cand = make_candidate("T", code_url="https://github.com/a/b", impact="h_index=10 (OpenAlex)")
        item = candidate_to_item(cand).validate()
        self.assertEqual(item.impact_factor, "h_index=10 (OpenAlex)")
        self.assertEqual(item.code_url, "https://github.com/a/b")
        self.assertEqual(item.paired_repo, "a/b")


class TestSelection(unittest.TestCase):
    def test_prefers_paired_and_tier(self):
        items = [
            make_item("P1", source="arXiv", tier=3),
            make_item("P2", source="Nature", tier=1, impact="2yr_mean_citedness=50 (OpenAlex)"),
            make_item("P3", source="arXiv", tier=3, code_url="https://github.com/x/y"),
            make_item("P4", source="JMLR", tier=2, impact="h_index=100 (OpenAlex)"),
            make_item("P5", source="arXiv", tier=3),
            make_item("P6", source="arXiv", tier=3, code_url="https://github.com/u/v"),
        ]
        sel = select_papers(items, 4, max_per_source=3, min_paired=2)
        self.assertEqual(len(sel.items), 4)
        self.assertGreaterEqual(sel.report["paired"], 2)

    def test_quota_error(self):
        items = [make_item("Only one")]
        with self.assertRaises(PaperQuotaError):
            select_papers(items, 5, max_per_source=5, min_paired=0)


class TestPaperEngine(unittest.TestCase):
    def test_collect_filters_and_selects(self):
        # build enough candidates across queries
        mapping = {}
        q = "large language model"
        mapping[("arxiv", q)] = [
            make_candidate(f"LLM paper {i}", arxiv_id=f"2601.0000{i}", code_url=("https://github.com/o/r" if i < 3 else ""))
            for i in range(4)
        ]
        mapping[("openalex", q)] = [
            make_candidate(f"OA paper {i}", source="Nature AI", tier=1, doi=f"10.1/{i}", impact="2yr_mean_citedness=10 (OpenAlex)")
            for i in range(3)
        ]
        engine = PaperEngine(
            sources=FakeSources(mapping),
            queries=[{"query": q, "hint": "general"}],
            max_per_source=3,
            min_paired=2,
            enrich_fulltext=True,
            enrich_limit=5,
        )
        sel = engine.collect(5, now=NOW)
        self.assertEqual(len(sel.items), 5)
        self.assertGreaterEqual(sel.report["paired"], 2)
        self.assertIn("arxiv", sel.report["sources"])
        self.assertIn("semantic_scholar", sel.report["sources"])  # queried (error)
        self.assertTrue(all(item.impact_factor for item in sel.items))

    def test_rejects_stale_no_date_not_ai_duplicate(self):
        mapping = {}
        q = "large language model"
        stale = make_candidate("Stale AI paper")
        stale.published_at = NOW - timedelta(days=40)
        nodate = make_candidate("No date AI paper")
        nodate.published_at = None
        not_ai = make_candidate("Cooking recipes")
        not_ai.abstract = "How to bake a cake."
        dup = make_candidate("LLM paper dup", arxiv_id="2601.99999")
        dup2 = make_candidate("LLM paper dup", arxiv_id="2601.99999")  # same arxiv id
        good = [make_candidate(f"Good AI {i}", arxiv_id=f"2601.1000{i}", source=f"S{i}") for i in range(6)]
        mapping[("arxiv", q)] = [stale, nodate, not_ai, dup, dup2] + good
        engine = PaperEngine(
            sources=FakeSources(mapping),
            queries=[{"query": q, "hint": "general"}],
            min_paired=0,
            enrich_fulltext=False,
        )
        with self.assertRaises(PaperQuotaError) as ctx:
            engine.collect(10, now=NOW)
        reasons = ctx.exception.report["rejected_counts"]
        self.assertIn("stale", reasons)
        self.assertIn("no_date", reasons)
        self.assertIn("not_ai", reasons)
        self.assertIn("duplicate", reasons)

    def test_enrichment_sets_fulltext_and_pairing(self):
        mapping = {("arxiv", "large language model"): [make_candidate(f"P{i}") for i in range(5)]}
        engine = PaperEngine(
            sources=FakeSources(mapping),
            queries=[{"query": "large language model"}],
            min_paired=0,
            enrich_fulltext=True,
            enrich_limit=5,
        )
        sel = engine.collect(5, now=NOW)
        self.assertTrue(any(item.parse_level == "fulltext" for item in sel.items))
        self.assertTrue(all(item.fulltext_excerpt for item in sel.items))


if __name__ == "__main__":
    unittest.main()
