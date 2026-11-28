# 論文 03：Intent-driven embodied artificial intelligence.

- 日期：2026-11-28
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務特定獎勵或提示層級指令，導致意圖鮮少被顯性表達，限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述最新進展，提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為可修訂、可驗證的中介建構，連結人類目標、環境約束與代理行為，提供可解釋決策、自適應任務分解與價值一致行為的統一視角，推動具身 AI 邁向可社會部署的穩健智慧系統。

## 方法
方法層面上，IDEAI 採四層概念架構： 1. 語義奠基：將原始感知資料（視覺、語言、本體感覺）映射至共享語義空間，建立實體、關係與動作的符號化表示，作為後續推理的基礎。 2. 概念生成與學習：利用大型語言模型與多模態對比學習，從交互經驗中抽取可組合的概念原語，並透過自我監督或少樣本微調持續擴充概念庫，支援開放詞彙理解。 3. 意圖建模：引入顯性意圖變數，將人類高層目標、環境約束與代理內部狀態編碼為結構化意圖圖（intent graph），包含目標分解、前置條件、後置條件與不確定性估計，並提供可修訂機制（如人機對話、線上重規劃）使意圖在執行過程中可動態更新。 4. 價值對齊：在意圖圖之上疊加價值函數或憲法式約束，透過強化學習、偏好學習或形式化驗證，確保生成的行動序列符合安全、倫理與社會規範。 整體流程為：感知→語義奠基→概念檢索→意圖生成/修訂→價值檢查→動作規劃→執行→環境回饋→意圖更新。關鍵差異在於將意圖從隱性獎勵或提示提升為可檢視、可修訂、可驗證的一級建構，並以四層模組化介面串接感知、認知與行動，區別於傳統端到端或提示式具身代理。

## 結果
本文為綜述與概念框架論文，未執行實證實驗，因此摘錄未提供可驗證數字。作者以定性分析指出：現有相關性驅動方法在長時程任務、因果推理與價值對齊上易失效；IDEAI 透過顯性意圖與四層架構可改善可解釋性、自適應分解與價值一致性，並列舉典型失效模式（如目標漂移、語義錯位、安全違規）說明框架如何對應解決。

## 限制與展望
限制在於：(1) 僅提出概念架構，缺乏具體實作細節、基準測試與消融實驗，難以量化效能提升；(2) 意圖表示、價值函數設計與可修訂機制的具體演算法仍待開發，可能面臨擴展性與即時性挑戰；(3) 評估指標僅停留於定性失效模式分析，缺少標準化開放世界基準；(4) 部署時需解決人機意圖協商的介面、隱私與法律合規風險。後續研究建議：建立統一意圖基準、開發可驗證的意圖修訂協議、結合形式化驗證與線上學習進行實證驗證。
