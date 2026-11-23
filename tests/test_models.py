import unittest
from datetime import datetime, timedelta, timezone

from core.models import (
    DailyBundle,
    NewsItem,
    PaperItem,
    RepoItem,
    SchemaError,
    TechArchItem,
)

NOW = datetime(2026, 11, 21, 12, 0, tzinfo=timezone.utc)


def days_ago(days: float) -> datetime:
    return NOW - timedelta(days=days)


def make_news(**overrides) -> NewsItem:
    data = dict(
        title="AI 模型新突破",
        url="https://example.com/news/1",
        source="Example News",
        published_at=days_ago(1),
        domains=["general"],
        summary="摘要內容",
    )
    data.update(overrides)
    return NewsItem(**data)


def make_paper(**overrides) -> PaperItem:
    data = dict(
        title="A Paper on Maritime AI",
        url="https://arxiv.org/abs/2601.01234",
        source_name="arXiv",
        source_tier=3,
        published_at=days_ago(5),
        parse_level="abstract",
        abstract="abstract",
    )
    data.update(overrides)
    return PaperItem(**data)


def make_repo(**overrides) -> RepoItem:
    data = dict(
        full_name="owner/repo",
        html_url="https://github.com/owner/repo",
        description="demo",
        stars=10,
        forks=2,
        language="Python",
        updated_at=days_ago(3),
    )
    data.update(overrides)
    return RepoItem(**data)


def make_tech(**overrides) -> TechArchItem:
    data = dict(
        name="Test Architecture",
        principle="說明原理" * 20,
        applications_maritime="海事應用說明" * 20,
        applications_medical="醫療應用說明" * 20,
        reference_urls=["https://example.com/tech"],
    )
    data.update(overrides)
    return TechArchItem(**data)


class TestNewsItem(unittest.TestCase):
    def test_valid(self):
        item = make_news().validate()
        self.assertEqual(item.domains, ["general"])

    def test_requires_https_or_http(self):
        with self.assertRaises(SchemaError):
            make_news(url="ftp://example.com/a").validate()
        with self.assertRaises(SchemaError):
            make_news(url="http://localhost/a").validate()

    def test_missing_title(self):
        with self.assertRaises(SchemaError):
            make_news(title="").validate()

    def test_unknown_domain(self):
        with self.assertRaises(SchemaError):
            make_news(domains=["space"]).validate()

    def test_domains_deduped(self):
        item = make_news(domains=["general", "general"]).validate()
        self.assertEqual(item.domains, ["general"])

    def test_is_maritime_adds_domain(self):
        item = make_news(is_maritime=True).validate()
        self.assertIn("maritime", item.domains)

    def test_bad_date(self):
        with self.assertRaises(SchemaError):
            make_news(published_at="not-a-date").validate()


class TestPaperItem(unittest.TestCase):
    def test_valid(self):
        paper = make_paper(code_url="https://github.com/owner/repo").validate()
        self.assertEqual(paper.code_url, "https://github.com/owner/repo")

    def test_tier_validation(self):
        with self.assertRaises(SchemaError):
            make_paper(source_tier=4).validate()

    def test_parse_level(self):
        with self.assertRaises(SchemaError):
            make_paper(parse_level="partial").validate()

    def test_sections_required(self):
        with self.assertRaises(SchemaError):
            make_paper().validate(require_sections=True)
        sections = {k: "內容" * 60 for k in ("background", "method", "results", "limitations")}
        paper = make_paper(sections=sections).validate(require_sections=True, min_section_chars=100)
        self.assertEqual(set(paper.sections), {"background", "method", "results", "limitations"})

    def test_unknown_section_rejected(self):
        with self.assertRaises(SchemaError):
            make_paper(sections={"intro": "x"}).validate()

    def test_bad_pdf_url(self):
        with self.assertRaises(SchemaError):
            make_paper(pdf_url="file:///etc/passwd").validate()


class TestRepoItem(unittest.TestCase):
    def test_valid(self):
        repo = make_repo().validate()
        self.assertEqual(repo.full_name, "owner/repo")

    def test_full_name_format(self):
        with self.assertRaises(SchemaError):
            make_repo(full_name="not a repo").validate()

    def test_negative_stars(self):
        with self.assertRaises(SchemaError):
            make_repo(stars=-1).validate()

    def test_sections_required(self):
        with self.assertRaises(SchemaError):
            make_repo().validate(require_sections=True)
        sections = {k: "內容" * 60 for k in ("what", "tech", "architecture")}
        repo = make_repo(sections=sections).validate(require_sections=True, min_section_chars=100)
        self.assertEqual(set(repo.sections), {"what", "tech", "architecture"})


