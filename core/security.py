"""URL／秘密資訊安全工具。

- `redact_secrets`：把常見 API key／Bearer token 樣式遮罩，供日誌與錯誤訊息使用。
- `assert_public_http_url`：SSRF 防護，只允許公開的 http/https 位址。

注意：DNS 解析後仍可能被導向內網（DNS rebinding），實際抓取時（P2）還需在
連線層再次檢查解析結果與重新導向目標；本模組提供第一道靜態檢查。
"""
from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlsplit

SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"AIza[0-9A-Za-z_\-]{30,}"),
    re.compile(r"AKIA[0-9A-Z]{12,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
    re.compile(r"(?i)(bearer\s+)[A-Za-z0-9._\-]{8,}"),
    re.compile(r"(?i)([?&](?:api[_-]?key|access[_-]?token|token|key)=)[^&\s]{8,}"),
]

_REDACTION = "****"


def redact_secrets(text: object) -> str:
    """回傳已遮罩敏感字串的文字（保留可讀的其餘內容）。"""
    if text is None:
        return ""
    result = str(text)
    for pattern in SECRET_PATTERNS:
        if pattern.groups:
            result = pattern.sub(lambda m: f"{m.group(1)}{_REDACTION}", result)
        else:
            result = pattern.sub(_REDACTION, result)
    return result


class UnsafeURLError(ValueError):
    """URL 不符合安全政策（非 http/https、含帳密、指向內網等）。"""


def _is_private_address(host: str) -> bool:
    normalized = host.strip("[]").lower()
    if normalized in {"localhost", "localhost.localdomain"} or normalized.endswith(".localhost"):
        return True
    if normalized.endswith(".local") or normalized.endswith(".internal"):
        return True
    try:
        address = ipaddress.ip_address(normalized)
    except ValueError:
        return False
    return not address.is_global or address.is_multicast or address.is_reserved


def assert_public_http_url(url: str, *, allowed_schemes: tuple[str, ...] = ("http", "https")) -> str:
    """驗證 URL 可安全抓取，回傳去除前後空白的 URL；不合格時丟 `UnsafeURLError`。"""
    if not url or not isinstance(url, str):
        raise UnsafeURLError("URL 不可為空")
    candidate = url.strip()
    if any(ch.isspace() for ch in candidate):
        raise UnsafeURLError("URL 不可包含空白")
    parts = urlsplit(candidate)
    if parts.scheme.lower() not in allowed_schemes:
        raise UnsafeURLError(f"不允許的 URL scheme：{parts.scheme or '(無)'}")
    if not parts.netloc or not parts.hostname:
        raise UnsafeURLError("URL 缺少主機名稱")
    if parts.username or parts.password:
        raise UnsafeURLError("URL 不可包含帳號或密碼")
    if _is_private_address(parts.hostname):
        raise UnsafeURLError(f"URL 指向內網或保留位址：{parts.hostname}")
    return candidate
