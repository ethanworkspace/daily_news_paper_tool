# 論文 04：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-20
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
現有計算病理基礎模型多在patch層級運作，或以影像目標、粗略組織標籤、病理報告學習切片級表示，但這些標籤因機構差異且具主觀性。本文提出THREADS，透過將組織形態與基因組/轉錄組特徵對齊，學習通用全切片表示，旨在解決現有方法依賴主觀標註與泛化能力不足的問題，建立分子導向預訓練策略。

## 方法
THREADS 針對現有病理基礎模型多停留在 patch 層級、或以影像重建、粗略組織標籤、主觀病理報告為監督訊號的問題，提出分子導向的全切片表示學習框架。問題設定為：輸入 H&E 染色全切片影像 (WSI) 與對應的基因體/轉錄體剖面，輸出可泛化的切片級向量表示，支援下游 107 項腫瘤學任務（亞型分級、微環境特徵、治療反應、生存分析）。整體架構採雙模態對齊設計：影像端以編碼器將 WSI 切分為 patches 並聚合為切片嵌入；分子端編碼基因表現或突變剖面；核心機制為跨模態對比學習或相似度最大化，將形態特徵與分子特徵對齊於共享潛在空間。資料處理上，利用超過 47,000 張 H&E 切片及其配對分子資料預訓練，避免依賴機構差異大的病理報告。訓練目標為最小化形態與分子表示的距離（如 InfoNCE 損失），並以大規模批次最佳化。推論時僅需影像編碼器即可產生切片表示，接輕量級分類器或生存模型微調。關鍵設計理由：分子剖面提供客觀、可量化、跨機構一致的監督訊號，使模型學習到與腫瘤生物學機制緊密相關的形態特徵，從而實現高標籤效率與強外部隊列遷移能力。

## 結果
本研究提出 THREADS，利用分子與轉錄組資料引導全切片表徵學習，於超過 47,000 張 H&E 切片預訓練，並在 107 項腫瘤學任務驗證，涵蓋癌症亞型分級、腫瘤微環境特徵、治療反應預測與生存分析。結果顯示 THREADS 在多項基準模型與監督式基線上均表現優異，具備跨外部隊列的強遷移能力與高標籤效率。然而，摘錄未提供可驗證數字，無法量化具體 AUC、準確率或消融實驗的數值提升。定性結論指出分子導向預訓練為學習通用全切片表徵的有效策略，並建議未來整合更多分子、空間與臨床模態。

## 限制與展望
摘錄未明確討論限制。潛在限制可能包括：需配對的H&E與分子數據、計算資源需求、對罕見癌型泛化性、臨床部署可行性。作者建議未來擴展整合更多分子、空間與臨床模態。依目前可取得資料，無法確認具體部署風險與評估盲點。
