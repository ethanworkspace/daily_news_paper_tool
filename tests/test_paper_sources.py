import unittest
from unittest.mock import patch

from collectors.news_http import FetchResult
from collectors.paper_sources import PaperSources


class SequenceFetcher:
    def __init__(self, results):
        self.results = list(results)
        self.calls = 0

    def fetch(self, url, *, check_robots=None, _skip_robots=False, headers=None):
        self.calls += 1
        if self.results:
            return self.results.pop(0)
        return FetchResult(url=url, status=200, content=b"{}")


class TestPaperSourceRetry(unittest.TestCase):
    def test_retries_brief_429_then_succeeds(self):
        fetcher = SequenceFetcher([
            FetchResult(url="https://api.example.test", status=429, error="http_429"),
            FetchResult(url="https://api.example.test", status=200, content=b"{}"),
        ])
        sources = PaperSources(fetcher=fetcher, robots_check=False)

        with patch("collectors.paper_sources.time.sleep") as sleep:
            result = sources._fetch_retry("https://api.example.test/search")

        self.assertTrue(result.ok)
        self.assertEqual(fetcher.calls, 2)
        sleep.assert_called_once()

    def test_persistent_429_cools_down_host(self):
        fetcher = SequenceFetcher([
            FetchResult(url="https://api.example.test", status=429, error="http_429"),
            FetchResult(url="https://api.example.test", status=429, error="http_429"),
            FetchResult(url="https://api.example.test", status=429, error="http_429"),
            FetchResult(url="https://api.example.test", status=200, content=b"{}"),
        ])
        sources = PaperSources(fetcher=fetcher, robots_check=False)

        with patch("collectors.paper_sources.time.sleep"):
            first = sources._fetch_retry("https://api.example.test/search")
            second = sources._fetch_retry("https://api.example.test/other")

        self.assertEqual(first.status, 429)
        self.assertEqual(second.status, 429)
        self.assertEqual(second.error, "rate_limit_cooldown")
        self.assertEqual(fetcher.calls, 3)


if __name__ == "__main__":
    unittest.main()
