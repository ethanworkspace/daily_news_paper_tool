"""時效窗工具：日期解析、UTC 正規化、14／30 天過濾。

設計原則：
- 所有比較都用 aware UTC，避免時區造成邊界誤差。
- 沒有時區的日期一律視為 UTC（保守：不會讓過期資料看起來比較新）。
- 視窗為「含頭含尾」：`age <= max_age_days` 才算合格。
- 允許最多 `future_tolerance_days` 的未來時間（來源時區標錯常見），超過視為不合格。
"""
from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
from email.utils import parsedate_to_datetime
from typing import Callable, Iterable, TypeVar

T = TypeVar("T")

_EPOCH_MS_THRESHOLD = 1e11
_FALLBACK_FORMATS = (
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y/%m/%d",
    "%Y.%m.%d",
    "%Y年%m月%d日",
    "%d %b %Y %H:%M:%S",
    "%d %B %Y %H:%M:%S",
    "%b %d, %Y %I:%M%p",
    "%b %d, %Y %I:%M %p",
    "%B %d, %Y %I:%M%p",
    "%b %d, %Y",
    "%B %d, %Y",
)


def parse_datetime(value: object, *, assume_tz: timezone = timezone.utc) -> datetime | None:
    """盡力解析各種來源日期；失敗回傳 None（不丟例外，交給呼叫端記錄）。"""
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=assume_tz)
    if isinstance(value, date):
        return datetime.combine(value, time.min, tzinfo=assume_tz)
    if isinstance(value, (int, float)):
        seconds = float(value)
        if seconds > _EPOCH_MS_THRESHOLD:
            seconds /= 1000.0
        try:
            return datetime.fromtimestamp(seconds, tz=timezone.utc)
        except (OverflowError, OSError, ValueError):
            return None
    if not isinstance(value, str):
        return None

    text = value.strip()
    if not text:
        return None
    if text.isdigit() and len(text) >= 10:
        parsed = parse_datetime(int(text))
        if parsed:
            return parsed

    iso_text = text[:-1] + "+00:00" if text.endswith(("Z", "z")) else text
    try:
        parsed = datetime.fromisoformat(iso_text)
        return parsed if parsed.tzinfo else parsed.replace(tzinfo=assume_tz)
    except ValueError:
        pass

    try:
        parsed = parsedate_to_datetime(text)
        if parsed is not None:
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=assume_tz)
    except (TypeError, ValueError, IndexError):
        pass

    for fmt in _FALLBACK_FORMATS:
        try:
            parsed = datetime.strptime(text, fmt)
            return parsed.replace(tzinfo=assume_tz)
        except ValueError:
            continue
    return None


def to_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def parse_date(value: object) -> date | None:
    parsed = parse_datetime(value)
    return parsed.date() if parsed else None


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def local_today() -> date:
    """日報歸檔日期用「本機日期」（排程與使用者時區一致），非 UTC 日期。"""
    return date.today()


def age_days(published: object, *, now: datetime | None = None) -> float | None:
    parsed = parse_datetime(published)
    if parsed is None:
        return None
    reference = to_utc(now or now_utc())
    return (reference - to_utc(parsed)).total_seconds() / 86400.0


def is_within_window(
    published: object,
    max_age_days: float,
    *,
    now: datetime | None = None,
    future_tolerance_days: float = 1.0,
) -> bool:
    """判斷日期是否落在 `[now-max_age_days, now+future_tolerance_days]`。"""
    age = age_days(published, now=now)
    if age is None:
        return False
    return age <= max_age_days and age >= -future_tolerance_days


def is_future(
    published: object,
    *,
    now: datetime | None = None,
    future_tolerance_days: float = 0.0,
) -> bool:
    """是否晚於報告截止時間。回補模式也必須拒絕未來資料。"""
    age = age_days(published, now=now)
    return age is not None and age < -future_tolerance_days


def is_acceptable_when_stale(
    published: object,
    *,
    now: datetime | None = None,
    future_tolerance_days: float = 0.0,
) -> bool:
    """回補模式：放寬舊資料下限，但仍拒絕未來資料。"""
    return not is_future(
        published, now=now, future_tolerance_days=future_tolerance_days
    )


def split_by_window(
    items: Iterable[T],
    get_published: Callable[[T], object],
    max_age_days: float,
    *,
    now: datetime | None = None,
    future_tolerance_days: float = 1.0,
) -> tuple[list[T], list[T]]:
    """回傳 (合格, 不合格)；日期無法解析者視為不合格。"""
    kept: list[T] = []
    dropped: list[T] = []
    for item in items:
        if is_within_window(
            get_published(item),
            max_age_days,
            now=now,
            future_tolerance_days=future_tolerance_days,
        ):
            kept.append(item)
        else:
            dropped.append(item)
    return kept, dropped


def window_bounds(max_age_days: float, *, now: datetime | None = None) -> tuple[datetime, datetime]:
    reference = to_utc(now or now_utc())
    return reference - timedelta(days=max_age_days), reference


def end_of_day_utc(day: date) -> datetime:
    return datetime.combine(day, time(23, 59, 59), tzinfo=timezone.utc)
