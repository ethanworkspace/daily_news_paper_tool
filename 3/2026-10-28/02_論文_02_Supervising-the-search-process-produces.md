# 論文 02：Supervising the search process produces reliable and generalizable information-seeking agents.

- 日期：2026-10-28
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-28T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43086220/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13809059/
- DOI：10.1038/s41467-026-78807-z
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1490（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Large language models (LLMs) are transforming web search by shifting from document ranking to synthesizing answers, and are increasingly deployed as autonomous agentic search systems that iteratively interact with external knowledge sources. Despite this progress, building effective search agents remains challenging because high-quality intermediate search steps are difficult to generate. Previous approaches have primarily relied on outcome supervision, rewarding agents only for producing correct final answers. This often leads to reward hacking and excessive dependence on parametric memory, limiting generalization to out-of-domain tasks. To address these limitations, we introduce RAG-Gym, a framework that shifts supervision from final answers to the search process itself. With RAG-Gym, we systematically investigate architecture design, parameter optimization, and action evaluation, identifying reasoning reflection as a critical capability for search agents. Building on this insight, we propose Re2Search++, a process-supervised agent that achieves substantial improvements on multi-hop information-seeking benchmarks, especially in out-of-domain settings. Performance gains are driven primarily by higher-quality search queries rather than answer optimization alone, and the learned search critics transfer across models, including proprietary LLMs. These findings show that supervising the search process produces more reliable and generalizable information-seeking agents.

## 背景與目的
大型語言模型正將網頁搜尋從文件排序轉向答案合成，並逐漸部署為自主代理式搜尋系統，能迭代與外部知識源互動。然而，構建高效搜尋代理仍具挑戰，因難以產生高品質的中間搜尋步驟。既有方法多採結果監督，僅獎勵最終答案正確，導致獎勵作弊與過度依賴參數記憶，限制跨領域泛化。本文旨在將監督從最終答案轉移至搜尋過程，提出 RAG-Gym 框架並發現推理反思為關鍵能力，進而設計 Re2Search++，提升多跳資訊尋找任務的可靠性與泛化性。

## 方法
RAG-Gym 將搜尋過程建模為可訓練的環境，輸入為用戶查詢，輸出為最終答案與一系列中間動作（查詢生成、文件檢索、推理反思）。架構包含三大模組：(1) 代理策略網路，根據當前狀態產生下一步動作；(2) 過程評論模型，對每個中間動作給予標量獎勵，評估查詢品質、檢索相關性與推理一致性；(3) 反思機制，讓代理在生成查詢前先對歷史資訊進行自我檢核，產生推理痕跡。訓練目標採用過程監督損失，結合動作級別的獎勵信號與策略梯度最佳化，並對評論模型進行參數優化以提升動作評估準確度。推論時，代理依序執行查詢生成→檢索→反思→更新狀態，直到達到終止條件再合成答案。與傳統結果監督不同，RAG-Gym 直接優化中間查詢品質，並證明學習到的評論模型可跨模型遷移，包括專有 LLM。Re2Search++ 在此基礎上加強反思模組並採用更精細的動作評分，形成完整的過程監督代理。

## 結果
作者報告 Re2Search++ 在多跳資訊尋找基準上顯著優於結果監督基線，尤其在域外設定表現更佳；效能提升主要源於生成的查詢品質提高，而非單純答案優化。學習到的搜尋評論模型能遷移至不同規模與專有模型。摘錄未提供可驗證數字，僅能觀察到定性結論：過程監督能產出更可靠且泛化性更強的代理。

## 限制與展望
目前僅在模擬環境與特定多跳基準驗證，真實網頁搜尋的噪聲、動態更新與延遲未充分評估；評論模型的遷移性雖跨模型但未測試極端領域偏移；訓練需大量標註過程資料，成本較高；部署時需考慮即時檢索與推理延遲的權衡。後續研究可探索線上自適應更新、更輕量的評論架構以及與人類反饋結合的混合監督。
