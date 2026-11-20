import json
import tempfile
import unittest
from pathlib import Path

from core.cache import CacheError, FileCache
from core.manifest import RunManifest
from core.paths import project_root


class FakeClock:
    def __init__(self, now: float = 1000.0):
        self.now = now

    def __call__(self) -> float:
        return self.now


class TestFileCache(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.clock = FakeClock()
        self.cache = FileCache(self.tmp.name, default_ttl=60, clock=self.clock)

    def tearDown(self):
        self.tmp.cleanup()

    def test_set_get_json(self):
        self.cache.set_json("key1", {"a": 1})
        self.assertEqual(self.cache.get_json("key1"), {"a": 1})

    def test_expiry(self):
        self.cache.set_json("key1", "value", ttl=10)
        self.clock.now += 11
        self.assertIsNone(self.cache.get_json("key1"))
        self.assertEqual(self.cache.get_json("key1", allow_expired=True), "value")

    def test_fetch_calls_producer_once(self):
        calls = []

        def producer():
            calls.append(1)
            return {"ok": True}

        self.assertEqual(self.cache.fetch("k", producer), {"ok": True})
        self.assertEqual(self.cache.fetch("k", producer), {"ok": True})
        self.assertEqual(len(calls), 1)

    def test_bytes_roundtrip(self):
        self.cache.set_bytes("bin", b"\x00\x01hello")
        self.assertEqual(self.cache.get_bytes("bin"), b"\x00\x01hello")

    def test_oversized_value_rejected(self):
        cache = FileCache(self.tmp.name, max_value_bytes=10, clock=self.clock)
        with self.assertRaises(CacheError):
            cache.set_json("big", "x" * 100)

    def test_purge_and_stats(self):
        self.cache.set_json("keep", 1, ttl=1000)
        self.cache.set_json("drop", 2, ttl=1)
        self.clock.now += 5
        self.assertEqual(self.cache.stats()["entries"], 2)
        self.assertEqual(self.cache.stats()["expired"], 1)
        self.assertEqual(self.cache.purge_expired(), 1)
        self.assertEqual(self.cache.stats()["entries"], 1)

    def test_corrupt_entry_returns_none(self):
        path = self.cache.path_for("bad")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{not json", encoding="utf-8")
        self.assertIsNone(self.cache.get_json("bad"))

    def test_key_cannot_escape_root(self):
        path = self.cache.path_for("../../evil")
        root = Path(self.tmp.name).resolve()
        self.assertTrue(str(path.resolve()).startswith(str(root)))

    def test_delete(self):
        self.cache.set_json("x", 1)
        self.assertTrue(self.cache.delete("x"))
        self.assertFalse(self.cache.delete("x"))


class TestRunManifest(unittest.TestCase):
    def test_stage_records_duration(self):
        manifest = RunManifest("2026-11-21")
        with manifest.stage("collect"):
            pass
        self.assertIn("collect", manifest.stages)
        self.assertGreaterEqual(manifest.stages["collect"], 0)

    def test_stage_records_and_reraises_error(self):
        manifest = RunManifest("2026-11-21")
        with self.assertRaises(RuntimeError):
            with manifest.stage("boom"):
                raise RuntimeError("bad")
        self.assertEqual(len(manifest.errors), 1)
        self.assertEqual(manifest.errors[0]["scope"], "boom")

    def test_errors_and_warnings_are_redacted(self):
        secret = "sk-" + "Z9" * 12
        manifest = RunManifest("2026-11-21")
        manifest.error("x", f"failed {secret}")
        manifest.warning(f"warn {secret}")
        self.assertNotIn(secret, json.dumps(manifest.to_dict(), ensure_ascii=False))

    def test_save_and_load(self):
        manifest = RunManifest("2026-11-21")
        manifest.counts = {"news": 10}
        manifest.source("rss", found=5, kept=3, errors=1)
        manifest.finish("ok")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "m.json"
            manifest.save(path)
            data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["counts"]["news"], 10)
        self.assertEqual(data["sources"]["rss"]["kept"], 3)
        self.assertTrue(data["finished_at"])

    def test_add_file_relative(self):
        manifest = RunManifest("2026-11-21")
        manifest.add_file(project_root() / "README.md")
        self.assertIn("README.md", manifest.files)

    def test_default_path(self):
        manifest = RunManifest("2026-11-21")
        path = manifest.default_path()
        self.assertEqual(path.parent.name, "2026-11-21")
        self.assertTrue(path.name.endswith(".json"))


if __name__ == "__main__":
    unittest.main()