class TestTechArchItem(unittest.TestCase):
    def test_valid(self):
        tech = make_tech().validate()
        self.assertEqual(tech.name, "Test Architecture")

    def test_requires_maritime_and_medical(self):
        with self.assertRaises(SchemaError):
            make_tech(applications_maritime="").validate()
        with self.assertRaises(SchemaError):
            make_tech(applications_medical="").validate()

    def test_requires_reference_urls(self):
        with self.assertRaises(SchemaError):
            make_tech(reference_urls=[]).validate()


class TestDailyBundle(unittest.TestCase):
    def build_bundle(self, **overrides) -> DailyBundle:
        news = [
            make_news(url=f"https://example.com/n/{i}", domains=["general"]) for i in range(7)
        ]
        news.append(make_news(url="https://example.com/n/mar", domains=["maritime"], is_maritime=True))
        news.append(make_news(url="https://example.com/n/med", domains=["medical"]))
        news.append(make_news(url="https://example.com/n/sec", domains=["cybersecurity"]))
        papers = [
            make_paper(url=f"https://arxiv.org/abs/2601.0123{i}", code_url=("https://github.com/o/r" if i < 3 else ""))
            for i in range(5)
        ]
        repos = [
            make_repo(full_name=f"owner/repo{i}", html_url=f"https://github.com/owner/repo{i}",
                      paper_url=("https://arxiv.org/abs/2601.01230" if i < 2 else ""))
            for i in range(5)
        ]
        data = dict(
            date="2026-11-21",
            news=news,
            papers=papers,
            repos=repos,
            tech=make_tech(),
        )
        data.update(overrides)
        return DailyBundle(**data)

    def test_valid_bundle_and_quotas(self):
        quotas = self.build_bundle().validate(now=NOW)
        self.assertEqual(quotas["news_total"], 10)
        self.assertEqual(quotas["cross_domain"], 3)
        self.assertEqual(quotas["maritime"], 1)
        self.assertTrue(quotas["cross_domain_ok"])
        self.assertEqual(quotas["paired_papers_seed"], 3)
        self.assertEqual(quotas["paired_repos_seed"], 2)
        self.assertEqual(quotas["paired_papers"], 1)
        self.assertEqual(quotas["paired_repos"], 2)

    def test_counts_enforced(self):
        bundle = self.build_bundle()
        bundle.news = bundle.news[:9]
        with self.assertRaises(SchemaError):
            bundle.validate(now=NOW)

    def test_tech_required(self):
        with self.assertRaises(SchemaError):
            self.build_bundle(tech=None).validate(now=NOW)

    def test_quota_failure(self):
        news = [make_news(url=f"https://example.com/g/{i}") for i in range(10)]
        with self.assertRaises(SchemaError) as ctx:
            self.build_bundle(news=news).validate(now=NOW)
        self.assertIn("跨域", str(ctx.exception))

    def test_maritime_failure(self):
        news = [
            make_news(url=f"https://example.com/g/{i}", domains=["general"]) for i in range(7)
        ] + [
            make_news(url="https://example.com/med", domains=["medical"]),
            make_news(url="https://example.com/sec", domains=["cybersecurity"]),
            make_news(url="https://example.com/elec", domains=["electronics"]),
        ]
        with self.assertRaises(SchemaError) as ctx:
            self.build_bundle(news=news).validate(now=NOW)
        self.assertIn("海事", str(ctx.exception))

    def test_stale_news_rejected(self):
        bundle = self.build_bundle()
        bundle.news[0].published_at = days_ago(20)
        with self.assertRaises(SchemaError):
            bundle.validate(now=NOW)

    def test_stale_paper_rejected(self):
        bundle = self.build_bundle()
        bundle.papers[0].published_at = days_ago(45)
        with self.assertRaises(SchemaError):
            bundle.validate(now=NOW)

    def test_stale_repo_rejected(self):
        bundle = self.build_bundle()
        bundle.repos[0].updated_at = days_ago(45)
        with self.assertRaises(SchemaError):
            bundle.validate(now=NOW)

    def test_flexible_pairing_allowed(self):
        bundle = self.build_bundle()
        for paper in bundle.papers:
            paper.code_url = ""
        for repo in bundle.repos:
            repo.paper_url = ""
        quotas = bundle.validate(now=NOW)
        self.assertEqual(quotas["paired_papers"], 0)
        self.assertTrue(quotas["cross_domain_ok"])

    def test_canonical_arxiv_url_pairing_counts(self):
        bundle = self.build_bundle()
        bundle.papers[0].url = "http://arxiv.org/abs/2601.01230v1"
        bundle.repos[0].paper_url = "https://arxiv.org/abs/2601.01230"
        quotas = bundle.validate(now=NOW)
        self.assertGreaterEqual(quotas["paired_papers"], 1)
        self.assertGreaterEqual(quotas["paired_repos"], 1)


if __name__ == "__main__":
    unittest.main()
