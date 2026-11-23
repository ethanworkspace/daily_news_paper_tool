"""寫入器輸出正規化測試。"""
from __future__ import annotations

import unittest

from summarizer.daily_writer import DailyWriter, _to_traditional


class FakeClient:
    has_keys = True

    def chat_max(self, prompt, **kwargs):
        return "围绕与实现"

    def chat_large(self, prompt, **kwargs):
        return "网络资料"

    def chat_coder(self, prompt, **kwargs):
        return "软体架构"

    def chat_json(self, prompt, **kwargs):
        return {"text": "医疗设备", "items": ["预测模型"]}


class TestTraditionalOutput(unittest.TestCase):
    def test_normalize_nested(self):
        data = _to_traditional({"a": "围绕", "b": ["实现", {"c": "网络"}]})
        self.assertEqual(data, {"a": "圍繞", "b": ["實現", {"c": "網絡"}]})

    def test_chat_and_json_are_normalized(self):
        writer = DailyWriter(client=FakeClient())
        self.assertEqual(writer._chat("x"), "圍繞與實現")
        self.assertEqual(writer._chat("x", model="large"), "網絡資料")
        self.assertEqual(writer._json("x")["text"], "醫療設備")
        self.assertEqual(writer._json("x")["items"][0], "預測模型")


if __name__ == "__main__":
    unittest.main()
