# 論文 03：Intent-driven embodied artificial intelligence.

- 日期：2026-10-02
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯性表達，限制因果連貫、長時程一致性與價值對齊。本文旨在綜述近期進展，並提出意圖驅動具身人工智慧（IDEAI）作為系統層級組織框架，使意圖成為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，推動可解釋決策、自適應任務分解與價值一致行為。

## 方法
問題設定與輸入輸出：IDEAI 將具身代理視為在開放世界中接收人類高層目標、環境感觀資料（視覺、語言、本體感覺等）為輸入，輸出具體行動序列。整體架構採四層概念組織：1) 語義錨定層，將原始多模態感觀映射至共享語義空間，建立符號與感觀的對應；2) 概念生成與學習層，在此語義空間上學習可組合的概念表示，支援新任務的快速泛化；3) 意圖建模層，將人類目標與環境約束轉化為顯性、可修訂的意圖結構，意圖具備因果鏈結與可驗證性；4) 價值對齊層，引入價值約束機制，確保意圖推演與行動規劃符合安全與社會規範。核心模組包含跨模態對齊編碼器、概念圖神經網路、意圖推理引擎（如規劃圖搜索或神經符號推理）與價值審核模組。資料前處理著重於多模態對齊、語義標註與意圖標註，但摘錄未給具體資料集、特徵維度或編碼細節。訓練目標與損失函數：文中未明確列出損失形式，僅指出需讓意圖顯性化、可修訂並受價值約束，推測可能包含語義對齊損失、意圖一致性損失與價值違規懲罰項。推論流程：感觀→語義錨定→概念檢索→意圖生成與修訂→價值審核→行動規劃→執行，並支援線上意圖修正。與既有方法關鍵差異在於將意圖提升為系統層級的顯性中介建構，而非隱含於獎勵或提示中，強調可解釋性、長時程一致性與價值對齊。

## 結果
本文為綜述性質，摘錄未提供可驗證數字。研究綜合具身智能近期進展，提出意圖驅動具身人工智慧（IDEAI）框架，將意圖定義為人類目標、環境約束與代理行為間明確、可修訂、可驗證的中介建構。提出四層概念架構：語義錨定、概念生成與學習、意圖建模與價值對齊，闡述顯性意圖如何調解感知、認知與行動。分析現有技術在意圖至執行管線中的失效模式，指出隱性意圖導致因果連貫性、長時程一致性與價值對齊受限。結論指出，顯性化意圖可支援可解釋決策、自適應任務分解與價值一致行為，為推動具身智能邁向穩健、可社會部署系統提供統一視角。

## 限制與展望
本文為綜述與概念框架，缺乏實際系統實作、基準測試與大規模實證驗證，無法確認四層架構在真實機器人或模擬環境中的效能與擴展性。語義錨定、概念學習與意圖推理的具體演算法、計算複雜度、資料需求與訓練穩定性均未說明。價值對齊機制的形式化定義、衝突解決策略與法律倫理合規性亦待進一步研究。後續工作需建立標準化評測協議、公開基準資料集，並探討線上意圖修訂的實時性與安全保證。
