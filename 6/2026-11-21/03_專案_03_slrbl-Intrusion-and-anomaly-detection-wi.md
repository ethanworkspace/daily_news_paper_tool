# GitHub 專案 03：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-21
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督機器學習工具，專門從應用程式日誌（如 HTTP 存取記錄）中自動發掘攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 進行密度聚類，將異常點標記為可能的攻擊痕跡。接著透過使用者可選擇的 LLM（例如 Ollama 上的 granite4 或 tev1）進行 Agentic AI 分析，給出詳細說明與可執行的建議。提供網頁介面讓 SOC 團隊檢視與管理事件，並內建 API 可將結果導入現有的 SIEM 生態系統。同時附帶輕量級 agent，可部署於各端點收集日誌並經由 API 傳送至偵測引擎。整體以 Docker Compose 打包，降低部署複雜度，適用於需要快速偵測未知威脅的安全分析師與雲端運維人員。

## 技術
專案主要使用 Python 3 實作端點 agent 與偵測引擎（包括 catch.py、api_test.py 等腳本），依賴 scikit-learn 提供 PCA 與 DBSCAN 進行無監督特徵降維與密度聚類。LLM 分析透過 Ollama 服務呼叫，支援使用者自行指定模型（如 granite4:latest、tev1:0.8b）。Web 應用程式提供介面供分析師檢視事件，並透過內建 REST API 接收偵測結果與向外部 SIEM 傳送資料。所有服務以 Docker Compose 整合，包含 detection API、Ollama 容器與 Web UI 三個主要容器，透過 settings.conf 檔案調整聚類參數與模型名稱。

## 架構
系統由四個主要模組組成：(1) Agent：部署於被監視端點，讀取本地日誌檔案並透過 HTTP POST 將原始日誌傳送至 detection API 的 /scan 端點。(2) Detection API：接收日誌後執行前處理（特徵編碼），使用 PCA 降維，再以 DBSCAN 進行聚類，將距離簇中心過遠的點標記為異常（潛在攻擊痕跡），然後將這些異常記錄發送至配置的 LLM 服務進行 Agentic AI 分析，取得說明與建議。(3) Ollama 服務：運行使用者選定的 LLM（如 granite4）與輔助模型（tev1），負責產生分析結果。(4) Webhawk Web Application：提供介面於 http://localhost:8080，讓分析師登入、檢視事件詳情、手動標記或匯出結果，同時提供 API 端點將事件資料推送至外部 SIEM。三個核心容器（detection API、Ollama、Web UI）透過 Docker Compose 啟動，agent 則為獨立的 Python 程式，需能連線至 Docker 主機的 8000 端口。資料流程為：端點日誌 → Agent → Detection API (特徵→PCA→DBSCAN) → 異常 → Ollama LLM 分析 → 結果寫入 Web UI 並可經 API 轉發至 SIEM。若需更細緻的叢流或非同步處理，專案提及未來可考慮使用 Kafka 進行資料脫鉤，但目前實作仍採用同步 HTTP 傳輸。

## README 摘錄（節選）
```text
# Webhawk/Catch 3.0
Unsupervised, AI-augmented detection of attacks in application logs.
Presented at Black Hat Arsenal USA 2023 (docs/blackhat/BHUS23-PPT-Arsenal-Slide-Webhawk-WD_v3.pdf), Black Hat Arsenal USA 2025, and DEF CON Labs Bahrain 2025.
Author: Walid Daboubi (https://github.com/slrbl)
## Abstract
Webhawk is an ML/AI powered detection tool designed to automatically identify attack traces in application logs (Eg: HTTP) without relying on preset rules. Using unsupervised machine learning, Webhawk groups log entries into clusters and detects outliers that may indicate potential attack traces. After detection, Webhawk leverages Agentic AI to provide detailed analysis and actionable recommendations.
Webhawk comes with a user-friendly web interface. Webhawk UI allows SOC team members to easily manage and review the detections. Detection results can also be fed to your existing SOC ecosystem (Eg: SIEM) thanks to the builtin API.
## Technical details
Webhawk transforms raw logs into numerical data and applies Principal Component Analysis (PCA) to extract the most relevant features (such as user-agent, IP address, and the number of transmitted parameters). It then uses the DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm to cluster log lines and identify anomalous points, which may represent potential attack traces.
Advanced users can fine-tune Webhawk through a set of configuration options that optimize the clustering algorithm—for example, by adjusting the minimum number of points per cluster or the maximum distance between points within the same cluster.
Once detections are complete, the results are sent to an LLM of your choice for in-depth analysis and actionable recommendations. Webhawk leverages agentic AI design patterns to ensure that the insights and suggestions delivered to users provide meaningful, real-world value.
To get data from your endpoints, Webhawk provide an agent that your can easily deploy on every endpoint. Once launched, this agent gets logs from the concerned file and transmit them to the detection engine via the API.
The tool is easy to deploy using Docker Compose, which simplifies the installation of the three main components: the detection engine, the web application, and the LLM services.
## Production setup
Production runs three Docker services on one server, plus an agent on each machine that holds logs. The detection API receives logs, Ollama runs the models, and the web application is where analysts review incidents.
Docker and Docker Compose are required on the server. Python 3 is required on each endpoint that runs the agent.
### Configure the detection engine
Create the configuration before the first build. The image copies `webhawk/` at build time, so a file created later is not included until you build again.
[code block omitted]
The template is already set for Docker Compose:
- `[LLM]` and `[JEV]` call Ollama at `http://ollama:11434`
- `[WEBAPP]` posts incidents to `http://webhawk_ui:8080/api/v1/incidents`
- `[LLM]` `model` is `granite4:latest`
- `[JEV]` `jev` is `tev1:0.8b`
`ollama_starter.sh` pulls those two models when the Ollama container starts. If you choose another analysis model, put the same name in `webhawk/settings.conf` and in `ollama_starter.sh`.
### Start the services
From the repository root:
[code block omitted]
The services listen on:
- analyst UI: `http://localhost:8080`
- detection API: `http://localhost:8000`
- Ollama: `http://localhost:11434`
The first start downloads `granite4:latest` and `tev1:0.8b`. Wait until the Ollama logs list both models and the UI is accepting connections before you send logs.
#### Webhawk
The detection API. It accepts an Apache access log and writes the incidents to the UI.
#### Ollama
Runs the analysis model and the JEV model.
#### Webhawk web application
The UI where analysts review incidents.
### Open the analyst UI
Open `http://localhost:8080` and create an account. The application has no default user.
###
```
