# 論文 03：Intent-driven embodied artificial intelligence.

- 日期：2026-09-19
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智能系統的新範式，強調智能源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫性、長時程一致性與價值對齊。本文旨在綜述最新進展，提出意圖驅動具身人工智慧（IDEAI）作為系統層級組織框架，將意圖定義為可修訂、可驗證的中介建構，連結人類目標、環境約束與代理行為，提供統一視角推動具身 AI 走向穩健、可社會部署的智能系統。

## 方法
方法層面上，本文並未提出具體演算法或模型架構，而是建構一個四層概念組織框架，作為 IDEAI 的系統級說明： 1. 語義錨定層：將原始感知資料（視覺、語言、本體感覺等）映射為可被符號操作的語義表示，建立環境實體與語言概念的對應關係。 2. 概念生成與學習層：在語義基礎上，透過大型語言模型與多模態學習產生抽象概念、關係圖譜與任務相關知識，支援泛化與組合推理。 3. 意圖建模層：將人類高層目標、環境約束與代理當前狀態整合，生成顯式、可修訂且可驗證的意圖表徵，作為感知‑認知‑行動管線的中介節點。 4. 價值對齊層：引入價值函數、安全約束與人類偏好機制，對意圖進行評估、修正與對齊，確保行動符合社會規範與安全要求。 框架強調意圖在管線中可被檢查、回溯與更新，並分析現有技術如何處理意圖到執行的常見失敗模式（如目標漂移、語義錯位、長時程規劃斷裂），指出隱性意圖導致的因果斷裂與價值偏移問題。整體而言，IDEAI 提供一個可解釋、可分解任務且價值一致的決策流程，為後續具體演算法設計提供統一理論基礎。

## 結果
本文為綜述性質，摘錄未提供可驗證數字。作者以定性方式總結現有具身 AI 研究在意圖顯式化上的不足，並闡述 IDEAI 框架如何解決因果連貫性、長時程一致性與價值對齊等反覆失敗模式。結論指出，將意圖設為可修訂、可驗證的中介建構，能支援可解釋決策、自適應任務分解與價值一致行為，為推動具身 AI 邁向穩健、可社會部署系統提供統一視角。

## 限制與展望
限制在於：本文僅提出概念框架，缺乏實證實驗、基線比較與量化指標，無法驗證四層架構在具體機器人或模擬環境中的效能；意圖表示的具體形式化、修訂機制與價值對齊演算法仍待具體化；評估僅停留於文獻分析，未涵蓋真實世界部署的安全性、延遲與資源限制。後續研究需將框架落地為可訓練模型、設計基準測試並探討跨領域泛化與人機協作中的倫理風險。
