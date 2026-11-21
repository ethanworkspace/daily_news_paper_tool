"""高科 iAI 多模型用戶端（P0 基礎建設）

功能：
- 多組 API key 金鑰池（輪替、冷卻、健康狀態）
- 多模型路由（Furen-max / Furen-large / Furen-coder / Pic-large）
- 併發控制（全域 + 每把 key 的 semaphore），支援「同時協作」
- 429/5xx/逾時重試與退避、金鑰遮罩、用量統計
- 文字、JSON、生圖三種呼叫
- 任何日誌與例外訊息都不會輸出完整 API key
"""
from __future__ import annotations

import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Iterable

import requests

from config import (
    IAI_BASE_URL,
    IAI_API_KEYS,
    IAI_MAX_CONCURRENCY,
    IAI_MAX_RETRIES,
    IAI_MODEL_CODER,
    IAI_MODEL_IMAGE,
    IAI_MODEL_LARGE,
    IAI_MODEL_MAX,
    IAI_PER_KEY_CONCURRENCY,
    IAI_TIMEOUT,
)

KEY_PATTERN = re.compile(r"sk-[A-Za-z0-9_\-]{6,}")


class IAIClientError(Exception):
    """iAI 用戶端例外（訊息已遮罩，不含金鑰）。"""


def mask_key(key: str) -> str:
    """只顯示前 3 碼與後 4 碼，其餘遮蔽。"""
    if not key:
        return "(未設定)"
    if len(key) <= 10:
        return "****"
    return f"{key[:3]}****{key[-4:]}"


def redact(text: Any) -> str:
    """遮蔽文字中的任何 API key 樣式。"""
    if text is None:
        return ""
    return KEY_PATTERN.sub("sk-****", str(text))


def clean_think_tags(text: str) -> str:
    """去除推理模型可能產生的 <think>...</think> 內容。"""
    if not text:
        return ""
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


