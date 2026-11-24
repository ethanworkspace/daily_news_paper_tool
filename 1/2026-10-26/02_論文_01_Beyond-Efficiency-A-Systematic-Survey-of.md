# 論文 01：Beyond Efficiency: A Systematic Survey of Resource-Efficient Large Language Models

- 日期：2026-10-26
- 來源層級：Tier 2
- 期刊/會議/來源：ACM Computing Surveys
- Venue：ACM Computing Surveys
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://doi.org/10.1145/3845797
- PDF：https://arxiv.org/pdf/2401.00625
- DOI：10.1145/3845797
- arXiv：2401.00625
- 影響指標：2yr_mean_citedness=57.06, h_index=406, i10_index=3033 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: ACM Computing Surveys
- 引用數：240
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2401.00625
- 全文字數：213471（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers
- 配對 Repo：tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers

## 摘要
The burgeoning field of Large Language Models (LLMs), exemplified by sophisticated models like OpenAI’s ChatGPT, represents a significant advancement in artificial intelligence. These models, however, bring forth substantial challenges in high consumption of computational, memory, energy, and financial resources, especially in environments with limited resource capabilities. This survey aims to systematically address these challenges by reviewing a broad spectrum of techniques designed to enhance the resource efficiency of LLMs. We categorize methods based on their optimization focus—covering computational, memory, energy, financial, and network resources—and their applicability across various stages of an LLM’s lifecycle, including architecture design, pre-training, fine-tuning, and system design. Additionally, the survey introduces a nuanced categorization of resource efficiency techniques by their specific resource types, which uncovers the intricate relationships and mappings between various resources and corresponding optimization techniques. A standardized set of evaluation metrics and datasets is also presented to facilitate consistent and fair comparisons across different models and techniques. By offering a comprehensive overview of the current state-of-the-art and identifying open research avenues, this survey serves as a foundational reference for researchers and practitioners, aiding them in developing more sustainable and efficient LLMs in a rapidly evolving landscape. To make the field more accessible to interested beginners, we not only make a systematic review of existing works and a highly structured taxonomy of resource-efficient LLMs but also release a website including a constantly-updated article list https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers.

## 背景與目的
大型語言模型（LLM）參數規模快速增長，導致計算、記憶體、能源、財務與網路通訊等資源消耗劇增，嚴重限制資源受限環境（如學術實驗室、醫療領域）的應用與部署。現有綜述多聚焦模型壓縮或推理加速，缺乏跨資源類型與生命週期階段的系統性分類，且評估指標未標準化，難以公平比較各技術。本文旨在建立資源高效 LLM 的完整分類體系，涵蓋架構設計、預訓練、微調與系統設計四階段，並提供標準化評估指標與資料集，填補領域空白，為永續 AI 發展提供基礎參考。

## 方法
本文採系統性文獻綜述方法，建立資源高效 LLM 的多維分類學。首先定義五大關鍵資源類別：計算（處理能力）、記憶體（儲存容量）、能源（電力消耗）、財務（基礎設施與營運成本）、通訊成本（頻寬與延遲）。依資源優化目標與 LLM 生命週期階段（架構設計、預訓練、微調、系統設計）雙軸構建分類框架，揭示各資源類型與對應優化技術的映射關係。核心模組包含：(1) 資源分類學：將既有技術按優化資源類型歸類，如計算優化含稀疏注意力、知識蒸餾；記憶體優化含量化、參數共享；能源優化含硬體感知排程；財務優化含高效資料選擇；通訊優化含分散式訓練策略。(2) 生命週期映射：分析各階段適用技術，如架構設計階段的高效注意力機制、預訓練階段的混合精度訓練、微調階段的 LoRA 等參數高效方法、系統設計階段的流水線並行與張量並行。(3) 評估標準化：整理通用指標（如 FLOPs、參數量、延遲、吞吐量、能耗、碳排放、訓練成本）與基準資料集，支援多目標公平比較。方法論上採納 PRISMA 風格系統性檢索，並發布持續更新的論文清單網站（GitHub）以利社群追蹤最新進展。關鍵差異在於首創「資源類型為主軸」的分類法，而非單一技術視角，並明確處理多資源權衡的多目標優化本質。

## 結果
本文產出三大成果：(1) 完整分類學，涵蓋五大資源類型與四大生命週期階段的技術映射表，系統梳理超過百篇代表性工作；(2) 標準化評估體系，定義統一指標集（計算、記憶體、能源、財務、通訊）與基準資料集，解決跨技術比較缺乏共同基準的問題；(3) 識別六大開放挑戰：自回歸生成低並行度、注意力機制平方複雜度、擴展律遞減報酬、封閉源碼模型限制、多目標評估指標缺失、專有訓練資料依賴。摘錄未提供可驗證數字，定性結論顯示資源高效技術呈現多樣化且權衡複雜，需跨層級協同優化。

## 限制與展望
作為綜述，本文固有限制：(1) 文獻覆蓋以截稿前公開論文為主，最新技術可能遺漏，雖有持續更新網站緩解；(2) 分類邊界可能存在重疊（如量化同時影響記憶體與計算），實際部署需綜合考量；(3) 評估指標標準化建議尚未經大規模社群驗證採納度未知；(4) 封閉源碼模型與專有資料限制了部分技術的適用性分析；(5) 缺乏實證實驗驗證分類法的實際指導效力。後續研究建議：建立動態基準測試平台、探索跨資源聯合優化理論框架、關注綠能計算與聯邦學習結合、推動開放模型生態降低準入門檻。
