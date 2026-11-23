# 論文 05：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-14
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
本研究旨在解決計算病理學中現有基礎模型多僅在patch層級運作，或以影像為目標、粗略組織標籤或病理報告學習切片層級表示的問題。這些方法受限於機構間標註差異與敘述主觀性，難以獲得通用的全切片表示。THREADS 提出以分子（基因組或轉錄組）資料指導預訓練，將組織形態與分子特徵對齊，從而學習通用的全切片表示，並在107項腫瘤學任務上驗證其泛化能力。

## 方法
THREADS 採用多模態對齊策略，輸入為超過 47,000 張 H&E 染色全切片影像與對應的基因組或轉錄組剖面。模型架構未於摘錄中詳細描述，但核心機制為將形態學特徵與分子特徵投影至共同潛在空間，透過對比學習或類似的跨模態對齊損失函數最佳化，使切片層級表示同時捕捉組織結構與分子表型。預訓練階段僅使用影像與分子資料，不依賴人工標註的病理標籤。微調或下游任務時，將凍結或微調編碼器，接上輕量分類頭進行癌症亞型分級、腫瘤微環境特徵化、治療反應預測與生存分析等 107 項任務。推論流程為：輸入全切片影像 → 編碼器提取特徵 → 下游頭輸出預測。與現有方法的關鍵差異在於引入分子導向的預訓練目標，而非單純影像重建或弱標籤分類，從而提升標籤效率與跨隊列遷移能力。摘錄未提供具體架構細節（如編碼器類型、注意力機制、損失函數形式）、訓練超參數、資料前處理（如切片切割、標準化）或最佳化策略。

## 結果
作者報告 THREADS 在 107 項腫瘤學任務上持續優於現有全切片基礎模型與監督式基線，並展現出強健的外部隊列遷移能力與高標籤效率。摘錄未提供可驗證的具體數值（如 AUC、準確率、C-index 等），僅能觀察到定性結論：分子導向預訓練能有效學習通用全切片表示，並在多樣下游任務中表現優異。

## 限制與展望
僅有摘要與部分全文摘錄，缺乏模型架構、損失函數、訓練細節、資料集組成、評估指標與統計顯著性等關鍵資訊，無法全面評估穩健性與潛在偏誤。預訓練資料來源、分子資料品質、跨機構異質性處理、計算資源需求與部署可行性均未說明。後續研究需補充技術細節、擴展更多模態、進行嚴格消融與外部驗證，以確認泛化極限與臨床轉譯潛力。
