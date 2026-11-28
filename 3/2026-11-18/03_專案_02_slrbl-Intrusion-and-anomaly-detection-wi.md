# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-18
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
Webhawk 是一個無監督機器學習工具，針對應用程式日誌（如 HTTP access log）進行異常偵測，透過 PCA 特徵抽取與 DBSCAN 聚類識別可疑攻擊痕跡，再利用選擇的 LLM 進行深度分析並提供可執行的建議，主要服務於需要即時威脅洞察的 SOC 團隊與安全工程師。

## 技術
專案主要以 Ruby 管理專案結構與腳本，偵測引擎與代理採用 Python 3 實作，使用 PCA 將原始日誌轉換為數值特徵，再以 DBSCAN 演算法進行密度基礎聚類與異常點偵測；異常點會傳送至本地 Ollama 服務，呼叫使用者自行選擇的 LLM（如 granite4:latest）進行語意分析與建議生成；透過 Docker Compose 組合偵測 API、網頁 UI 與 Ollama 服務，並提供可部署於各端點的 Python 代理負責日誌收集與傳輸。

## 架構
系統架構由三個主要 Docker 服務組成：偵測 API（Webhawk）負責接收日誌、執行 PCA 特徵抽取與 DBSCAN 聚類，將異常點傳送至 Ollama 服務；Ollama 運行使用者指定的 LLM（如 granite4:latest）與輔助模型（tev1:0.8b），進行語意分析並回傳建議；網頁 UI（Webhawk web application）提供分析師介面，顯示事件並允許手動審查或匯出。此外，每個受監控主機上運行的 Python 代理會讀取本機日誌檔案，透過 HTTP POST 將原始日誌傳送至偵測 API 的 /scan 端點。資料流程為：日誌 → 代理 → 偵測 API（特徵化、聚類、異常偵測） → Ollama LLM 分析 → UI 呈現；若需整合既有 SIEM，可透過內建 API 將事件推送至外部系統。所有服務透過 Docker Compose 啟動，設定檔為 webhawk/settings.conf，其中定義 LLM 模型、JEV 模型及各服務端點。

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
