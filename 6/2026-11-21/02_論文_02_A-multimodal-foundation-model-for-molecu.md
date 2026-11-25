# 論文 02：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-21
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
計算病理學中，現有基礎模型多僅在patch層級運作，或以影像目標、粗略組織標籤、病理報告學習切片層級表徵，但這些標籤因機構差異與敘述主觀性而不一致。本研究旨在解決此缺口，提出THREADS，透過將組織形態學與基因組/轉錄組概況對齊，學習通用全切片表徵，建立分子導向預訓練策略，以提升下游癌症亞型分級、微環境特徵化、治療反應預測與生存分析等任務表現。

## 方法
THREADS為多模態基礎模型，問題設定為全切片表徵學習，輸入為H&E染色切片影像與對應的基因組/轉錄組概況，輸出為切片層級的通用表徵向量。整體架構採用多模態對齊框架，核心機制為將形態學特徵與分子概況在共同潛在空間對齊，具體演算法細節（如編碼器架構、注意力機制、融合策略）摘錄未說明。資料前處理方面，使用超過47,000張H&E染色切片進行預訓練，特徵表示方式未描述。訓練目標推測為跨模態對比學習或對齊損失，但摘錄未提供具體損失函數、最佳化策略或超參數。推論流程為利用預訓練編碼器提取切片表徵，再接下游分類/迴歸頭進行微調或線性探針。關鍵差異在於以分子概況指導預訓練，而非單純影像重建或粗略標籤，實現標籤高效與跨隊列泛化。

## 結果
作者報告於107項腫瘤學任務（涵蓋癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）評估，THREADS持續優於領先的全切片基礎模型與監督式基線，並展現強健的外部隊列遷移能力與高標籤效率。摘錄未提供可驗證數字（如AUC、準確率、p值等），僅能觀察到定性結論：分子導向預訓練有效提升全切片表徵品質。

## 限制與展望
摘錄未討論限制。依目前可取得資料，無法確認具體限制；潛在風險包括：需配對分子數據導致資料獲取困難、模型計算資源需求大、對罕見癌症類型泛化能力未知、多模態對齊可能引入噪聲、臨床部署時的標準化與解釋性挑戰。後續研究方向或可擴展至空間轉錄組、蛋白質組等更多模態，並驗證於前瞻性臨床試驗。
