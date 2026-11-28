# 論文 01：Intent-driven embodied artificial intelligence.

- 日期：2026-11-02
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯式表達，進而限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述最新進展，並提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為人類目標、環境約束與代理行為之間可顯式、可修訂、可驗證的中介建構，期望為具身 AI 提供統一視角，推動其邁向可部署、社會可接受的智慧系統。

## 方法
本文提出的 IDEAI 框架採四層概念組織，分別為語義奠基、概念生成與學習、意圖建模、價值對齊。第一層語義奠基負責將多模態感知資料（視覺、語言、本體感覺等）映射至共享語義空間，使代理能以統一表示理解環境與指令。第二層概念生成與學習在此語義空間上抽象出可重用的概念與關係，支援跨任務的知識遷移與組合。第三層意圖建模將人類高層目標轉化為顯式、可修訂且可驗證的意圖表徵，並作為感知、認知與行動之間的中介，確保決策過程的因果連貫與長時程一致。第四層價值對齊在意圖之上引入價值約束機制，使代理行為符合安全、倫理與社會規範。框架並分析意圖到執行管線中常見失效模式（如意圖隱性導致的目標漂移、規劃不一致、價值衝突），指出現有技術多在單層優化而缺乏跨層協調。整體推理流程為：感知→語義奠基→概念檢索→意圖生成與修訂→價值檢查→行動規劃與執行，並在執行中持續回饋修正意圖。此設計強調意圖的顯式性、可修訂性與可驗證性，作為統一具身系統感知‑認知‑行動循環的核心中介。

## 結果
摘錄未提供可驗證數字。作者以綜述形式報告：現有具身 AI 方法多為相關性驅動，意圖隱性導致因果連貫性、長時程一致性與價值對齊不足；提出的 IDEAI 四層框架能將意圖顯式化、可修訂、可驗證，並分析意圖到執行管線的常見失效模式，指出跨層協調缺失為關鍵缺口。定性結論顯示，若在需要結構化處的場景使意圖顯式化，可支援可解釋決策、自適應任務分解與價值一致行為，為具身 AI 邁向穩健、可社會部署系統提供統一視角。

## 限制與展望
本文為理論綜述與概念框架提出，缺乏實證實驗、基線比較與量化指標，無法驗證四層架構在具體機器人或模擬環境中的實際效能。框架僅於概念層級說明意圖的顯式化機制，未具體定義語義奠基、概念學習、意圖建模與價值對齊的具體演算法、資料需求或計算複雜度。此外，價值對齊層涉及社會倫理規範的形式化表達與衝突解決，目前仍屬開放問題。後續研究需在具體任務上實作並評估各層模組、跨層協調機制與長時程部署的安全性，並探討意圖修訂的即時性與人機互動介面設計。
