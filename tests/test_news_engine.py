import unittest
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime

from collectors.news_engine import (
    NewsEngine,
    NewsQuotaError,
    build_bing_news_url,
    build_google_news_history_url,
    detect_ai_focus,
    detect_domains,
    is_ai_related,
    select_news,
)
from collectors.news_http import FetchResult
from core.models import NewsItem

NOW = datetime(2026, 11, 21, 12, 0, tzinfo=timezone.utc)
FEED_URL = "https://example.com/feed.xml"


class FakeFetcher:
    def __init__(self, mapping, errors=None):
        self.mapping = mapping
        self.errors = errors or {}
        self.calls = []

    def fetch(self, url, check_robots=None, _skip_robots=False):
        self.calls.append({"url": url, "check_robots": check_robots})
        if url in self.errors:
            return FetchResult(url=url, status=500, error=self.errors[url])
        content = self.mapping.get(url)
        if content is None:
            return FetchResult(url=url, status=404, error="http_404")
        return FetchResult(url=url, status=200, content=content, content_type="application/rss+xml")


def rfc(dt: datetime) -> str:
    return format_datetime(dt.astimezone(timezone.utc), usegmt=True)


def item_xml(title, link, published, source="TestSource", desc="AI 技術最新進展") -> str:
    date_tag = f"<pubDate>{rfc(published)}</pubDate>" if published else ""
    return (
        "<item>"
        f"<title>{title}</title>"
        f"<link>{link}</link>"
        f"{date_tag}"
        f"<description><![CDATA[{desc}]]></description>"
        f"<News:Source>{source}</News:Source>"
        "</item>"
    )


def rss(items) -> bytes:
    return (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<rss version="2.0" xmlns:News="https://www.bing.com/news/search">'
        "<channel><title>Test</title>" + "".join(items) + "</channel></rss>"
    ).encode("utf-8")


def make_item(title, *, source="SourceA", domains=("general",), age_hours=1) -> NewsItem:
    return NewsItem(
        title=title,
        url=f"https://example.com/{abs(hash(title))}",
        source=source,
        published_at=NOW - timedelta(hours=age_hours),
        domains=list(domains),
        is_maritime="maritime" in domains,
    ).validate()


class TestTagging(unittest.TestCase):
    def test_ai_related(self):
        self.assertTrue(is_ai_related("OpenAI releases a new LLM"))
        self.assertTrue(is_ai_related("人工智慧應用於醫療"))
        self.assertFalse(is_ai_related("今天天氣很好"))
        self.assertFalse(is_ai_related("Said the captain"))

    def test_detect_domains(self):
        self.assertIn("maritime", detect_domains("AI 應用於船舶航行與港口調度"))
        self.assertIn("maritime", detect_domains("AI marine technology for vessels"))
        self.assertIn("medical", detect_domains("AI medical imaging for hospital diagnosis"))
        self.assertIn("cybersecurity", detect_domains("AI 資安防禦與漏洞偵測"))
        self.assertIn("electronics", detect_domains("AI chip and semiconductor manufacturing"))
        self.assertIn("robotics", detect_domains("humanoid robot embodied AI"))
        self.assertEqual(detect_domains("AI 技術發展"), [])

    def test_marine_odor_does_not_become_maritime(self):
        self.assertNotIn("maritime", detect_domains("tasting notes: nutty, peachy, marine"))
        self.assertNotIn("maritime", detect_domains("AI logistics for warehouse fleets"))
        self.assertNotIn("maritime", detect_domains("Nvidia stops shipping AI chips to China"))

    def test_ai_focus(self):
        self.assertEqual(detect_ai_focus("large language model release"), "llm")
        self.assertEqual(detect_ai_focus("deep learning neural network"), "dl")
        self.assertEqual(detect_ai_focus("machine learning model"), "ml")


class TestBingUrl(unittest.TestCase):
    def test_builds_encoded_url(self):
        url = build_bing_news_url({"query": "海事 AI", "lang": "zh-tw", "cc": "TW"})
        self.assertTrue(url.startswith("https://www.bing.com/news/search?"))
        self.assertIn("format=RSS", url)
        self.assertIn("q=%E6%B5%B7%E4%BA%8B+AI", url)
        self.assertIn("setlang=zh-tw", url)
        self.assertIn("cc=TW", url)


