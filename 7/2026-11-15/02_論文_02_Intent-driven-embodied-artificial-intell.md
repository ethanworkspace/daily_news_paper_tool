# 論文 02：Intent-driven embodied artificial intelligence.

- 日期：2026-11-15
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
具身人工智慧（Embodied AI）被視為發展更通用、適應性更強智慧系統的新範式，強調智慧源於感知、認知與行動在真實環境中的持續互動。近年雖大量引入大型語言模型與多模態學習，但現有方法多為相關性驅動，依賴隱性目標、任務專用獎勵或提示層級指令，導致意圖鮮少被顯式表達，限制因果連貫性、長時程一致性與價值對齊在開放世界中的穩健性。本文旨在綜述最新進展，並提出「意圖驅動具身人工智慧」（IDEAI）作為系統層級組織框架，將意圖定義為人類目標、環境約束與代理行為之間可修訂、可驗證的中介建構，以推動可解釋決策、自適應任務分解與價值一致行為，為具身 AI 邁向社會可部署的穩健智慧系統提供統一視角。

## 方法
方法上，作者並未提出具體演算法或實驗系統，而是建構一個四層概念架構作為 IDEAI 的組織原則。第一層「語義奠基」負責將原始感知訊號（視覺、語言、本體感覺等）映射為可被符號操作的語義表示，強調多模態對齊與情境化理解。第二層「概念生成與學習」在語義基礎上，透過大型語言模型、知識圖譜或自我監督學習，抽取可重組的概念單元，支援抽象推理與泛化。第三層「意圖建模」將人類指令、環境約束與代理內部狀態轉化為顯式、可修訂的意圖表徵，採用層次化規劃、因果圖或程式化意圖語言，使意圖可被驗證、回溯與動態更新。第四層「價值對齊」引入安全規範、倫理準則與人類偏好模型，對意圖進行約束檢查與優化，確保執行行為符合價值一致性。作者進一步分析意圖到執行管線中常見失效模式——如意圖模糊、概念漂移、獎勵駭客與長時程規劃崩解——並說明現有技術（提示工程、強化學習、規劃器、世界模型）如何在各層緩解這些問題。關鍵差異在於將意圖從隱性獎勵或提示提升為可檢視、可修訂的中介結構，並以四層架構統一感知、認知與行動的耦合關係。

## 結果
本文為綜述性質，摘錄未提供可驗證數字。作者報告的主要結論為：現有具身 AI 多採隱性目標，導致因果連貫性、長時程一致性與價值對齊不足；提出的 IDEAI 四層框架能將意圖顯式化、可修訂且可驗證，進而支援可解釋決策、自適應任務分解與價值一致行為；並指出現有技術在各層可部分緩解失效模式，但缺乏統一的意圖中介機制。定性上，IDEAI 被定位為推動具身 AI 邁向社會可部署、穩健智慧系統的統一視角。

## 限制與展望
限制方面，本文僅為理論綜述，缺乏實證實驗驗證四層架構的具體效能；框架的具體實現細節（如意圖表徵形式、價值對齊優化算法）未給出，難以直接部署；分析依賴現有文獻範圍，可能遺漏最新具身智能體系統；且未討論計算資源、實時性與安全認證等工程落地挑戰。後續研究需在具體機器人或模擬平台上實作並量化評估，並探討意圖修訂機制的收斂性與人機協作中的動態價值協商。
