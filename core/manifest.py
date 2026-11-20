"""每次執行的可觀測性紀錄（run manifest）。

內容包含：日期、run id、各階段耗時、數量、配額、來源命中、配對、模型用量、
產出檔案、錯誤與警告。所有錯誤訊息在寫入前都會遮罩敏感字串。

預設輸出：`.system_generated/runs/<date>/<run_id>.json`
"""
from __future__ import annotations

import json
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

from core.paths import atomic_write_text, project_root
from core.security import redact_secrets

MANIFEST_VERSION = 1


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


@dataclass
class RunManifest:
    target_date: str
    run_id: str = field(default_factory=lambda: uuid.uuid4().hex[:12])
    started_at: str = field(default_factory=_utc_now)
    finished_at: str = ""
    status: str = "running"
    stages: dict[str, float] = field(default_factory=dict)
    counts: dict[str, int] = field(default_factory=dict)
    quotas: dict[str, Any] = field(default_factory=dict)
    sources: dict[str, dict[str, int]] = field(default_factory=dict)
    pairing: dict[str, int] = field(default_factory=dict)
    model_usage: dict[str, Any] = field(default_factory=dict)
    images: int = 0
    files: list[str] = field(default_factory=list)
    errors: list[dict[str, str]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    notes: dict[str, Any] = field(default_factory=dict)

    # ---------- 階段計時 ----------
    @contextmanager
    def stage(self, name: str) -> Iterator[None]:
        """量測階段耗時；發生例外時記錄錯誤後原樣拋出。"""
        start = time.monotonic()
        try:
            yield
        except Exception as exc:  # noqa: BLE001 - 記錄後交由呼叫端處理
            self.error(name, exc)
            raise
        finally:
            elapsed = time.monotonic() - start
            self.stages[name] = round(self.stages.get(name, 0.0) + elapsed, 3)

    # ---------- 觀測 ----------
    def source(self, name: str, *, found: int = 0, kept: int = 0, errors: int = 0) -> None:
        entry = self.sources.setdefault(name, {"found": 0, "kept": 0, "errors": 0})
        entry["found"] += found
        entry["kept"] += kept
        entry["errors"] += errors

    def error(self, scope: str, message: object) -> None:
        self.errors.append({"scope": scope, "message": redact_secrets(message), "at": _utc_now()})

    def warning(self, message: object) -> None:
        self.warnings.append(redact_secrets(message))

    def add_file(self, path: Path | str) -> None:
        candidate = Path(path)
        try:
            relative = candidate.resolve().relative_to(project_root().resolve())
            text = str(relative).replace("\\", "/")
        except (ValueError, OSError):
            text = str(candidate).replace("\\", "/")
        if text not in self.files:
            self.files.append(text)

    def set_models(self, usage: dict[str, Any]) -> None:
        self.model_usage = dict(usage)

    def finish(self, status: str = "ok") -> None:
        self.status = status
        self.finished_at = _utc_now()

    # ---------- 輸出 ----------
    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": MANIFEST_VERSION,
            "run_id": self.run_id,
            "target_date": self.target_date,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "status": self.status,
            "stages": dict(self.stages),
            "counts": dict(self.counts),
            "quotas": dict(self.quotas),
            "sources": {k: dict(v) for k, v in self.sources.items()},
            "pairing": dict(self.pairing),
            "model_usage": dict(self.model_usage),
            "images": self.images,
            "files": list(self.files),
            "errors": list(self.errors),
            "warnings": list(self.warnings),
            "notes": dict(self.notes),
        }

    def default_path(self) -> Path:
        return project_root() / ".system_generated" / "runs" / self.target_date / f"{self.run_id}.json"

    def save(self, path: Path | str | None = None) -> Path:
        target = Path(path) if path else self.default_path()
        atomic_write_text(
            target,
            json.dumps(self.to_dict(), ensure_ascii=False, indent=2),
        )
        return target
