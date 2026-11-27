# 論文 02：TRAFFICGEN: a multi-agent LLM orchestration for smart mobility and emergency corridor pre-emption.

- 日期：2026-09-30
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
本研究旨在探討以大型語言模型（LLM）為核心的多代理協調機制，應用於自適應交通號誌控制，解決傳統固定時制與黑箱數值優化難以提供可解釋決策的問題。現有方法多依賴啟發式規則或強化學習，缺乏語義層面的推理紀錄，導致決策過程不透明且難以整合緊急車輛優先通行等複雜需求。本文提出 TrafficGen 原型系統，採用「代理委員會」架構，結合 Gemini 2.5 Flash 與 LangGraph，在單一路口確定性模擬環境中驗證零樣本語義協調的可行性，並提供人類可讀的思維鏈日誌，期望為智慧城市交通管理開啟可解釋、可擴展的新範式。

## 方法
問題設定：輸入為文字描述的單一路口交通狀態（車流量、佇列長度、緊急車輛位置等），輸出為各相位的綠燈時長與切換指令。系統整體架構採用 LangGraph 構建的有向圖，節點對應不同角色的 LLM 代理，形成「代理委員會」（Council of Agents）：包括感知代理、規劃代理、執行代理與審核代理。核心機制為零樣本語義協調：感知代理將模擬器回傳的結構化資料轉為自然語言提示，規劃代理依據提示生成思維鏈推理，產生號誌時制建議；執行代理將建議轉換為模擬器指令；審核代理檢查安全性與緊急車輛優先權，必要時覆寫決策。語義轉譯層負責在每個決策週期記錄完整的推理日誌，確保可解釋性。模型使用 Gemini 2.5 Flash 作為底層 LLM，採用零樣本提示，無額外微調；優化目標為最小化等待負擔分數（Wait Burden Score）並保證綠色走廊（Green Corridor）100% 成功率。推論流程：每仿真步驟依序執行感知→規劃→審核→執行，決策覆寫延遲測量為 1,556 ms。與既有基於啟發式規則的 LLM 控制器相比，TrafficGen 不依賴手工規則，完全由語義推理驅動。

## 結果
實證實驗在四個自訂壓力情境下各執行 30 次獨立運行。TrafficGen 平均將等待負擔分數從固定時制的 6,370 點降至 3,380 點，平均減少 46.9% ± 2.8%。緊急車輛動態優先通行的綠色走廊成功率達 100%。系統決策覆寫延遲為 1,556 ms，生命安全評估下綠色走廊成功率亦為 100%。作者指出零樣本語義協調優於帶啟發式規則的 LLM 控制器，但結果僅限單一路口確定性模擬，摘錄未提供其他基線（如自適應時制、強化學習）的可驗證數字。

## 限制與展望
研究限制包括：僅在單一路口、確定性、文字表示的模擬環境驗證，缺乏多路口協調、真實感測器噪聲、非確定性交通流與大規模部署的實證；延遲 1.5 秒可能不滿足實時控制需求；未與傳統自適應號誌（SCATS、SCOOT）或強化學習基線直接比較；零樣本提示的穩健性在不同 LLM 版本或語言下未測試；後續工作需擴展至網路層級、引入線上學習與安全驗證機制。
