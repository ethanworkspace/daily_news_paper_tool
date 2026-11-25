# 🤖 每日 AI 科技新聞匯報 Agent (Daily AI News Agent)

自動化每日 AI 情報管線：爬取新聞、論文與 GitHub 專案，透過**高科 iAI**（`Furen-max` / `Furen-large` / `Furen-coder` / `Pic-large`）產出深度分析、技術架構拆解與每日匯報，並自動 commit / push 到 GitHub。

---

## 📁 輸出結構

```
1/ .. 7/<YYYY-MM-DD>/                  # 依星期對應的主題目錄
├── 01_新聞_10篇.md                    # 10 則新聞（含 AI 深度解說）
├── 02_論文_01..05_<slug>.md           # 5 篇論文深度導讀
├── 03_專案_01..05_<slug>.md           # 5 個開源專案深度評析
├── 04_AI技術架構_深度拆解.md          # 技術架構深度拆解（五個章節）
└── assets/04_architecture.png         # Pic-large 生成的架構示意圖

每日匯報/<YYYY-MM-DD>_每日匯報.md      # 逐條摘要新聞/論文/專案/技術
.system_generated/runs/<date>/*.json   # 每次執行的 manifest（來源真相）
.system_generated/logs/*.json          # 執行日誌與警告
```

| 星期 | 目錄 | 主題 |
| :--- | :--- | :--- |
| 一 | `1/` | LLM、RAG、Fine-tuning |
| 二 | `2/` | 機器學習、AI 資訊安全 |
| 三 | `3/` | 深度學習 |
| 四 | `4/` | AI Agent |
| 五 | `5/` | 智慧機器人、具身智能 |
| 六 | `6/` | AI 硬體應用、AI 自動化 |
| 日 | `7/` | 海事 AI、醫療 AI |

---

## 📦 每日產出規格

1. **📰 10 則新聞**：AI 核心為主，至少 3 則跨領域（海事／資安／醫療／電子／機器人／具身智能），海事每日至少 1 則；新聞年齡 ≤ 14 天，可使用國外來源，抓取全文而非僅 metadata。
2. **📄 5 篇論文**：優先頂級會議/期刊，arXiv 為補充；擴充免費合法全文來源，解析無頁數上限的 PDF 並支援 OCR/字型解析；標註 IF／影響力與 Venue 層級；深度拆解包含「背景與目的／方法／結果／限制與展望」，方法忠於原文。
3. **💻 5 個專案**：深度說明「在做什麼／技術／架構」；配對為加分項而非必要配額。挑選優先序為：**期刊/頂會論文且有 GitHub 專案 > 期刊/頂會論文 > 論文且有 GitHub 專案 > 論文 > GitHub 專案**；無法配對者明確標註，絕不偽造；排除 Awesome／survey／paper-list 等低資訊量 repo。
4. **🏗️ 1 篇技術架構深度拆解**：固定五章節（架構原理與核心機制／海事應用／醫療應用／其他產業應用／限制風險與治理建議），含 Pic-large 生成示意圖與真實案例。
5. **📋 每日匯報**：每則新聞、論文、專案與技術項目均有簡要摘要，不只是連結。

所有輸出均為**繁體中文**，模型輸出會經過保守的簡→繁正常化守衛。

---

## ⚙️ 環境變數（僅存於 Windows 使用者環境，不得寫入程式或檔案）

| 變數 | 用途 |
| :--- | :--- |
| `IAI_API_KEYS` | iAI 金鑰池（逗號分隔）；舊 `IAI_API_KEY` 在設定此變數時忽略 |
| `IAI_MODEL_MAX` / `IAI_MODEL_LARGE` / `IAI_MODEL_CODER` / `IAI_MODEL_IMAGE` | 模型名稱（`Furen-max` / `Furen-large` / `Furen-coder` / `Pic-large`） |
| `IAI_BASE_URL` | `https://www.iai.nkust.edu.tw/aihub/v1` |
| `GITHUB_TOKEN` | 選填，提升 GitHub 搜尋配額；僅於命令環境暫時使用 |

金鑰一律由 `get_secure_env()` 讀取，日誌與錯誤訊息會遮罩；支援 429/5xx/timeout 重試、金鑰輪替與**額度耗盡熔斷**（`ExceededBudget` 出現時停止重試）。

---

## 🚀 使用方式

```bash
pip install -r requirements.txt

python main.py                                   # 今日報表
python main.py --test                            # 連線驗證（少量抓取）
python main.py --weekday 3                       # 指定星期主題（0=一）
python main.py --no-push                         # 不自動推送

python main.py --backfill-from 2026-09-12 --backfill-to 2026-11-21 --allow-stale --force
```

`--allow-stale` 放寬歷史回補的新鮮度下限，但**仍拒絕任何晚於報告日的資料**；manifest 與警告會標記 `stale_backfill=true`。回補新聞改用 Google News RSS 的 `after:/before:` 日期限定查詢，最多回溯 14 天（比照既有 `news_collector.py` 的公開 RSS 端點處理），論文/專案來源也加上日期窗口；GitHub 401/403 或種子抓取失敗會以 `seed_repo_fetch_failed`／`quota_shortfall` 警告記錄，不偽造配對或專案。

---

## ⏰ 自動化排程

- `setup_scheduler.bat`：以系統管理員註冊每日 08:30 的 `DailyAINewsAgent` 工作，支援登入補跑與錯過補跑。
- `python scheduler.py`：Python 背景守護程序，同樣每日 08:30 觸發。

---

## ⚠️ 已知限制（歷史回補）

- 回補模式已改用日期限定區間抓取，並在收集與 `DailyBundle.validate()` 兩層阻擋未來資料；既有 71 天舊版輸出若仍含未來日期，需以 `--allow-stale --force` 重跑才能清除。
- GitHub _search/種子抓取可能受 401/403 或速率限制影響，導致專案數不足 5；此類情形會以 `seed_repo_fetch_failed`／`quota_shortfall` 警告記錄，不偽造資料。論文↔專案配對數僅供參考，不足不再視為警告或失敗。
- `2026-11-20` 有一次模型重試失敗後成功（`model_usage.errors=1`、`errors=[]`），屬已回收事件；最終驗收僅將未回收的 pipeline 錯誤視為失敗。

---

## ✅ 驗證

```bash
python -m unittest discover -s tests
```

每次執行的 manifest 會記錄檔案清單、配額、配對數、模型用量與警告，可做逐日結構與內容驗收。舊版 `1.LLM...`～`8.每日新聞總結` 結構已封存於 `legacy_archive/`，不再使用。
