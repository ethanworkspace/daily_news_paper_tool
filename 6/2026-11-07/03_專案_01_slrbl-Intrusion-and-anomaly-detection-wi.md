# GitHub 專案 01：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-07
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督機器學習工具，專門從應用程式日誌（如 HTTP 存取記錄）中自動偵測攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 PCA 提取關鍵欄位，再以 DBSCAN 群聚演算法將日誌條目分群並標記離群點作為可疑攻擊。偵測結果會送至使用者選擇的 LLM（透過 Ollama）進行深度分析並產出具體建議，同時提供網頁介面與 API 供安全運營中心（SOC）團隊檢視、管理及與既有 SIEM 整合。適合需要自動化威脅偵測與事件分析的安全分析師與運維人員。

## 技術
Webhawk 的核心實作以 Python 為主，使用 scikit-learn 提供 PCA 與 DBSCAN 演算法進行無監督特徵降維與聚類；日誌先經過數值編碼（如使用者代理、IP、參數數量）後送入這些模型。偵測完成後，結果會透過 HTTP API 傳送至 Ollama 容器內的 LLM（預設 granite4:latest）與 JEV 模型（tev1:0.8b）進行代理人工智慧（Agentic AI）分析，產出可讀的事件說明與建議。網頁介面與 API 透過 Docker Compose 組織為三個服務：偵測引擎（Webhawk API）、Ollama 模型服務與 Web 應用程式。Agent 以 Python 腳本運行於各端點，讀取本地日誌並 POST 至偵測 API。整個流程依賴 Docker、Docker Compose 與 Python 3。

## 架構
Webhawk 架構由四個主要部分組成：(1) 偵測引擎（Webhawk API），負責接收來自 Agent 的原始日誌，執行數值編碼、PCA 特徵提取與 DBSCAN 聚類，將離群點標記為事件並寫入資料庫；(2) Ollama 服務，運行選定的 LLM（granite4:latest）與 JEV 模型（tev1:0.8b），接收偵測引擎傳送的事件摘要，執行 Agentic AI 分析後回傳建議；(3) 網頁應用程式（Webhawk UI），提供登入、事件瀏覽、過濾與手動標註介面，同時接受偵測引擎寫入的事件；(4) 日誌 Agent，部署於每台產生日誌的主機，讀取本地檔案（如 Apache access log）並透過 HTTP POST 將資料送至偵測引擎的 /scan 端點。資料流程為：Agent → 偵測 API → 特徵處理與聚類 → 事件產出 → UI 儲存 → Ollama LLM/JEV 分析 → 分析結果回到 UI。所有服務透過 Docker Compose 組態啟動，偵測 API 監聽 8000、UI 監聽 8080、Ollama 監聽 11434。Agent 需能連線至 Docker 主機的 8000 端口。

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
