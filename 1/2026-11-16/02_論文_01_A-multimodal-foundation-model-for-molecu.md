# 論文 01：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-16
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
現有計算病理基礎模型多在patch層級運作，或使用影像目標、粗略組織標籤、病理報告學習切片層級表示，這些標籤因機構差異與主觀敘述而異。本文提出THREADS，透過將組織形態與基因組/轉錄組特徵對齊，學習通用全切片表示，旨在解決現有方法依賴主觀標籤與patch層級限制的缺口，建立分子導向預訓練策略，提升癌症亞型分級、微環境特徵化、治療反應預測與生存分析等任務表現。

## 方法
問題設定：輸入為H&E染色全切片影像與對應的基因組/轉錄組特徵，輸出為通用全切片表示向量。模型整體架構：摘錄未詳細描述具體架構（如骨幹網路、融合模組），僅指出THREADS採用多模態對齊策略，將形態學影像與分子特徵在潛在空間對齊。核心模組與演算法機制：摘錄未提供具體模組細節（如注意力機制、對比學習損失、投影頭結構），無法確認是否採用對比學習、掩碼建模或其他自監督目標。資料前處理/特徵/表示：預訓練使用超過47,000張H&E切片，但未說明切片切割、patch大小、標準化、基因組資料預處理（如標準化、降維）等細節。訓練目標與損失函數：摘錄未明確給出損失函數形式（如對比損失、互資訊最大化）或最佳化策略（學習率、批次大小、訓練輪數）。推論流程：未描述推論時如何處理新切片、是否需分子特徵、表示提取方式。關鍵差異：與現有patch層級或影像目標/粗略標籤監督的切片模型不同，THREADS以分子特徵為指導訊號進行全切片表示學習，強調分子導向預訓練的泛化優勢。依目前可取得資料，無法確認具體架構、損失函數、超參數等技術細節。

## 結果
摘錄未提供可驗證數字（如AUC、準確率、C-index等量化指標）。定性結論：THREADS在107項腫瘤學任務（癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）上，持續優於領先的全切片基礎模型與監督式基線；展現出在外部隊列的強遷移能力與高標籤效率，確立分子導向預訓練為學習通用全切片表示的有效策略。

## 限制與展望
資料限制：預訓練僅涵蓋H&E切片與基因組/轉錄組，缺乏空間轉錄組、蛋白質組、臨床變數等模態；外部驗證隊列細節未揭露。方法限制：未說明模型對染色差異、切片品質變異的魯棒性；分子特徵獲取成本高可能限制臨床部署。評估限制：107項任務的具體指標、統計顯著性、消融實驗未提供。潛在風險：分子導向對齊可能引入批次效應、過擬合特定癌種。後續方向：整合更多模態、空間資訊、臨床數據，擴展至更多癌種與任務。依目前可取得資料，無法確認具體部署限制與風險範圍。
