# GitHub 專案 04：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-09-12
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk 是一個無監督學習結合 AI 增強的應用程式日誌入侵與異常偵測工具，目標使用者為安全運營中心 (SOC) 分析師與系統管理員。它透過非規則式的方法，自動從 HTTP 等應用日誌中發現可能的攻擊痕跡，並提供可操作的建議，減少對預設規則的依賴。

## 技術
專案主要使用 Python 進行特徵工程、PCA 降維與 DBSCAN 聚類，透過 Ollama 呼叫本地大型語言模型 (如 granite4:latest、tev1:0.8b) 進行異常說明與建議生成；前端採用 Ruby 架構的網頁應用提供分析師介面，透過 Docker Compose 整合偵測引擎、LLM 服務與 Web UI 三個容器，並提供 Python 執行的端點代理程式負責日誌收集與傳輸。

## 架構
系統架構分為四部分：(1) 偵測引擎 (Webhawk API) 接收經代理程式上傳的原始日誌，先將日誌轉為數值特徵，使用 PCA 提取關鍵維度，再以 DBSCAN 演算法進行密度基礎聚類，將離群點標記為潛在攻擊；(2) 偵測結果被送至 Ollama 容器內的 LLM，利用 Agentic AI 產出詳細分析與緩解建議；(3) Web 應用 (Webhawk UI) 提供登入、事件瀏覽與管理介面，分析師可在此檢視與標記事件；(4) 端點代理程式 (Webhawk Agent) 安裝於每台產生日誌的主機，負責讀取本地日誌檔並透過 HTTP POST 將資料傳送至偵測引擎的 /scan 端點。所有服務透過 Docker Compose 啟動，分別對應偵測 API (port 8000)、Ollama (port 11434) 與 Web UI (port 8080)。

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
