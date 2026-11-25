# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-15
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督機器學習工具，專門從應用程式日誌（如 HTTP 存取記錄）中自動偵測可能的攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 群聚演算法將日誌條目分群，將群聚中的離群點視為可疑攻擊行為。偵測結果會傳送至使用者選擇的大型語言模型（LLM）進行深度分析，並利用 Agentic AI 產出可執行的建議與報告。專案提供網頁介面供安全運營中心（SOC）團隊檢視事件，同時提供 API 可將結果整合至既有的 SIEM 或其他安全平台，並附帶可部署於各端點的輕量 agent，負責將本機日誌傳送至偵測引擎。目標使用者為需要快速發現未知威脅的安全分析師、事件響應人員以及 DevOps 工程師，核心問題在於如何在缺少已知簽名或規則的情況下，有效地從大量雜訊日誌中識出異常行為。

## 技術
專案主要以 Ruby 實作專案框架與網頁介面，偵測引擎與端點代理則採用 Python 3 開發。日誌前處理與特徵萃取使用標準函式庫，降維採用 Principal Component Analysis (PCA)，群聚則依賴 DBSCAN 演算法。偵測完成後，透過 HTTP 呼叫本地 Ollama 服務，載入使用者指定的大型語言模型（如 granite4:latest）與輔助模型（tev1:0.8b）進行自然語言分析與建議生成，體現 Agentic AI 設計模式。偵測 API 提供 RESTful 端點接收日誌並回傳事件，網頁介面則透過同一 API 顯示與管理事件。整套系統透過 Docker Compose orchestrate 三個容器：偵測引擎、網頁應用與 Ollama，端點代理僅需 Python 與網路連線即可將本機日誌 POST 至偵測 API。未來規劃中提到考慮引入 Kafka 進行資料流 decoupling。

## 架構
系統由四個模組組成：偵測引擎（Webhawk API）負責日誌接收、特徵抽取、PCA 降維、DBSCAN 群聚與異常點偵測；Ollama 服務運行使用者指定的 LLM（如 granite4:latest）與輔助模型，提供自然語言分析與建議；網頁介面（Webhawk UI）提供登入、事件檢視與匯出，透過 API 取得偵測結果；端點代理（Webhawk Agent）部署於產生日誌的主機，讀取日誌檔並透過 HTTP POST 將內容傳送至偵測引擎的 /scan 端點。資料流程為：代理讀取日誌 → POST 至偵測 API → 前處理與 PCA 降維 → DBSCAN 群聚 → 標記異常為 incident → 傳送至 Ollama 進行 LLM 分析 → 分析結果返回 API → API 轉發至 UI 顯示或推送至外部 SIEM。所有服務經 Docker Compose orchestrate，設定透過 webhawk/settings.conf 調整。README 未提供類別圖或訊息佇列細節，以上說明基於文件描述的元件與流程進行推斷。

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
