# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-19
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督學習結合 AI 增強的應用程式日誌入侵偵測工具，目標使用者為資安運營中心（SOC）分析師與安全工程師。它不依賴預先定義的規則，而是將原始日誌轉換為數值特徵，利用主成分分析（PCA）降維後，以 DBSCAN 密度基礎聚類演算法將日誌條目分群並標記異常點作為潛在攻擊痕跡。偵測結果會送至使用者選擇的大型語言模型（LLM）進行深度分析，產出可執行的建議與事件摘要，最後透過網頁介面或 API 提供給現有的 SIEM 系統。

## 技術
專案主要使用 Ruby 作為倉庫語言，但核心偵測腳本（catch.py、api_test.py）與端點代理均以 Python 3 實作。特徵抽取階段採用 scikit-learn 的 Principal Component Analysis (PCA)，聚類則使用 DBSCAN 演算法。偵測後的異常日誌會經由 REST API 傳送至本地 Ollama 服務，呼叫使用者自行選擇的 LLM（例如 granite4:latest）進行自然語言分析與建議生成。整體透過 Docker Compose 部署三個主要服務：偵測引擎（Webhawk API）、網頁應用程式（Webhawk UI）與 Ollama 模型服務，端點代理則需在每台主機上安裝 Python 依賴並透過 HTTP 將日誌上傳至偵測 API。

## 架構
系統架構由四個主要組件構成：(1) 偵測引擎（Webhawk API）負責接收日誌、執行 PCA 特徵轉換、DBSCAN 聚類與異常點辨識，然後將結果 POST 至網頁 UI 或供外部 SIEM 消費；(2) 網頁應用程式（Webhawk UI）提供分析師帳號管理、事件瀏覽與手動標註介面，運行在 port 8080；(3) Ollama 服務運行於 port 11434，負責載使用者指定的 LLM 與 JEV 模型，提供離線推論能力；(4) 端點代理（Webhawk Agent）部署於每台產生日誌的主機，讀取指定日誌檔案（如 Apache access log）並透過 HTTP POST 將內容送至偵測 API 的 /scan 端點。資料流程為：端點代理 → 偵測 API（PCA → DBSCAN → 異常偵測） → Ollama LLM 分析 → 結果存儲 → Webhawk UI 顯示。所有服務可透過 docker-compose.yml 一鍵啟動，偵測 API 監聽 8000，UI 監聽 8080，Ollama 監聽 11434。

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
