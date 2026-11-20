"""日誌工具：檔案輪替、主控台輸出、敏感資訊遮罩。

用法：
    from core.logging_utils import setup_logger
    logger = setup_logger("collect")
    logger.info("抓取 %s", url)

特性：
- 日誌檔位於 `.system_generated/logs/`（已 gitignore）
- 每 5MB 輪替、保留 3 份
- 所有訊息、例外堆疊都先經過 `redact_secrets`
"""
from __future__ import annotations

import logging
import logging.handlers
import sys
from pathlib import Path

from core.paths import project_root
from core.security import redact_secrets

LOG_FORMAT = "%(asctime)s %(levelname)-7s %(name)s | %(message)s"
MAX_BYTES = 5 * 1024 * 1024
BACKUP_COUNT = 3


class RedactionFilter(logging.Filter):
    """把 record 內所有文字（含例外）置換為遮罩版本。"""

    def filter(self, record: logging.LogRecord) -> bool:
        try:
            message = record.getMessage()
        except Exception:  # noqa: BLE001 - 格式錯誤時仍要能寫日誌
            message = str(record.msg)
        record.msg = redact_secrets(message)
        record.args = ()
        if record.exc_info:
            formatter = logging.Formatter()
            record.exc_text = redact_secrets(formatter.formatException(record.exc_info))
        return True


def default_log_dir() -> Path:
    return project_root() / ".system_generated" / "logs"


def setup_logger(
    name: str = "daily_report",
    *,
    log_dir: Path | str | None = None,
    level: int = logging.INFO,
    console: bool = True,
    filename: str = "run.log",
) -> logging.Logger:
    """建立（或取回）已設定的 logger，重複呼叫不會疊加 handler。"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if getattr(logger, "_daily_configured", False):
        return logger

    formatter = logging.Formatter(LOG_FORMAT)
    redaction = RedactionFilter()

    directory = Path(log_dir) if log_dir else default_log_dir()
    directory.mkdir(parents=True, exist_ok=True)
    file_handler = logging.handlers.RotatingFileHandler(
        directory / filename,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.addFilter(redaction)
    logger.addHandler(file_handler)

    if console:
        stream = logging.StreamHandler(sys.stderr)
        stream.setFormatter(formatter)
        stream.addFilter(redaction)
        logger.addHandler(stream)

    logger._daily_configured = True  # type: ignore[attr-defined]
    return logger


def reset_logger(name: str = "daily_report") -> None:
    """測試用：移除並關閉 handler。"""
    logger = logging.getLogger(name)
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()
    if hasattr(logger, "_daily_configured"):
        delattr(logger, "_daily_configured")
