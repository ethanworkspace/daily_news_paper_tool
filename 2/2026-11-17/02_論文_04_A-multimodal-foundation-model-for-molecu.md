# 論文 04：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-17
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
現有計算病理基礎模型多在patch層級運作，或使用影像目標、粗略組織標籤或病理報告學習切片層級表徵，但這些標籤跨機構差異大且主觀。本研究旨在開發一種通用全切片表徵學習方法，透過對齊組織形態與基因組/轉錄組特徵來克服上述限制。

## 方法
THREADS輸入為H&E染色全切片影像，核心機制為多模態對比學習，將切片形態特徵與對應的基因組或轉錄組特徵對齊。預訓練使用超過47,000張H&E切片，並結合分子特徵進行自監督式對齊。推論時直接輸出全切片表徵，可應用於下游癌症亞型分級、微環境特徵化、治療反應預測與生存分析等任務。

## 結果
在107項腫瘤學任務上評估，THREADS持續優於現有領先的全切片基礎模型與監督式基準，展現出強大的外部隊列遷移能力與高標籤效率。摘錄提供預訓練切片數47,000+與評估任務數107等可驗證數字，並結論分子導向預訓練為學習通用全切片表徵的有效策略。

## 限制與展望
摘錄未詳細說明模型架構細節、分子數據類型範圍、計算資源需求、不同癌症類型的表現差異，亦未討論臨床部署的可解釋性與監管考量。未來工作可擴展更多模態、空間與臨床數據，並驗證於更大規模前瞻性隊列。
