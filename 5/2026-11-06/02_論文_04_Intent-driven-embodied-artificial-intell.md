# 論文 04：Intent-driven embodied artificial intelligence.

- 日期：2026-11-06
- 來源層級：Tier 1
- 期刊/會議/來源：National science review
- Venue：National science review
- 發布時間：2026-11-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43054956/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13781017/
- DOI：10.1093/nsr/nwag476
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1836（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Embodied Artificial Intelligence (Embodied AI) has emerged as a promising paradigm for developing more general and adaptive intelligent systems, emphasizing that intelligence emerges from continuous interaction among perception, cognition and action in real-world environments. Recent advances increasingly integrate large language models and multimodal learning into embodied agents; however, most existing approaches remain correlation-driven, relying on implicit objectives, task-specific rewards or prompt-level instructions. As a consequence, intent is rarely represented explicitly, limiting causal coherence, long-horizon consistency and robust value alignment in open-world settings. In this review, we synthesize recent progress in Embodied AI and articulate Intent-Driven Embodied Artificial Intelligence (IDEAI) as a system-level organizing framework in which intent functions as an explicit, revisable and verifiable mediating construct between human goals, environmental constraints and agent behavior. Building on this synthesis, we propose a four-layer conceptual organization-semantic grounding, concept generation and learning, intent modeling and value alignment-that clarifies how explicit intent mediates perception, cognition and action in embodied systems. We analyze how existing techniques address recurring failure modes along the intent-to-execution pipeline and highlight the limitations that arise when intent remains implicit. By making intent explicit, revisable and value-constrained where such structure is needed, IDEAI supports interpretable decision-making, adaptive task decomposition and value-consistent behavior in open-ended, human-interactive and safety-critical embodied domains, providing a unifying perspective for advancing Embodied AI toward robust, socially deployable intelligent systems.

## 背景與目的
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫、長時程一致性與價值對齊。本文綜合近期進展，提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，旨在提供可解釋決策、自適應任務分解與價值一致行為的統一視角，推動具身 AI 走向穩健、可社會部署的智慧系統。

## 方法
本文提出的 IDEAI 採四層概念架構：1. 語義奠基：將原始感知訊號映射為具備共享語義的表示，建立環境與代理之間的共同詞彙基礎。2. 概念生成與學習：在語義空間上進行抽象概念的形成、組合與持續更新，使代理能從經驗中提煉可複用的知識單元。3. 意圖建模：將人類高層目標、環境約束與代理內部狀態轉化為顯式、可修訂的意圖表徵，並提供驗證機制確保意圖與行為一致。4. 價值對齊：在意圖層之上引入價值約束，使決策過程受社會規範、安全準則與長期目標引導。框架強調意圖作為中介，串聯感知→認知→行動管線，並指出現有技術在意圖隱性時常見的失效模式（如因果斷裂、長時程偏移、價值衝突）。然而，摘錄未提供具體模型架構、神經網路細節、訓練目標、損失函數、最佳化策略、推論流程或資料前處理方式，僅停留於概念層級描述。

## 結果
本綜述綜合具身人工智慧近期進展，提出意圖驅動具身人工智慧（IDEAI）框架，確立意圖為明確、可修訂、可驗證的中介建構。研究建構四層概念組織：語義奠基、概念生成與學習、意圖建模與價值對齊，闡明顯性意圖如何調解感知、認知與行動。分析顯示，現有方法多為相關驅動，依賴隱性目標、任務專用獎勵或提示指令，導致意圖鮮少顯性表達，限制因果連貫、長時程一致性與價值對齊。將意圖顯性化、可修訂且受價值約束，可支援可解釋決策、自適應任務分解與價值一致行為，為推進具身AI邁向穩健、可社會部署智慧系統提供統一視角。摘錄未提供可驗證數字。

## 限制與展望
限制在於：(1) 僅提出概念架構，缺乏實證驗證與量化基線；(2) 未詳細說明各層具體演算法、資料表示、訓練目標與推論機制，難以直接實作；(3) 價值對齊的形式化定義與衡量指標未給出；(4) 框架對開放世界動態環境的擴展性、計算效率與部署安全性仍待後續研究探索。
