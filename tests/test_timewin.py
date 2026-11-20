import unittest
from datetime import date, datetime, timedelta, timezone

from core.timewin import (
    age_days,
    end_of_day_utc,
    is_within_window,
    local_today,
    parse_date,
    parse_datetime,
    split_by_window,
    to_utc,
    window_bounds,
)

NOW = datetime(2026, 11, 21, 0, 0, 0, tzinfo=timezone.utc)


class TestParseDatetime(unittest.TestCase):
    def test_iso_with_z(self):
        parsed = parse_datetime("2026-11-20T12:30:00Z")
        self.assertEqual(parsed, datetime(2026, 11, 20, 12, 30, tzinfo=timezone.utc))

    def test_iso_with_offset(self):
        parsed = parse_datetime("2026-11-20T20:30:00+08:00")
        self.assertEqual(parsed.astimezone(timezone.utc).hour, 12)

    def test_rfc2822(self):
        parsed = parse_datetime("Fri, 20 Nov 2026 12:00:00 +0800")
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed.astimezone(timezone.utc).hour, 4)

    def test_epoch_seconds_and_milliseconds(self):
        seconds = 1795000000
        self.assertEqual(parse_datetime(seconds), parse_datetime(seconds * 1000))

    def test_common_formats(self):
        self.assertEqual(parse_date("2026/11/20"), date(2026, 11, 20))
        self.assertEqual(parse_date("2026年11月20日"), date(2026, 11, 20))
        self.assertEqual(parse_date("Nov 19, 2026 2:47pm"), date(2026, 11, 19))
        self.assertEqual(parse_date("November 19, 2026 2:47 PM"), date(2026, 11, 19))

    def test_date_object_becomes_midnight_utc(self):
        self.assertEqual(
            parse_datetime(date(2026, 11, 20)),
            datetime(2026, 11, 20, tzinfo=timezone.utc),
        )

    def test_naive_assumed_utc(self):
        self.assertEqual(parse_datetime("2026-11-20 08:00:00").tzinfo, timezone.utc)

    def test_invalid_returns_none(self):
        for value in (None, "", "not a date", object(), True, []):
            self.assertIsNone(parse_datetime(value))


class TestAgeAndWindow(unittest.TestCase):
    def test_age_days(self):
        self.assertAlmostEqual(age_days("2026-11-20T00:00:00Z", now=NOW), 1.0)

    def test_age_handles_naive_now(self):
        naive_now = NOW.replace(tzinfo=None)
        self.assertAlmostEqual(age_days("2026-11-20T00:00:00Z", now=naive_now), 1.0)

    def test_window_is_inclusive(self):
        exactly_14 = NOW - timedelta(days=14)
        self.assertTrue(is_within_window(exactly_14, 14, now=NOW))
        just_over = NOW - timedelta(days=14, seconds=1)
        self.assertFalse(is_within_window(just_over, 14, now=NOW))

    def test_future_tolerance(self):
        self.assertTrue(is_within_window(NOW + timedelta(hours=12), 14, now=NOW))
        self.assertFalse(is_within_window(NOW + timedelta(days=2), 14, now=NOW))

    def test_unparseable_is_not_fresh(self):
        self.assertFalse(is_within_window("garbage", 14, now=NOW))

    def test_split_by_window(self):
        items = [
            {"d": NOW - timedelta(days=1)},
            {"d": NOW - timedelta(days=20)},
            {"d": "bad"},
        ]
        kept, dropped = split_by_window(items, lambda x: x["d"], 14, now=NOW)
        self.assertEqual(len(kept), 1)
        self.assertEqual(len(dropped), 2)

    def test_window_bounds(self):
        start, end = window_bounds(14, now=NOW)
        self.assertEqual(end, NOW)
        self.assertEqual(start, NOW - timedelta(days=14))

    def test_end_of_day_utc(self):
        self.assertEqual(end_of_day_utc(date(2026, 11, 21)).hour, 23)

    def test_local_today_matches_system_date(self):
        self.assertEqual(local_today(), date.today())

    def test_to_utc_naive(self):
        self.assertEqual(to_utc(datetime(2026, 1, 1)).tzinfo, timezone.utc)


if __name__ == "__main__":
    unittest.main()
