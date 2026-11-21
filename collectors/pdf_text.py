"""PDF 全文萃取：pypdf + fontTools 字型解析 + RapidOCR 掃描頁補救。

設計原則
- 一般文字型 PDF：pypdf 逐頁萃取，預設不限頁數；必要時改用 layout 模式保留欄位。
- 字型/CFF 編碼：安裝 fontTools 後 pypdf 可正確解碼；本模組會捕捉 pypdf 字型警告，回報是否需要補救。
- 掃描型 PDF（整頁圖片）：以 pypdfium2 將該頁渲染成影像，再用 RapidOCR（ONNX）辨識。
- 任一選用依賴缺少時自動降級，不讓整個蒐集流程失敗。
"""
from __future__ import annotations

import importlib.util
import io
import logging
import re
import threading
import time
from dataclasses import dataclass, field

try:  # pypdf 為必要依賴
    from pypdf import PdfReader  # type: ignore
except Exception:  # pragma: no cover - runtime guard
    PdfReader = None  # type: ignore[assignment]

_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
_GARBLED = re.compile(r"[\ufffd\ue000-\uf8ff]")
_HAS_TEXT = re.compile(r"[0-9A-Za-z\u4e00-\u9fff]")
_HEADING_RE = re.compile(
    r"^(?:\d+(?:\.\d+)*\.?\s+)?(?:abstract|introduction|related work|background|method|methods|methodology|"
    r"approach|experiment|experiments|results|discussion|conclusion|limitations|future work|references|"
    r"acknowledg(?:e)?ments?)\b",
    re.IGNORECASE,
)

_OCR_LOCK = threading.Lock()
_OCR_ENGINE = None
_OCR_INIT_FAILED = False


def ocr_available() -> bool:
    return importlib.util.find_spec("rapidocr") is not None and importlib.util.find_spec("pypdfium2") is not None


def fonttools_available() -> bool:
    return importlib.util.find_spec("fontTools") is not None


@dataclass
class PdfExtraction:
    text: str = ""
    pages: int = 0
    ocr_pages: int = 0
    layout_pages: int = 0
    font_warnings: int = 0
    fonttools: bool = False
    ocr_engine: str = ""
    note: str = ""
    page_stats: list[dict] = field(default_factory=list)

    @property
    def kind(self) -> str:
        if self.ocr_pages:
            return "pdf+ocr"
        return "pdf"


def clean_pdf_text(text: str) -> str:
    """去除 PDF 控制字元、處理斷字並合併被硬換行的段落。"""
    if not text:
        return ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = _CONTROL_CHARS.sub(" ", text)
    text = re.sub(r"([A-Za-z])-\n([A-Za-z])", r"\1\2", text)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    out: list[str] = []
    para: list[str] = []
    for line in lines:
        if not line:
            if para:
                out.append(" ".join(para).strip())
                para = []
            out.append("")
            continue
        if _HEADING_RE.match(line) or (len(line) < 60 and line.isupper()):
            if para:
                out.append(" ".join(para).strip())
                para = []
            out.append(line)
            out.append("")
            continue
        if line.endswith((".", "?", "!", ":", ";")) or len(line) < 45:
            para.append(line)
            out.append(" ".join(para).strip())
            para = []
        else:
            para.append(line)
    if para:
        out.append(" ".join(para).strip())
    merged = "\n".join(out)
    merged = re.sub(r"\n{3,}", "\n\n", merged)
    return merged.strip()


def garbled_ratio(text: str) -> float:
    if not text:
        return 1.0
    bad = len(_GARBLED.findall(text))
    alnum = len(_HAS_TEXT.findall(text))
    if not alnum:
        return 1.0
    return bad / max(len(text), 1)


def is_suspicious_text(text: str, *, min_chars: int = 40) -> bool:
    compact = "".join((text or "").split())
    if len(compact) < min_chars:
        return True
    return garbled_ratio(text) > 0.15


class _FontWarningCollector(logging.Handler):
    def __init__(self) -> None:
        super().__init__(level=logging.WARNING)
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover - logging callback
        try:
            message = record.getMessage()
        except Exception:
            return
        low = message.lower()
        if "font" in low or "cff" in low or "glyph" in low:
            self.messages.append(message[:300])


