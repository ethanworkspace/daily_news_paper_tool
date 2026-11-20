"""安全 HTTP 抓取：SSRF 防護、重新導向驗證、大小上限、robots.txt。

只用於公開的 http/https 資源；每次重新導向都會重新驗證目標，避免被導向內網。
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from typing import Callable, Iterable
from urllib.parse import urljoin, urlsplit
from urllib.robotparser import RobotFileParser

import requests

from config import NEWS_HTTP_TIMEOUT, NEWS_MAX_BYTES, NEWS_USER_AGENT
from core.security import UnsafeURLError, assert_public_http_url

REDIRECT_STATUSES = {301, 302, 303, 307, 308}
ROBOTS_TTL_SECONDS = 6 * 60 * 60


@dataclass
class FetchResult:
    url: str
    status: int = 0
    content: bytes = b""
    content_type: str = ""
    error: str = ""
    final_url: str = ""
    redirects: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.status == 200 and not self.error


class SafeHttpFetcher:
    def __init__(
        self,
        *,
        session: requests.Session | None = None,
        timeout: int = NEWS_HTTP_TIMEOUT,
        max_bytes: int = NEWS_MAX_BYTES,
        user_agent: str = NEWS_USER_AGENT,
        max_redirects: int = 5,
        clock: Callable[[], float] = time.monotonic,
    ):
        self.session = session or requests.Session()
        self.timeout = timeout
        self.max_bytes = max_bytes
        self.user_agent = user_agent
        self.max_redirects = max_redirects
        self._clock = clock
        self._robots_cache: dict[str, tuple[float, RobotFileParser | None]] = {}
        self._robots_lock = threading.Lock()

    # ---------- robots ----------
    def _robots_parser(self, url: str) -> RobotFileParser | None:
        parts = urlsplit(url)
        origin = f"{parts.scheme}://{parts.netloc}"
        now = self._clock()
        with self._robots_lock:
            cached = self._robots_cache.get(origin)
            if cached and cached[0] > now:
                return cached[1]

        robots_url = f"{origin}/robots.txt"
        result = self.fetch(robots_url, check_robots=False, _skip_robots=True)
        parser: RobotFileParser | None = None
        # robots.txt 不存在或不可讀時採 fail-open（業界慣例），但仍記錄錯誤。
        if result.ok and result.content:
            try:
                parser = RobotFileParser()
                parser.parse(result.content.decode("utf-8", errors="replace").splitlines())
            except Exception:  # noqa: BLE001 - robots 格式異常不應阻斷抓取
                parser = None

        with self._robots_lock:
            self._robots_cache[origin] = (now + ROBOTS_TTL_SECONDS, parser)
        return parser

    def _robots_allowed(self, url: str) -> bool:
        parser = self._robots_parser(url)
        if parser is None:
            return True
        parts = urlsplit(url)
        path = parts.path or "/"
        if parts.query:
            path = f"{path}?{parts.query}"
        return parser.can_fetch(self.user_agent, path)

    # ---------- 抓取 ----------
    def fetch(
        self,
        url: str,
        *,
        check_robots: bool | None = None,
        _skip_robots: bool = False,
        headers: dict[str, str] | None = None,
    ) -> FetchResult:
        try:
            current = assert_public_http_url(url)
        except UnsafeURLError as exc:
            return FetchResult(url=url, error=f"unsafe_url: {exc}")

        if check_robots and not _skip_robots:
            try:
                if not self._robots_allowed(current):
                    return FetchResult(url=current, status=403, error="robots_disallowed", final_url=current)
            except Exception as exc:  # noqa: BLE001 - robots 檢查失敗採 fail-open
                return FetchResult(url=current, error=f"robots_error: {type(exc).__name__}")

        redirects: list[str] = []
        request_headers = {
            "User-Agent": self.user_agent,
            "Accept": "application/json, application/atom+xml, application/rss+xml, application/xml, text/html, text/plain, */*",
        }
        if headers:
            request_headers.update(headers)

        for _ in range(self.max_redirects + 1):
            try:
                response = self.session.get(
                    current,
                    headers=request_headers,
                    timeout=self.timeout,
                    allow_redirects=False,
                    stream=True,
                )
            except requests.RequestException as exc:
                return FetchResult(
                    url=url, error=f"request_error: {type(exc).__name__}",
                    final_url=current, redirects=redirects,
                )
            except Exception as exc:  # noqa: BLE001
                return FetchResult(
                    url=url, error=f"unexpected_error: {type(exc).__name__}",
                    final_url=current, redirects=redirects,
                )

            status = getattr(response, "status_code", 0)
            if status in REDIRECT_STATUSES:
                location = (getattr(response, "headers", {}) or {}).get("Location", "")
                self._close(response)
                if not location:
                    return FetchResult(
                        url=url, status=status, error="redirect_without_location",
                        final_url=current, redirects=redirects,
                    )
                target = urljoin(current, location)
                try:
                    target = assert_public_http_url(target)
                except UnsafeURLError as exc:
                    return FetchResult(
                        url=url, status=status, error=f"unsafe_redirect: {exc}",
                        final_url=target, redirects=redirects,
                    )
                redirects.append(target)
                current = target
                continue

            if status != 200:
                self._close(response)
                return FetchResult(
                    url=url, status=status, error=f"http_{status}",
                    final_url=current, redirects=redirects,
                )

            content_type = (getattr(response, "headers", {}) or {}).get("Content-Type", "") or ""
            chunks: list[bytes] = []
            total = 0
            try:
                for chunk in self._iter_content(response):
                    if not chunk:
                        continue
                    total += len(chunk)
                    if total > self.max_bytes:
                        return FetchResult(
                            url=url, status=status, error="too_large",
                            content_type=content_type, final_url=current, redirects=redirects,
                        )
                    chunks.append(chunk)
            except Exception as exc:  # noqa: BLE001
                return FetchResult(
                    url=url, status=status, error=f"read_error: {type(exc).__name__}",
                    content_type=content_type, final_url=current, redirects=redirects,
                )
            finally:
                self._close(response)

            return FetchResult(
                url=url, status=status, content=b"".join(chunks),
                content_type=content_type, final_url=current, redirects=redirects,
            )

        return FetchResult(
            url=url, status=0, error="too_many_redirects",
            final_url=current, redirects=redirects,
        )

    @staticmethod
    def _iter_content(response: requests.Response) -> Iterable[bytes]:
        iterator = getattr(response, "iter_content", None)
        if callable(iterator):
            return iterator(64 * 1024)
        return [getattr(response, "content", b"")]

    @staticmethod
    def _close(response: requests.Response) -> None:
        close = getattr(response, "close", None)
        if callable(close):
            try:
                close()
            except Exception:  # noqa: BLE001
                pass
