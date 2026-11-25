# 論文 03：Intent-driven embodied artificial intelligence.

- 日期：2026-11-21
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯性表達，進而限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述近期進展，並提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，期望提供統一視角推動具身 AI 走向可部署、社會可接受的智慧系統。

## 方法
本文屬綜述性質，未提出具體可訓練模型，而是構建一個四層概念架構作為 IDEAI 的組織原則。第一層「語義錨定」負責將原始感知訊號（視覺、語言、本體感覺等）映射為可被符號操作的語義表示，建立感知與符號空間的對應。第二層「概念生成與學習」在語義基礎上，透過結構化學習（如圖神經網路、原型學習或語言引導的概念發現）形成可組合、可泛化的概念庫，支援後續推理。第三層「意圖建模」將人類高層目標、環境約束與代理內部狀態轉化為顯性、可修訂的意圖表徵，採用層次化規劃、因果圖或程式合成等機制，使意圖能在執行過程中動態修正與驗證。第四層「價值對齊」引入價值函數、偏好學習或憲法式約束，確保意圖衍生的行動符合安全、倫理與社會規範。整體流程為：感知→語義錨定→概念檢索/生成→意圖推導與修訂→價值檢查→行動執行，並強調意圖在管線中作為可觀測、可干預的中介變數，區別於傳統隱性目標或提示式控制。

## 結果
摘錄未提供可驗證數字。作者僅在概念層面闡述 IDEAI 如何解決意圖隱性導致的因果斷裂、長時程不一致與價值對齊失效等失效模式，並指出現有技術在語義錨定、概念學習、意圖建模與價值對齊四層的進展，但未呈現實驗基線、資料集規模或量化比較結果。定性結論為：顯性、可修訂、可驗證的意圖表徵能提升決策可解釋性、任務分解彈性與價值一致行為，為開放、人機互動與安全關鍵領域提供統一視角。

## 限制與展望
本文為理論綜述，缺乏實證驗證與基準測試，四層架構的具體實現細節、計算複雜度、資料需求與泛化能力均未量化分析。意圖的顯性表徵形式、修訂機制與驗證協議仍屬概念描述，缺乏標準化定義，難以直接部署於實體機器人或模擬環境。價值對齊層依賴人類偏好建模，潛在風險包括偏好獲取成本高、價值衝突解決不明確，以及在開放世界中價值函數可能過時。後續研究需著重於：將四層轉化為可訓練的端到端系統、設計意圖驗證基準、探討跨領域概念遷移與長時程意圖一致性評估。