class TestSelection(unittest.TestCase):
    def test_prefers_maritime_and_cross_domain(self):
        items = [
            make_item("一般 AI 新聞 1"),
            make_item("一般 AI 新聞 2"),
            make_item("海事 AI 船舶", domains=("maritime",)),
            make_item("醫療 AI 診斷", domains=("medical",)),
            make_item("資安 AI 防禦", domains=("cybersecurity",)),
        ]
        selection = select_news(items, 3, min_cross=2, min_maritime=1)
        self.assertEqual(len(selection.items), 3)
        titles = [item.title for item in selection.items]
        self.assertIn("海事 AI 船舶", titles)
        self.assertGreaterEqual(selection.report["cross_domain"], 2)

    def test_relaxes_source_cap_when_needed(self):
        items = [make_item(f"AI 新聞 {i}") for i in range(3)]
        selection = select_news(items, 2, max_per_source=1, min_cross=0, min_maritime=0)
        self.assertEqual(len(selection.items), 2)
        self.assertTrue(selection.report["relaxed_source_cap"])

    def test_domain_cap_promotes_diversity(self):
        items = [make_item(f"一般 AI {i}", source=f"G{i}") for i in range(6)]
        items += [make_item(f"資安 AI {i}", source=f"C{i}", domains=("cybersecurity",)) for i in range(6)]
        items.append(make_item("醫療 AI 診斷", source="M", domains=("medical",)))
        items.append(make_item("海事 AI 船舶", source="S", domains=("maritime",)))
        selection = select_news(items, 10, max_per_source=0, max_per_domain=4)
        domains = [d for item in selection.items for d in item.domains]
        self.assertLessEqual(domains.count("cybersecurity"), 4)
        self.assertIn("醫療 AI 診斷", [item.title for item in selection.items])

    def test_maritime_quota_failure(self):
        items = [make_item(f"一般 AI 新聞 {i}", source=f"S{i}") for i in range(10)]
        with self.assertRaises(NewsQuotaError) as ctx:
            select_news(items, 10)
        self.assertIn("海事", str(ctx.exception))

    def test_count_failure(self):
        items = [make_item("海事 AI", domains=("maritime",))]
        with self.assertRaises(NewsQuotaError) as ctx:
            select_news(items, 10)
        self.assertIn("數量不足", str(ctx.exception))


