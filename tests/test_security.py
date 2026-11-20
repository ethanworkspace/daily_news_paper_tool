import unittest

from core.security import (
    UnsafeURLError,
    assert_public_http_url,
    redact_secrets,
)


class TestRedact(unittest.TestCase):
    def test_masks_openai_style_key(self):
        secret = "sk-" + "A1b2" * 6
        self.assertNotIn(secret, redact_secrets(f"key={secret}"))
        self.assertIn("****", redact_secrets(f"key={secret}"))

    def test_masks_bearer_token(self):
        redacted = redact_secrets("Authorization: Bearer abcdefghijklmnop")
        self.assertNotIn("abcdefghijklmnop", redacted)
        self.assertIn("Bearer ****", redacted)

    def test_masks_query_token(self):
        redacted = redact_secrets("https://x.com/a?api_key=supersecretvalue&b=1")
        self.assertNotIn("supersecretvalue", redacted)
        self.assertIn("b=1", redacted)

    def test_keeps_plain_text(self):
        self.assertEqual(redact_secrets("一般訊息"), "一般訊息")
        self.assertEqual(redact_secrets(None), "")


class TestPublicURL(unittest.TestCase):
    def test_accepts_public_http_urls(self):
        for url in (
            "https://arxiv.org/abs/2601.01234",
            "http://example.com:8080/path?q=1",
            "https://github.com/owner/repo",
        ):
            self.assertEqual(assert_public_http_url(url), url)

    def test_rejects_bad_schemes_and_forms(self):
        for url in (
            "",
            "ftp://example.com/a",
            "javascript:alert(1)",
            "file:///etc/passwd",
            "https://user:pass@example.com/",
            "https://exa mple.com/",
            "https:///nohost",
        ):
            with self.assertRaises(UnsafeURLError):
                assert_public_http_url(url)

    def test_rejects_private_and_reserved_hosts(self):
        for url in (
            "http://localhost/admin",
            "http://127.0.0.1/",
            "http://[::1]/",
            "http://169.254.169.254/latest/meta-data",
            "http://printer.local/",
            "http://metadata.internal/",
        ):
            with self.assertRaises(UnsafeURLError):
                assert_public_http_url(url)


if __name__ == "__main__":
    unittest.main()
