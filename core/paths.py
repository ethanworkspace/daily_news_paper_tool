"""輸出目錄與檔名規則（凍結規格）。

結構：
    <root>/1..7/<YYYY-MM-DD>/
        01_新聞_10篇.md
        02_論文_01_<slug>.md ... 02_論文_05_<slug>.md
        03_專案_01_<slug>.md ... 03_專案_05_<slug>.md
        04_AI技術架構_深度拆解.md
        assets/
    <root>/每日匯報/<YYYY-MM-DD>_每日匯報.md

本模組同時提供 Windows 安全檔名與路徑穿越防護。
"""
from __future__ import annotations

import os
import re
import unicodedata
import uuid
from datetime import date, datetime
from pathlib import Path

from config import BASE_DIR, DAILY_DIGEST_FOLDER_NAME

WEEKDAY_FOLDERS = {index: str(index + 1) for index in range(7)}  # 0=週一 → "1"

INVALID_FILENAME_CHARS = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WHITESPACE_RUN = re.compile(r"\s+")
SEPARATOR_RUN = re.compile(r"[-_]{2,}")
RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{i}" for i in range(1, 10)),
    *(f"LPT{i}" for i in range(1, 10)),
}

NEWS_FILENAME = "01_新聞_10篇.md"
TECH_FILENAME = "04_AI技術架構_深度拆解.md"
ASSETS_FOLDER = "assets"


class PathSafetyError(ValueError):
    """路徑超出允許的根目錄，或檔名不合法。"""


def as_date(value: date | datetime) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    raise TypeError(f"需要 date 或 datetime，收到 {type(value).__name__}")


def date_str(value: date | datetime) -> str:
    return as_date(value).isoformat()


def week_folder(value: date | datetime) -> str:
    """週一→"1" … 週日→"7"。"""
    return WEEKDAY_FOLDERS[as_date(value).weekday()]


def day_dir(root: Path | str, value: date | datetime) -> Path:
    return Path(root) / week_folder(value) / date_str(value)


def digest_dir(root: Path | str) -> Path:
    return Path(root) / DAILY_DIGEST_FOLDER_NAME


def digest_path(root: Path | str, value: date | datetime) -> Path:
    return digest_dir(root) / f"{date_str(value)}_每日匯報.md"


def news_path(root: Path | str, value: date | datetime) -> Path:
    return day_dir(root, value) / NEWS_FILENAME


def tech_path(root: Path | str, value: date | datetime) -> Path:
    return day_dir(root, value) / TECH_FILENAME


def paper_path(root: Path | str, value: date | datetime, index: int, slug: str) -> Path:
    return day_dir(root, value) / f"02_論文_{_index(index)}_{slugify(slug, 40)}.md"


def repo_path(root: Path | str, value: date | datetime, index: int, slug: str) -> Path:
    return day_dir(root, value) / f"03_專案_{_index(index)}_{slugify(slug, 40)}.md"


def assets_dir(root: Path | str, value: date | datetime) -> Path:
    return day_dir(root, value) / ASSETS_FOLDER


def _index(index: int) -> str:
    if not isinstance(index, int) or index < 1:
        raise ValueError("索引必須是從 1 開始的整數")
    return f"{index:02d}"


def slugify(text: str, max_length: int = 40, fallback: str = "item") -> str:
    """把任意標題轉為 Windows 安全、保留中日韓文字的檔名片段。"""
    raw = unicodedata.normalize("NFKC", str(text or "")).strip()
    raw = INVALID_FILENAME_CHARS.sub("-", raw)
    raw = WHITESPACE_RUN.sub("-", raw)
    raw = SEPARATOR_RUN.sub("-", raw)
    raw = raw.strip(" .-_")
    if not raw:
        raw = fallback
    if len(raw) > max_length:
        raw = raw[:max_length].rstrip(" .-_") or fallback
    if raw.upper().split(".")[0] in RESERVED_NAMES:
        raw = f"{raw}_file"
    return raw


def safe_join(root: Path | str, *parts: str | Path) -> Path:
    """安全組合路徑；任何逃出 root 的嘗試都會被拒絕。"""
    root_path = Path(root).resolve()
    for part in parts:
        part_text = str(part)
        if part_text in {"", "."}:
            continue
        part_path = Path(part_text)
        if part_path.is_absolute() or part_path.drive or ".." in part_path.parts:
            raise PathSafetyError(f"不允許的路徑片段：{part_text!r}")
    candidate = root_path.joinpath(*[str(p) for p in parts]).resolve()
    if candidate != root_path and root_path not in candidate.parents:
        raise PathSafetyError(f"路徑逃出根目錄：{candidate}")
    return candidate


def ensure_day_tree(root: Path | str, value: date | datetime) -> dict[str, Path]:
    """建立當日所需目錄，回傳常用路徑。"""
    paths = {
        "day": day_dir(root, value),
        "assets": assets_dir(root, value),
        "digest": digest_dir(root),
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def expected_output_names() -> list[str]:
    """當日應產出的 13 個檔名規則（論文/專案以 <slug> 表萬用字元）。"""
    return [
        NEWS_FILENAME,
        *(f"02_論文_{i:02d}_<slug>.md" for i in range(1, 6)),
        *(f"03_專案_{i:02d}_<slug>.md" for i in range(1, 6)),
        TECH_FILENAME,
        "<YYYY-MM-DD>_每日匯報.md",
    ]


def atomic_write_text(path: Path | str, text: str, encoding: str = "utf-8") -> Path:
    """原子寫檔：先寫暫存檔再 replace，避免中斷造成半個檔案。"""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_name(f".{target.name}.{uuid.uuid4().hex[:8]}.tmp")
    try:
        temp.write_text(text, encoding=encoding, newline="\n")
        os.replace(temp, target)
    finally:
        if temp.exists():
            temp.unlink(missing_ok=True)
    return target


def project_root() -> Path:
    return BASE_DIR
