# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-14
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
Webhawk/Catch 3.0 是一個無監督的 AI 增強型入侵與異常偵測工具，專為分析應用程式日誌（如 HTTP 存取記錄）而設計。它利用非監督式機器學習將日誌條目進行聚類，並辨識離群點作為潛在攻擊痕跡。偵測結果會送至選擇的大型語言模型（LLM）進行深度分析，並透過具代理能力的 AI 產出可執行的建議。目標使用者為安全運營中心（SOC）人員與需要自動化威脅偵測的開發或運維團隊。核心問題在於傳統規則基礎的入侵偵測難以捕捉未知或變形攻擊，而 Webhawk 透過聚類與 LLM 分析提供無規則、適應性的偵測方案。

## 技術
專案主要使用 Python 3 實作偵測引擎與代理（agent），透過 Principal Component Analysis (PCA) 將原始日誌轉換為數值特徵（如使用者代理、IP 位址、參數數量），再採用 DBSCAN（密度基礎空間聚類）演算法進行聚類與離群點偵測。偵測結果會經由 REST API 傳送至 Ollama 容器內的大型語言模型（預設為 granite4:latest 與 tev1:0.8b）進行深度分析與建議生成。網頁介面與偵測 API 皆以 Docker Compose 方式部署，包含三個主要服務：偵測引擎（Webhawk API）、Ollama 模型服務以及 Web UI。代理則是一個可在各端點上執行的 Python 腳本，負責讀取本地日誌並透過 HTTP POST 將資料送至偵測 API。

## 架構
系統架構由四個主要模組組成：(1) 端點代理（webhawk_agent）負責讀取應用程式日誌並透過 HTTP POST 將日誌上傳至偵測 API；(2) 偵測引擎（Webhawk API）接收日誌後進行特徵編碼、PCA 降維、DBSCAN 聚類，將被判定為離群點的日誌標記為潛在事件；(3) Ollama 服務執行預設的 LLM（granite4:latest）與輔助模型（tev1:0.8b），對偵測引擎傳送的事件進行自然語言分析並產出可操作的建議；(4) Web UI（webhawk_ui）提供分析師介面，顯示偵測結果與 LLM 建議，並允許手動審核與匯出。資料流程為：端點代理 → 偵測 API → 特徵處理與聚類 → 離群點標記 → 呼叫 Ollama LLM → 分析結果回傳 → Web UI 顯示。此外，偵測 API 也可直接將事件推送至既有的 SIEM 系統。若 README 未明確說明某些實作細節（例如 Web UI 的前端框架），則以上說明僅基於可見的服務與資料流程進行合理推斷。

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
