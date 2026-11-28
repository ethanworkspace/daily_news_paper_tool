# 論文 01：Intent-driven embodied artificial intelligence.

- 日期：2026-11-19
- 來源層級：Tier 1（頂級期刊）
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致「意圖」鮮少被顯性表達，進而限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述近期進展，並提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級的組織框架，使意圖成為人類目標、環境約束與代理行為之間可顯性、可修訂、可驗證的中介建構，提供統一視角推動具身 AI 走向可部署、社會可接受的智慧系統。

## 方法
本文提出四層概念架構，作為 IDEAI 的核心組織： 1. 語義錨定：將原始感知訊號（視覺、語言、本體感覺等）映射為具備共享語義空間的表示，建立感知與符號層的對應關係。 2. 概念生成與學習：在語義空間上進行抽象概念的發現、組合與持續學習，支援跨任務的知識複用與泛化。 3. 意圖建模：將人類高層目標、環境約束與代理內部狀態整合為顯性、可修訂的意圖表徵，意圖具備結構化、可驗證特性，並能在執行過程中動態更新。 4. 價值對齊：引入價值約束機制，確保意圖衍生的行動符合安全、倫理與社會規範，提供可解釋的決策依據。 整體流程為：感知經語義錨定進入概念層，概念層支撐意圖生成與修訂，意圖再經價值對齊檢查後轉化為具體行動計畫，形成感知‑認知‑行動的閉環。與既有方法的關鍵差異在於將「意圖」顯性化為可檢視、可修正的中介結構，而非隱含於獎勵函數或提示中，從而提升因果推理、長時程規劃與價值一致性。

## 結果
本文為綜述性質，未呈現實驗數據、基線比較或消融研究等可驗證數字。摘錄未提供可驗證數字。作者以定性分析指出：現有相關性驅動方法在因果連貫、長時程一致與價值對齊上存在系統性失效；IDEAI 框架透過顯性意圖與四層架構，能改善可解釋決策、自適應任務分解與價值一致行為，為開放式、人機互動及安全關鍵具身領域提供統一視角。

## 限制與展望
作為理論綜述，IDEAI 缺乏實證驗證與具體實作細節，未提供基準測試、計算複雜度或部署案例。四層架構的具體模組設計、訓練目標、損失函數與最佳化策略仍待後續研究具體化。評估面向僅限定性論證，缺少量化指標與跨領域泛化證據。潛在風險包括意圖表徵的過度剛性、價值對齊機制的文化依賴性，以及在真實機器人平台上的即時性與資源限制。後續研究需著重於具體算法實作、大規模實驗驗證、可擴展的意圖修訂機制與跨文化價值對齊框架。
