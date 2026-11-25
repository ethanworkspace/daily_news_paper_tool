# GitHub 專案 02：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-13
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：https://doi.org/10.7910/dvn/3qbyb5
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
Webhawk 是一個無監督學習結合具代理能力的 AI 工具，專門從應用程式日誌（如 HTTP access log）中自動發掘可能的攻擊痕跡。它先將日誌轉換為數值特徵，使用 PCA 降維後以 DBSCAN 進行聚類，將異常點標記為可疑入侵。偵測結果會傳送至選擇的大型語言模型（透過 Ollama）進行深度分析並給出可執行的建議，最後透過網頁介面讓 SOC 分析師檢視與管理事件，同時也能透過內建 API 將結果匯入現有的 SIEM 系統。目標使用者為安全運營中心人員、資安工程師與需要快速識別未知攻擊行為的團隊。

## 技術
專案主要使用 Ruby 作為倉庫語言，偵測引擎與代理端則依賴 Python 3 實作。特徵抽取採用 Principal Component Analysis (PCA)，聚類演算法使用 DBSCAN（Density-Based Spatial Clustering with Noise）來分組日誌並找出離群點。異常偵測後，結果會經由 HTTP 呼叫傳送至 Ollama 容器內的大型語言模型（預設為 granite4:latest 與 tev1:0.8b）進行生成式分析與建議。整體透過 Docker Compose 組織三個服務：偵測 API、Ollama 模型服務與網頁 UI，並提供可安裝於各端點的 Python 代理程式負責讀取日誌並上傳至偵測 API。

## 架構
系統架構採用微服務方式，由 Docker Compose 啟動三個主要容器：(1) 偵測引擎（Webhawk API）負責接收代理上傳的原始日誌、進行數值編碼、PCA 特徵降維、DBSCAN 聚類、異常點標記，並將偵測結果寫入資料庫或直接轉發至 UI；(2) Ollama 容器內執行選擇的 LLM（granite4:latest）與 JEV 模型（tev1:0.8b），提供異常點的語意分析與可執行建議；(3) 網頁應用程式（Webhawk UI）提供分析師介面，顯示事件列表、詳細報告並允許手動標註或匯出。每個受監控的主機上安裝的 Python 代理程式會讀取指定的日誌檔（如 Apache access log），透過 HTTP POST 將內容傳送至偵測 API 的 /scan 端點。偵測完成後，UI 會從 API 取得事件並展示；同時，API 也可對外提供 RESTful 端點，使現有的 SIEM 或其他安全平台能訂閱或拉取偵測結果。設定透過 webhawk/settings.conf 檔案調整，包括 Ollama 位置、模型名稱、DBSCAN 參數等。若需進一步擴充，專案曾提及考慮使用 Kafka 進行資料傳輸的可能性。

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
