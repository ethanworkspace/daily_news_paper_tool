# 論文 04：Intent-driven embodied artificial intelligence.

- 日期：2026-11-03
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述近期進展，並提出意圖驅動具身人工智慧（IDEAI）作為系統層級組織框架，將意圖定義為可修訂、可驗證的中介建構，連結人類目標、環境約束與代理行為，以推動可解釋決策、自適應任務分解與價值一致行為。

## 方法
本文提出的 IDEAI 採四層概念架構，自下而上分別為：\n1. 語義奠基：將原始感知訊號（視覺、語言、本體感覺等）映射至共享語義空間，建立跨模態的實體與關係表示，作為後續意圖推理的基礎。\n2. 概念生成與學習：在語義空間上進行抽象概念的發現、組合與持續學習，使代理能從經驗中形成可重用的知識單元，支援新任務的快速泛化。\n3. 意圖建模：將人類高層目標、環境約束與代理內部狀態轉化為顯式、可修訂的意圖表徵，意圖具備因果結構、可驗證性與版本控制，並作為感知‑認知‑行動管線的中介變數。\n4. 價值對齊：在意圖層引入價值函數與約束機制，確保意圖演化與執行符合安全、倫理與社會規範，提供可審計的決策依據。\n方法論上，IDEAI 強調意圖在「意圖→執行」管線中作為可觀測、可干預的中介，分析現有技術（如提示工程、強化學習獎勵設計、規劃模組）如何處理常見失敗模式（意圖漂移、語義錯位、長時程規劃崩解），並指出隱性意圖導致的因果斷裂與價值偏移問題。由於屬綜述性質，文中未給出具體模型架構、損失函數、訓練流程或推演算法細節，僅提供概念層面的組織原則與系統級設計指導。

## 結果
本文為綜述文章，未進行實證實驗，因此摘錄未提供可驗證數字。作者從理論層面總結：顯式意圖機制可改善因果連貫性、長時程一致性與價值對齊；四層架構能統一語義奠基、概念學習、意圖建模與價值約束，為開放世界、人機互動與安全關鍵具身任務提供統一視角。質性結論指出，現有相關性驅動方法在意圖隱性時易出現意圖漂移、語義錯位與規劃失效，IDEAI 框架可作為後續具體模型設計的指導藍圖。

## 限制與展望
作為綜述，IDEAI 僅提出概念框架，缺乏具體演算法實作、基準測試與實證驗證，難以量化其對下游任務的提升幅度。四層抽象層級的邊界劃分在實際系統中可能模糊，語義奠基與概念學習的可擴展性、意圖修訂機制的即時性、價值函數的形式化定義皆待進一步研究。此外，框架假設具備完整的跨模態感知與語言理解能力，若感知模組錯誤將傳播至意圖層，造成安全風險。後續工作需開發可訓練的端到端模型、設計可驗證的意圖表示與價值對齊機制，並在真實機器人平台進行長時程、多任務評估。
