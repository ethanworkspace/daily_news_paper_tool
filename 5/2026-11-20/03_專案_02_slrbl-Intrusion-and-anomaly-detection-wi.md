# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-20
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
Webhawk/Catch 3.0 是一個無監督學習結合 AI 增強的入侵與異常偵測工具，專為分析應用程式日誌（如 HTTP 存取記錄）而設計。它不依賴預先定義的規則，而是利用非監督式機器學習將日誌條目分群，找出可能代表攻擊痕跡的離群點，然後透過 Agentic AI 產生深入分析與可執行的建議，並提供友善的網頁介面與 API，方便 SOC 團隊檢視與將結果匯入現有的 SIEM 系統。

## 技術
技術棧主要以 Python 實作，包括使用 scikit-learn 的 Principal Component Analysis (PCA) 降維與 DBSCAN 密度基礎聚類演算法進行無監督異常偵測；偵測結果透過 REST API 傳送至 Ollama 服務，呼叫 Granite4:latest 與 TEV:0.8b 兩個大型語言模型進行 Agentic AI 分析與建議生成；網頁介面透過 Docker Compose 啟動的 Web 應用程式提供分析師操作界面；端點代理則以 Python 腳本讀取日誌並 POST 至偵測 API。

## 架構
架構採用 Docker Compose 將偵測引擎（Webhawk API）、網頁介面（Webhawk UI）與 Ollama 服務三個容器組合成一個服務單元。偵測引擎提供 REST API (/scan) 接受端點代理傳送的原始日誌，先執行 PCA 特徵萃取，再使用 DBSCAN 進行聚類，將被標記為噪聲或小簇的記錄視為潛在攻擊事件，並寫入資料庫同時推送至 Web UI 供分析師檢視。異常事件同時經由 API 轉發至 Ollama 呼叫 Granite4 與 TEV 模型，產生 Agentic AI 的深度分析與緩建議，結果回傳至 UI 顯示。端點代理以 Python 腳本運行，讀取本機日誌檔案並透過 HTTP POST 將資料送至偵測 API，完成日誌收集與傳輸。

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
