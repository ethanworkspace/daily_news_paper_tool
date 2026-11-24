# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-10-24
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk/Catch 3.0 是一個無監督學習結合具代理能力的 AI 工具，專門從應用程式日誌（如 HTTP 存取記錄）中自動發掘攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 群聚演算法找出異常點，再透過使用者可選擇的 LLM（例如 Ollama 上的 granite4）提供深度分析與可執行的建議。目標使用者為安全運營中心（SOC）分析師、資安工程師與 DevOps 團隊，協助他們快速識別潛在入侵、減少誤報並將結果整合至現有的 SIEM 或警示系統。

## 技術
專案主要使用 Ruby 構建網頁介面與 API 服務，偵測引擎與端點代理則以 Python 實作，負責日誌讀取、特徵抽取與聚類。特徵工程採用 Principal Component Analysis (PCA) 降維，聚類演算法選擇 DBSCAN（含噪點）來分組正常流量與標記異常。異常點會傳送至 Ollama 服務上的使用者自選 LLM（如 granite4:latest）進行自然語言分析與建議生成。整體透過 Docker Compose 組織三個容器：偵測 API、網頁應用與 Ollama，端點代理僅需 Python 3 與網路連線即可將日誌 POST 至 /scan 端點。

## 架構
系統架構由四個主要部分組成：(1) 偵測引擎（Webhawk API）負責接收日誌、進行 PCA 特徵轉換、使用 DBSCAN 群聚並輸出異常點；(2) Ollama 容器運行使用者指定的 LLM 與 JEV 模型，負責對異常點進行自然語言分析與產出建議；(3) 網頁應用（Webhawk UI）提供分析師介面，顯示事件、允許手動標註與匯出；(4) 端點代理（Webhawk Agent）部署於每台產生日誌的主機，讀取本地日誌檔案並透過 HTTP POST 將資料送至偵測 API 的 /scan 端點。資料流程為：代理收集日誌 → 偵測 API 前處理 → PCA 降維 → DBSCAN 群聚 → 異常點傳送至 Ollama → LLM 產出分析 → 結果回傳至 UI 並可經 API 轉發至外部 SIEM。所有服務透過 Docker Compose 組態啟動，設定檔為 webhawk/settings.conf。由於 README 未詳細說明內部模組間的訊息傳遞格式（例如是否使用 JSON 或 Protobuf），此部分屬於合理推斷。

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
