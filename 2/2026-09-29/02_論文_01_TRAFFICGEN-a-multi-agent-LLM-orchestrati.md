# 論文 01：TRAFFICGEN: a multi-agent LLM orchestration for smart mobility and emergency corridor pre-emption.

- 日期：2026-09-29
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Frontiers in artificial intelligence
- Venue：Frontiers in artificial intelligence
- 發布時間：2026-01-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42824146/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13627399/
- DOI：10.3389/frai.2026.1894645
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1743（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
This research work introduces TrafficGen, a proof-of-concept software prototype that explores the possibility of adaptive traffic signal management using LLM-based agentic orchestration. The framework is evaluated in a single-intersection, deterministic simulation environment that uses text to represent the various intersections and can operate with Gemini 2.5 Flash and LangGraph to implement a "Council of Agents" control architecture. TrafficGen uses a semantic translation layer to generate human-readable chain-of-thought reasoning logs for each signal decision, enabling it to manage complex traffic patterns. In empirical stochastic evaluations, TrafficGen was tested using four custom stress scenarios and 30 independent runs, yielding a mean reduction of 46.9% ± 2.8% in Wait Burden Score across all scenarios and runs (from 6,370 points to 3,380 points per run, compared to standard fixed-time signal controllers). Additionally, 100% of the Green Corridor maintained a success rate for dynamic emergency vehicle pre-emption. Architecturally, the system achieved a 100% decision override latency of 1,556 ms and a Green Corridor success rate of 100% for life safety evaluations. The quantitative results show the effectiveness of zero-shot semantic LLM orchestration compared to other LLM controllers with heuristic rules. These results come from a controlled single intersection environment and may not guarantee similar performance when deploying traffic management in municipalities generally, but TrafficGen paves the way for traffic management to move beyond black-box numerical paradigms and into explainable decision-making. Finally, this paper is an initial step towards adaptive traffic management for smart urban mobility.

## 背景與目的
傳統交通號誌控制多採固定時制或黑箱數值優化，缺乏可解釋性且難以即時應對複雜車流與緊急車輛需求。本研究旨在探討以大型語言模型（LLM）為核心的多代理編排機制，是否能實現自適應號誌管理並提供人類可讀的決策推理，進而推動智慧城市交通從數值範式轉向可解釋決策。

## 方法
問題設定為單一路口、確定性模擬環境，輸入為以文字描述的路口狀態（車流、緊急車輛位置等），輸出為號誌相位決策。系統架構採用「Council of Agents」設計，透過 LangGraph 協調多個 LLM 代理，底層模型為 Gemini 2.5 Flash。核心模組包含： 1. 語義轉譯層：將模擬器的數值狀態轉為自然語言提示，並將 LLM 產生的連續思維鏈（chain‑of‑thought）記錄為可讀日誌。 2. 多代理協作：各代理分別負責車流評估、緊急車輛優先、整體協調等子任務，經由 LangGraph 圖結構進行訊息傳遞與共識形成。 3. 零樣本語義編排：無需額外微調或啟發式規則，直接利用 LLM 內建推理能力進行決策。 資料前處理僅將模擬器輸出格式化為文本，特徵表示為自然語言描述。訓練目標不存在傳統損失函數，系統以零樣本推論運行，最佳化策略為提示工程與代理圖拓撲設計。推論流程：模擬器→文字狀態→語義轉譯→多代理協商→號誌指令→模擬器更新，並記錄每步推理日誌。與既有方法關鍵差異在於採用純語義、可解釋的 LLM 編排，而非數值優化或啟發式規則。

## 結果
在四種自訂壓力情境、各 30 次獨立運行中，TrafficGen 平均將 Wait Burden Score 從 6,370 點降至 3,380 點，平均減少 46.9% ± 2.8%。綠色走廊對緊急車輛的動態優先通行成功率達 100%。決策覆寫延遲為 1,556 ms。結果顯示零樣本語義 LLM 編排優於含啟發式規則的其他 LLM 控制器，但僅在單一路口確定性模擬下驗證。

## 限制與展望
評估環境僅限單一路口、確定性模擬，缺乏多路口協調、真實感測器噪聲、非確定性車流與大規模部署的驗證。延遲 1.5 秒可能不滿足實時控制需求。實驗未提供與傳統自適應控制（如 SCATS、SCOOT）的直接比較數據。後續研究需擴展至網絡層級、引入真實數據、優化推理延遲並探討安全性與法規合規。
