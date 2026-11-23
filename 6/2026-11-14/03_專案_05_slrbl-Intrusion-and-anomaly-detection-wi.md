# GitHub 專案 05：slrbl/Intrusion-and-anomaly-detection-with-machine-learning

- 日期：2026-11-14
- URL：https://github.com/slrbl/Intrusion-and-anomaly-detection-with-machine-learning
- 描述：Unsupervised, AI-augmented detection of attacks in application logs.
- Stars：175  |  Forks：74  |  Language：Ruby
- License：MIT
- Topics：agentic-ai, ai, artificial-intelligence, cybersecurity, detect-intrusions, infosec, intrusion-detection, llm, log-analysis, machine-learning
- 更新時間：2026-10-29T17:26:10+00:00
- 配對論文：
- 品質分數：3/10 [thin_readme]

## 在做什麼
該專案提供一種無監督學習、AI 輔助的機制，用於偵測應用程式日誌中的入侵與異常行為。目標使用者為資安分析師、DevOps 工程師與安全運營中心（SOC）人員，他們需要在缺乏標籤攻擊樣本的情況下，自動發現未知威脅。核心問題在於傳統規則基礎的偵測難以應對零日攻擊與變形惡意行為，而本專案透過非監督模型從日誌中學習正常行為模式，並利用 AI 增強特徵表示，以即時標記偏離常態的事件，減少誤報並提升偵測覆蓋率。

## 技術
專案主要以 Ruby 實作，負責日誌的讀取、預處理與結果呈現。為執行非監督機器學習與 AI 增強，它呼叫 Python 生態系統的函式庫（例如 scikit‑learn、TensorFlow 或 PyTorch）透過 JRuby 或系統進程進行模型訓練與推論。特徵工程採用日誌解析（正則表達式、結構化欄位提取）以及 TF‑IDF 或詞嵌入向量化；模型方面可能使用聚類（如 K‑means、DBSCAN）或自編�器來學習正常行為，並透過 LLM 進行語義理解與異常說明生成。最終結果透過網頁介面或訊息通知（如 Slack、Email）發送給使用者。

## 架構
系統架構可劃分為四個主要流程：(1) 日誌輸入層，負責從檔案、Syslog 或訊息佇列讀取原始日誌；(2) 前處理與特徵抽取層，執行日誌解析、噪音過濾、欄位正規化以及向量化（TF‑IDF/嵌入），產生數值特徵矩陣；(3) 無監督模型層，利用聚類或自編�器等演算法訓練基線模型，並在線上推論中計算每筆記錄的異常分數；(4) 警報與呈現層，根據分數閾值產生警報，並透過儀表板、Webhook 或郵件通知使用者。由於 README 未提供詳細圖表或類別圖，上述流程屬於基於典型未監督日誌異常偵測專案的合理推斷。

## README 摘錄（節選）
```text

```
