# 🤖 每日 AI 科技新聞匯報 Agent (Daily AI News Agent)

專為 AI 從業人員與研究者設計的自動化情報 Agent。每日自動爬取新聞、論文與熱門 GitHub 專案，並透過**高科大 iAI (Furen-large)** 模型進行深度智慧解說、趨勢洞察，並自動歸檔至主題資料夾與每日總結。

---

## 🗓️ 每日爬取主題規劃

Agent 每日會依據星期自動鎖定專屬領域進行深度採集：

| 星期 | 主題名稱 | 歸檔資料夾 | 涵蓋重點 |
| :--- | :--- | :--- | :--- |
| **禮拜一** | `LLM、RAG、Fine tune` | `1.LLM、RAG、Fine tune` | 大語言模型、檢索增強生成、模型微調 |
| **禮拜二** | `機器學習` | `2.機器學習` | 經典機器學習、統計學習理論、前沿演算法 |
| **禮拜三** | `深度學習` | `3.深度學習` | 神經網路架構、電腦視覺 (CV)、自然語言處理 |
| **禮拜四** | `ai agent` | `4.ai agent` | 智慧代理、自主代理、多代理協作系統 (Multi-Agent) |
| **禮拜五** | `智慧機器人` | `5.智慧機器人` | 具身智能 (Embodied AI)、機器人運動學、感測融合 |
| **禮拜六** | `AI硬體應用、AI自動化` | `6.AI硬體應用、AI自動化` | AI 晶片 (NPU/GPU/ASIC)、邊緣運算、工業自動化 |
| **禮拜日** | `海事AI、醫療AI` | `7.海事AI、醫療AI` | 智慧航運、無人船隻自主導航、港口自動化、AI 輔助醫療診斷、醫學影像 |

> 📌 **雙檔存放機制**：每日產生兩份 Markdown — **完整詳細日報**（含每篇新聞/論文/專案的 AI 深度解說）存入對應的主題資料夾；**「今日匯報總結」**（分別以 AI 總結新聞、論文、專案，再附重點清單）存入 `8.每日新聞總結` 資料夾。每日還會**自動 commit 並推送至 GitHub**。

---

## 📦 資料採集規格 (每份日報包含)

1. **📰 5 篇科技重點新聞**：
   - 支援 Google Custom Search API / 即時 Google News RSS
   - 提取標題、報導連結、來源媒體、時間與原文摘要
   - 由 Furen-large 提供【事件詳細解說】【技術與產業意義】【總結】完整分析
2. **📄 5 篇前沿學術論文 (多來源，優先挑選附帶 GitHub 程式碼專案的論文)**：
   - 依序從多個學術管道收集並去重：**arXiv**（官方 API/RSS，優先含 GitHub 專案連結）→ **Google Scholar**（被 Google 阻擋時自動跳過）→ **Semantic Scholar API** → **OpenAlex API** → **PubMed**（醫療/生醫主題尤佳）
   - 提取論文標題、作者群、發布年份、原文網址、PDF 下載連結、期刊/資料庫來源與 GitHub 專案
   - 由 Furen-large 深度導讀：【這篇在做什麼】【研究目的】【架構設計】【核心方法】【實驗結果】【總結】
3. **💻 5 個熱門開源專案 (GitHub)**：
   - 篩選高星數、近期活躍更新的開源倉庫
   - 由 Furen-large 詳細評析：【在做什麼】【架構】【方法】【結果】【總結】
4. **💡 今日情報總覽與跨領域洞察**：
   - 融合今日所有採集情報，產出趨勢綜合解讀與未來行動建議
5. **📋 今日匯報總結**：
   - 先由 AI **分別對新聞、論文、專案撰寫總結**，再附上各類別的重點清單，存放於 `8.每日新聞總結`

---

## 🚀 快速開始

### 1. 安裝環境依賴

```bash
pip install -r requirements.txt
```

### 2. 環境變數設定 (`.env` 或 系統環境變數)

建議於系統環境變數或專案 `.env` 中設定（程式碼絕不硬編碼任何金鑰）：
```env
# 高科 iAI 設定
IAI_API_KEY=your_iai_api_key_here
IAI_BASE_URL=https://www.iai.nkust.edu.tw/aihub/v1
IAI_MODEL=Furen-large

# Google API 設定 (選填：若無設定 CX 則自動切換至 Google News RSS)
GOOGLE_CSE_API_KEY=your_google_api_key_here
GOOGLE_CSE_CX=

# GitHub API 設定 (選填：填入可提升每分鐘搜尋次數)
GITHUB_TOKEN=your_github_token_here

# Semantic Scholar API 設定 (選填：若無金鑰則易觸發共用額度 429；有金鑰更穩定)
SEMANTIC_SCHOLAR_API_KEY=your_semantic_scholar_key_here
```

### 3. 手動執行

- **執行今日主題匯報**：
  ```bash
  python main.py
  ```

- **快速測試模式** (各抓取 1 筆進行連線驗證)：
  ```bash
  python main.py --test
  ```

- **手動指定星期幾的主題** (0=禮拜一, 1=禮拜二, ..., 6=禮拜日)：
  ```bash
  # 例如測試「禮拜四：ai agent」主題：
  python main.py --weekday 3
  ```

- **不推送 GitHub**（例如只想本地生成，不自動上傳）：
  ```bash
  python main.py --no-push
  ```

---

## 🚀 每日自動推送到 GitHub

生成日報後，Agent 會自動執行 `git add`（僅今日生成的 2 份 markdown）→ `git commit` → `git push origin HEAD:main`，將新聞日報備份至 GitHub。

**認證方式（由安全到備援）**：
1. **優先使用 Git Credential Manager**：若本機已登入 GitHub 並儲存憑證，直接 `git push` 即可，token 不會出現在任何檔案中。
2. **備援使用 `GITHUB_TOKEN`**：若 GCM 無憑證，Agent 會從系統環境變數/登錄檔讀取 `GITHUB_TOKEN`，以暫存 credential helper 完成推送後立即刪除暫存檔，**token 不會寫入程式碼、設定檔或指令列**。

> ⚠️ 請將 `GITHUB_TOKEN` 設定於**系統環境變數**（或 `.env`），勿將其寫入任何會被 git 追蹤的檔案。`.env` 與 `*.log` 已列入 `.gitignore`。

---

## ⏰ 自動化排程設定 (每天 08:30 自動執行)

### 方法 A：Windows 工作排程器 (推薦，電腦開機自動在後台跑)
1. 對專案目錄中的 `setup_scheduler.bat` 按右鍵，選擇**「以系統管理員身分執行」**。
2. 系統會註冊每日 08:30 的 `DailyAINewsAgent` 任務，並支援：
   - **每次登入自動補檢查**：今日若尚未執行會立即補跑
   - **睡著錯過 08:30**：喚醒後自動補跑
   - 內建**每日僅執行一次**護衛，避免重複觸發浪費 API
3. 執行記錄會自動追加到 `run.log` 中。

### 方法 B：Python 背景守護程序 (支援錯過時間自動補跑)
若不使用 Windows 工作排程器，也可直接啟動：
```bash
python scheduler.py
```
視窗保持開啟，每當時間到達 08:30 便會自動觸發並生成日報；若開機晚於 08:30 且今日尚未執行，也會立即補跑。
