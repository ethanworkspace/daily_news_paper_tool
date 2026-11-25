# GitHub 專案 01：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-10-31
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk/Catch 3.0 是一個無監督學習的安全工具，目標是自動從應用程式日誌（如 HTTP 存取記錄）中發掘可能的攻擊痕跡，無需預先定義規則。它主要服務於安全運營中心（SOC）分析師與需要即時威脅偵測的系統管理員，透過聚類與異常點偵測將可疑記錄標記出來，再利用大型語言模型提供深入分析與可執行的建議，協助使用者快速了解與回應潛在入侵。

## 技術
專案主要使用 Ruby 作為倉庫語言，核心偵測引擎以 Python 實作，採用 PCA 降維後以 DBSCAN 密度聚類進行無監督分群，將異常點視為潛在攻擊追蹤。偵測結果送至 Ollama 本地運行的 LLM（如 granite4:latest）與 JEV 模型，採用 Agentic AI 進行深度分析與行動建議。提供 Docker Compose 部署的三個服務：偵測 API、網頁 UI 與 Ollama；以及以 Python 編寫的輕量級 agent，負責讀取端點日誌並經 HTTP POST 傳送至偵測 API。網頁 UI 使用網頁前端技術供分析師檢視與管理事件。

## 架構
系統由四個主要模組組成：(1) Agent：運行在每個監控主機上，讀取指定日誌檔案並透過 HTTP POST 將原始日誌傳送至偵測 API 的 /scan 端點；(2) 偵測 API（Webhawk）：接收日誌後進行數值化編碼，使用 PCA 提取特徵，再以 DBSCAN 進行聚類，將密度低的點標記為異常（潛在攻擊），並將結果寫入資料庫或直接推送至 UI；(3) Ollama 容器：本地運行 LLM 與 JEV 模型，接收偵測 API 的異常紀錄，產生可讀的分析報告與建議；(4) 網頁 UI：提供分析師登入、事件瀏覽、標註與匯出功能，透過 API 取得偵測結果與 LLM 分析內容。所有服務透過 Docker Compose 編排，Agent 僅需能連接到 Docker 主機的 8000 端點即可將日誌送入偵測管線。

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