def _get_ocr_engine():  # noqa: ANN202
    global _OCR_ENGINE, _OCR_INIT_FAILED
    if _OCR_ENGINE is not None or _OCR_INIT_FAILED:
        return _OCR_ENGINE
    with _OCR_LOCK:
        if _OCR_ENGINE is not None or _OCR_INIT_FAILED:
            return _OCR_ENGINE
        try:
            for name in ("RapidOCR", "rapidocr"):
                logging.getLogger(name).setLevel(logging.ERROR)
            from rapidocr import RapidOCR  # type: ignore

            _OCR_ENGINE = RapidOCR(params={"Global.log_level": "ERROR"})
        except Exception:  # noqa: BLE001
            _OCR_INIT_FAILED = True
            _OCR_ENGINE = None
    return _OCR_ENGINE


def _render_page_image(raw: bytes, page_index: int, dpi: int):  # noqa: ANN202
    import numpy as np
    import pypdfium2 as pdfium  # type: ignore

    document = pdfium.PdfDocument(raw)
    try:
        page = document[page_index]
        scale = max(1.0, dpi / 72.0)
        # 避免惡意/異常巨大頁面造成記憶體爆量（上限約 1600 萬像素）
        try:
            width_pt, height_pt = page.get_size()
            pixels = (width_pt * scale) * (height_pt * scale)
            max_pixels = 16_000_000
            if pixels > max_pixels:
                scale *= (max_pixels / pixels) ** 0.5
        except Exception:
            pass
        bitmap = page.render(scale=scale)
        image = bitmap.to_pil().convert("RGB")
        return np.asarray(image)
    finally:
        try:
            document.close()
        except Exception:
            pass


def _result_text(result) -> str:  # noqa: ANN001
    texts = getattr(result, "txts", None) or ()
    scores = getattr(result, "scores", None) or ()
    lines: list[str] = []
    for index, text in enumerate(texts):
        value = str(text or "").strip()
        if not value:
            continue
        try:
            score = float(scores[index]) if index < len(scores) else 1.0
        except (TypeError, ValueError):
            score = 1.0
        if score < 0.3:
            continue
        lines.append(value)
    return "\n".join(lines)


def _ocr_embedded_images(page, engine, *, max_images: int = 4, min_pixels: int = 200_000) -> str:  # noqa: ANN001
    """優先辨識 PDF 內嵌的掃描頁影像（原生解析度，通常比整頁渲染清晰）。"""
    try:
        images = list(getattr(page, "images", []) or [])
    except Exception:  # noqa: BLE001
        return ""
    if not images:
        return ""
    try:
        from PIL import Image  # type: ignore
    except Exception:  # noqa: BLE001
        return ""

    ranked = []
    for image_file in images[: max(1, max_images) * 2]:
        try:
            pil = getattr(image_file, "image", None)
            if pil is None:
                data = getattr(image_file, "data", b"")
                if not data:
                    continue
                pil = Image.open(io.BytesIO(data))
            width, height = pil.size
            pixels = int(width) * int(height)
            if pixels < min_pixels:
                continue
            ranked.append((pixels, pil))
        except Exception:  # noqa: BLE001
            continue
    ranked.sort(key=lambda item: item[0], reverse=True)

    lines: list[str] = []
    for _pixels, pil in ranked[:max_images]:
        try:
            import numpy as np

            rgb = pil.convert("RGB")
            result = engine(np.asarray(rgb))
            value = _result_text(result)
        except Exception:  # noqa: BLE001
            continue
        if value:
            lines.append(value)
    return "\n".join(lines)


def ocr_page(raw: bytes, page_index: int, *, dpi: int = 200, page=None) -> str:  # noqa: ANN001
    engine = _get_ocr_engine()
    if engine is None:
        return ""
    if page is not None:
        embedded = _ocr_embedded_images(page, engine)
        if embedded:
            return embedded
    try:
        image = _render_page_image(raw, page_index, dpi)
        result = engine(image)
    except Exception:  # noqa: BLE001
        return ""
    return _result_text(result)


