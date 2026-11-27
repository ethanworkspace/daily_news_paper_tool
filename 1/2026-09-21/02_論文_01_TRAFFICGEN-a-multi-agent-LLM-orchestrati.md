# 論文 01：TRAFFICGEN: a multi-agent LLM orchestration for smart mobility and emergency corridor pre-emption.

- 日期：2026-09-21
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
傳統號誌控制多採固定時制或黑箱數值優化，缺乏可解釋性且難以應對突發緊急車輛與複雜流型。現有基於 LLM 的控制器多依賴啟發式規則，難以實現零樣本語義推理。本文提出 TrafficGen 原型，旨在探索以 LLM 多代理編排實現自適應號誌管理，並提供人類可讀的思維鏈日誌，推動智慧交通向可解釋決策邁進。

## 方法
問題設定：單一路口、確定性模擬環境，以文字描述路口狀態（車流佇列、緊急車輛請求）作為輸入，輸出號誌相位決策。整體架構採用「代理委員會」，以 Gemini 2.5 Flash 為核心 LLM，透過 LangGraph 協調多個專責代理（流量評估、緊急通道、相位選擇）。核心模組包含語義轉譯層，將模擬狀態轉為結構化提示，並生成每次決策的思維鏈推理日誌，實現可解釋性。資料表示採純文本狀態向量，無需數值特徵工程。訓練目標為零樣本推理，無梯度更新，損失函數不適用；最佳化策略僅在提示工程與代理協作邏輯上迭代。推論流程：環境狀態 → 語義轉譯 → 多代理協商 → 產生相位指令 → 執行並記錄延遲（決策覆寫延遲 1,556 ms）。關鍵差異在於以語義編排取代啟發式規則，並提供完整推理軌跡。

## 結果
實證實驗設計四種壓力情境，各 30 次獨立運行。TrafficGen 平均將等待負擔分數降低 46.9% ± 2.8%（從 6,370 點降至 3,380 點），優於固定時制控制器。緊急車輛綠色走廊成功率達 100%，決策覆寫延遲穩定在 1,556 ms。作者指出零樣本語義編排優於帶啟發式規則的 LLM 控制器，但結果僅限單一路口模擬。

## 限制與展望
限制包括：僅在單一路口、確定性、文字模擬環境驗證，未涵蓋多路口協調、真實感測器噪聲、通訊延遲與多樣化交通需求；決策延遲 1.5 秒可能不符合實時管制需求；僅測試 Gemini 2.5 Flash，模型泛化性未知；缺乏與傳統自適應控制（如感應式、強化學習）的基線比較；後續需擴展至網格路網、實地部署並評估擴展性與安全性。
