# 論文 01：Aligning Perception, Reasoning, Modeling and Interaction: A Survey on Physical AI.

- 日期：2026-10-11
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：IEEE transactions on pattern analysis and machine intelligence
- Venue：IEEE transactions on pattern analysis and machine intelligence
- 發布時間：2026-10-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42284175/
- PDF：
- DOI：10.1109/tpami.2026.3703038
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1638（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The convergence of embodied intelligence and world models has catalyzed growing interest in integrating physical laws into AI systems. While prior surveys have examined world models and embodied intelligence separately, we focus on the progression that connects these capabilities as a unified developmental pathway from passive observation to active physical comprehension. This survey provides a systematic framework revealing how physical AI advances through four interconnected stages: perception transforms sensory data into structured physical representations, reasoning derives explanations from observed phenomena, modeling enables predictive simulation grounded in physical principles, and embodied interaction closes the loop through physical manipulation and environmental feedback. Each stage enables and enhances the next: perceptual grounding supports causal reasoning, reasoning unlocks predictive capabilities, and robust models drive genuine physical interaction. Through analysis of developments spanning architectural innovations, training methodologies, causal inference, and embodied systems, we synthesize how physical understanding emerges through cumulative integration across this progression. Our framework reveals the evolution from isolated, task-specific solutions toward integrated architectures that advance from pattern recognition toward causal reasoning and counterfactual prediction. This perspective provides foundations for next-generation physical AI systems with direct implications for safe, generalizable, and interpretable deployment across robotics, scientific discovery, and autonomous systems.

## 背景與目的
隨著具身智慧與世界模型的融合，將物理定律納入 AI 系統成為研究熱點。既有調查多將世界模型與具身智慧分開討論，缺乏從被動觀測到主動物理理解的統一發展路徑。本文旨在建立系統性框架，闡明物理 AI 如何透過感知、推理、建模與具身互動四個相互關聯的階段逐步進化，並指出從孤立任務導向解決方案走向整合架構、從模式識別邁向因果推理與反事實預測的趨勢，為機器人、科學發現與自主系統的安全、泛化與可解釋部署奠基。

## 方法
本調查將物理 AI 定義為四階段的累積整合流程： 1. 問題設定與輸入輸出：以多模態感測資料（視覺、觸覺、本體感覺等）為輸入，輸出為結構化物理表徵、因果解釋、預測模擬與具身控制策略。 2. 整體架構：提出感知→推理→建模→互動的串聯管線，各階段輸出作為下一階段輸入，形成閉環。 3. 核心模組機制： - 感知階段：將原始感測訊號轉換為物理屬性（如質量、摩擦係數、幾何結構）的結構化表示，強調幾何與語意的聯合編碼。 - 推理階段：基於感知輸出進行因果推斷，利用圖神經網路、符號推理或神經符號混合方法推導物理機制。 - 建模階段：構建以物理定律為先驗的世界模型，包含可微分物理引擎、神經常微分方程、基於能量的模型等，支援前向預測與反事實模擬。 - 具身互動階段：將預測模型部屬於實體或模擬機器人，透過主動操作與環境回饋進行線上適應與策略優化。 4. 資料前處理與表示：強調多模態對齊、時空同步、物理參數標註與反事實資料增強。 5. 訓練目標與最佳化：綜合監督式感知損失、因果推理一致性損失、物理一致性正則化、模型預測誤差與強化學習回報，採用多任務聯合訓練或課程學習策略。 6. 推論與執行流程：感知編碼→因果圖構建→世界模型前向推演→策略生成→環境互動→回饋更新各階段參數。 7. 與既有方法差異：傳統工作多單獨優化感知或控制，本框架強調四階段的耦合與累積整合，並明確引入因果推理與物理先驗作為跨階段橋樑。

## 結果
摘錄未提供可驗證數字。作者報告的定性結論包括：四階段框架能系統性梳理物理 AI 發展脈絡；感知奠基支撐因果推理，推理釋放預測能力，穩健模型驅動真實具身互動；整合架構較孤立任務方案更具泛化與可解釋性；展望下一代物理 AI 在機器人、科學發現與自主系統的安全部署潛力。

## 限制與展望
本文為綜述性質，缺乏實證實驗與量化基準，無法驗證框架在具體任務上的效能優勢。方法層面未給出具體模型架構細節、超參數設定或訓練資料規模，難以直接複現。評估面僅以定性論述替代實證比較，可能忽略跨領域遷移、實時性與安全性等部署挑戰。後續研究建議：建立統一基準測試集、設計跨階段消融實驗、探討大規模多模態物理資料的獲取與標註策略、研究可擴展的因果發現演算法與實時具身控制架構。
