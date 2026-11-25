# GitHub 專案 01：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-09
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督學習結合 AI 增強的攻擊偵測工具，設計用於自動從應用程式日誌（如 HTTP 存取記錄）中尋找攻擊痕跡，而不依賴預先定義的規則。它首先將原始日誌轉換為數值特徵，使用 PCA 提取關鍵維度，再以 DBSCAN 進行密度基礎聚類，將異常點標記為潛在攻擊。偵測結果會送至使用者選擇的 LLM（透過 Ollama）進行深度分析並產出可執行的建議，最後透過網頁介面或 API 提供給安全運營中心（SOC）人員檢閱與整合。目標使用者為需要快速發現未知威脅的安全分析師、SOC 團隊與 DevOps 人員。

## 技術
專案主要使用 Python 實作偵測引擎（catch.py、Webhawk API），透過 scikit-learn 的 PCA 與 DBSCAN 進行特徵降維與聚類；日誌收集端提供 Python 代理程式（webhawk_agent），負責讀取本地日誌並經 HTTP POST 傳送至偵測 API。分析階段呼叫 Ollama 運行的大型語言模型（如 granite4:latest）與輔助模型（tev1:0.8b）進行 Agentic AI 推理，產出文字報告與建議。前端採用網頁應用（Webhawk UI）提供事件檢視與帳號管理，後端服務皆以 Docker Compose 組織為三個容器：偵測 API、網頁 UI 與 Ollama。此外，專案仍保留 Ruby 作為倉庫語言，但核心功能依賴 Python 與容器化基礎設施。

## 架構
系統架構由三個主要 Docker 服務與分散式代理組成。偵測 API（Webhawk）接收來自代理或手動上傳的原始日誌，先進行數值編碼，接著使用 PCA 提取特徵，再以 DBSCAN 進行聚類，將低密度或噪聲點標記為異常；這些異常點會被封裝為事件並經 HTTP 傳送至 Ollama 容器，其中運行的 LLM 進行 Agentic AI 分析，產出可讀的攻擊描述與緩解建議。分析結果返回至偵測 API，再寫入資料庫或直接推送至網頁 UI（Webhawk UI）供分析師檢閱；UI 亦提供 REST API 讓外部 SIEM 或票務系統 ingest 事件。每個受監控主機上安裝的 Python 代理程式（webhawk_agent）負責讀取指定日誌檔（如 Apache access.log）並透過 POST 請求將資料送到偵測 API 的 /scan 端點；代理可設定目標 Docker 主機 IP，以 127.0.0.1 為同機部署預設值。整個流程以 Docker Compose 啟動，確保偵測引擎、網頁介面與 Ollama 服務能在同一主機上快速部署與擴展。

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
