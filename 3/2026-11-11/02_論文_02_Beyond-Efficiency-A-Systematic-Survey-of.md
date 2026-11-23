# 論文 02：Beyond Efficiency: A Systematic Survey of Resource-Efficient Large Language Models

- 日期：2026-11-11
- 來源層級：Tier 2
- 期刊/會議/來源：ACM Computing Surveys
- Venue：ACM Computing Surveys
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://doi.org/10.1145/3845797
- PDF：https://arxiv.org/pdf/2401.00625
- DOI：10.1145/3845797
- arXiv：2401.00625
- 影響指標：2yr_mean_citedness=56.75, h_index=405, i10_index=3031 (OpenAlex)
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
大型語言模型（LLM）參數規模急劇增長，導致計算、記憶體、能源、資金與網路通訊等資源消耗極大，嚴重限制其在資源受限環境的部署與普及。現有研究雖提出多種效率優化技術，但缺乏系統性分類與統一評估標準，難以跨領域比較與選擇適當方法。本文旨在建立資源高效 LLM 的綜合性分類體系，涵蓋模型全生命週期各階段，並提供標準化評估指標與資料集，填補領域空白，為永續 AI 發展奠基。

## 方法
本研究採系統性文獻調查方法，針對資源高效 LLM 技術進行全面梳理。首先定義五大核心資源類別：計算、記憶體、能源、財務成本與通訊成本；並依 LLM 生命週期劃分為架構設計、預訓練、微調與系統設計四階段。核心貢獻在於建立雙維度分類法：按優化資源類型與生命週期階段交叉映射技術，揭示資源間複雜關聯與權衡。調查涵蓋模型壓縮（剪枝、量化、知識蒸餾）、高效架構（稀疏注意力、線性注意力、混合專家）、訓練優化（梯度累積、混合精度、分散式並行策略）、推理加速（投機解碼、KV 快取壓縮、動態批次）等技術族群。同時彙整標準化評估指標集，包含 FLOPs、參數量、延遲、吞吐率、能耗、碳排放、記憶體佔用、財務成本等多維度度量，並列舉常用基準資料集（如 GLUE、SuperGLUE、MMLU、代碼生成任務等）以利公平比較。作者另發布持續更新的論文清單網站，支援社群追蹤最新進展。

## 結果
摘錄未提供可驗證數字。本文為綜述性質，主要成果為定性結論：完成首個專注資源效率的 LLM 系統性調查，建立五大資源類別與四階段生命週期的雙維度分類法，彙整標準化評估指標與資料集，並識別出自迴歸生成並行度低、注意力二次複雜度、擴展定律遞減回報、封閉源模型限制等關鍵瓶頸，指出未來研究方向包含多目標聯合優化、理論與系統協同設計、開放資料與模型生態建設。

## 限制與展望
作為綜述論文，本研究固有限制包括：文獻覆蓋截止至 2024 年底，可能遺漏最新技術；分類法依賴作者主觀判斷，邊界可能模糊；未對所列技術進行實證基準測試，無法量化比較優劣；標準化指標尚未經社群廣泛驗證；潛在選擇偏誤（如偏向開源論文）。後續研究可建立動態基準平台、引入多目標優化基準、探討理論極限與實際部署差距。
