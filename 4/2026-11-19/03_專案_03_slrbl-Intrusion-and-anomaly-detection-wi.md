# GitHub 專案 03：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

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
Webhawk 是一個無監督學習結合具代理能力的 AI 工具，專門從應用程式日誌（如 HTTP access log）中自動尋找可能的攻擊痕跡。它先將日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 進行聚類，將異常點標記為可疑入侵。接著透過使用者可選擇的 LLM（透過 Ollama）提供深度分析與可執行的建議，並提供網頁介面讓 SOC 人員檢視與管理事件，同時提供 API 可將結果匯入既有的 SIEM 系統。目標使用者為安全運營中心分析師、資安工程師與需要快速偵測異常流量的系統管理員。

## 技術
專案主要使用 Ruby 構建網頁介面，偵測引擎與端點代理則以 Python 3 實作。特徵抽取採用 Principal Component Analysis (PCA)，聚類採用 Density-Based Spatial Clustering of Applications with Noise (DBSCAN)。異常點送至 Ollama 服務執行的大型語言模型（如 granite4:latest）進行 Agentic AI 風格的分析與建議生成。服務之間透過 RESTful API 互通，偵測 API 監聽 8000 端點，網頁 UI 監聽 8080 端點，Ollama 監聽 11434 端點。部署採用 Docker Compose，將偵測引擎、網頁應用與 Ollama 三個容器組合；端點代理僅需 Python 與能連線至 Docker 主機的 8000 端點。可見的技術堆疊包括：Ruby、Python、PCA、DBSCAN、Ollama/LLM、Docker、Docker Compose、REST API。

## 架構
系統架構由三個 Docker 服務與分散於各主機的端點代理組成。偵測引擎（Webhawk API）負責接收經代理上傳的原始日誌，先進行數值編碼，接著執行 PCA 特徵萃取與 DBSCAN 聚類，將被判定為噪聲或小簇的日誌標記為潛在攻擊事件。這些事件會被送往 Ollama 容器內的 LLM 模型，利用 Agentic AI 產出可讀的分析報告與緩建議。分析結果透過 HTTP POST 發送至網頁應用（Webhawk UI）的 /api/v1/incidents 端點，UI 於 8080 端點提供登入、事件瀏覽與管理介面。端點代理運行於需要監控的主機上，讀取指定的日誌檔（如 Apache access log）並透過 HTTP POST 將檔案上傳至偵測引擎的 /scan 端點；代理僅需 Python 3 與能連線至 Docker 主機的 8000 端點。資料流程為：端點代理 → 偵測 API (PCA+DBSCAN) → Ollama LLM → 網頁 UI。所有服務透過 Docker Compose 啟動，配置檔 settings.conf 用於調整 DBSCAN 參數、選擇 LLM 模型以及設定各服務的 URL。若需進一步擴散，專案曾提及考慮使用 Kafka 進行資料脫鉤，但目前實作仍採用直接 HTTP 傳輸。

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
