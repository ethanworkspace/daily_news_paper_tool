# 論文 04：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-19
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
現有病理基礎模型多在patch層級運作，或以影像目標、粗略組織標籤、病理報告學習切片級表示，但標籤跨機構差異大且主觀。THREADS旨在透過形態學與基因組/轉錄組數據對齊，學習通用全切片表示。

## 方法
輸入為H&E染色全切片影像與配對的基因組/轉錄組剖面。核心機制為多模態對齊預訓練，將組織形態與分子特徵在潛在空間對齊。預訓練使用超過47,000張切片，推論時輸出全切片向量供下游107項腫瘤學任務微調或零樣本評估。

## 結果
於107項腫瘤學任務（亞型分級、微環境特徵、治療反應、生存分析）評估，THREADS持續優於現有全切片基礎模型與監督式基線，展現跨外部隊列的強遷移能力與高標籤效率。摘錄未提供可驗證數字。

## 限制與展望
摘錄未詳細說明限制。潛在限制包括：依賴配對分子數據獲取困難、罕見癌種泛化未驗證、計算資源需求大。未來方向為整合更多模態（空間、臨床）以擴展應用。
