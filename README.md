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
| **禮拜日** | `海事AI` | `7.海事AI` | 智慧航運、無人船隻自主導航、港口自動化、海洋AI |

> 📌 **雙重存檔機制**：每日產生的 Markdown 日報將**同時**存入對應的主題資料夾，並完整同步儲存至 `8.每日新聞總結` 資料夾。

---

## 📦 資料採集規格 (每份日報包含)

1. **📰 5 篇科技重點新聞**：
   - 支援 Google Custom Search API / 即時 Google News RSS
   - 提取標題、報導連結、來源媒體、時間與原文摘要
   - 由 Furen-large 提供【核心事件】、【產業影響】、【關鍵結論】分析
2. **📄 5 篇前沿學術論文 (arXiv)**：
   - 檢索最新提交的頂級學術論文
   - 提取論文標題、作者群、提交日期、arXiv 網址、PDF 下載連結
   - 由 Furen-large 提供【研究背景與痛點】、【核心方法】、【實證價值】導讀
3. **💻 3 個熱門開源專案 (GitHub)**：
   - 篩選高星數、近期活躍更新的開源倉庫
   - 提取專案名稱、Star 數、語言、主題標籤與描述
   - 由 Furen-large 提供【專案定位】、【關鍵特性】、【推薦場景】評析
4. **💡 今日情報總覽與跨領域洞察**：
   - 融合今日所有採集情報，產出趨勢綜合解讀與未來行動建議

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

---

## ⏰ 自動化排程設定 (每天 08:30 自動執行)

### 方法 A：Windows 工作排程器 (推薦，電腦開機自動在後台跑)
1. 對專案目錄中的 `setup_scheduler.bat` 按右鍵，選擇**「以系統管理員身分執行」**。
2. 系統會自動註冊每日 08:30 的 Windows 工作排程器任務 `DailyAINewsAgent`。
3. 執行記錄會自動追加到 `run.log` 中。

### 方法 B：Python 背景守護程序
若不使用 Windows 工作排程器，也可直接啟動：
```bash
python scheduler.py
```
視窗保持開啟，每當時間到達 08:30 便會自動觸發並生成日報。
