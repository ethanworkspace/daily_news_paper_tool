"""每日報告輸出測試。"""
from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from core.paths import assets_dir, ensure_day_tree, tech_path
from report.daily_reporter import embed_tech_image


class TestEmbedTechImage(unittest.TestCase):
    def test_embeds_relative_image_link_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day = "2026-11-01"
            day_date = date(2026, 11, 1)
            ensure_day_tree(root, day_date)
            target = tech_path(root, day_date)
            target.write_text(
                "# 深度拆解\n\n## 一、架構原理與核心機制\n內容\n",
                encoding="utf-8",
            )
            image = assets_dir(root, day_date) / "04_architecture.png"
            image.write_bytes(b"png")

            self.assertTrue(embed_tech_image(root, day, image))
            text = target.read_text(encoding="utf-8")
            self.assertIn("![AI 技術架構示意圖](assets/04_architecture.png)", text)
            self.assertLess(text.index("![AI"), text.index("## 一、"))

            # 重複呼叫不會插入第二次
            self.assertFalse(embed_tech_image(root, day, image))
            self.assertEqual(text.count("![AI"), 1)


if __name__ == "__main__":
    unittest.main()
