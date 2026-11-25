# 論文 04：Beyond Efficiency: A Systematic Survey of Resource-Efficient Large Language Models

- 日期：2026-10-22
- 來源層級：Tier 2
- 期刊/會議/來源：ACM Computing Surveys
- Venue：ACM Computing Surveys
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://doi.org/10.1145/3845797
- PDF：https://arxiv.org/pdf/2401.00625
- DOI：10.1145/3845797
- arXiv：2401.00625
- 影響指標：2yr_mean_citedness=57.17, h_index=408, i10_index=3038 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: ACM Computing Surveys
- 引用數：239
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2401.00625
- 全文字數：213471（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers
- 配對 Repo：tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers

## 摘要
The burgeoning field of Large Language Models (LLMs), exemplified by sophisticated models like OpenAI’s ChatGPT, represents a significant advancement in artificial intelligence. These models, however, bring forth substantial challenges in high consumption of computational, memory, energy, and financial resources, especially in environments with limited resource capabilities. This survey aims to systematically address these challenges by reviewing a broad spectrum of techniques designed to enhance the resource efficiency of LLMs. We categorize methods based on their optimization focus—covering computational, memory, energy, financial, and network resources—and their applicability across various stages of an LLM’s lifecycle, including architecture design, pre-training, fine-tuning, and system design. Additionally, the survey introduces a nuanced categorization of resource efficiency techniques by their specific resource types, which uncovers the intricate relationships and mappings between various resources and corresponding optimization techniques. A standardized set of evaluation metrics and datasets is also presented to facilitate consistent and fair comparisons across different models and techniques. By offering a comprehensive overview of the current state-of-the-art and identifying open research avenues, this survey serves as a foundational reference for researchers and practitioners, aiding them in developing more sustainable and efficient LLMs in a rapidly evolving landscape. To make the field more accessible to interested beginners, we not only make a systematic review of existing works and a highly structured taxonomy of resource-efficient LLMs but also release a website including a constantly-updated article list https://github.com/tiingweii-shii/Awesome-Resource-Efficient-LLM-Papers.

## 背景與目的
大型語言模型（LLM）參數規模快速增長，導致計算、記憶體、能源、資金與網路通訊等資源消耗劇增，嚴重限制學術與資源受限環境的應用。現有研究多針對單一資源或特定階段提出優化，缺乏跨資源、跨生命週期的系統性歸納與統一評估標準。本文旨在填補此缺口，提供首份專注於資源效率的綜合性調查，建立分類學、標準化指標與持續更新的論文清單，以利研究者與從業者開發更永續、可及的 LLM。

## 方法
本調查採系統性文獻回顧方法，首先定義 LLM 生命週期四階段：架構設計、預訓練、微調、系統部署。接著將關鍵資源劃分為計算、記憶體、能源、財務、網路通訊五大類，並依資源優化目標對既有技術進行二維分類（資源類型 × 生命週期階段）。對每類技術進一步梳理核心機制，如模型壓縮（剪枝、量化、知識蒸餾）、高效注意力機制（稀疏、線性化）、參數共享與動態路由、分散式訓練與推理系統優化（張量/流水線並行、激活重計算）、低精度訓練與混合精度、資料高效微調（LoRA、Prefix-tuning）等。調查同時彙整標準化評估指標集，涵蓋 FLOPs、參數量、延遲、吞吐率、顯存佔用、能耗、碳排放、訓練/推理成本、通訊頻寬等多維度指標，並列舉常用基準資料集（如 GLUE、SuperGLUE、MMLU、LongBench 等）以利跨方法公平比較。最後建立線上持續更新清單（GitHub），提供結構化標籤與檢索功能，支援研究者快速定位相關工作。

## 結果
調查成果為一套完整的資源效率分類學、標準化評估指標與資料集清單，並歸納出各資源類型與生命週期階段的技術映射表。作者指出現有方法多聚焦單一資源，跨資源權衡研究稀缺；封閉源碼模型限制參數級優化；評估指標缺乏統一標準導致比較困難。摘錄未提供可驗證數字，僅呈現定性結論：系統性分類與指標標準化有助於未來研究與實務部署。

## 限制與展望
本調查以公開文獻為主，可能遺漏最新未發表或專有技術；分類依賴作者主觀判斷，邊界可能模糊；未對列舉方法進行實譯基準測試，無法量化優劣；封閉源碼模型與專有資料集限制了部分優化技術的適用性驗證；未來研究需建立統一實驗平台、探索多目標聯合優化、關注硬體感知設計與綠色 AI 標準化。
