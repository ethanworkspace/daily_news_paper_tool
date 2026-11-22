# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-17
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk/Catch 3.0 是一款無監督機器學習工具，專為安全運營中心（SOC）分析師與 DevOps 設計，能自動從應用程式日誌（如 HTTP 存取記錄）中發掘潛在攻擊痕跡。它透過特徵向量化、PCA 降維與 DBSCAN 聚類找出異常點，再利用選擇的大型語言模型提供深度分析與可執行建議，協助使用者在無預設規則的情況下快速偵測與應對入侵行為。

## 技術
專案主要使用 Ruby 構建 Web 介面，偵測引擎與代理採用 Python 實作。特徵萃取階段採用 Principal Component Analysis (PCA)，聚類則使用 DBSCAN 演算法識離群點。異常點送至 Ollama 服務，運行使用者指定的大型語言模型（如 granite4:latest）與 JEV 模型進行 Agentic AI 分析。系統透過 Docker Compose 組織三個核心容器：偵測 API、Ollama 與 Web UI，並提供可於各端點部署的 Python 代理，負責讀取日誌並經由 HTTP POST 將資料傳送至偵測 API。

## 架構
系統由四個主要模組組成：(1) 端點代理（webhawk_agent）讀取本機日誌並透過 HTTP 發送至偵測 API；(2) 偵測引擎（Webhawk API）負責接收日誌、進行特徵向量化、PCA 降維、DBSCAN 聚類，將被標記為異常的日誌條目發送至 Ollama 服務；(3) Ollama 容器運行選擇的 LLM 與 JEV 模型，產生深度分析與可執行建議；(4) Web 應用程式（Webhawk UI）提供分析師介面，顯示事件、允許手動審核並可經由內建 API 將結果匯入既有的 SIEM。所有服務透過 Docker Compose 啟動，代理僅需 Python 3 與能連線至 Docker 主機的 8000 埠。若 README 未明確說明某些內部細節（例如特徵向量的具體欄位），則該部分屬於推斷。

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
