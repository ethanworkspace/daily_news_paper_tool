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
大型語言模型（LLM）參數規模急遽增長，導致計算、記憶體、能源、資金與網路通訊等資源消耗極大，嚴重限制其在資源受限環境的部署與普及。現有綜述多聚焦模型壓縮或推理加速，缺乏跨生命週期、跨資源類型的系統性分類與統一評估標準。本文旨在建立資源高效 LLM 的完整分類體系，涵蓋架構設計、預訓練、微調與系統設計四階段，並依資源類型（計算、記憶體、能源、資金、通訊）劃分優化技術，提供標準化評估指標與資料集，填補領域空白，為永續 AI 發展奠基。

## 方法
本文採系統性文獻回顧法，建立資源高效 LLM 的雙維度分類框架：(1) 依 LLM 生命週期劃分為架構設計、預訓練、微調、系統設計四階段；(2) 依優化目標資源類型劃分為計算、記憶體、能源、資金、網路通訊五大類。作者蒐集大量相關論文，對每類技術進行深度歸納，揭示資源類型與優化技術的對應關係。同時，彙整標準化評估指標集（含計算量、延遲、吞吐率、記憶體佔用、能耗、碳排放、訓練/推理成本等）與常用基準資料集，以利跨方法公平比較。調查過程包含文獻篩選、分類編碼、關係映射與差距分析，並發布持續更新的論文清單網站（GitHub）作為社群資源。

## 結果
本文主要貢獻為：(1) 提出首個專注資源效率的 LLM 系統性綜述，構建雙維度分類法（生命週期×資源類型），涵蓋 5 大資源類型與 4 個生命週期階段；(2) 整理標準化評估指標與資料集清單，促進跨研究公平比較；(3) 識別當前瓶頸：自回歸生成並行度低、注意力機制平方複雜度、擴展定律遞減效應、系統設計複雜度、專有資料與閉源模型限制、多目標評估指標缺失；(4) 釋出持續更新的論文庫（Awesome-Resource-Efficient-LLM-Papers）。摘錄未提供可驗證的量化實驗數字或消融研究結果。

## 限制與展望
作為綜述論文，本文未執行實證實驗，無法驗證各技術實際效能；分類框架可能隨領域快速演進而需更新；文獻覆蓋以公開論文為主，可能遺漏產業內部最佳實踐；標準化指標雖被提出，但實際採納度與跨平台可比性仍待觀察；未深入探討硬體感知優化與軟硬體協同設計的具體落地細節。後續研究可朝統一基準測試平台、動態資源權衡機制、綠能感知訓練/推理調度等方向發展。
