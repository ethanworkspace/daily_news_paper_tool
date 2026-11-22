# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-20
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk/Catch 3.0 是一款無監督機器學習工具，專為分析應用程式日誌（如 HTTP 存取記錄）而設計，能自動將日誌條目轉換為數值特徵，經 PCA 降維後使用 DBSCAN 群聚演算法找出異常點，進而標記可能的攻擊痕跡。偵測結果會交給選擇的大型語言模型進行 Agentic AI 深度分析，提供可操作的建議。透過內建 Web 介面與 API，安全運營中心（SOC）人員可即時檢視、管理事件，並將結果導入既有的 SIEM 系統。適合需要自動化威脅偵測且不依賴靜態規則的安全團隊與開發人員。

## 技術
專案主要以 Python 實作偵測引擎與日誌代理人，使用 PCA 將原始日誌轉為數值特徵，再以 DBSCAN 演算法進行密度基礎群聚與異常點偵測。偵測後，結果會透過 API 傳送至本地 Ollama 服務，呼叫使用者自行選擇的大型語言模型（如 granite4:latest）進行 Agentic AI 深度分析並產出可操作建議。Web 應用程式提供介面供安全分析師檢視事件，並透過內建 API 將事件導入 SIEM。整體透過 Docker Compose 組合三個服務（偵測 API、Ollama、Web UI），並在每個端點上運行 Python 代理人採集日誌並 POST 至偵測 API。儘管倉庫語言標示為 Ruby，但實際執行依賴 Python 與 Docker 環境。

## 架構
系統架構由三個主要 Docker 服務組成：偵測 API（Webhawk）負責接收代理人傳來的日誌，執行 PCA 特徵萃取與 DBSCAN 群聚，產出異常事件；Ollama 服務運行選定的大型語言模型與輔助模型，提供 Agentic AI 分析與建議；Web 應用程式提供介面讓分析師檢視事件、管理帳號，並透過 API 將事件推送至外部 SIEM。每個受監控的主機上運行 Python 代理人，讀取本地日誌檔案（如 Apache access log）並透過 HTTP POST 將資料送至偵測 API 的 /scan 端點。偵測 API 完成異常偵測後，會將事件 JSON 發送至 Web UI 介面（http://localhost:8080/api/v1/incidents）供前端顯示，同時也可經由同一 API 直接供 SIEM 消費。設定檔 settings.conf 控制 PCA 參數、DBSCAN 的 eps 與 min_samples、選擇的 LLM 名稱等，讓進階使用者能微調群聚行為。整個流程透過 Docker Compose 一鍵啟動，降低部署複雜度。

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
