import unittest

import requests

from collectors.news_http import SafeHttpFetcher


class FakeResponse:
    def __init__(self, status=200, headers=None, body=b"", chunks=None):
        self.status_code = status
        self.headers = headers or {}
        self.body = body
        self._chunks = chunks
        self.closed = False

    def iter_content(self, size):
        if self._chunks is not None:
            yield from self._chunks
        else:
            yield self.body

    def close(self):
        self.closed = True


class FakeSession:
    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append((url, kwargs))
        if url not in self.routes:
            raise requests.ConnectionError(f"no route for {url}")
        value = self.routes[url]
        if callable(value):
            return value(url)
        return value


class TestSafeHttpFetcher(unittest.TestCase):
    def make(self, routes, **kwargs):
        session = FakeSession(routes)
        fetcher = SafeHttpFetcher(session=session, **kwargs)
        return fetcher, session

    def test_rejects_private_url_without_request(self):
        fetcher, session = self.make({})
        result = fetcher.fetch("http://127.0.0.1/secret")
        self.assertFalse(result.ok)
        self.assertIn("unsafe_url", result.error)
        self.assertEqual(session.calls, [])

    def test_fetch_success(self):
        fetcher, _ = self.make({"https://example.com/feed": FakeResponse(body=b"hello")})
        result = fetcher.fetch("https://example.com/feed", check_robots=False)
        self.assertTrue(result.ok)
        self.assertEqual(result.content, b"hello")

    def test_redirect_is_followed_and_validated(self):
        fetcher, _ = self.make(
            {
                "https://example.com/a": FakeResponse(302, {"Location": "/b"}),
                "https://example.com/b": FakeResponse(200, body=b"final"),
            }
        )
        result = fetcher.fetch("https://example.com/a", check_robots=False)
        self.assertTrue(result.ok)
        self.assertEqual(result.content, b"final")
        self.assertEqual(result.final_url, "https://example.com/b")

    def test_redirect_to_private_rejected(self):
        fetcher, _ = self.make(
            {
                "https://example.com/a": FakeResponse(302, {"Location": "http://169.254.169.254/latest"}),
            }
        )
        result = fetcher.fetch("https://example.com/a", check_robots=False)
        self.assertFalse(result.ok)
        self.assertIn("unsafe_redirect", result.error)

    def test_too_many_redirects(self):
        fetcher, _ = self.make(
            {
                "https://example.com/loop": FakeResponse(302, {"Location": "/loop"}),
            },
            max_redirects=2,
        )
        result = fetcher.fetch("https://example.com/loop", check_robots=False)
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "too_many_redirects")

    def test_size_limit(self):
        fetcher, _ = self.make(
            {"https://example.com/big": FakeResponse(body=b"x" * 100)},
            max_bytes=10,
        )
        result = fetcher.fetch("https://example.com/big", check_robots=False)
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "too_large")

    def test_http_error(self):
        fetcher, _ = self.make({"https://example.com/missing": FakeResponse(404)})
        result = fetcher.fetch("https://example.com/missing", check_robots=False)
        self.assertFalse(result.ok)
        self.assertEqual(result.status, 404)

    def test_connection_error(self):
        fetcher, _ = self.make({})
        result = fetcher.fetch("https://example.com/offline", check_robots=False)
        self.assertFalse(result.ok)
        self.assertIn("request_error", result.error)

    def test_robots_disallow(self):
        robots = FakeResponse(body=b"User-agent: *\nDisallow: /private\n")
        fetcher, session = self.make(
            {
                "https://example.com/robots.txt": robots,
                "https://example.com/private/page": FakeResponse(body=b"secret"),
            }
        )
        result = fetcher.fetch("https://example.com/private/page", check_robots=True)
        self.assertFalse(result.ok)
        self.assertEqual(result.error, "robots_disallowed")
        self.assertNotIn("https://example.com/private/page", [url for url, _ in session.calls])

    def test_robots_allow_and_cache(self):
        robots = FakeResponse(body=b"User-agent: *\nAllow: /\n")
        fetcher, session = self.make(
            {
                "https://example.com/robots.txt": robots,
                "https://example.com/a": FakeResponse(body=b"a"),
                "https://example.com/b": FakeResponse(body=b"b"),
            }
        )
        self.assertTrue(fetcher.fetch("https://example.com/a", check_robots=True).ok)
        self.assertTrue(fetcher.fetch("https://example.com/b", check_robots=True).ok)
        robots_calls = [url for url, _ in session.calls if url.endswith("/robots.txt")]
        self.assertEqual(len(robots_calls), 1)

    def test_robots_unavailable_allows(self):
        fetcher, _ = self.make({"https://example.com/a": FakeResponse(body=b"a")})
        # robots.txt 不在路由中 → ConnectionError → fail-open
        result = fetcher.fetch("https://example.com/a", check_robots=True)
        self.assertTrue(result.ok)


if __name__ == "__main__":
    unittest.main()
