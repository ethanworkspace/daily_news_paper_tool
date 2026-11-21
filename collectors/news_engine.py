"""新聞蒐集引擎：多來源 → 清洗 → 時效/主題過濾 → 去重 → 領域標註 → 配額選文。

來源：
- Bing News RSS（查詢式聚合，遵守 robots.txt；可關閉）
- 直接媒體 RSS（來源清單在 config.NEWS_FEEDS，可插拔）

輸出：`NewsSelection`（含 10 篇 NewsItem、統計報告、被排除原因）。
配額不足時丟 `NewsQuotaError`，由呼叫端決定擴查或中止。
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Iterable
from urllib.parse import quote_plus

from config import (
    NEWS_BING_ENABLED,
    NEWS_FEEDS,
    NEWS_MAX_AGE_DAYS,
    NEWS_MAX_PER_DOMAIN,
    NEWS_MAX_PER_SOURCE,
    NEWS_QUERIES,
    NEWS_ROBOTS_CHECK,
)
from core.dedupe import Deduper, is_similar_title, make_keys
from core.models import CROSS_DOMAIN, DOMAINS, NewsItem, SchemaError
from core.timewin import is_within_window, now_utc, parse_datetime, to_utc
from collectors.news_http import FetchResult, SafeHttpFetcher
from collectors.news_parse import RawNews, parse_feed, strip_html

BING_NEWS_ENDPOINT = "https://www.bing.com/news/search"

AI_TERMS = (
    "artificial intelligence", "machine learning", "deep learning", "neural network",
    "large language model", "language model", "generative ai", "genai", "foundation model",
    "transformer", "computer vision", "reinforcement learning", "ai agent", "agentic",
    "gpt", "llm", "chatbot", "diffusion model", "fine-tuning", "fine tuning", "inference",
    "人工智慧", "人工智能", "機器學習", "深度學習", "神經網路", "神經網絡",
    "大語言模型", "大型語言模型", "生成式", "生成式ai",
)
_AI_SHORT_TERMS = ("ai", "ml", "dl", "nn")

DOMAIN_KEYWORDS: dict[str, tuple[str, ...]] = {
    "maritime": (
        "maritime", "vessel", "cargo ship", "container ship", "tanker",
        "port", "harbor", "harbour", "seaport", "seafarer", "shipowner", "shipyard",
        "ship management", "ship manager", "ocean shipping", "ocean freight",
        "shipping industry", "shipping company", "shipping line", "shipping sector",
        "shipping market", "container shipping", "maritime shipping",
        "offshore", "naval", "subsea", "shipbuilding", "ferry",
        "marine technology", "marine industry", "marine engineering", "marine safety",
        "maritime security", "maritime safety", "autonomous ship",
        "海事", "航運", "海運", "船舶", "港口", "海洋", "離岸", "漁業", "海巡",
        "貨櫃", "船隊", "造船", "水下", "藍色經濟", "碼頭", "船員", "海運業",
    ),
    "cybersecurity": (
        "cybersecurity", "cyber security", "malware", "ransomware", "phishing",
        "vulnerability", "zero-day", "breach", "hacker", "cyberattack", "cyber attack",
        "intrusion", "threat intelligence", "ddos",
        "資安", "網路安全", "資訊安全", "勒索", "漏洞", "駭客", "釣魚",
        "惡意程式", "入侵", "零日", "威脅情報",
    ),
    "medical": (
        "medical", "healthcare", "health tech", "clinical", "hospital", "diagnosis",
        "patient", "radiology", "genomics", "drug discovery", "fda", "biomedical",
        "醫療", "醫學", "臨床", "醫院", "診斷", "病患", "藥物", "生醫",
        "健康", "影像判讀", "精準醫療",
    ),
    "electronics": (
        "chip", "semiconductor", "gpu", "npu", "tpu", "wafer", "foundry",
        "transistor", "edge computing", "fpga", "asic", "memory chip",
        "晶片", "半導體", "電子", "硬體", "晶圓", "邊緣運算", "記憶體", "封裝",
    ),
    "robotics": (
        "robot", "robotics", "humanoid", "embodied", "drone", "uav",
        "autonomous vehicle", "manipulator", "self-driving", "ros",
        "機器人", "具身", "無人機", "自駕", "機械手臂", "人形", "自主移動",
    ),
}

_ASCII_TERM_CACHE: dict[str, re.Pattern[str]] = {}


class NewsQuotaError(RuntimeError):
    def __init__(self, message: str, report: dict):
        super().__init__(message)
        self.report = report


@dataclass
class NewsSelection:
    items: list[NewsItem]
    report: dict = field(default_factory=dict)
    rejected: list[dict] = field(default_factory=list)


def _term_regex(term: str) -> re.Pattern[str]:
    cached = _ASCII_TERM_CACHE.get(term)
    if cached:
        return cached
    if re.fullmatch(r"[a-z0-9 .\-]+", term):
        pattern = re.compile(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", re.IGNORECASE)
    else:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
    _ASCII_TERM_CACHE[term] = pattern
    return pattern


def _contains(text: str, term: str) -> bool:
    return bool(_term_regex(term).search(text))


def is_ai_related(text: str) -> bool:
    if not text:
        return False
    lowered = text.lower()
    if any(_contains(lowered, term) for term in AI_TERMS):
        return True
    return any(_contains(lowered, term) for term in _AI_SHORT_TERMS)


def detect_domains(text: str) -> list[str]:
    if not text:
        return []
    lowered = text.lower()
    matched = [domain for domain, terms in DOMAIN_KEYWORDS.items() if any(_contains(lowered, t) for t in terms)]
    return matched


def detect_ai_focus(text: str) -> str:
    lowered = (text or "").lower()
    focus = [
        ("llm", ("llm", "large language model", "gpt", "大語言模型", "大型語言模型")),
        ("model", ("foundation model", "model release", "模型")),
        ("agent", ("agent", "代理")),
        ("ml", ("machine learning", "機器學習")),
        ("dl", ("deep learning", "neural network", "深度學習", "神經網路")),
    ]
    for name, terms in focus:
        if any(_contains(lowered, term) for term in terms):
            return name
    return "general"


def build_bing_news_url(query: dict) -> str:
    params = [
        f"q={quote_plus(str(query.get('query', '')))}",
        "format=RSS",
    ]
    if query.get("lang"):
        params.append(f"setlang={quote_plus(str(query['lang']))}")
    if query.get("cc"):
        params.append(f"cc={quote_plus(str(query['cc']))}")
    return f"{BING_NEWS_ENDPOINT}?{'&'.join(params)}"


def _is_cross_domain(item: NewsItem) -> bool:
    return any(domain in CROSS_DOMAIN for domain in item.domains)


def _is_maritime(item: NewsItem) -> bool:
    return item.is_maritime or "maritime" in item.domains


def _published_key(item: NewsItem) -> datetime:
    return item.published_at or datetime.min.replace(tzinfo=timezone.utc)


def select_news(
    items: Iterable[NewsItem],
    count: int,
    *,
    max_per_source: int = NEWS_MAX_PER_SOURCE,
    max_per_domain: int = NEWS_MAX_PER_DOMAIN,
    min_cross: int = 3,
    min_maritime: int = 1,
) -> NewsSelection:
    """依「海事優先 → 跨域達標 → 最新補滿」選文，盡量分散來源與領域。"""
    ordered = sorted(items, key=_published_key, reverse=True)
    selected: list[NewsItem] = []
    remaining = list(ordered)
    per_source: Counter[str] = Counter()
    per_domain: Counter[str] = Counter()
    relaxed = False

    def eligible(item: NewsItem) -> bool:
        source_ok = max_per_source <= 0 or per_source[item.source] < max_per_source
        domain_ok = max_per_domain <= 0 or any(
            per_domain[domain] < max_per_domain for domain in item.domains
        )
        return source_ok and domain_ok

    def register(item: NewsItem) -> None:
        per_source[item.source] += 1
        for domain in item.domains:
            per_domain[domain] += 1

    def take(predicate) -> bool:  # noqa: ANN001
        nonlocal relaxed
        for index, item in enumerate(remaining):
            if predicate(item) and eligible(item):
                remaining.pop(index)
                selected.append(item)
                register(item)
                return True
        for index, item in enumerate(remaining):
            if predicate(item):
                remaining.pop(index)
                selected.append(item)
                register(item)
                relaxed = True
                return True
        return False

    while len(selected) < count:
        maritime = sum(1 for item in selected if _is_maritime(item))
        cross = sum(1 for item in selected if _is_cross_domain(item))
        if maritime < min_maritime and take(_is_maritime):
            continue
        if cross < min_cross and take(_is_cross_domain):
            continue
        if take(lambda _item: True):
            continue
        break

    maritime = sum(1 for item in selected if _is_maritime(item))
    cross = sum(1 for item in selected if _is_cross_domain(item))
    domain_counts = Counter(domain for item in selected for domain in item.domains)
    report = {
        "pool_size": len(ordered),
        "selected": len(selected),
        "target": count,
        "cross_domain": cross,
        "maritime": maritime,
        "cross_domain_ok": cross >= min_cross,
        "maritime_ok": maritime >= min_maritime,
        "per_source": dict(per_source),
        "domain_counts": dict(domain_counts),
        "relaxed_source_cap": relaxed,
        "relaxed_caps": relaxed,
    }
    if len(selected) < count:
        raise NewsQuotaError(f"新聞數量不足：{len(selected)}/{count}", report)
    if maritime < min_maritime:
        raise NewsQuotaError(f"海事新聞不足：{maritime}/{min_maritime}", report)
    if cross < min_cross:
        raise NewsQuotaError(f"跨域新聞不足：{cross}/{min_cross}", report)
    return NewsSelection(items=selected, report=report)


class NewsEngine:
    def __init__(
        self,
        *,
        fetcher: SafeHttpFetcher | None = None,
        queries: list[dict] | None = None,
        feeds: list[dict] | None = None,
        max_per_source: int = NEWS_MAX_PER_SOURCE,
        max_per_domain: int = NEWS_MAX_PER_DOMAIN,
        max_age_days: int = NEWS_MAX_AGE_DAYS,
        robots_check: bool = NEWS_ROBOTS_CHECK,
        bing_enabled: bool = NEWS_BING_ENABLED,
        min_cross: int = 3,
        min_maritime: int = 1,
        allow_stale: bool = False,
    ):
        self.fetcher = fetcher or SafeHttpFetcher()
        self.queries = NEWS_QUERIES if queries is None else queries
        self.feeds = NEWS_FEEDS if feeds is None else feeds
        self.max_per_source = max_per_source
        self.max_per_domain = max_per_domain
        self.max_age_days = max_age_days
        self.robots_check = robots_check
        self.bing_enabled = bing_enabled
        self.min_cross = min_cross
        self.min_maritime = min_maritime
        self.allow_stale = allow_stale

    # ---------- 對外 ----------
    def collect(self, count: int = 10, *, now: datetime | None = None) -> NewsSelection:
        reference = now or now_utc()
        raw_items: list[RawNews] = []
        sources: dict[str, dict[str, int]] = {}

        if self.queries and self.bing_enabled:
            for query in self.queries:
                name = f"bing:{query.get('hint', 'general')}:{query.get('query', '')[:40]}"
                url = build_bing_news_url(query)
                raw_items.extend(self._fetch_feed(name, url, query, sources))

        for feed in self.feeds:
            name = f"rss:{feed.get('name', feed.get('url', ''))}"
            raw_items.extend(self._fetch_feed(name, feed.get("url", ""), feed, sources))

        items, rejected = self._filter(raw_items, reference)
        try:
            selection = select_news(
                items, count, max_per_source=self.max_per_source,
                max_per_domain=self.max_per_domain,
                min_cross=self.min_cross, min_maritime=self.min_maritime,
            )
        except NewsQuotaError as exc:
            exc.report.setdefault("sources", sources)
            exc.report.setdefault("raw_count", len(raw_items))
            exc.report.setdefault("unique_items", len(items))
            exc.report.setdefault("rejected_counts", dict(Counter(r["reason"] for r in rejected)))
            raise
        selection.rejected = rejected
        selection.report["sources"] = sources
        selection.report["raw_count"] = len(raw_items)
        selection.report["unique_items"] = len(items)
        selection.report["rejected_counts"] = dict(Counter(r["reason"] for r in rejected))
        return selection

    # ---------- 內部 ----------
    def _fetch_feed(self, name: str, url: str, source_cfg: dict, stats: dict) -> list[RawNews]:
        entry = stats.setdefault(name, {"found": 0, "errors": 0, "fetched": 0})
        if not url:
            entry["errors"] += 1
            return []
        result: FetchResult = self.fetcher.fetch(url, check_robots=self.robots_check)
        if not result.ok:
            entry["errors"] += 1
            entry["error"] = result.error or f"http_{result.status}"
            return []
        entry["fetched"] += 1
        try:
            parsed = parse_feed(
                result.content,
                feed_name=source_cfg.get("name", name),
                language=source_cfg.get("lang", ""),
                country=source_cfg.get("cc", source_cfg.get("country", "")),
                hint=source_cfg.get("hint", "general"),
            )
        except Exception as exc:  # noqa: BLE001 - 單一來源失敗不影響整體
            entry["errors"] += 1
            entry["error"] = f"parse_error: {type(exc).__name__}"
            return []
        entry["found"] += len(parsed)
        return parsed

    def _filter(self, raw_items: list[RawNews], reference: datetime) -> tuple[list[NewsItem], list[dict]]:
        deduper = Deduper()
        kept: list[NewsItem] = []
        rejected: list[dict] = []

        for raw in raw_items:
            reason = ""
            published = parse_datetime(raw.published_raw)
            if published is None:
                rejected.append({"title": raw.title[:160], "reason": "no_date", "source": raw.source})
                continue
            published = to_utc(published)
            if not self.allow_stale and not is_within_window(published, self.max_age_days, now=reference):
                rejected.append({"title": raw.title[:160], "reason": "stale", "source": raw.source})
                continue

            text = f"{raw.title} {raw.snippet}".strip()
            if not is_ai_related(text):
                rejected.append({"title": raw.title[:160], "reason": "not_ai", "source": raw.source})
                continue

            domains = detect_domains(text)
            if not domains:
                hint = raw.hint if raw.hint in DOMAINS else "general"
                domains = [hint]

            item = NewsItem(
                title=raw.title,
                url=raw.url,
                source=raw.source or raw.feed,
                published_at=published,
                language=raw.language,
                country=raw.country,
                ai_focus=detect_ai_focus(text),
                domains=domains,
                is_maritime="maritime" in domains,
                summary=strip_html(raw.snippet or raw.title, max_length=600),
                key_point="",
            )
            try:
                item.validate()
            except SchemaError as exc:
                rejected.append({"title": raw.title[:160], "reason": f"invalid: {exc}", "source": raw.source})
                continue

            keys = make_keys(url=raw.url, title=raw.title)
            if not deduper.add(*keys):
                rejected.append({"title": raw.title[:160], "reason": "duplicate", "source": raw.source})
                continue
            if any(is_similar_title(item.title, other.title) for other in kept):
                rejected.append({"title": raw.title[:160], "reason": "similar_title", "source": raw.source})
                continue

            kept.append(item)

        return kept, rejected


def collect_daily_news(count: int = 10, *, now: datetime | None = None) -> NewsSelection:
    """便利函式：使用 config 預設來源蒐集當日新聞。"""
    return NewsEngine().collect(count, now=now)
