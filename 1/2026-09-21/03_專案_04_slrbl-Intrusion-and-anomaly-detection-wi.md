# GitHub 專案 04：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-09-21
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk 是一個無監督學習結合 AI 增強的應用程式日誌入侵偵測工具，目標使用者為 SOC 分析師、資安工程師與 DevOps 團隊。它透過 PCA 特徵提取與 DBSCAN 聚類自動發現異常記錄，再利用選擇的 LLM（如 granite4:latest）進行深度分析並給出可執行建議，提供網頁介面與 API 以便將偵測結果匯入既有的 SIEM 或工作流程。該工具不依賴預先定義的規則，適合處理 HTTP、應用程式及作業系統程序日誌，可透過 Docker Compose 快速部署，並提供代理程式在各端點收集日誌送至偵測引擎。

## 技術
技術重點包括：使用 Python 的 catch.py 進行日誌前處理，套用 Principal Component Analysis (PCA) 提取特徵（如 User‑Agent、IP、參數數量），再以 DBSCAN 演算法進行密度基礎聚類與異常點偵測；偵測結果傳送至 Ollama 運行的 LLM（預設 granite4:latest 與 tev1:0.8b）進行 Agentic AI 分析與建議生成；透過 Docker Compose 啟動三項服務（偵測引擎 API、Ollama、Web 應用程式），並提供 Python 實作的 agent 在各端點讀取日誌並 POST 至 /scan 端點；網頁介面則以 Ruby 開發（專案主要語言）提供事件檢視與帳號管理。

## 架構
架構由三個 Docker 服務與端點代理組成：(1) 偵測引擎 API（Webhawk）接收經 agent 傳送的原始日誌，內部執行 PCA 特徵轉換與 DBSCAN 聚類，將異常點標記為事件；(2) Ollama 容器載入設定的 LLM 與 JEV 模型，負責對事件進行深度語言分析並產出可執行建議；(3) Web 應用程式提供分析師介面於 http://localhost:8080，顯示事件與 LLM 分析結果，並支援建立帳號。代理程式安裝於每台需要監視的主機，讀取指定日誌檔（如 Apache access log）並透過 HTTP POST 將資料送至偵測引擎的 /scan 端點；偵測完成後，事件會經 API 傳送至 Web 應用程式，亦可直接轉發至既有的 SIEM。若需自訂聚類參數，可透過 webhawk/settings.conf 調整 DBSCAN 的 eps 與 min_samples。由於 README 未提供詳細的類別圖或訊息佇列實作，以上架構說明僅基於文件中描述的服務角色與資料流程推斷。

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
