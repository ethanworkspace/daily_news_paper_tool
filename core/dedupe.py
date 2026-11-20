"""去重工具：URL、標題、DOI、arXiv ID、GitHub repo。

- URL：去除追蹤參數（utm_*、fbclid…）、排序 query、統一大小寫與結尾斜線。
- 標題：NFKC + casefold + 只保留英數與中日韓字元，降低標點與空白差異。
- DOI／arXiv：正規化版本號與前綴，避免同一篇論文重複收錄。
"""
from __future__ import annotations

import re
import unicodedata
from difflib import SequenceMatcher
from typing import Callable, Iterable, TypeVar
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

T = TypeVar("T")

TRACKING_PARAMS = {
    "fbclid", "gclid", "dclid", "msclkid", "yclid", "igshid",
    "mc_cid", "mc_eid", "ref", "ref_src", "ref_url", "source", "spm",
    "cmpid", "campaign", "at_medium", "at_campaign",
}

_DOI_PREFIXES = ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:")
_ARXIV_PATTERNS = (
    re.compile(r"(?:arxiv:|abs/|pdf/)(\d{4}\.\d{4,5})", re.IGNORECASE),
    re.compile(r"(?:arxiv:|abs/|pdf/)([a-z\-]+/\d{7})", re.IGNORECASE),
    re.compile(r"\b(\d{4}\.\d{4,5})(?:v\d+)?\b"),
    re.compile(r"\b([a-z][a-z\-]*/\d{7})(?:v\d+)?\b", re.IGNORECASE),
)
_ARXIV_VERSION = re.compile(r"v\d+$", re.IGNORECASE)


def normalize_url(url: object) -> str:
    if not url or not isinstance(url, str):
        return ""
    candidate = url.strip()
    if not candidate:
        return ""
    parts = urlsplit(candidate)
    if not parts.scheme or not parts.netloc:
        return candidate

    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    port = parts.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"

    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/")

    query_pairs = [
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_PARAMS and not k.lower().startswith("utm_")
    ]
    query = urlencode(sorted(query_pairs))

    return urlunsplit((scheme, host, path, query, ""))


def title_fingerprint(title: object) -> str:
    if not title or not isinstance(title, str):
        return ""
    text = unicodedata.normalize("NFKC", title).casefold()
    return "".join(ch for ch in text if ch.isalnum())


def is_similar_title(left: object, right: object, threshold: float = 0.92) -> bool:
    a = title_fingerprint(left)
    b = title_fingerprint(right)
    if not a or not b:
        return False
    if a == b:
        return True
    shorter, longer = sorted((a, b), key=len)
    if len(shorter) >= 12 and shorter in longer:
        return True
    return SequenceMatcher(None, a, b).ratio() >= threshold


def normalize_doi(value: object) -> str:
    if not value or not isinstance(value, str):
        return ""
    text = value.strip().lower()
    for prefix in _DOI_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):]
    text = text.strip().strip(".,;)")
    return text if text.startswith("10.") else ""


def extract_arxiv_id(value: object) -> str:
    if not value or not isinstance(value, str):
        return ""
    text = value.strip()
    for pattern in _ARXIV_PATTERNS:
        match = pattern.search(text)
        if match:
            return normalize_arxiv_id(match.group(1))
    return ""


def normalize_arxiv_id(value: object) -> str:
    if not value or not isinstance(value, str):
        return ""
    text = value.strip().lower()
    for prefix in ("arxiv:", "abs/", "pdf/"):
        if text.startswith(prefix):
            text = text[len(prefix):]
    text = _ARXIV_VERSION.sub("", text)
    return text.strip()


def make_keys(
    *,
    url: object = "",
    title: object = "",
    doi: object = "",
    arxiv_id: object = "",
    repo: object = "",
) -> list[str]:
    keys: list[str] = []
    normalized_url = normalize_url(url)
    if normalized_url:
        keys.append(f"url:{normalized_url}")
    fingerprint = title_fingerprint(title)
    if fingerprint:
        keys.append(f"title:{fingerprint}")
    normalized_doi = normalize_doi(doi) or normalize_doi(url)
    if normalized_doi:
        keys.append(f"doi:{normalized_doi}")
    normalized_arxiv = normalize_arxiv_id(arxiv_id) or extract_arxiv_id(url)
    if normalized_arxiv:
        keys.append(f"arxiv:{normalized_arxiv}")
    if repo:
        keys.append(f"repo:{str(repo).strip().lower()}")
    return keys


class Deduper:
    """記住已出現的鍵；`add` 回傳 True 表示這是新項目。"""

    def __init__(self) -> None:
        self._seen: set[str] = set()

    def __len__(self) -> int:
        return len(self._seen)

    def seen(self, *keys: object) -> bool:
        return any(str(k) in self._seen for k in keys if k)

    def add(self, *keys: object) -> bool:
        cleaned = [str(k) for k in keys if k]
        is_new = not any(k in self._seen for k in cleaned)
        self._seen.update(cleaned)
        return is_new


def dedupe_items(items: Iterable[T], key_func: Callable[[T], Iterable[str]]) -> list[T]:
    deduper = Deduper()
    result: list[T] = []
    for item in items:
        if deduper.add(*key_func(item)):
            result.append(item)
    return result
