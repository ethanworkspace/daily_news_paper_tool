# 論文 03：Intent-driven embodied artificial intelligence.

- 日期：2026-10-09
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務特定獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫性、長時程一致性與價值對齊。本文旨在綜述最新進展，並提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為可修訂、可驗證的中介建構，連結人類目標、環境約束與代理行為，提供統一視角推動具身 AI 走向穩健、可社會部署的智慧系統。

## 方法
本文提出四層概念架構作為 IDEAI 的核心組織： 1. 語義奠基層：將多模態感知資料（視覺、語言、本體感覺）映射至共享語義空間，建立實體、關係與動作的符號化表示，作為後續推理的基礎。 2. 概念生成與學習層：利用大型語言模型與結構化知識圖譜，從語義表示中抽取或生成可組合的概念原語，支援概念的持續擴充與泛化。 3. 意圖建模層：將人類高層目標轉換為顯式、可修訂的意圖表徵，包含意圖分解、時序規劃與不確定性量化，使意圖成為感知‑認知‑行動管線的中介變數。 4. 價值對齊層：引入價值函數與約束機制，對意圖執行過程進行可驗證的安全性、倫理與社會規範檢查，確保行為與人類價值一致。 架構上，意圖在四層間雙向流動：語義奠基提供證據，概念層供給抽象原語，意圖層進行規劃與修訂，價值層施加約束並回饋修正。作者並分析現有技術在意圖到執行管線中的常見失效模式（如隱性目標導致的因果斷裂、長時程規劃漂移、價值衝突），指出顯式意圖可提升可解釋決策、自適應任務分解與價值一致行為。

## 結果
摘錄未提供可驗證數字。本文為綜述性質，主要結論為：現有具身 AI 方法多隱性處理意圖，導致因果連貫性、長時程一致性與價值對齊不足；提出的 IDEAI 四層框架能將意圖顯式化、可修訂且可驗證，理論上可改善可解釋決策、自適應任務分解與價值一致行為，為推動具身 AI 走向穩健、可社會部署提供統一視角。

## 限制與展望
本文為理論綜述，缺乏實證實驗驗證四層架構在具體機器人或模擬環境中的效能；框架層次與模組界定較為抽象，未給出具體模型架構、訓練目標或基準測試細節。意圖的顯式表徵、修訂機制與價值對齊約束在開放世界中的可擴展性、計算成本與即時性仍待探索。此外，價值對齊層依賴人類標註的價值函數，可能引入主觀偏誤與文化差異。後續研究需提供具體實作、標準化評估指標與大規模實驗，以驗證 IDEAI 是否能解決現有失效模式並滿足安全關鍵應用需求。