def extract_json(text: str) -> Any:
    """從模型輸出擷取第一個合法 JSON（容忍 markdown 圍籬與前後說明）。"""
    if not text:
        raise ValueError("空輸出")
    cleaned = text.strip()
    # 去掉 ```json ... ``` 圍籬
    fence = re.search(r"```(?:json)?\s*(.*?)```", cleaned, flags=re.DOTALL)
    if fence:
        cleaned = fence.group(1).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 掃描第一個 { 或 [，並以括號配對找出結尾（避開字串內的括號）
    start = min(
        [i for i in (cleaned.find("{"), cleaned.find("[")) if i >= 0],
        default=-1,
    )
    if start < 0:
        raise ValueError("找不到 JSON 起始符號")
    opening = cleaned[start]
    closing = "}" if opening == "{" else "]"
    depth = 0
    in_string = False
    escape = False
    for index in range(start, len(cleaned)):
        char = cleaned[index]
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == opening:
            depth += 1
        elif char == closing:
            depth -= 1
            if depth == 0:
                candidate = cleaned[start:index + 1]
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    # try loose fixes
                    fixed = re.sub(r",\s*([}\]])", r"\1", candidate)
                    return json.loads(fixed)
    # salvage: take partial object and close brackets
    tail = cleaned[start:].rstrip()
    tail = re.sub(r",\s*([}\]])", r"\1", tail)
    # remove trailing incomplete string/value
    tail = re.sub(r',?\s*"[^"\\]*(?:\\.[^"\\]*)*"?\s*:?\s*"?[^"\}\]]*$', '', tail, flags=re.DOTALL)
    # balance
    opens = tail.count('{') - tail.count('}')
    openb = tail.count('[') - tail.count(']')
    if opens > 0 or openb > 0:
        tail2 = tail + (']' * max(openb,0)) + ('}' * max(opens,0))
        tail2 = re.sub(r",\s*([}\]])", r"\1", tail2)
        try:
            return json.loads(tail2)
        except Exception:
            pass
    raise ValueError("JSON 括號不完整")


class KeyPool:
    """執行緒安全的金鑰池：輪替使用、429/401 冷卻、全部冷卻時回報等待時間。"""

    def __init__(self, keys: Iterable[str]):
        self._keys = [k for k in keys if k]
        self._lock = threading.Lock()
        self._index = 0
        self._cooldown_until: dict[str, float] = {}

    def __len__(self) -> int:
        return len(self._keys)

    def masked(self) -> list[str]:
        return [mask_key(k) for k in self._keys]

    def next_key(self) -> str | None:
        with self._lock:
            if not self._keys:
                return None
            now = time.monotonic()
            total = len(self._keys)
            for offset in range(total):
                key = self._keys[(self._index + offset) % total]
                if self._cooldown_until.get(key, 0.0) <= now:
                    self._index = (self._index + offset + 1) % total
                    return key
            return None

    def cooldown(self, key: str, seconds: float) -> None:
        with self._lock:
            until = time.monotonic() + max(seconds, 0.0)
            self._cooldown_until[key] = max(self._cooldown_until.get(key, 0.0), until)

    def earliest_wait(self) -> float:
        with self._lock:
            now = time.monotonic()
            waits = [self._cooldown_until.get(k, 0.0) - now for k in self._keys]
            waits = [w for w in waits if w > 0]
            return min(waits) if waits else 0.0


class IAIClient:
    """高科 iAI OpenAI 相容介面用戶端。"""

    def __init__(
        self,
        keys: Iterable[str] | None = None,
        base_url: str | None = None,
        model_max: str | None = None,
        model_large: str | None = None,
        model_coder: str | None = None,
        model_image: str | None = None,
        max_concurrency: int | None = None,
        per_key_concurrency: int | None = None,
        timeout: int | None = None,
        max_retries: int | None = None,
        session: requests.Session | None = None,
        sleep_fn: Callable[[float], None] | None = None,
    ):
        self.pool = KeyPool(keys if keys is not None else IAI_API_KEYS)
        self.base_url = (base_url or IAI_BASE_URL).rstrip("/")
        self.model_max = model_max or IAI_MODEL_MAX
        self.model_large = model_large or IAI_MODEL_LARGE
        self.model_coder = model_coder or IAI_MODEL_CODER
        self.model_image = model_image or IAI_MODEL_IMAGE
        self.timeout = timeout or IAI_TIMEOUT
        self.max_retries = max_retries if max_retries is not None else IAI_MAX_RETRIES
        self.session = session or requests.Session()
        self._sleep = sleep_fn or time.sleep

        self._global_sem = threading.BoundedSemaphore(max_concurrency or IAI_MAX_CONCURRENCY)
        self._per_key_limit = per_key_concurrency or IAI_PER_KEY_CONCURRENCY
        self._key_sems: dict[str, threading.BoundedSemaphore] = {}
        self._key_sems_lock = threading.Lock()

        self._stats_lock = threading.Lock()
        self.stats = {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0, "images": 0, "errors": 0}

    # ---------- 對外屬性 ----------
    @property
    def has_keys(self) -> bool:
        return len(self.pool) > 0

    def _key_sem(self, key: str) -> threading.BoundedSemaphore:
        with self._key_sems_lock:
            if key not in self._key_sems:
                self._key_sems[key] = threading.BoundedSemaphore(self._per_key_limit)
            return self._key_sems[key]

    def _record(self, *, prompt_tokens: int = 0, completion_tokens: int = 0, images: int = 0, error: bool = False) -> None:
        with self._stats_lock:
            self.stats["calls"] += 1
            self.stats["prompt_tokens"] += prompt_tokens
            self.stats["completion_tokens"] += completion_tokens
            self.stats["images"] += images
            if error:
                self.stats["errors"] += 1

    def usage(self) -> dict[str, int]:
        with self._stats_lock:
            return dict(self.stats)

    # ---------- HTTP ----------
    def _request(self, method: str, path: str, payload: dict | None = None, timeout: int | None = None):
        if not self.has_keys:
            raise IAIClientError("未設定任何 iAI API key（請設定 IAI_API_KEYS 或 IAI_API_KEY_1..4）")

        url = f"{self.base_url}{path}"
        attempts = max(self.max_retries, 1) + 1
        last_error = "未知錯誤"

        for attempt in range(attempts):
            key = self.pool.next_key()
            if key is None:
                wait = self.pool.earliest_wait()
                self._sleep(min(max(wait, 0.5), 30.0))
                last_error = "所有金鑰都在冷卻中"
                continue

            headers = {
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "User-Agent": "DailyAIReport/2.0",
            }
            try:
                with self._global_sem, self._key_sem(key):
                    response = self.session.request(
                        method, url, headers=headers, json=payload,
                        timeout=timeout or self.timeout,
                    )
            except requests.RequestException as exc:
                last_error = f"連線例外：{type(exc).__name__}"
                self._sleep(min(2 ** attempt, 15))
                continue

            if response.status_code == 200:
                return response

            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After", "")
                try:
                    cooldown = float(retry_after)
                except (TypeError, ValueError):
                    cooldown = min(2 ** attempt, 30)
                self.pool.cooldown(key, cooldown)
                last_error = f"HTTP 429（金鑰 {mask_key(key)} 冷卻 {cooldown:.0f}s）"
                continue

            if response.status_code in (401, 403):
                # 金鑰無效/無權限：長時間冷卻並換下一把
                self.pool.cooldown(key, 3600)
                last_error = f"HTTP {response.status_code}（金鑰 {mask_key(key)} 停用 1 小時）"
                continue

            if response.status_code >= 500:
                last_error = f"HTTP {response.status_code}"
                self._sleep(min(2 ** attempt, 15))
                continue

            raise IAIClientError(
                f"HTTP {response.status_code}：{redact(response.text[:300])}"
            )

        self._record(error=True)
        raise IAIClientError(f"請求失敗（已重試 {attempts} 次）：{redact(last_error)}")

    def _resolve_model(self, model: str | None, default: str) -> str:
        name = (model or default or "").strip()
        aliases = {
            "max": self.model_max, "furen-max": self.model_max,
            "large": self.model_large, "furen-large": self.model_large,
            "coder": self.model_coder, "furen-coder": self.model_coder,
            "image": self.model_image, "pic-large": self.model_image,
        }
        return aliases.get(name.lower(), name)

    # ---------- 文字 ----------
    def chat(
        self,
        prompt: str | None = None,
        *,
        messages: list[dict] | None = None,
        model: str | None = None,
        system: str | None = None,
        temperature: float = 0.3,
        max_tokens: int | None = None,
        response_format: dict | None = None,
        timeout: int | None = None,
    ) -> str:
        model = self._resolve_model(model, self.model_large)
        if messages is None:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt or ""})

        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        if max_tokens:
            payload["max_tokens"] = max_tokens
        if response_format:
            payload["response_format"] = response_format

        req_payload = {k: v for k, v in payload.items() if k != "_retried"}
        response = self._request("POST", "/chat/completions", req_payload, timeout=timeout)
        data = response.json()
        usage = data.get("usage") or {}
        text = ""
        choices = data.get("choices") or []
        finish_reason = (choices[0].get("finish_reason") if choices else None) or "unknown"
        if choices:
            text = (choices[0].get("message") or {}).get("content", "") or ""
        if not text or finish_reason == "length":
            # reasoning/length-truncated output: retry once with larger budget
            if (payload.get("max_tokens") or 0) < 4096 and not payload.get("_retried"):
                payload2 = dict(payload)
                payload2["max_tokens"] = max(int(payload.get("max_tokens") or 0), 4096)
                payload2["_retried"] = True
                try:
                    req_payload2 = {k: v for k, v in payload2.items() if k != "_retried"}
                    response2 = self._request("POST", "/chat/completions", req_payload2, timeout=timeout)
                    data2 = response2.json()
                    usage2 = data2.get("usage") or {}
                    choices2 = data2.get("choices") or []
                    text2 = (choices2[0].get("message") or {}).get("content", "") if choices2 else ""
                    finish2 = (choices2[0].get("finish_reason") if choices2 else None) or "unknown"
                    if text2:
                        self._record(
                            prompt_tokens=int(usage.get("prompt_tokens") or 0) + int(usage2.get("prompt_tokens") or 0),
                            completion_tokens=int(usage.get("completion_tokens") or 0) + int(usage2.get("completion_tokens") or 0),
                        )
                        text = text2
                        finish_reason = finish2
                except Exception:
                    pass
        if not text:
            self._record(error=True)
            raise IAIClientError(
                f"模型回應為空（finish_reason={finish_reason}）；若為推理模型請提高 max_tokens"
            )
        self._record(
            prompt_tokens=int(usage.get("prompt_tokens") or 0),
            completion_tokens=int(usage.get("completion_tokens") or 0),
        )
        return clean_think_tags(text)

    def chat_max(self, prompt: str, **kwargs) -> str:
        return self.chat(prompt, model=self.model_max, **kwargs)

    def chat_large(self, prompt: str, **kwargs) -> str:
        return self.chat(prompt, model=self.model_large, **kwargs)

    def chat_coder(self, prompt: str, **kwargs) -> str:
        return self.chat(prompt, model=self.model_coder, **kwargs)

    def chat_json(
        self,
        prompt: str,
        *,
        model: str | None = None,
        system: str | None = None,
        schema_hint: str = "",
        max_repair: int = 2,
        **kwargs,
    ) -> Any:
        """要求模型輸出 JSON，失敗時自動要求修復（最多 max_repair 次）。"""
        model = self._resolve_model(model, self.model_max)
        system = system or "你是嚴謹的資料工程師，只輸出合法 JSON。"
        hint = f"\nJSON schema hint: {schema_hint}" if schema_hint else ""
        user_prompt = f"{prompt}{hint}\n\n請只輸出合法 JSON，不要加上任何說明或 markdown 圍籬。"

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ]
        last_exc = None
        for attempt in range(max_repair + 1):
            try:
                text = self.chat(messages=messages, model=model, **kwargs)
            except IAIClientError as exc:
                last_exc = exc
                if attempt >= max_repair:
                    raise
                # on empty/length error, ask for shorter JSON
                messages = messages + [
                    {"role": "user", "content": "上一個回應為空或被截斷。請只輸出短而完整的合法 JSON。"},
                ]
                kwargs = dict(kwargs)
                kwargs["max_tokens"] = max(int(kwargs.get("max_tokens") or 0), 4096)
                continue
            try:
                return extract_json(text)
            except (ValueError, json.JSONDecodeError) as exc:
                last_exc = exc
                # salvage partial object before giving up
                if attempt == max_repair:
                    try:
                        salvaged = extract_json(text + "}")
                    except Exception:
                        pass
                    else:
                        if isinstance(salvaged, dict):
                            return salvaged
                    raise IAIClientError(f"JSON 解析失敗（已修復 {max_repair} 次）：{exc}") from exc
                messages = messages + [
                    {"role": "assistant", "content": text[:4000]},
                    {"role": "user", "content": f"上述輸出不是合法 JSON（{exc}）。請修正並只輸出合法 JSON。"},
                ]
        if last_exc:
            raise last_exc

    # ---------- 生圖 ----------
    def image(
        self,
        prompt: str,
        *,
        model: str | None = None,
        size: str = "1024x1024",
        n: int = 1,
        timeout: int | None = None,
    ) -> list[dict]:
        payload = {
            "model": model or self.model_image,
            "prompt": prompt,
            "size": size,
            "n": n,
        }
        response = self._request("POST", "/images/generations", payload, timeout=timeout or max(self.timeout, 180))
        data = response.json()
        items = data.get("data") or []
        if not items:
            self._record(error=True)
            raise IAIClientError("生圖回應為空")
        self._record(images=len(items))
        return items

    def save_image(self, item: dict, path, max_bytes: int = 10 * 1024 * 1024) -> Any:
        """將生圖結果（url 或 b64_json）存檔，回傳路徑。"""
        from pathlib import Path
        import base64

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        if item.get("b64_json"):
            raw = base64.b64decode(item["b64_json"])
            if len(raw) > max_bytes:
                raise IAIClientError("生圖檔案超過大小上限")
            path.write_bytes(raw)
            return path

        url = item.get("url")
        if not url:
            raise IAIClientError("生圖結果缺少 url 或 b64_json")

        response = self.session.get(url, timeout=self.timeout)
        if response.status_code != 200:
            raise IAIClientError(f"下載生圖失敗：HTTP {response.status_code}")
        raw = response.content
        if len(raw) > max_bytes:
            raise IAIClientError("生圖檔案超過大小上限")
        path.write_bytes(raw)
        return path

    # ---------- 能力探測 ----------
    def list_models(self) -> list[dict]:
        """逐把 key 查詢 /models，回傳遮罩後的結果（絕不含明文金鑰）。"""
        results = []
        keys = list(getattr(self.pool, "_keys", []))
        for key in keys:
            entry = {"key": mask_key(key), "status": None, "models": [], "error": ""}
            try:
                response = self.session.get(
                    f"{self.base_url}/models",
                    headers={"Authorization": f"Bearer {key}"},
                    timeout=self.timeout,
                )
                entry["status"] = response.status_code
                if response.status_code == 200:
                    data = response.json()
                    models = data.get("data") if isinstance(data, dict) else None
                    if models is None and isinstance(data, list):
                        models = data
                    entry["models"] = [
                        (m.get("id") if isinstance(m, dict) else str(m)) for m in (models or [])
                    ]
                else:
                    entry["error"] = redact(response.text[:200])
            except Exception as exc:
                entry["error"] = f"{type(exc).__name__}: {redact(exc)}"
            results.append(entry)
        return results


def run_parallel(func: Callable, items: Iterable, max_workers: int = 4) -> list[tuple[Any, Any, Exception | None]]:
    """平行執行（用於多模型/多篇項目同時協作），回傳 (item, result, error)。"""
    results: list[tuple[Any, Any, Exception | None]] = []
    items = list(items)
    if not items:
        return results
    with ThreadPoolExecutor(max_workers=min(max_workers, len(items))) as executor:
        futures = {executor.submit(func, item): item for item in items}
        for future in as_completed(futures):
            item = futures[future]
            try:
                results.append((item, future.result(), None))
            except Exception as exc:  # noqa: BLE001 - 收集後交由呼叫端處理
                results.append((item, None, exc))
    return results


def get_client() -> IAIClient:
    """建立預設用戶端（金鑰由環境變數/登錄檔讀取）。"""
    return IAIClient()
