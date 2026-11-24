# GitHub 專案 03：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-10-27
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk 是一個無監督學習結合具代理能力的 AI 工具，專門從應用程式日誌（如 HTTP access log）中自動發掘可能的攻擊痕跡。它先將原始日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 進行聚類，將異常點標記為可疑攻擊。之後透過 LLM（Ollama）提供深度分析與可執行建議，並提供網頁介面讓 SOC 分析師檢視與管理結果，同時支援透過 API 將偵測資料傳入現有的 SIEM 系統。目標使用者為安全運營中心人員與需要快速偵測未知威脅的資安團隊。

## 技術
專案主要使用 Ruby 作為倉庫語言，偵測引擎與端點代理均以 Python 3 實作，核心演算法包括 PCA 特徵提取與 DBSCAN 密度基礎聚類。異常點送至 Ollama 容器內的 LLM（如 granite4:latest）進行自然語言分析與建議生成。網頁介面透過 Docker Compose 啟動，提供 RESTful API 接收日誌掃描結果並將事件發送至 UI。Agent 透過 HTTP 將日誌檔案上傳至偵測 API（http://host:8000/scan），Ollama 同時運行分析模型與 JEV 輔助模型。所有服務皆可透過 Docker 快速部署。

## 架構
系統採用三容器 Docker 架構：(1) 偵測 API（Webhawk）負責接收來自 Agent 的日誌，執行 PCA 特徵轉換與 DBSCAN 聚類，產出異常事件並呼叫 Ollama 服務進行 LLM 分析；(2) Ollama 容器運行指定的生成模型（granite4:latest）與 JEV 模型（tev1:0.8b），負責產出可讀取的攻擊描述與建議；(3) Webhawk 網頁應用提供介面讓分析師登入、檢視事件、執行過濾與匯出。Agent 安裝於每台產生日誌的主機，讀取指定日誌檔案並透過 HTTP POST 至偵測 API 的 /scan 端點。事件經 API 傳送至 UI 亦可同時轉發至外部 SIEM。設定透過 webhawk/settings.conf 調整聚類參數與模型名稱。若需進一步解耦資料傳輸，專案規劃使用 Kafka 或等效訊息佇列。

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