def _page_text(page) -> tuple[str, bool]:  # noqa: ANN001
    try:
        text = page.extract_text() or ""
    except Exception:  # noqa: BLE001
        text = ""
    if is_suspicious_text(text, min_chars=20):
        layout = ""
        try:
            layout = page.extract_text(extraction_mode="layout") or ""
        except (TypeError, ValueError):
            layout = ""
        except Exception:  # noqa: BLE001
            layout = ""
        if layout and (len(layout) > len(text) or is_suspicious_text(text, min_chars=20)):
            if not is_suspicious_text(layout, min_chars=20):
                return layout, True
    return text, False


def extract_pdf_document(
    raw: bytes | bytearray | None,
    *,
    max_length: int = 300000,
    max_pages: int | None = None,
    ocr: bool = True,
    ocr_max_pages: int = 120,
    ocr_max_seconds: float = 600.0,
    ocr_dpi: int = 200,
    ocr_min_chars: int = 40,
) -> PdfExtraction:
    """萃取 PDF 全文。max_pages=None 表示不限制頁數（OCR 另有頁數/時間上限）。"""
    result = PdfExtraction(fonttools=fonttools_available())
    if not raw or PdfReader is None:
        result.note = "unavailable"
        return result

    collector = _FontWarningCollector()
    pypdf_logger = logging.getLogger("pypdf")
    pypdf_logger.addHandler(collector)
    try:
        try:
            reader = PdfReader(io.BytesIO(bytes(raw)))
        except Exception:  # noqa: BLE001
            result.note = "reader_error"
            return result

        if getattr(reader, "is_encrypted", False):
            try:
                reader.decrypt("")
            except Exception:  # noqa: BLE001
                pass

        try:
            pages = list(getattr(reader, "pages", []))
        except Exception:  # noqa: BLE001
            result.note = "pages_error"
            return result

        if max_pages is not None:
            pages = pages[: max(0, max_pages)]

        can_ocr = bool(ocr and ocr_available())
        ocr_budget = max(0, int(ocr_max_pages))
        started = time.monotonic()
        parts: list[str] = []
        total = 0

        for index, page in enumerate(pages):
            warnings_before = len(collector.messages)
            text, used_layout = _page_text(page)
            font_issue = len(collector.messages) > warnings_before
            if used_layout:
                result.layout_pages += 1

            page_note = ""
            needs_ocr = is_suspicious_text(text, min_chars=ocr_min_chars) or (
                font_issue and garbled_ratio(text) > 0.05
            )
            if can_ocr and needs_ocr:
                if ocr_budget and result.ocr_pages >= ocr_budget:
                    page_note = "ocr_skipped_page_limit"
                elif ocr_max_seconds and (time.monotonic() - started) > ocr_max_seconds:
                    page_note = "ocr_skipped_time_limit"
                else:
                    ocr_text = ocr_page(bytes(raw), index, dpi=ocr_dpi, page=page)
                    if ocr_text and len("".join(ocr_text.split())) >= 10:
                        text = ocr_text
                        result.ocr_pages += 1
                        result.ocr_engine = "rapidocr"
                        page_note = "ocr"
                    else:
                        page_note = "ocr_empty"

            cleaned = clean_pdf_text(text)
            result.pages += 1
            result.page_stats.append(
                {
                    "page": index + 1,
                    "chars": len(cleaned),
                    "layout": used_layout,
                    "font_issue": font_issue,
                    "note": page_note,
                }
            )
            if not cleaned:
                continue
            parts.append(f"\n\n[Page {index + 1}]\n{cleaned}")
            total += len(cleaned)
            if max_length and total >= max_length:
                break

        merged = "".join(parts).strip()
        if max_length:
            merged = merged[:max_length]
        result.text = merged
        result.font_warnings = len(collector.messages)
        if can_ocr:
            result.note = "ocr_ready" if result.ocr_pages == 0 else "ocr_used"
        else:
            result.note = "ocr_unavailable" if ocr else "ocr_disabled"
        return result
    finally:
        pypdf_logger.removeHandler(collector)
