# GitHub 專案 04：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-10-01
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
Webhawk 是一個無監督機器學習工具，設計用於自動從應用程式日誌（如 "HTTP" 存取記錄）中尋找攻擊痕跡，無需預先定義規則。它先將原始日誌轉換為數值特徵，使用 "PCA" 提取關鍵欄位，再以 "DBSCAN" 群聚演算法將日誌條目分群，將異常點標記為可能的攻擊痕跡。偵測完成後，結果會傳送至使用者選擇的大型語言模型（"LLM"）進行深度分析並產出可執行的建議。透過內建的網頁介面與 "API"，安全運營中心（"SOC"）團隊可以檢視、管理偵測結果，並將其導入現有的 "SIEM" 生態系統。目標使用者為負責日誌監控與威脅偵測的資安分析師與 SOC 人員。

## 技術
技術上，Webhawk 以 Python 為主要實作語言，使用 scikit-learn 提供的 "PCA" 與 "DBSCAN" 進行無監督特徵降維與密度基礎聚類。日誌先經過特徵編碼（如使用者代理、IP 位址、參數數量）轉為向量。偵測引擎透過 REST "API" 接收日誌，進行聚類與異常點辨識後，將結果發送至 Ollama 容器內運行的 LLM（預設為 granite4:latest）與輔助模型（tev1:0.8b）進行語言理解與建議生成。網頁介面採用輕量級 Web 框架（如 Flask）提供於 port 8080，供分析師登入與檢視事件。Agent 以 Python 腳本運行於各端點，讀取本地日誌檔並透過 HTTP POST 將資料傳送至偵測 "API"（port 8000）。整體可透過 Docker Compose 一鍵啟動三個主要服務：偵測引擎、網頁應用與 Ollama。

## 架構
架構方面，系統採用微服務式的 Docker Compose 部署模式。主要包含三個容器：(1) 偵測 "API"（Webhawk），負責接收來自 Agent 的原始日誌，執行特徵編碼、"PCA" 降維與 "DBSCAN" 聚類，產出異常事件並寫入資料庫或直接推送至 UI；(2) Ollama 容器，運行使用者選擇的 LLM（如 granite4:latest）與輔助模型（tev1:0.8b），提供語言分析與建議生成服務；(3) 網頁應用容器（Webhawk UI），提供登入、事件瀏覽與管理介面，監聽 port 8080，並透過 "API" 顯示偵測結果。Agent 為輕量級 Python 腳本，部署於每台需要監控的主機，讀取指定日誌檔（如 Apache access log）並透過 HTTP POST 將資料發送至偵測 "API" 的 /scan 端點。資料流程為：Agent → 偵測 "API" (特徵化 → "PCA" → "DBSCAN") → 異常點 → Ollama ("LLM" 分析) → 網頁 UI 顯示。所有服務透過 Docker 內部網路互通，偵測 "API" 預設監聽 port 8000，網頁 UI 監聽 port 8080，Ollama 監聽 port 11434。若需擴充，可於未來引入 Kafka 等訊息隊列解耦資料傳輸（專案已列為 TODO）。

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
