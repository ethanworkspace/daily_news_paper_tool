"""P0 模型能力探測：確認 4 組金鑰與 4 個模型（Furen-max/large/coder、Pic-large）是否可用。

用法：
    python scripts/probe_models.py                # 只查 /models（不扣生成額度）
    python scripts/probe_models.py --chat-check   # 再對三個文字模型各發一次極短測試
    python scripts/probe_models.py --image-check  # 再測試一次生圖（會產生費用）

安全：
- 只從環境變數/登錄檔讀取金鑰，不寫入任何檔案。
- 輸出與 JSON 僅包含遮罩後的金鑰（sk-****last4）。
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from config import BASE_DIR  # noqa: E402
from iai_client import IAIClient, mask_key, redact  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="高科 iAI 模型能力探測")
    parser.add_argument("--chat-check", action="store_true", help="對文字模型發送極短測試請求")
    parser.add_argument("--image-check", action="store_true", help="測試生圖模型（會產生費用）")
    args = parser.parse_args()

    client = IAIClient()
    if not client.has_keys:
        print("[P0] 找不到任何 iAI API key。")
        print("     請先設定環境變數 IAI_API_KEYS（逗號分隔）或 IAI_API_KEY_1..4。")
        return 2

    print(f"[P0] 金鑰數量：{len(client.pool)}（{', '.join(client.pool.masked())}）")
    print(f"[P0] Base URL：{client.base_url}")

    report = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "base_url": client.base_url,
        "key_count": len(client.pool),
        "keys": client.pool.masked(),
        "models_endpoint": client.list_models(),
        "chat_check": {},
        "image_check": {},
    }

    print("\n== /models 查詢結果 ==")
    for entry in report["models_endpoint"]:
        status = entry.get("status")
        count = len(entry.get("models") or [])
        print(f"- 金鑰 {entry['key']}：HTTP {status}，模型數 {count}")
        if entry.get("error"):
            print(f"    錯誤：{redact(entry['error'])[:120]}")

    if args.chat_check:
        print("\n== 文字模型測試 ==")
        for label, model in (
            ("Furen-max", client.model_max),
            ("Furen-large", client.model_large),
            ("Furen-coder", client.model_coder),
        ):
            try:
                # 推理型模型會先產生 reasoning_content，max_tokens 太小會讓 content 為空，
                # 因此給足以完成一次極短回覆的額度。
                text = client.chat("請只回覆：OK", model=model, max_tokens=256, temperature=0)
                report["chat_check"][label] = {"model": model, "ok": True, "reply": text[:40]}
                print(f"- {label} ({model})：OK -> {text[:40]!r}")
            except Exception as exc:  # noqa: BLE001
                report["chat_check"][label] = {"model": model, "ok": False, "error": redact(exc)}
                print(f"- {label} ({model})：失敗 -> {redact(exc)[:120]}")

    if args.image_check:
        print("\n== 生圖模型測試 ==")
        try:
            items = client.image("a simple blue circle on white background", n=1)
            report["image_check"] = {
                "model": client.model_image,
                "ok": bool(items),
                "fields": sorted(items[0].keys()) if items else [],
            }
            print(f"- {client.model_image}：OK（回傳 {len(items)} 張）")
        except Exception as exc:  # noqa: BLE001
            report["image_check"] = {"model": client.model_image, "ok": False, "error": redact(exc)}
            print(f"- {client.model_image}：失敗 -> {redact(exc)[:120]}")

    out_dir = BASE_DIR / ".system_generated"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "p0_capability.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[P0] 能力矩陣已寫入：{out_path}（僅含遮罩金鑰，已列入 gitignore）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
