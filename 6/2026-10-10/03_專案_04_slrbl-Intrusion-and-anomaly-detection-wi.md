# GitHub 專案 04：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-10-10
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk 是一個無監督學習結合 AI 增強的應用程式日誌攻擊偵測工具，目標使用者為 SOC 分析師、資安工程師與 DevOps 團隊。它透過將原始日誌轉換為數值特徵、使用 PCA 降維及 DBSCAN 聚類來自動發現異常點，進而利用 LLM 與 agentic AI 提供深度分析與可執行的建議，並提供網頁介面與 API 方便將偵測結果導入現有的 SIEM 或安全工作流程。

## 技術
專案主要使用 Ruby 作為倉庫語言，偵測引擎以 Python 實作，依賴 scikit-learn 的 PCA 與 DBSCAN 進行特徵提取與聚類；異常點會被送至 Ollama 服務上的 LLM（granite4:latest 與 tev1:0.8b）進行分析，採用 agentic AI 模式產出可操作的建議；網頁介面與 API 同樣以 Ruby 構建，透過 Docker Compose 部署三個核心服務：偵測 API、Ollama 與 Web UI；端點上的 agent 則是 Python 腳本，負責讀取日誌並經由 HTTP POST 將資料傳送至偵測 API。

## 架構
系統架構由四個主要模組組成：(1) 偵測引擎 API（Webhawk）負責接收日誌、執行 PCA 特徵轉換、使用 DBSCAN 進行聚類並標記離群點；(2) Ollama 容器運行選定的 LLM 與 JEV 模型，提供深度語言分析；(3) Web 應用程式提供分析師介面，顯示事件、允許手動標註與匯出；(4) 部署於每台主機的 agent 讀取本地日誌檔並透過 HTTP 發送至偵測 API。資料流程為：端點 → agent → 偵測 API (PCA → DBSCAN) → 離群點 → Ollama LLM 分析 → 結果寫入資料庫 → Web UI 呈現，同時可經由 API 轉發至外部 SIEM。所有服務透過 Docker Compose 啟動，偵測 API 監聽 8000、Web UI 監聽 8080、Ollama 監聽 11434。

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
