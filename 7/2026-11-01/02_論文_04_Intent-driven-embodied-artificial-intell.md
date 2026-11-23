# 論文 04：Intent-driven embodied artificial intelligence.

- 日期：2026-11-01
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務特定獎勵或提示層級指令，導致意圖鮮少被顯性表達，限制因果連貫、長時程一致性與價值對齊。本文旨在綜述近期進展，提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為可修訂、可驗證的中介建構，連結人類目標、環境約束與代理行為，提供可解釋決策、自適應任務分解與價值一致行為的統一視角。

## 方法
本文提出四層概念架構作為 IDEAI 的核心組織： 1. 語義奠基：將多模態感知資料（視覺、語言、本體感覺）映射至共享語義空間，建立實體、關係與動作的符號化表示，作為後續推理的基礎。 2. 概念生成與學習：利用大型語言模型與結構化知識圖譜，從語義奠基層抽象出可組合的概念原語，支援概念的增量學習、組合與泛化。 3. 意圖建模：引入顯性意圖表示，將人類高層目標轉換為可修訂、可驗證的意圖物件，包含目標狀態、約束條件與優先序，並透過意圖推理模組進行分解、排程與一致性檢查。 4. 價值對齊：在意圖執行前後引入價值函數與安全約束，透過價值驗證機制確保行為符合社會規範與安全準則。 意圖至執行管線：感知→語義奠基→概念組合→意圖生成→價值驗證→動作規劃→執行，並提供回饋迴路以修訂意圖。與既有相關性驅動方法的關鍵差異在於：意圖被顯性化為可檢查的中介結構，而非隱含於獎勵或提示中，從而支援因果連貫、長時程一致與可解釋決策。

## 結果
本文為綜述性質，摘錄未提供可驗證數字。作者通過文獻綜合指出：現有具身 AI 多為相關性驅動，意圖隱性導致因果連貫、長時程一致與價值對齊不足；提出的 IDEAI 四層框架能將意圖顯性化、可修訂且可驗證，進而支援可解釋決策、自適應任務分解與價值一致行為，為開放世界、人機互動與安全關鍵領域提供統一視角。

## 限制與展望
作為綜述，IDEAI 仍屬概念框架，缺乏實證實驗驗證其在具體機器人平台上的效能與擴展性；四層架構的具體模組設計、訓練目標與優化策略未在文中給出細節，難以直接複製。評估指標僅停留於定性描述，缺少標準化基準與量化比較。後續研究需在真實具身系統中落地各層模組、建立可測試的意圖表示與價值對齊基準，並探討意圖修訂機制的即時性與計算開銷。
