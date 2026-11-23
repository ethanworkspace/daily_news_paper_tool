import base64
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import iai_client as ic
from config import parse_api_keys


class FakeResponse:
    def __init__(self, status=200, data=None, text="", headers=None, content=b""):
        self.status_code = status
        self._data = data if data is not None else {}
        self.text = text
        self.headers = headers or {}
        self.content = content

    def json(self):
        return self._data


class FakeSession:
    def __init__(self, request_responses=None, get_responses=None):
        self.request_responses = list(request_responses or [])
        self.get_responses = list(get_responses or [])
        self.requests = []
        self.gets = []

    def request(self, method, url, **kwargs):
        self.requests.append((method, url, kwargs))
        if not self.request_responses:
            raise AssertionError("沒有預設的 request 回應")
        return self.request_responses.pop(0)

    def get(self, url, **kwargs):
        self.gets.append((url, kwargs))
        if not self.get_responses:
            raise AssertionError("沒有預設的 get 回應")
        return self.get_responses.pop(0)


def chat_payload(text):
    return {"choices": [{"message": {"content": text}}], "usage": {"prompt_tokens": 3, "completion_tokens": 5}}


class TestMasking(unittest.TestCase):
    def test_mask_key(self):
        self.assertEqual(ic.mask_key("sk-test-1234mnop"), "sk-****mnop")
        self.assertEqual(ic.mask_key("short"), "****")
        self.assertEqual(ic.mask_key(""), "(未設定)")

    def test_redact(self):
        fake_key = "sk-" + "A" * 16
        text = f"token {fake_key} leaked"
        self.assertNotIn(fake_key, ic.redact(text))
        self.assertIn("sk-****", ic.redact(text))


class TestExtractJson(unittest.TestCase):
    def test_plain_json(self):
        self.assertEqual(ic.extract_json('{"a": 1}'), {"a": 1})

    def test_fenced_json(self):
        self.assertEqual(ic.extract_json('說明\n```json\n{"a": 2}\n```\n結尾'), {"a": 2})

    def test_json_inside_prose(self):
        self.assertEqual(ic.extract_json('結果如下：{"a": {"b": [1, 2]}} 完畢'), {"a": {"b": [1, 2]}})

    def test_invalid_raises(self):
        with self.assertRaises(ValueError):
            ic.extract_json("完全沒有 JSON")


class TestKeyPool(unittest.TestCase):
    def test_rotation(self):
        pool = ic.KeyPool(["k1", "k2", "k3"])
        self.assertEqual([pool.next_key() for _ in range(4)], ["k1", "k2", "k3", "k1"])

    def test_cooldown_skips_key(self):
        pool = ic.KeyPool(["k1", "k2"])
        pool.cooldown("k1", 60)
        self.assertEqual(pool.next_key(), "k2")
        self.assertEqual(pool.next_key(), "k2")

    def test_all_cooling_returns_none(self):
        pool = ic.KeyPool(["k1"])
        pool.cooldown("k1", 60)
        self.assertIsNone(pool.next_key())
        self.assertGreater(pool.earliest_wait(), 0)

    def test_masked(self):
        pool = ic.KeyPool(["sk-aaaaaaaaaaaa"])
        self.assertEqual(pool.masked(), ["sk-****aaaa"])


