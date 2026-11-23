# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-10
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk/Catch 3.0 是一個無監督學習的入侵與異常偵測工具，設計用於自動從應用程式日誌（如 HTTP 存取記錄）中發掘可能的攻擊痕跡，無需預先定義規則。目標使用者為安全運營中心（SOC）分析師與系統管理員，協助他們在大量日誌中快速識別可疑行為，獲得 LLM 驅動的深度分析與可執行建議，並透過網頁介面或 API 將結果整合至現有的 SIEM 生態系統。

## 技術
Webhawk 使用 Python 進行日誌特徵抽取，先以主成分分析 (PCA) 降維取得關鍵特徵（如使用者代理、IP 位址、參數數量），再採用 DBSCAN 密度基礎聚類演算法識離群點作為潛在攻擊痕跡。偵測結果會傳送至 Ollama 容器中的大型語言模型（例如 granite4:latest、tev1:0.8b）進行 Agentic AI 分析與建議生成。網頁介面以 Ruby 實作，提供互動儀表板讓分析師檢視事件。整個系統透過 Docker Compose 部署三個主要服務：偵測 API、Ollama 模型服務與 Web 應用，而端點上輕量的 Python 代理負責擷取日誌並經 HTTP POST 至 /scan 端點。

## 架構
系統架構由四個主要模組組成：(1) 偵測引擎（Webhawk API）負責接收日誌、執行 PCA 特徵轉換、使用 DBSCAN 進行聚類並標記離群點；(2) Ollama 服務運行選擇的 LLM 與 JEV 模型，接收偵測引擎傳送的異常點並產生深度分析與行動建議；(3) Web 應用提供介面讓分析師檢視、管理事件，並可透過內建 API 將結果導出至 SIEM；(4) 端點代理（Webhawk Agent）在每台機器上運行，讀取本地日誌並透過 HTTP 將其發送至偵測 API 的 /scan 端點。這四個模組透過 Docker Compose 協調運行，資料流為：端點 → 代理 → 偵測 API（PCA → DBSCAN） → Ollama LLM 分析 → 結果儲存 → Web UI 呈現；同時偵測 API 也可直接將事件推送至外部 SIEM 系統。

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
