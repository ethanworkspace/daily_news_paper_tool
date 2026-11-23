# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-11
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：
- 品質分數：3/10 [thin_readme]

## 在做什麼
此專案專注於利用無監督機器學習與 AI 增強技術，分析應用程式日誌以偵測入侵與異常行為。目標使用者為資訊安全分析師、DevOps 工程師及系統管理員，他們需要快速識別潛在攻擊而不依賴預先定義的規則或標籤資料。核心問題在於傳統規則基礎的入侵偵測難以應對新型或變形攻擊，而標註日誌資料成本高；本專案透過無監督學習自動發現日誌中的異常模式，並結合 AI 輔助（如大型語言模型）提升偵測的解釋性與準確性，協助使用者在真實環境中進行主動威脅獵捕與事件響應。

## 技術
專案以 Ruby 為主要開發語言，利用 Ruby 生態系統中的機器學習與資料處理函式庫（具體名稱未在 README 中說明）進行特徵抽取與模型訓練。根據專案主題，它結合了 LLM（大型語言模型）技術來增強偵測結果，可能透過 API 呼叫或本地模型進行日誌語意理解與異常說明。此外，專案著重於日誌分析流程，讀取應用程式產生的文字或結構化日誌，經過預處理（如正則解析、TF-IDF 或詞嵌入）後送入無監督模型（例如聚類、自編碼器或 Isolation Forest）進行異常評分。整體技術棧因此可見為：Ruby 語言、機器學習函式庫、LLM 增強模組以及日誌解析與特徵工程管道。

## 架構
README 摘錄未提供足夠的模組與資料流程描述，無法確定專案內部的具體架構（例如是否採用管線式設計、背後的服務或批次處理方式）。因此，僅能根據可見的資訊推斷：專案 likely 包含日誌輸入模組、前處理與特徵抽取元件、無監督機器學習模型核心、LLM 增強解釋層以及結果輸出或警示機制。但由於缺乏明確說明，此部分的架構描述屬於推斷，依據不足。

## README 摘錄（節選）
```text

```
