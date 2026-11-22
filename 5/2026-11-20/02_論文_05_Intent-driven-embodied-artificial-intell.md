# 論文 05：Intent-driven embodied artificial intelligence.

- 日期：2026-11-20
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
具身人工智慧（Embodied AI）近年結合大型語言模型與多模態學習，期望在真實環境中實現感知、認知與行動的持續互動。然而現有方法多為相關性驅動，依賴隱性目標、任務特定獎勵或提示層級指令，導致意圖鮮少被顯性表達，限制因果連貫性、長時程一致性與價值對齊。本文旨在綜述近期進展，提出意圖驅動具身人工智慧（IDEAI）作為系統層級組織框架，將意圖定義為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，並建立四層概念架構，以統一視角推動具身 AI 走向穩健、可社會部署的智慧系統。

## 方法
本文提出 IDEAI 框架，包含四層概念組織： 1. 語義奠基：將原始感知訊號映射為有意義的符號表示，建立感知與概念的連結。 2. 概念生成與學習：從奠基經驗中抽象形成可複用的概念結構，支援泛化與推理。 3. 意圖建模：將意圖顯性化為可修訂、可驗證的中介建構，連接人類目標、環境約束與代理行動，支援因果推理與長時程規劃。 4. 價值對齊：引入價值約束機制，確保意圖與人類價值、安全規範一致，提供行為評估準則。 框架闡述顯性意圖如何在感知、認知、行動管線中調解，並分析現有技術如何應對意圖到執行管線的常見失效模式（如目標錯位、規劃不一致），指出隱性意圖導致的局限。此為綜述性方法，未提出具體演算法或訓練目標，而是提供概念架構與分析視角。

## 結果
摘錄未提供可驗證數字。本文為綜述文章，主要結論為定性分析：IDEAI 框架透過顯性意圖表達，能支援可解釋決策、自適應任務分解與價值一致行為，為開放式、人機互動及安全關鍵具身領域提供統一視角。作者綜合現有技術，指出隱性意圖導致因果連貫性、長時程一致性與價值對齊不足，並證明顯性意圖可改善上述問題。

## 限制與展望
本文為概念性綜述，缺乏實證驗證與具體實作細節；四層架構的操作化定義、評估基準與量化指標未提出。框架可能過度抽象，難以直接指導系統建構；未討論計算複雜度、即時性需求與部署可行性。後續研究需開發具體實例化方法、建立基準測試、驗證安全性與價值對齊效果，並探討跨領域泛化能力。
