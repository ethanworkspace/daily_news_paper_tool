# 論文 01：TRAFFICGEN: a multi-agent LLM orchestration for smart mobility and emergency corridor pre-emption.

- 日期：2026-09-23
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
本研究針對自適應交通號誌控制難題，提出 TrafficGen 概念驗證原型，利用 LLM 多代理編排實現可解釋決策。現有定時控制器缺乏動態適應性，黑箱數值範式則難以提供決策依據。TrafficGen 引入「代理委員會」架構，結合 Gemini 2.5 Flash 與 LangGraph，透過語義轉譯層產生人類可讀的思維鏈日誌，實現零樣本語義編排，並支援緊急車輛動態綠波預emption，旨在邁向智慧城市行動的可解釋自適應管理。

## 方法
TrafficGen 在單一路口、確定性模擬環境中運作，路口狀態以文本表示。核心架構為由 LangGraph 編排的「代理委員會」，以 Gemini 2.5 Flash 為推理引擎。語義轉譯層將原始交通觀測轉為結構化提示詞，使代理能在無啟發式規則下進行零樣本推理；各代理協同決策並輸出思維鏈日誌，解釋號誌相位選擇。系統另設綠波走廊機制：編排層可覆寫常規號誌計畫，優先放行緊急車輛，決策覆寫延遲測得為 1,556 ms。實驗設計四種自訂壓力情境，各執行 30 次獨立隨機運行，以 Wait Burden Score（累積車輛等待時間指標）為主要度量，分別與標準定時控制器及採用啟發式規則的其他 LLM 控制器比較。

## 結果
跨四大壓力情境、30 次運行，TrafficGen 使 Wait Burden Score 平均降低 46.9% ± 2.8%（從 6,370 點降至 3,380 點/次），優於定時控制器。緊急車輛預emption 在動態交通與生命安全評估中均達 100% 綠波成功率；決策覆寫延遲 1,556 ms 且 100% 可靠。零樣本語義編排表現優於含啟發式規則的 LLM 基線。作者強調結果來自受控單一路口環境，不保證推廣至市政部署時維持同等效能。

## 限制與展望
評估僅限單一路口、確定性模擬與文本狀態表示，未涵蓋真實感測器雜訊、多路口協調、網路層級動態。基線僅含定時控制器與啟發式 LLM，缺乏與 SCATS、強化學習等自適應控制器的比較。1,556 ms 延遲對安全關鍵預emption 可能偏高。對多樣路口幾何、交通文化、市政基礎設施的泛化性未經驗證。後續研究需解決擴展性、魯棒性、實地部署及與最新自適應控制器的基準比較。
