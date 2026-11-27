# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-21
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
Webhawk 是一個無監督機器學習工具，專為分析應用程式日誌（如 HTTP 存取記錄）中的攻擊痕跡而設計，目標使用者為安全運營中心（SOC）分析師與資訊安全工具開發者。它透過將日誌轉換為數值特徵、使用 PCA 降維及 DBSCAN 聚類來自動發現異常點，進而利用 Agentic AI 與大型語言模型提供深入分析與可執行的修復建議，解決傳統規則型入侵偵測無法覆蓋未知攻擊向量的問題。

## 技術
專案主要使用 Ruby 作為倉庫語言，但偵測引擎與端點代理均以 Python 3 實作。特徵抽取採用 Principal Component Analysis (PCA)，聚類則使用 DBSCAN（Density-Based Spatial Clustering of Applications with Noise）演算法。異常偵測結果會經由內建 API 傳送至 Ollama 服務，其中運行使用者可選擇的大型語言模型（如 granite4:latest）與輔助模型（tev1:0.8b）進行 Agentic AI 驅動的深度分析與建議生成。前端採用網頁應用程式提供介面，後端服務透過 Docker Compose 組織為三個容器：偵測 API、Ollama 與 Web UI。端點代理負責讀取本地日誌並經 HTTP POST 將資料送至偵測 API。

## 架構
系統架構分為四個主要模組：(1) 偵測引擎（Webhawk API）負責接收日誌、執行 PCA 特徵轉換、使用 DBSCAN 進行聚類並標記離群點；(2) Ollama 服務運行大型語言模型與輔助模型，接收偵測引擎傳送的異常摘要，利用 Agentic AI 產出可讀取的分析報告與修復建議；(3) 網頁應用程式（Webhawk UI）提供登入、事件瀏覽與管理介面，分析師可在此檢視偵測結果並將其匯出至 SIEM；(4) 端點代理（Webhawk Agent）部署於每台產生日誌的主機，讀取本地檔案（如 Apache access log）並透過 HTTP POST 將資料送至偵測 API。資料流程為：日誌 → 端點代理 → 偵測 API (PCA → DBSCAN) → 離群點摘要 → Ollama LLM → 分析建議 → Web UI 顯示。所有服務透過 Docker Compose 啟動，偵測 API 監聽 8000 端口，UI 監聽 8080 端口，Ollama 監聽 11434 端口。若需進一步擴充，可將資料傳輸層替換為 Kafka 等訊息佇列（專案中標註的 TODO）。

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
