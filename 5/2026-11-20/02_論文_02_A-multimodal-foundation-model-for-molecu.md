# 論文 02：A multimodal foundation model for molecular and morphologic data in oncology.

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
計算病理學中，現有基礎模型多在patch層級運作，或使用影像目標、粗略組織標籤、病理報告學習切片層級表示，但這些標籤因機構差異與主觀敘述而異。本文提出THREADS，透過將組織形態與基因組或轉錄組概況對齊，學習通用全切片表示，旨在解決現有方法依賴主觀標籤與patch層級限制的缺口，建立分子導向預訓練策略，提升癌症亞型分級、微環境特徵、治療反應預測與生存分析等任務表現。

## 方法
問題設定：輸入為H&E染色全切片影像與對應的基因組/轉錄組概況，輸出為通用全切片表示向量。模型整體架構：摘錄未詳細描述具體架構（如視覺編碼器、分子編碼器、融合模組），僅指出THREADS透過對齊組織形態與分子概況學習表示。核心模組與演算法機制：採用多模態對齊策略，將形態特徵與分子特徵映射至共同潛在空間，但具體對齊損失（如對比損失、互資訊最大化）與訓練目標未在摘錄中說明。資料前處理/特徵表示：使用超過47,000張H&E切片，推測需進行切片分塊、特徵提取，但具體前處理流程、分子資料標準化方式未提供。訓練目標、損失函數或最佳化策略：摘錄未提供。推論或執行流程：預訓練後可凍結編碼器提取切片表示，下游任務微調或線性探針，但細節未提及。與既有方法關鍵差異：現有模型多依賴影像重建、patch級自監督或粗略標籤，THREADS創新在於引入分子概況作為監督信號，實現分子導向的全切片表示學習。

## 結果
摘錄未提供可驗證數字。作者報告THREADS在107項腫瘤學任務（涵蓋癌症亞型分級、腫瘤微環境特徵、治療反應預測、生存分析）上，持續優於領先的全切片基礎模型與監督式基線，並展現強大的外部隊列遷移能力與高標籤效率。定性結論顯示分子導向預訓練能有效學習通用全切片表示。

## 限制與展望
依目前可取得資料，無法確認模型架構細節、訓練超參數、分子資料來源多樣性、外部驗證隊列具體規模與人口統計分布。潛在風險包括分子資料獲取困難限制臨床部署、模型對罕見癌型泛化能力未知、多模態對齊可能引入噪聲。後續研究方向建議擴展更多模態（空間轉錄組、臨床數據）、探討可解釋性與公平性評估。
