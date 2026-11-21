# P4：PDF 全文、字型解析與 OCR

本文件記錄論文全文解析能力（pypdf + fontTools + RapidOCR）的設計、設定、驗收證據與限制。

## 目標

1. 論文全文解析**不限頁數**，不再只取摘要。
2. 正確處理 PDF 字型/CFF 編碼，降低亂碼。
3. 掃描型 PDF（整頁圖片）以 OCR 補救，仍能取得正文。
4. 對外仍以期刊/頂會（venue/journal）標示論文來源。

## 架構

```
paper_sources.enrich_fulltext()
  ├─ HTML 全文（arXiv HTML / PMC / landing page）
  ├─ PDF 全文（paper.pdf_url / arXiv PDF / landing 內 PDF）
  │    └─ collectors.pdf_text.extract_pdf_document()
  │         ├─ pypdf 逐頁 extract_text()（預設不限頁數）
  │         │    └─ fontTools：CFF/Type1 字型編碼解碼（pypdf 自動使用）
  │         ├─ 文字可疑時改用 layout 模式（保留欄位/順序）
  │         ├─ 每頁品質判斷（字元數、U+FFFD/私用區比例、字型警告）
  │         └─ 可疑頁 → pypdfium2 渲染 → RapidOCR（ONNX）辨識
  └─ 失敗才回退 abstract（parse_level=abstract）
```

### 套件與選型

| 套件 | 用途 | 說明 |
| :--- | :--- | :--- |
| `pypdf>=5.0.0` | PDF 文字層萃取 | 既有依賴；逐頁、可選 layout 模式 |
| `fonttools>=4.50` | 字型解析 | 讓 pypdf 正確解碼 CFF/Type1 編碼，消除「fontTools is required」警告 |
| `pypdfium2>=4.30` | PDF 頁面渲染 | PDFium 綁定，將掃描頁輸出為影像 |
| `onnxruntime>=1.20` | OCR 推論 | RapidOCR 的執行引擎 |
| `rapidocr>=3.0` | OCR | PP-OCR 模型隨套件提供，免系統安裝 Tesseract；支援 Python 3.14 |

> 注意：`rapidocr-onnxruntime` 舊套件限制 Python <3.13，本專案使用 Python 3.14，因此採用新版 `rapidocr`（同樣以 ONNX Runtime 執行）。

## 行為細節

### 1. 不限頁數

- `extract_pdf_document(max_pages=None)` 預設讀取全部頁面。
- `PAPER_FULLTEXT_MAX_CHARS` 預設 300,000 字元，避免極端檔案佔用記憶體；一般論文（20–40 頁）可完整保留。
- 每頁輸出加上 `[Page N]` 標記，便於後續章節定位與引用。

### 2. 字型解析

- 安裝 `fonttools` 後，pypdf 會用 fontTools 解析 CFF/Type1 字型編碼。
- 模組會捕捉 pypdf 的 font/glyph 相關警告：
  - `PdfExtraction.font_warnings`：警告數量。
  - 每頁 `page_stats[].font_issue`：該頁是否出現字型警告。
- 若某頁有字型警告且文字品質不佳（U+FFFD/私用區比例 >5%），會觸發 OCR 補救。

### 3. OCR 觸發條件

單頁符合任一條件即視為可疑頁：

- 有效字元少於 `PAPER_OCR_MIN_CHARS`（預設 40）。
- 亂碼比例（U+FFFD、私用區字元）超過 15%。
- 有字型警告且亂碼比例超過 5%。

OCR 流程：

1. 先嘗試辨識 PDF 內嵌的掃描頁影像（原生解析度，通常比整頁渲染清晰）。
2. 若無可用內嵌影像，`pypdfium2` 以 `PAPER_OCR_DPI`（預設 200 DPI）渲染該頁。
3. `RapidOCR` 辨識，丟棄信心度 <0.3 的片段。
4. 以換行組合成該頁文字，並記錄 `ocr_pages`。

保護機制：

