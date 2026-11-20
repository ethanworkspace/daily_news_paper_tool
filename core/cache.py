"""檔案快取：避免重複抓取相同頁面／API，降低外部負擔與 iAI 成本。

- 檔案以 SHA-256(key) 命名，key 不會直接變成路徑（防路徑穿越）。
- 每筆資料包含建立時間與到期時間（TTL）。
- JSON 與二進位內容都支援（二進位以 base64 儲存）。
- 寫入採原子操作。
"""
from __future__ import annotations

import base64
import hashlib
import json
import time
from pathlib import Path
from typing import Any, Callable

from core.paths import atomic_write_text, project_root

DEFAULT_TTL_SECONDS = 24 * 60 * 60
MAX_VALUE_BYTES = 8 * 1024 * 1024


class CacheError(ValueError):
    """快取內容不合法（過大、損毀）。"""


def default_cache_dir() -> Path:
    return project_root() / ".system_generated" / "cache"


class FileCache:
    def __init__(
        self,
        root: Path | str | None = None,
        *,
        default_ttl: int = DEFAULT_TTL_SECONDS,
        max_value_bytes: int = MAX_VALUE_BYTES,
        clock: Callable[[], float] = time.time,
    ):
        self.root = Path(root) if root else default_cache_dir()
        self.root.mkdir(parents=True, exist_ok=True)
        self.default_ttl = default_ttl
        self.max_value_bytes = max_value_bytes
        self._clock = clock

    # ---------- 路徑 ----------
    def path_for(self, key: str) -> Path:
        digest = hashlib.sha256(str(key).encode("utf-8")).hexdigest()
        return self.root / digest[:2] / f"{digest}.json"

    # ---------- 基本操作 ----------
    def set(self, key: str, value: Any, *, ttl: int | None = None) -> Path:
        payload = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        if len(payload.encode("utf-8")) > self.max_value_bytes:
            raise CacheError("快取內容超過大小上限")
        now = self._clock()
        envelope = {
            "key": str(key),
            "created": now,
            "expires": now + (self.default_ttl if ttl is None else ttl),
            "encoding": "json",
            "value": value,
        }
        return atomic_write_text(self.path_for(key), json.dumps(envelope, ensure_ascii=False))

    def set_bytes(self, key: str, data: bytes, *, ttl: int | None = None, content_type: str = "") -> Path:
        if len(data) > self.max_value_bytes:
            raise CacheError("快取內容超過大小上限")
        now = self._clock()
        envelope = {
            "key": str(key),
            "created": now,
            "expires": now + (self.default_ttl if ttl is None else ttl),
            "encoding": "base64",
            "content_type": content_type,
            "value": base64.b64encode(data).decode("ascii"),
        }
        return atomic_write_text(self.path_for(key), json.dumps(envelope, ensure_ascii=False))

    def _read_envelope(self, key: str) -> dict | None:
        path = self.path_for(key)
        if not path.is_file():
            return None
        try:
            envelope = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        if not isinstance(envelope, dict) or envelope.get("key") != str(key):
            return None
        return envelope

    def get(self, key: str, *, allow_expired: bool = False) -> Any | None:
        envelope = self._read_envelope(key)
        if envelope is None:
            return None
        if not allow_expired and float(envelope.get("expires", 0)) < self._clock():
            return None
        return envelope.get("value")

    def get_bytes(self, key: str, *, allow_expired: bool = False) -> bytes | None:
        envelope = self._read_envelope(key)
        if envelope is None:
            return None
        if not allow_expired and float(envelope.get("expires", 0)) < self._clock():
            return None
        if envelope.get("encoding") != "base64":
            return None
        try:
            return base64.b64decode(envelope.get("value", ""))
        except (ValueError, TypeError):
            return None

    def delete(self, key: str) -> bool:
        path = self.path_for(key)
        if path.is_file():
            path.unlink()
            return True
        return False

    # ---------- 便利方法 ----------
    def get_json(self, key: str, *, allow_expired: bool = False) -> Any | None:
        envelope = self._read_envelope(key)
        if envelope is None:
            return None
        if not allow_expired and float(envelope.get("expires", 0)) < self._clock():
            return None
        if envelope.get("encoding") != "json":
            return None
        return envelope.get("value")

    def set_json(self, key: str, value: Any, *, ttl: int | None = None) -> Path:
        return self.set(key, value, ttl=ttl)

    def fetch(self, key: str, producer: Callable[[], Any], *, ttl: int | None = None) -> Any:
        """有快取就回傳，否則呼叫 producer() 並寫入快取。"""
        cached = self.get_json(key)
        if cached is not None:
            return cached
        value = producer()
        self.set_json(key, value, ttl=ttl)
        return value

    # ---------- 維護 ----------
    def purge_expired(self) -> int:
        removed = 0
        now = self._clock()
        for path in self.root.rglob("*.json"):
            try:
                envelope = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                path.unlink(missing_ok=True)
                removed += 1
                continue
            if float(envelope.get("expires", 0)) < now:
                path.unlink(missing_ok=True)
                removed += 1
        return removed

    def stats(self) -> dict[str, int]:
        files = list(self.root.rglob("*.json"))
        total_bytes = sum(p.stat().st_size for p in files if p.is_file())
        now = self._clock()
        expired = 0
        for path in files:
            try:
                envelope = json.loads(path.read_text(encoding="utf-8"))
                if float(envelope.get("expires", 0)) < now:
                    expired += 1
            except (OSError, json.JSONDecodeError):
                expired += 1
        return {"entries": len(files), "expired": expired, "bytes": total_bytes}
