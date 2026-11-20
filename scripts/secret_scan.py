"""全庫秘密掃描：檢查 git 追蹤的檔案是否含有 API key/token 等敏感字串。

用法：
    python scripts/secret_scan.py

退出碼：0 = 未發現；1 = 發現疑似秘密。
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PATTERNS = {
    "openai-like": re.compile(r"sk-[A-Za-z0-9_\-]{16,}"),
    "github-token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "github-pat": re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    "google-api-key": re.compile(r"AIza[0-9A-Za-z_\-]{35}"),
    "aws-access-key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "slack-token": re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
}

SKIP_PARTS = {".git", "__pycache__", ".system_generated", "node_modules", ".venv", "venv"}
SKIP_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip", ".exe", ".dll", ".pyc"}
MAX_BYTES = 2 * 1024 * 1024


def tracked_files() -> list[Path]:
    try:
        output = subprocess.check_output(
            ["git", "ls-files"], cwd=ROOT, text=True, encoding="utf-8", errors="replace"
        )
    except Exception as exc:  # noqa: BLE001
        print(f"[SecretScan] 無法取得 git 檔案清單：{exc}")
        return []
    files = []
    for line in output.splitlines():
        path = ROOT / line.strip()
        if not path.is_file():
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in SKIP_SUFFIXES:
            continue
        if path.stat().st_size > MAX_BYTES:
            continue
        files.append(path)
    return files


def mask(value: str) -> str:
    if len(value) <= 10:
        return "****"
    return f"{value[:4]}****{value[-4:]}"


def main() -> int:
    findings = []
    files = tracked_files()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:  # noqa: BLE001
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for name, pattern in PATTERNS.items():
                for match in pattern.finditer(line):
                    findings.append((path.relative_to(ROOT), line_no, name, mask(match.group(0))))

    if not findings:
        print(f"[SecretScan] 通過：掃描 {len(files)} 個追蹤檔案，未發現疑似秘密。")
        return 0

    print(f"[SecretScan] 發現 {len(findings)} 筆疑似秘密：")
    for rel, line_no, name, masked in findings:
        print(f"  - {rel}:{line_no} [{name}] {masked}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
