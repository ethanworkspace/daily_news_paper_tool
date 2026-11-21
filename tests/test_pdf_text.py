"""P4 PDF 全文/字型/OCR 測試。"""
from __future__ import annotations

import logging
import unittest

import collectors.pdf_text as pdf_text
from collectors.pdf_text import (
    PdfExtraction,
    clean_pdf_text,
    extract_pdf_document,
    garbled_ratio,
    is_suspicious_text,
)


class CleanTextTests(unittest.TestCase):
    def test_dehyphenate_and_headings(self):
        raw = "Abstract\nThis paper stud-\nies maritime AI.\n\n1 Introduction\nWe propose a model."
        text = clean_pdf_text(raw)
        self.assertIn("studies maritime AI", text)
        self.assertIn("1 Introduction", text)

    def test_garbled_ratio(self):
        self.assertGreater(garbled_ratio("\ufffd\ufffd\ufffd"), 0.5)
        self.assertLess(garbled_ratio("Maritime AI model"), 0.01)
        self.assertTrue(is_suspicious_text("", min_chars=10))
        self.assertFalse(is_suspicious_text("A" * 100, min_chars=10))


class FakePage:
    def __init__(self, text: str, *, layout: str | None = None, warn: bool = False) -> None:
        self.text = text
        self.layout = layout
        self.warn = warn

    def extract_text(self, extraction_mode=None):  # noqa: ANN001
        if self.warn:
            logging.getLogger("pypdf._page").warning(
                "fontTools is required to fully parse the encoding of a CFF Type1 font"
            )
        if extraction_mode == "layout" and self.layout is not None:
            return self.layout
        return self.text


class FakeReader:
    pages: list[FakePage] = []

    def __init__(self, _buf) -> None:
        self.pages = list(FakeReader.pages)
        self.is_encrypted = False


class PdfDocumentTests(unittest.TestCase):
    def setUp(self):
        self._orig_reader = pdf_text.PdfReader
        self._orig_ocr_page = pdf_text.ocr_page
        self._orig_available = pdf_text.ocr_available
        pdf_text.PdfReader = FakeReader
        pdf_text.ocr_available = lambda: False
        FakeReader.pages = []

    def tearDown(self):
        pdf_text.PdfReader = self._orig_reader
        pdf_text.ocr_page = self._orig_ocr_page
        pdf_text.ocr_available = self._orig_available

    def test_unlimited_pages_and_font_warning(self):
        FakeReader.pages = [FakePage("Page one text " * 20, warn=(i == 0)) for i in range(30)]
        result = extract_pdf_document(b"%PDF-fake", ocr=False)
        self.assertIsInstance(result, PdfExtraction)
        self.assertEqual(result.pages, 30)
        self.assertIn("[Page 30]", result.text)
        self.assertEqual(result.ocr_pages, 0)
        self.assertEqual(result.font_warnings, 1)

    def test_layout_mode_used_when_plain_is_garbled(self):
        FakeReader.pages = [FakePage("\ufffd" * 200, layout="Layout text " * 30)]
        result = extract_pdf_document(b"%PDF-fake", ocr=False)
        self.assertEqual(result.layout_pages, 1)
        self.assertIn("Layout text", result.text)

    def test_ocr_fallback_for_scanned_page(self):
        FakeReader.pages = [
            FakePage("Normal text " * 40),
            FakePage(""),  # scanned page
        ]
        pdf_text.ocr_available = lambda: True
        calls = []

        def fake_ocr(raw, index, *, dpi=200, page=None):  # noqa: ANN001
            calls.append((index, dpi))
            return "OCR recovered maritime vessel detection results."

        pdf_text.ocr_page = fake_ocr
        result = extract_pdf_document(b"%PDF-fake", ocr=True, ocr_max_pages=5, ocr_dpi=150)
        self.assertEqual(result.ocr_pages, 1)
        self.assertEqual(result.kind, "pdf+ocr")
        self.assertIn("OCR recovered", result.text)
        self.assertEqual(calls, [(1, 150)])

    def test_ocr_page_limit(self):
        FakeReader.pages = [FakePage("") for _ in range(4)]
        pdf_text.ocr_available = lambda: True
        pdf_text.ocr_page = lambda raw, index, *, dpi=200, page=None: "ocr text " * 20
        result = extract_pdf_document(b"%PDF-fake", ocr=True, ocr_max_pages=2)
        self.assertEqual(result.ocr_pages, 2)
        notes = [p["note"] for p in result.page_stats]
        self.assertIn("ocr_skipped_page_limit", notes)

    def test_no_ocr_when_disabled(self):
        FakeReader.pages = [FakePage("")]
        result = extract_pdf_document(b"%PDF-fake", ocr=False)
        self.assertEqual(result.ocr_pages, 0)
        self.assertEqual(result.note, "ocr_disabled")


if __name__ == "__main__":
    unittest.main()