class TestNewsEngine(unittest.TestCase):
    def make_engine(self, content: bytes, **kwargs):
        fetcher = FakeFetcher({FEED_URL: content})
        engine = NewsEngine(
            fetcher=fetcher,
            queries=[],
            feeds=[{"name": "Test", "url": FEED_URL, "hint": "general"}],
            bing_enabled=False,
            **kwargs,
        )
        return engine, fetcher

    def test_full_collect_with_quotas_and_filters(self):
        items = []
        for i in range(8):
            items.append(item_xml(f"AI 技術新聞 {i}", f"https://example.com/n/{i}",
                                  NOW - timedelta(hours=i + 1), source=f"Source{i % 4}"))
        items.append(item_xml("AI 船舶航運安全", "https://example.com/maritime",
                              NOW - timedelta(hours=2), source="SourceA", desc="海事 AI 船舶與港口"))
        items.append(item_xml("AI 醫療影像診斷", "https://example.com/medical1",
                              NOW - timedelta(hours=3), source="SourceB", desc="醫療 AI 醫院"))
        items.append(item_xml("AI 醫療臨床應用", "https://example.com/medical2",
                              NOW - timedelta(hours=4), source="SourceC", desc="臨床 AI 病患"))
        items.append(item_xml("AI 資安漏洞防禦", "https://example.com/cyber",
                              NOW - timedelta(hours=5), source="SourceD", desc="資安 AI 漏洞"))
        engine, fetcher = self.make_engine(rss(items))

        selection = engine.collect(10, now=NOW)
        self.assertEqual(len(selection.items), 10)
        self.assertGreaterEqual(selection.report["cross_domain"], 3)
        self.assertGreaterEqual(selection.report["maritime"], 1)
        self.assertEqual(selection.report["sources"][f"rss:Test"]["found"], 12)
        self.assertTrue(all(item.published_at <= NOW for item in selection.items))
        self.assertTrue(fetcher.calls[0]["check_robots"] is engine.robots_check)

    def test_filters_stale_no_date_and_non_ai_and_duplicates(self):
        items = [
            item_xml("AI 技術新聞", "https://example.com/1", NOW - timedelta(days=1)),
            item_xml("AI 技術新聞", "https://example.com/2", NOW - timedelta(days=1)),  # duplicate title
            item_xml("AI 過期新聞", "https://example.com/3", NOW - timedelta(days=20)),
            item_xml("AI 無日期新聞", "https://example.com/4", None),
            item_xml("Sports championship", "https://example.com/5", NOW - timedelta(days=1),
                     desc="match results"),
            item_xml("AI 內網連結", "http://127.0.0.1/x", NOW - timedelta(days=1)),
        ]
        engine, _ = self.make_engine(rss(items))
        with self.assertRaises(NewsQuotaError) as ctx:
            engine.collect(10, now=NOW)
        reasons = ctx.exception.report["rejected_counts"]
        self.assertEqual(reasons.get("duplicate"), 1)
        self.assertEqual(reasons.get("stale"), 1)
        self.assertEqual(reasons.get("no_date"), 1)
        self.assertEqual(reasons.get("not_ai"), 1)
        self.assertTrue(any(key.startswith("invalid") for key in reasons))

    def test_three_consecutive_dates_pass_quotas(self):
        for offset in range(3):
            reference = NOW - timedelta(days=offset)
            items = [
                item_xml(f"AI 一般新聞 {offset}-{i}", f"https://example.com/{offset}/{i}",
                         reference - timedelta(hours=i + 1), source=f"G{i % 3}")
                for i in range(7)
            ]
            items.append(item_xml(f"AI 海事船舶 {offset}", f"https://example.com/{offset}/mar",
                                  reference - timedelta(hours=2), source="Mar", desc="海事 船舶 AI"))
            items.append(item_xml(f"AI 醫療診斷 {offset}", f"https://example.com/{offset}/med",
                                  reference - timedelta(hours=3), source="Med", desc="醫療 AI"))
            items.append(item_xml(f"AI 資安防禦 {offset}", f"https://example.com/{offset}/cyb",
                                  reference - timedelta(hours=4), source="Cyb", desc="資安 AI"))
            engine, _ = self.make_engine(rss(items))
            selection = engine.collect(10, now=reference)
            self.assertEqual(len(selection.items), 10)
            self.assertGreaterEqual(selection.report["cross_domain"], 3)
            self.assertGreaterEqual(selection.report["maritime"], 1)

    def test_source_failure_does_not_break_other_sources(self):
        good_url = "https://example.com/good.xml"
        bad_url = "https://example.com/bad.xml"
        content = rss([
            item_xml(f"AI 新聞 {i}", f"https://example.com/g/{i}", NOW - timedelta(hours=i + 1),
                     source=f"S{i % 3}")
            for i in range(6)
        ] + [
            item_xml("AI 海事船舶", "https://example.com/maritime", NOW - timedelta(hours=2),
                     source="SMar", desc="海事 船舶 AI"),
            item_xml("AI 醫療診斷", "https://example.com/medical", NOW - timedelta(hours=2),
                     source="SMed", desc="醫療 AI"),
            item_xml("AI 資安防禦", "https://example.com/cyber", NOW - timedelta(hours=2),
                     source="SCyb", desc="資安 AI"),
            item_xml("AI 機器人", "https://example.com/robot", NOW - timedelta(hours=2),
                     source="SRob", desc="機器人 具身 AI"),
        ])
        fetcher = FakeFetcher({good_url: content})
        engine = NewsEngine(
            fetcher=fetcher,
            queries=[],
            feeds=[
                {"name": "Bad", "url": bad_url, "hint": "general"},
                {"name": "Good", "url": good_url, "hint": "general"},
            ],
            bing_enabled=False,
        )
        selection = engine.collect(9, now=NOW)
        self.assertEqual(len(selection.items), 9)
        self.assertEqual(selection.report["sources"]["rss:Bad"]["errors"], 1)
        self.assertEqual(selection.report["sources"]["rss:Good"]["errors"], 0)

    def test_allow_stale_uses_history_feed_and_rejects_future(self):
        target = datetime(2026, 9, 14, 23, 59, 59, tzinfo=timezone.utc)
        query = {"query": "人工智慧", "lang": "zh-tw", "cc": "TW", "hint": "general"}
        url = build_google_news_history_url(query, target.date())
        items = [
            item_xml(f"AI 技術新聞 {i}", f"https://example.com/h/{i}",
                     target - timedelta(hours=i + 2), source=f"S{i % 4}")
            for i in range(8)
        ]
        items += [
            item_xml("AI 海事船舶", "https://example.com/h/mar", target - timedelta(hours=3),
                     source="Mar", desc="海事 船舶 AI"),
            item_xml("AI 醫療診斷", "https://example.com/h/med", target - timedelta(hours=4),
                     source="Med", desc="醫療 AI 醫院"),
            item_xml("AI 資安防禦", "https://example.com/h/cyb", target - timedelta(hours=5),
                     source="Cyb", desc="資安 AI 漏洞"),
            item_xml("未來 AI 新聞", "https://example.com/h/future", target + timedelta(days=60),
                     source="Future"),
        ]
        fetcher = FakeFetcher({url: rss(items)})
        engine = NewsEngine(
            fetcher=fetcher,
            queries=[query],
            feeds=[],
            allow_stale=True,
            bing_enabled=False,
        )

        selection = engine.collect(10, now=target)

        titles = [item.title for item in selection.items]
        self.assertEqual(len(titles), 10)
        self.assertNotIn("未來 AI 新聞", titles)
        self.assertTrue(all(item.published_at <= target for item in selection.items))
        self.assertTrue(any(
            "news.google.com/rss/search" in call["url"]
            and "after%3A2026-09-13" in call["url"]
            and "before%3A2026-09-15" in call["url"]
            and call["check_robots"] is False
            for call in fetcher.calls
        ))


if __name__ == "__main__":
    unittest.main()
