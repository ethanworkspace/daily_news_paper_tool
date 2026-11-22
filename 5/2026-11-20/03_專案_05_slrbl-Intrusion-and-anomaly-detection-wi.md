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
Webhawk/Catch 3.0 是一個無監督學習結合具代理能力的 AI 工具，專門從應用程式日誌（如 HTTP 存取記錄）中自動發掘可能的攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 進行密度聚類，將異常點標記為可疑攻擊線索。隨後，偵測結果會送至使用者選擇的大型語言模型（LLM）進行深度分析，並產出可執行的建議。透過內建的網頁介面與 REST API，安全運營中心（SOC）人員可以即時檢視、管理事件，並將結果匯入現有的 SIEM 生態系統。目標使用者為負責日誌監控與威脅偵測的安全分析師、事件響應團隊以及 DevSecOps 工程師。

## 技術
專案主要使用 Ruby 作為倉庫語言，但核心偵測引擎與端點代理皆以 Python 實作。特徵抽取階段採用主成分分析（PCA）將原始日誌欄位（如使用者代理、IP、參數數量）轉為數值向量；聚類則採用 DBSCAN（基於密度的空間聚類與噪聲）演算法，透過可調整的 eps 與 min_samples 參數控制簇形成。異常點送至 Ollama 服務執行的大型語言模型（預設為 granite4:latest 與 tev1:0.8b）進行 Agentic AI 風格的分析與建議生成。整體透過 Docker Compose 部署三個服務：偵測 API（Webhawk）、Ollama 模型執行環境、網頁介面（Webhawk UI）。端點代理僅需 Python 3，負責讀取本地日誌並經 HTTP POST 將資料傳送至偵測 API 的 /scan 端點。此外，專案提供 REST API 供外部系統（如 SIEM）整合，並預留未來使用 Kafka 進行資料流 decoupling 的規劃。

## 架構
系統架構採用微服務與容器化設計，由 Docker Compose 啟動三個主要容器：(1) 偵測引擎（Webhawk API）負責接收日誌、執行 PCA 特徵轉換、DBSCAN 聚類，將被標記為異常的日誌條目送至 LLM 進行分析；(2) Ollama 容器運行預先拉好的語言模型（granite4:latest、tev1:0.8b）並提供推論服務；(3) Webhawk 網頁介面容器提供分析師登入、事件檢視與管理功能，並透過 API 接收偵測結果。每個受監控的主機上部署輕量級 Python 代理（webhawk_agent），代理讀取指定的應用程式日誌（如 Apache access log）並透過 HTTP POST 發送至偵測 API 的 http://<docker-host>:8000/scan 端點。偵測 API 完成聚類與異常偵測後，會將事件 JSON 發送至網頁介面的 http://webhawk_ui:8080/api/v1/incidents 端點，同時也可直接供外部 SIEM 消費。資料流程為：端點日誌 → 代理 → 偵測 API（特徵抽取/PCA → DBSCAN 聚類） → 異常點 → Ollama LLM 分析 → 結果寫入 UI 及 API。README 中尚未實作的 Kafka decoupling 僅列為未來 TODO，因此目前架構僅包含上述同步 HTTP 流程。

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
