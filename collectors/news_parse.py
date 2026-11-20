"""RSS/Atom 解析與 HTML 清洗。

- 不解析 DTD 內部實體（拒絕 `<!ENTITY`），降低 XXE / entity expansion 風險。
- 以 HTMLParser 移除 script/style 並保留可讀文字（不用正規表達式硬砍）。
- 支援 RSS 2.0 與 Atom；Bing News 的 apiclick 轉址會還原成原始媒體網址。
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from urllib.parse import parse_qs, urlsplit

MAX_ITEMS_PER_FEED = 120
MAX_TEXT_LENGTH = 600

_SKIP_TAGS = {"script", "style", "noscript", "template"}
_BLOCK_TAGS = {
    "p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6",
    "tr", "td", "th", "blockquote", "section", "article",
}
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


class FeedParseError(ValueError):
    """Feed 無法解析。"""


@dataclass
class RawNews:
    title: str
    url: str
    snippet: str = ""
    source: str = ""
    published_raw: str = ""
    language: str = ""
    country: str = ""
    hint: str = ""
    feed: str = ""


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        tag = tag.lower()
        if tag in _SKIP_TAGS:
            self._skip_depth += 1
        elif tag in _BLOCK_TAGS and not self._skip_depth:
            self.parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in _SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
        elif tag in _BLOCK_TAGS and not self._skip_depth:
            self.parts.append(" ")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self.parts.append(data)


def strip_html(raw: object, max_length: int = MAX_TEXT_LENGTH) -> str:
    """把 HTML 轉為純文字，移除 script/style、解碼實體、壓縮空白。"""
    if not raw:
        return ""
    text = str(raw)
    parser = _TextExtractor()
    try:
        parser.feed(text)
        parser.close()
        text = "".join(parser.parts)
    except Exception:  # noqa: BLE001 - 格式異常時退回粗略清理
        text = re.sub(r"<[^>]*>", " ", text)
    text = unescape(text)
    text = _CONTROL_CHARS.sub(" ", text)
    text = " ".join(text.split())
    return text[:max_length]


def unwrap_aggregator_url(url: str) -> str:
    """還原 Bing News apiclick 轉址內的原始網址；其他網址原樣回傳。"""
    if not url:
        return ""
    try:
        parts = urlsplit(url)
    except ValueError:
        return url
    host = (parts.hostname or "").lower()
    if host.endswith("bing.com") and "apiclick" in parts.path:
        target = parse_qs(parts.query).get("url", [""])[0]
        if target.startswith(("http://", "https://")):
            return target
    return url


def _localname(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower() if "}" in tag else tag.lower()


def _text_of(element: ET.Element | None, *, clean: bool = True) -> str:
    if element is None:
        return ""
    try:
        raw = ET.tostring(element, encoding="unicode", method="text")
    except Exception:  # noqa: BLE001
        raw = element.text or ""
    return strip_html(raw) if clean else (raw or "").strip()


def _first_child(element: ET.Element, names: set[str]) -> ET.Element | None:
    for child in list(element):
        if _localname(child.tag) in names:
            return child
    return None


def _child_text(element: ET.Element, names: set[str], *, clean: bool = True) -> str:
    child = _first_child(element, names)
    return _text_of(child, clean=clean) if child is not None else ""


def _atom_link(entry: ET.Element) -> str:
    fallback = ""
    for child in list(entry):
        if _localname(child.tag) != "link":
            continue
        href = child.attrib.get("href", "").strip()
        rel = child.attrib.get("rel", "alternate")
        if href and rel in ("alternate", ""):
            return href
        if href and not fallback:
            fallback = href
    return fallback


def _atom_author(entry: ET.Element) -> str:
    author = _first_child(entry, {"author"})
    if author is None:
        return ""
    return _child_text(author, {"name"})


def _clean_title(title: str, source: str) -> str:
    title = " ".join(title.split())
    if source and title.endswith(f" - {source}"):
        title = title[: -len(f" - {source}")].strip()
    return title


def parse_feed(
    content: bytes,
    *,
    feed_name: str,
    language: str = "",
    country: str = "",
    hint: str = "",
) -> list[RawNews]:
    if not content:
        return []
    head = content[:8192].lower()
    if b"<!entity" in head:
        raise FeedParseError("偵測到 DTD 實體宣告，拒絕解析")

    try:
        root = ET.fromstring(content)
    except ET.ParseError as exc:
        raise FeedParseError(f"XML 解析失敗：{exc}") from exc

    root_name = _localname(root.tag)
    items: list[RawNews] = []

    if root_name == "feed":  # Atom
        entries = [el for el in root.iter() if _localname(el.tag) == "entry"]
        for entry in entries[:MAX_ITEMS_PER_FEED]:
            title = _clean_title(_child_text(entry, {"title"}), "")
            url = unwrap_aggregator_url(_atom_link(entry))
            published = _child_text(entry, {"published", "updated", "created"}, clean=False)
            summary = _child_text(entry, {"summary", "content"})
            author = _atom_author(entry) or feed_name
            if not title or not url:
                continue
            items.append(
                RawNews(
                    title=title, url=url, snippet=summary, source=author,
                    published_raw=published, language=language, country=country,
                    hint=hint, feed=feed_name,
                )
            )
        return items

    # RSS 2.0 / RSS 1.0
    for item in root.iter():
        if _localname(item.tag) != "item":
            continue
        if len(items) >= MAX_ITEMS_PER_FEED:
            break
        title = _clean_title(_child_text(item, {"title"}), "")
        url = unwrap_aggregator_url(_child_text(item, {"link"}, clean=False))
        if not url:
            guid = _child_text(item, {"guid"}, clean=False)
            if guid.startswith(("http://", "https://")):
                url = guid
        source = _child_text(item, {"source"}) or feed_name
        title = _clean_title(title, source)
        published = _child_text(item, {"pubdate", "published", "updated", "date", "created"}, clean=False)
        summary = _child_text(item, {"description", "summary", "content", "encoded", "subtitle"})
        if not title or not url:
            continue
        items.append(
            RawNews(
                title=title, url=url, snippet=summary, source=source,
                published_raw=published, language=language, country=country,
                hint=hint, feed=feed_name,
            )
        )
    return items