- `PAPER_OCR_MAX_PAGES`（預設 120，`0` = 不限）避免整本掃描書耗時過久。
- `PAPER_OCR_MAX_SECONDS`（預設 600 秒）總時間預算；超過後跳過 OCR 並在 `page_stats[].note` 標記 `ocr_skipped_time_limit`。
- `PAPER_OCR_ENABLED=false` 可完全停用 OCR；缺少套件時自動降級，不影響文字型 PDF。

### 4. 輸出欄位

`PaperItem` / smoke 報告新增：

| 欄位 | 說明 |
| :--- | :--- |
| `fulltext_kind` | `pdf`、`pdf+ocr`、`html`、`abstract` |
| `fulltext_source` | 實際取得全文的 URL |
| `fulltext_pages` | PDF 頁數（HTML 為 0） |
| `ocr_pages` | 實際 OCR 的頁數 |
| `parse_level` | `fulltext` / `abstract` / `metadata` |

## 設定（環境變數）

| 變數 | 預設 | 說明 |
| :--- | :--- | :--- |
| `PAPER_FULLTEXT_MAX_CHARS` | `300000` | 全文保留字元上限 |
| `PAPER_MAX_BYTES` | `20971520` | 單一 PDF 下載上限（20 MB） |
| `PAPER_OCR_ENABLED` | `true` | 啟用掃描頁 OCR |
| `PAPER_OCR_MAX_PAGES` | `120` | OCR 頁數上限，`0` = 不限 |
| `PAPER_OCR_MAX_SECONDS` | `600` | OCR 總時間預算（秒） |
| `PAPER_OCR_DPI` | `200` | 渲染解析度 |
| `PAPER_OCR_MIN_CHARS` | `40` | 每頁視為掃描頁的字元門檻 |

## 驗收證據（2026-11-21）

### 單元測試

```text
python -m unittest discover -s tests
Ran 200 tests ... OK
```

- 新增 `tests/test_pdf_text.py`：不限頁數、layout 模式、字型警告、OCR 觸發、OCR 頁數上限、OCR 停用。
- 既有 `tests/test_paper_parse.py` 改為驗證 45 頁 PDF 仍完整輸出（含 `[Page 45]`）。

### 實際論文（Paper smoke）

```text
python scripts/paper_smoke.py --count 5
```

- 5/5 `parse_level=fulltext`。
- 全文長度 98,017–149,423 字元。
- Nature Machine Intelligence 論文：`fulltext_kind=pdf+ocr`、`fulltext_pages=30`、`ocr_pages=3`、127,010 字元。
- 期刊/頂會標示：ACM TOSEM、Nature Machine Intelligence、SIAM Journal on Scientific Computing、SIAM Review。
- 無 `enrich_error`。

### 掃描型 PDF（合成測試）

以 3 頁純圖片 PDF 驗證：

```text
pages=3, ocr_pages=3, kind=pdf+ocr, font_warnings=0
```

OCR 成功還原「autonomous vessel detection」「multimodal learning」「94.2 percent accuracy」等內容。

### 安全與依賴

```text
python scripts/secret_scan.py      # 無疑似金鑰
python -m pip_audit -r requirements.txt  # No known vulnerabilities found
```

- 所有下載仍經 `SafeHttpFetcher`（SSRF/重新導向/大小/robots 檢查）。
- PDF 下載上限 20 MB；OCR 渲染另有約 1,600 萬像素上限，避免異常巨大頁面造成記憶體爆量。
- OCR 模型為本機推論，不上傳論文內容。
- 不記錄 API 金鑰；PDF/OCR 統計只寫入報告。

## 已知限制

- OCR 對數學公式、表格、雙欄版面與特殊符號仍可能失真；必要時可再比較 pypdf 文字層與 OCR 結果（目前取可用者）。
- 掃描頁 OCR 速度取決於 CPU；已用頁數與時間預算控制成本。
- 若出版社阻擋 PDF（403）且無 arXiv/PMC 全文，仍只能落到 abstract。
- `pypdfium2`/`rapidocr`/`onnxruntime` 需對應平台 wheel；目前已驗證 Windows + Python 3.14。
