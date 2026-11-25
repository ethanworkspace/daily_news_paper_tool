# 論文 01：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-13
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
現有計算病理基礎模型多在patch層級運作，或以影像目標、粗略組織標籤、病理報告學習切片級表示，但這些標籤因機構差異與敘述主觀性而不一致。THREADS旨在透過將組織形態與基因組/轉錄組概況對齊，學習通用全切片表示，解決現有方法依賴主觀標籤的缺口。本文提出分子導向預訓練策略，於超過47,000張H&E染色切片上預訓練，並在107項腫瘤學任務評估，確立分子導向預訓練為有效策略，並展現強遷移與高標籤效率。

## 方法
問題設定：輸入為H&E全切片影像與配對的基因組/轉錄組分子概況，輸出為通用全切片向量表示。模型架構：採用多模態對齊框架，包含影像編碼器（處理切片形態）與分子編碼器（處理基因組/轉錄組資料），透過對比學習或相似度最大化將兩模態映射至共同潛在空間。資料前處理：將切片切分為patch並提取特徵，分子資料標準化後輸入。訓練目標：最小化形態與分子表示間的距離，使影像編碼器學習含分子資訊的表徵。預訓練使用超過47,000張配對切片。推論時僅需影像編碼器產生切片表示，下游任務以線性探針或微調評估。關鍵差異：以分子概況作為監督信號，而非影像重建、粗略標籤或病理報告，提供更客觀、跨機構一致的監督。註：摘錄未詳細揭露編碼器架構、對齊損失函數形式、優化策略等細節。

## 結果
THREADS在107項腫瘤學任務（癌症亞型分級、腫瘤微環境特徵、治療反應預測、生存分析）上持續優於領先的全切片基礎模型與監督式基線，並展現強跨隊列遷移能力與高標籤效率。摘錄未提供可驗證數字（如AUC、準確率、統計顯著性），僅能觀察到定性結論：分子導向預訓練有效提升全切片表示泛化性能。

## 限制與展望
資料限制：預訓練隊列規模、分子資料類型、癌症種類分布、外部驗證隊列細節未揭露，可能影響泛化性評估。方法限制：對齊機制、模態間資訊瓶頸、配對資料稀缺性未討論。評估限制：107項任務具體定義、基線模型名稱、統計檢定缺失，難以獨立驗證優越性。部署風險：需配對分子資料預訓練，臨床獲取成本高；模型計算量與解釋性未提及。後續方向：整合更多模態（空間、臨床）、探討對齊策略與擴展至其他疾病。
