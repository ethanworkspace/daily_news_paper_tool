# GitHub 專案 01：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-04
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk/Catch 3.0 是一款無監督機器學習工具，專為安全運營中心（SOC）分析師與資訊安全工程師設計，能自動從應用程式日誌（如 HTTP 存取記錄）中發掘攻擊痕跡，無需預先定義規則。透過將日誌轉換為數值特徵、使用 PCA 降維與 DBSCAN 聚類，識別異常點作為潛在攻擊線索；之後利用 Agentic AI 與使用者選擇的大型語言模型（LLM）進行深度分析，提供可執行的修復建議，並透過網頁介面與 API 將結果融入現有的 SIEM 生態系統。

## 技術
專案主要使用 Python 3 編寫偵測引擎與端點代理，利用 PCA 進行特徵降維並採用 DBSCAN 進行密度基礎聚類以偵測異常日誌。偵測結果會傳送至 Ollama 容器內的大型語言模型（如 granite4:latest、tev1:0.8b）進行 Agentic AI 分析與建議生成。網頁介面透過 Docker Compose 啟動，提供 REST API 接收日誌與回傳事件。整體依賴 Docker、Docker Compose 與 Ollama 來實現模型服務與容器化部署。

## 架構
系統由三個 Docker 服務組成：偵測 API（Webhawk）、網頁應用程式（Webhawk UI）與 Ollama 模型服務。端點上運行的 Python 代理讀取本地日誌檔案，透過 HTTP POST 將日誌傳送至偵測 API 的 /scan 端點。偵測 API 先將原始日誌轉換為數值向量，使用 PCA 提取主要特徵，接著以 DBSCAN 演算法進行聚類，將不屬於任何密集簇的點標記為異常（潛在攻擊痕跡）。異常點會被封裝後發送至 Ollama 容器內的選定 LLM，利用 Agentic AI 產生可讀的分析報告與修復建議。分析結果經由 API 回傳至網頁應用程式，供安全分析師在 UI 中檢視、管理與匯出；同時亦可透過同一 API 將事件推送至既有的 SIEM 或其他安全平台。所有服務透過 Docker Compose 一鍵啟動，簡化部署與擴展。

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