class TestClientChat(unittest.TestCase):
    def make_client(self, session, keys=("sk-aaaaaaaaaaaa",)):
        return ic.IAIClient(
            keys=keys,
            session=session,
            sleep_fn=lambda _s: None,
            max_retries=2,
            max_concurrency=2,
            per_key_concurrency=1,
        )

    def test_chat_success(self):
        session = FakeSession([FakeResponse(200, chat_payload("Hello"))])
        client = self.make_client(session)
        self.assertEqual(client.chat("hi", model="Furen-max"), "Hello")

    def test_chat_retries_on_429(self):
        session = FakeSession([
            FakeResponse(429, {}, headers={"Retry-After": "0"}),
            FakeResponse(200, chat_payload("OK")),
        ])
        client = self.make_client(session, keys=("sk-aaaaaaaaaaaa", "sk-bbbbbbbbbbbb"))
        self.assertEqual(client.chat("hi"), "OK")
        self.assertEqual(len(session.requests), 2)

    def test_chat_authorization_header_uses_key(self):
        session = FakeSession([FakeResponse(200, chat_payload("OK"))])
        client = self.make_client(session)
        client.chat("hi")
        _, _, kwargs = session.requests[0]
        self.assertTrue(kwargs["headers"]["Authorization"].startswith("Bearer sk-"))

    def test_chat_raises_without_keys(self):
        client = ic.IAIClient(keys=[], session=FakeSession([]))
        with self.assertRaises(ic.IAIClientError):
            client.chat("hi")

    def test_chat_json_repairs(self):
        session = FakeSession([
            FakeResponse(200, chat_payload("這不是 JSON")),
            FakeResponse(200, chat_payload('{"ok": true}')),
        ])
        client = self.make_client(session)
        self.assertEqual(client.chat_json("給我一組 JSON"), {"ok": True})
        self.assertEqual(len(session.requests), 2)

    def test_chat_json_raises_after_repairs(self):
        session = FakeSession([
            FakeResponse(200, chat_payload("壞")),
            FakeResponse(200, chat_payload("還是壞")),
            FakeResponse(200, chat_payload("仍壞")),
        ])
        client = self.make_client(session)
        with self.assertRaises(ic.IAIClientError):
            client.chat_json("給我一組 JSON", max_repair=2)

    def test_retry_errors_are_tracked_separately(self):
        client = self.make_client(FakeSession([]))

        state = {"calls": 0}

        def chat_side_effect(*_args, **_kwargs):
            state["calls"] += 1
            if state["calls"] == 1:
                client._record(error=True, detail="empty_response")
                raise ic.IAIClientError("empty_response")
            return '{"ok": true}'

        client.chat = mock.Mock(side_effect=chat_side_effect)
        self.assertEqual(client.chat_json("給我一組 JSON"), {"ok": True})
        usage = client.usage()
        self.assertEqual(usage["errors"], 1)
        self.assertEqual(usage["retry_errors"], 1)
        events = client.recent_error_events()
        self.assertEqual([e["kind"] for e in events], ["error", "retry"])
        self.assertIn("empty_response", events[-1]["detail"])


class TestModelsAndImages(unittest.TestCase):
    def test_list_models_masks_keys(self):
        session = FakeSession(get_responses=[
            FakeResponse(200, {"data": [{"id": "Furen-max"}, {"id": "Furen-large"}]}),
            FakeResponse(401, {}, text="unauthorized"),
        ])
        client = ic.IAIClient(keys=["sk-aaaaaaaaaaaa", "sk-bbbbbbbbbbbb"], session=session)
        result = client.list_models()
        self.assertEqual(result[0]["key"], "sk-****aaaa")
        self.assertEqual(result[0]["models"], ["Furen-max", "Furen-large"])
        self.assertEqual(result[1]["status"], 401)
        self.assertNotIn("sk-bbbbbbbbbbbb", json.dumps(result))

    def test_save_image_b64(self):
        session = FakeSession()
        client = ic.IAIClient(keys=["sk-aaaaaaaaaaaa"], session=session)
        payload = base64.b64encode(b"image-bytes").decode()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "assets" / "demo.png"
            saved = client.save_image({"b64_json": payload}, path)
            self.assertEqual(saved.read_bytes(), b"image-bytes")

    def test_image_returns_items(self):
        session = FakeSession([FakeResponse(200, {"data": [{"url": "https://example.com/a.png"}]})])
        client = ic.IAIClient(keys=["sk-aaaaaaaaaaaa"], session=session, sleep_fn=lambda _s: None)
        items = client.image("draw a cat")
        self.assertEqual(items[0]["url"], "https://example.com/a.png")
        self.assertEqual(client.stats["images"], 1)


class TestParallelAndKeys(unittest.TestCase):
    def test_run_parallel_collects_errors(self):
        def work(item):
            if item == 2:
                raise ValueError("boom")
            return item * 2

        results = ic.run_parallel(work, [1, 2, 3], max_workers=2)
        by_item = {item: (res, err) for item, res, err in results}
        self.assertEqual(by_item[1][0], 2)
        self.assertIsNone(by_item[1][1])
        self.assertIsInstance(by_item[2][1], ValueError)

    def test_parse_api_keys_dedupe(self):
        keys = parse_api_keys("a,b , a", "c", ["d", "", "b"])
        self.assertEqual(keys, ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
