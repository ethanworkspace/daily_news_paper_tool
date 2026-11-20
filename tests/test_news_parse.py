import unittest
from urllib.parse import quote

from collectors.news_parse import (
    FeedParseError,
    parse_feed,
    strip_html,
    unwrap_aggregator_url,
)


def rss_document(items: str) -> bytes:
    return (
        '<?xml version="1.0" encoding="utf-8"?>'
        '<rss version="2.0" xmlns:News="https://www.bing.com/news/search">'
        "<channel><title>Test</title>"
        f"{items}"
        "</channel></rss>"
    ).encode("utf-8")


class TestStripHtml(unittest.TestCase):
    def test_removes_tags_and_scripts(self):
        html = "<p>Hello <b>world</b></p><script>alert('x')</script><style>.a{}</style>"
        self.assertEqual(strip_html(html), "Hello world")

    def test_decodes_entities(self):
        self.assertEqual(strip_html("AI &amp; ML &lt;test&gt;"), "AI & ML <test>")

    def test_collapses_whitespace_and_controls(self):
        self.assertEqual(strip_html("a\n\t b\x00  c"), "a b c")

    def test_truncates(self):
        self.assertEqual(len(strip_html("x" * 100, max_length=10)), 10)

    def test_empty(self):
        self.assertEqual(strip_html(None), "")


class TestUnwrap(unittest.TestCase):
    def test_unwraps_bing_apiclick(self):
        target = "https://example.com/article?id=1&x=2"
        url = (
            "https://www.bing.com/news/apiclick.aspx?ref=FexRss&aid=1"
            f"&url={quote(target, safe='')}"
        )
        self.assertEqual(unwrap_aggregator_url(url), target)

    def test_keeps_other_urls(self):
        self.assertEqual(unwrap_aggregator_url("https://example.com/a"), "https://example.com/a")
        self.assertEqual(unwrap_aggregator_url(""), "")


class TestParseRss(unittest.TestCase):
    def test_parses_items(self):
        doc = rss_document(
            "<item>"
            "<title>AI 新技術 - TestSource</title>"
            "<link>https://example.com/a</link>"
            "<pubDate>Fri, 20 Nov 2026 10:00:00 GMT</pubDate>"
            "<description><![CDATA[<p>重點 &amp; 內容</p>]]></description>"
            "<News:Source>TestSource</News:Source>"
            "</item>"
            "<item>"
            "<title>Second</title><link>https://example.com/b</link>"
            "<pubDate>Sat, 21 Nov 2026 01:00:00 GMT</pubDate>"
            "<description>plain</description>"
            "</item>"
        )
        items = parse_feed(doc, feed_name="TestFeed", language="en", country="US", hint="general")
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].title, "AI 新技術")
        self.assertEqual(items[0].source, "TestSource")
        self.assertEqual(items[0].snippet, "重點 & 內容")
        self.assertEqual(items[1].source, "TestFeed")
        self.assertEqual(items[1].language, "en")

    def test_skips_items_without_title_or_link(self):
        doc = rss_document("<item><title>No link</title></item>")
        self.assertEqual(parse_feed(doc, feed_name="f"), [])

    def test_uses_guid_as_link(self):
        doc = rss_document(
            "<item><title>T</title><guid>https://example.com/g</guid>"
            "<pubDate>Fri, 20 Nov 2026 10:00:00 GMT</pubDate></item>"
        )
        items = parse_feed(doc, feed_name="f")
        self.assertEqual(items[0].url, "https://example.com/g")

    def test_rejects_entity_declarations(self):
        doc = (
            '<?xml version="1.0"?><!DOCTYPE rss [<!ENTITY x "boom">]>'
            "<rss><channel><item><title>&x;</title></item></channel></rss>"
        ).encode("utf-8")
        with self.assertRaises(FeedParseError):
            parse_feed(doc, feed_name="f")

    def test_malformed_raises(self):
        with self.assertRaises(FeedParseError):
            parse_feed(b"<rss><channel>", feed_name="f")


class TestParseAtom(unittest.TestCase):
    def test_parses_entries(self):
        doc = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<feed xmlns="http://www.w3.org/2005/Atom">'
            "<title>Feed</title>"
            "<entry>"
            "<title>Atom AI News</title>"
            '<link rel="alternate" href="https://example.com/atom/1"/>'
            "<published>2026-11-20T08:00:00Z</published>"
            "<summary>summary text</summary>"
            "<author><name>Alice</name></author>"
            "</entry>"
            "</feed>"
        ).encode("utf-8")
        items = parse_feed(doc, feed_name="AtomFeed", language="en")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Atom AI News")
        self.assertEqual(items[0].url, "https://example.com/atom/1")
        self.assertEqual(items[0].source, "Alice")
        self.assertEqual(items[0].published_raw, "2026-11-20T08:00:00Z")


if __name__ == "__main__":
    unittest.main()
