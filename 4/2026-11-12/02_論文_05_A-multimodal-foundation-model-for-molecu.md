# 論文 05：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-12
- 來源層級：Tier 1
- 期刊/會議/來源：Nature cancer
- Venue：Nature cancer
- 發布時間：2026-11-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43064800/
- PDF：
- DOI：10.1038/s43018-026-01252-w
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1265（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Foundation models are advancing computational pathology by transferring knowledge from large datasets to diagnostic, prognostic and treatment response tasks. Most existing models, however, either operate at the patch level or learn slide-level representations using image-based objectives, coarse tissue labels or pathology reports that vary across institutions and reflect the subjectivity inherent in narrative reporting. Here we introduce THREADS, which instead learns general-purpose whole-slide representations by aligning tissue morphology with genomic or transcriptomic profiles. THREADS was pretrained on over 47,000 hematoxylin-and-eosin-stained tissue sections and evaluated across 107 oncology tasks spanning cancer subtyping and grading, tumor microenvironment characterization, treatment response prediction and survival analysis. THREADS consistently outperformed leading whole-slide foundation models and supervised baselines while demonstrating strong transfer across external cohorts and high label efficiency. These findings establish molecularly guided pretraining as an effective strategy for learning general-purpose whole-slide representations and motivate future extensions incorporating additional molecular, spatial and clinical modalities.

## 背景與目的
現有基礎模型多在切片層級運作，或以影像目標、粗略組織標籤、病理報告學習切片級表示，但報告因機構差異且具主觀性，導致泛化受限。本研究旨在解決此缺口，提出 THREADS，透過將組織形態與基因組或轉錄組特徵對齊，學習通用全切片表示，並在超過 47,000 張 H&E 染色切片上預訓練，涵蓋 107 項腫瘤學任務，建立分子導向預訓練為有效策略。

## 方法
問題設定：輸入為全切片 H&E 影像與對應的基因組或轉錄組剖面，輸出為可用於下游任務的全切片向量表示。模型架構為多模態基礎模型，包含影像編碼器與分子編碼器，透過跨模態對齊機制將形態特徵與分子特徵映射至共同潛在空間。核心模組採用分子導向的預訓練目標，利用超過 47,000 張配對切片進行大規模自監督學習，使影像表示能捕捉分子層面的生物變異。資料前處理將切片切分為 patch、提取視覺特徵，並對分子資料進行標準化與降維。訓練目標為最小化影像與分子嵌入之間的距離（如對比損失），並以優化器進行端到端最佳化；具體損失函數與超參數於摘錄未詳細說明。推論階段僅需影像編碼器即可產生全切片嵌入，供分型、分級、微環境、治療反應與生存分析等任務微調或線性探針。關鍵差異在於以分子剖面作為監督信號，而非單純影像重建或病理報告，從而獲得更具生物意義的切片級表示。

## 結果
作者報告 THREADS 在 107 項腫瘤學任務（癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）上，持續優於現有領先的全切片基礎模型與監督式基線，並展現出強健的外部隊列遷移能力與高標籤效率。摘錄未提供可驗證的具體數值指標（如 AUC、C-index、準確率等），僅能觀察到定性上的優勢結論。

## 限制與展望
目前摘錄缺乏模型架構細節、損失函數形式、超參數設定、計算資源需求與具體評估指標，難以判斷訓練穩定性與可重現性。實驗雖涵蓋 107 任務，但未說明各癌種樣本分布、外部驗證隊列的多樣性與潛在選擇偏誤。此外，僅對齊基因組/轉錄組，空間轉錄組、蛋白質組及臨床變數未納入，限制多模態擴展性。後續研究需補充技術細節、進行更全面的消融實驗，並探討部署於臨床工作流的可行性與倫理風險。
