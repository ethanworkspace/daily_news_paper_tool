import unittest

from core.dedupe import (
    Deduper,
    dedupe_items,
    extract_arxiv_id,
    is_similar_title,
    make_keys,
    normalize_arxiv_id,
    normalize_doi,
    normalize_url,
    title_fingerprint,
)


class TestNormalizeUrl(unittest.TestCase):
    def test_strips_tracking_and_normalizes(self):
        url = "HTTPS://Example.COM:443/a/b/?utm_source=x&b=2&a=1&fbclid=z#frag"
        self.assertEqual(normalize_url(url), "https://example.com/a/b?a=1&b=2")

    def test_keeps_root_slash(self):
        self.assertEqual(normalize_url("https://example.com/"), "https://example.com/")

    def test_collapses_duplicate_trailing_slash(self):
        self.assertEqual(normalize_url("https://example.com/a///"), "https://example.com/a")

    def test_non_url_returned_trimmed(self):
        self.assertEqual(normalize_url("  not a url  "), "not a url")
        self.assertEqual(normalize_url(None), "")


class TestTitleFingerprint(unittest.TestCase):
    def test_removes_punctuation_and_spaces(self):
        self.assertEqual(title_fingerprint("AI：模型 新突破！"), "ai模型新突破")

    def test_similar_titles(self):
        self.assertTrue(is_similar_title("AI：模型新突破", "AI 模型新突破！"))
        self.assertFalse(is_similar_title("AI 模型新突破", "海事船舶航行安全"))

    def test_containment(self):
        self.assertTrue(is_similar_title("OpenAI releases GPT-5 model", "OpenAI releases GPT-5 model today"))


class TestDoiAndArxiv(unittest.TestCase):
    def test_normalize_doi(self):
        self.assertEqual(normalize_doi("https://doi.org/10.1000/ABC.123"), "10.1000/abc.123")
        self.assertEqual(normalize_doi("doi:10.5555/xyz."), "10.5555/xyz")
        self.assertEqual(normalize_doi("not-a-doi"), "")

    def test_extract_arxiv_id(self):
        self.assertEqual(extract_arxiv_id("https://arxiv.org/abs/2601.01234v3"), "2601.01234")
        self.assertEqual(extract_arxiv_id("arXiv:2601.01234"), "2601.01234")
        self.assertEqual(extract_arxiv_id("cs/0701001"), "cs/0701001")
        self.assertEqual(extract_arxiv_id("nothing here"), "")

    def test_normalize_arxiv_id(self):
        self.assertEqual(normalize_arxiv_id("arXiv:2601.01234v12"), "2601.01234")

    def test_make_keys(self):
        keys = make_keys(
            url="https://arxiv.org/abs/2601.01234v2",
            title="Paper: Test",
            doi="https://doi.org/10.1/ABC",
            repo="Owner/Repo",
        )
        self.assertIn("url:https://arxiv.org/abs/2601.01234v2", keys)
        self.assertIn("title:papertest", keys)
        self.assertIn("doi:10.1/abc", keys)
        self.assertIn("arxiv:2601.01234", keys)
        self.assertIn("repo:owner/repo", keys)


class TestDeduper(unittest.TestCase):
    def test_add_semantics(self):
        deduper = Deduper()
        self.assertTrue(deduper.add("url:x"))
        self.assertFalse(deduper.add("url:x"))
        self.assertTrue(deduper.add("url:y", "title:t"))
        self.assertFalse(deduper.add("title:t"))

    def test_dedupe_items_keeps_first(self):
        items = [
            {"u": "https://a.com/x", "t": "A"},
            {"u": "https://a.com/x/", "t": "A!"},
            {"u": "https://b.com/y", "t": "B"},
        ]
        unique = dedupe_items(items, lambda x: make_keys(url=x["u"], title=x["t"]))
        self.assertEqual(len(unique), 2)
        self.assertEqual(unique[0]["u"], "https://a.com/x")


if __name__ == "__main__":
    unittest.main()
