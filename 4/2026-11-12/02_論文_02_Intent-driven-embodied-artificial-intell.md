# 論文 02：Intent-driven embodied artificial intelligence.

- 日期：2026-11-12
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
具身人工智慧作為發展更通用、適應性強的智慧系統範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務特定獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫、長時程一致性與價值對齊。本文旨在綜述進展並提出意圖驅動具身人工智慧（IDEAI）作為系統層級組織框架，使意圖成為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，推動可解釋決策、自適應任務分解與價值一致行為。

## 方法
本文提出四層概念架構作為 IDEAI 的核心組織：第一層語義奠基，將多模態感知資料映射至共享語義空間，建立環境實體與語言符號的對應；第二層概念生成與學習，利用大型語言模型與結構化知識圖譜，從語義表示中抽取可組合的概念並支援持續學習；第三層意圖建模，將人類高層目標轉化為顯式、可修訂的意圖表徵，包含意圖分解、時序規劃與不確定性量化，使意圖成為感知、認知與行動之間的中介；第四層價值對齊，引入價值函數與約束機制，確保意圖執行過程符合安全、倫理與社會規範。論文並分析意圖到執行管線中常見失效模式（如意圖模糊、規劃偏離、價值衝突），說明顯式意圖如何提供可驗證的中介結構，支援可解釋決策、自適應任務分解與長時程一致性。

## 結果
摘錄未提供可驗證數字。本文為綜述性質，主要結論為：現有具身 AI 多採隱性目標，導致因果連貫與價值對齊不足；提出的 IDEAI 四層框架能將意圖顯式化、可修訂且可驗證，進而改善可解釋性、長時程一致性與安全性；並指出顯式意圖可緩解意圖模糊、規劃偏離等失效模式，為開放世界、人機互動與安全關鍵場景提供統一視角。

## 限制與展望
本文為理論綜述，缺乏實證實驗與基線比較，無法量化 IDEAI 在具體任務上的效能提升；四層架構的具體實作細節、計算複雜度與擴展性尚未驗證；價值對齊機制的形式化定義與跨文化泛化仍待研究；後續需在真實機器人平台進行端到端評估，並探討意圖修訂的即時性與人類介入機制。
