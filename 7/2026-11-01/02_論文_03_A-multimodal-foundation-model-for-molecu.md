# 論文 03：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-01
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
現有計算病理基礎模型多在 patch 層級運作，或以影像目標、粗略組織標籤、病理報告學習切片級表示，但這些標籤因機構差異與主觀敘述而異質。本文提出 THREADS，透過對齊組織形態與基因組/轉錄組特徵，學習通用全切片表示，旨在解決現有方法依賴主觀標籤與單一模態的缺口，建立分子導向預訓練策略，提升下游腫瘤學任務表現。

## 方法
問題設定：輸入為 H&E 染色全切片影像與對應的基因組/轉錄組剖面，輸出為通用全切片表示向量。模型整體架構：摘錄未詳細描述編碼器結構、融合機制或對齊模組細節。核心機制：採用分子導向預訓練，將切片形態特徵與分子特徵在共享潛在空間對齊，以學習包含分子資訊的形態表示。資料前處理：使用超過 47,000 張 H&E 切片進行預訓練，但未說明切片切割、正規化、分子資料處理流程。訓練目標：推測為跨模態對比損失或相似度最大化，但摘錄未提供具體損失函數、最佳化策略。推論流程：預訓練後凍結編碼器，於 107 項腫瘤學任務（亞型分級、微環境特徵、治療反應、生存分析）上線性探針或微調評估。關鍵差異：不同於純影像自監督或標籤監督方法，THREADS 引入分子剖面作為監督信號，實現形態-分子對齊，提升標籤效率與跨隊列泛化。註：摘錄缺乏架構、超參數、基線模型名稱等技術細節，無法進一步深入說明。

## 結果
摘錄未提供可驗證數字。作者報告 THREADS 在 107 項腫瘤學任務上持續優於領先的全切片基礎模型與監督式基線，展現強跨外部隊列遷移能力與高標籤效率。定性結論確立分子導向預訓練為學習通用全切片表示的有效策略，並顯示於癌症亞型分級、微環境特徵、治療反應預測與生存分析等任務均有優勢。

## 限制與展望
資料限制：僅說明預訓練切片數量（>47,000），未揭露分子資料來源、癌症類型分布、隊列多樣性。方法限制：摘錄未提供模型架構、對齊演算法、損失函數、訓練超參數，無法評估計算成本與可擴展性。評估限制：未列出具體基線模型名稱、評估指標、消融實驗，無法驗證統計顯著性。部署風險：跨機構染色差異、分子測序平台異質性對泛化影響未討論。後續方向：作者建議擴展至更多模態（空間、臨床），但具體實施路徑未明。
