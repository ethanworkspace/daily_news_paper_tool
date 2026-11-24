# 論文 01：Beyond Efficiency: A Systematic Survey of Resource-Efficient Large Language Models

- 日期：2026-10-24
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
大型語言模型（LLM）參數規模快速增長，導致計算、記憶體、能源、資金與網路通訊等多維資源消耗劇增，嚴重限制學術、醫療等資源受限環境的應用與永續發展。現有研究多針對單一資源或特定階段提出優化策略，缺乏跨資源、跨生命週期的系統性整理與統一評估標準，難以公平比較各方法優劣。本文旨在填補此缺口，提供首份專注於 LLM 資源效率的系統性綜述，建立分類體系、標準化指標與開放論文清單，為研究者與實務者提供全景參考。

## 方法
本綜述採取系統性文獻回顧方法，首先界定 LLM 生命週期四大階段：架構設計、預訓練、微調與系統設計。接著將關鍵資源劃分為計算、記憶體、能源、財務與網路通訊五類，並依資源優化目標建立雙維度分類法（資源類型 × 生命週期階段）。對每類技術進一步梳理核心機制，例如：模型壓縮（剪枝、量化、知識蒸餾）、高效注意力機制（稀疏注意力、線性注意力）、參數共享與動態路由、分散式訓練與推理系統優化（張量/流水線/資料並行、激活重計算、混合精度）、以及硬體感知排程與能源感知訓練策略。綜述同時蒐集並整理常用評估基準（如 GLUE、SuperGLUE、MMLU、代碼生成基準）與資源效率指標（FLOPs、參數量、峰值記憶體、訓練/推理延遲、能耗、碳排放、雲端成本），提出標準化報告範本以利跨研究比較。最後建立持續更新的開放論文庫（GitHub），並依分類法標註每篇文獻的優化資源與適用階段，形成可檢索的知識圖譜。

## 結果
綜述呈現四大貢獻：(1) 涵蓋架構到系統全生命週期的資源效率技術全景圖；(2) 建立以資源類型為主軸的系統性分類法，揭示不同資源間的權衡與映射關係；(3) 提出標準化評估指標與資料集清單，促進公平比較；(4) 識別現有研究的缺口（如跨資源聯合優化理論不足、閉源模型難以應用壓縮技術、評估指標缺乏實證驗證）並指出未來方向。摘錄未提供可驗證數字，僅以定性結論說明各類技術在不同資源上的相對優勢。

## 限制與展望
作為綜述，本文覆蓋範圍受限於截止 2024 年底的公開文獻，極新發表的方法可能未納入；分類法雖具體系性，但實際部署中多資源同時受限的聯合優化案例較少，難以量化權衡；標準化指標尚未經大規模實證驗證其預測實際部署成本的準確性；且閉源模型與專有資料集限制了部分壓縮與蒸餾技術的可行性分析。後續研究可朝向跨資源聯合優化理論、開放基準建立、硬體感知自動化搜尋與長期能源/碳足跡追蹤等方向深入。
