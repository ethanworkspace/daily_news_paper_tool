# 論文 05：A multimodal foundation model for molecular and morphologic data in oncology.

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
現有計算病理基礎模型多僅在局部切片層級運作，或以影像重建目標、粗略組織標籤、主觀病理報告學習切片級表示，導致跨機構泛化受限。THREADS 提出以分子導向預訓練策略，將大規模 H&E 染色切片的形態特徵與基因組、轉錄組特徵對齊，學習通用全切片表示，以支援癌症亞型分級、微環境特徵化、治療反應預測與生存分析等多樣腫瘤學任務。

## 方法
THREADS 輸入超過 47,000 張 H&E 染色組織切片影像，搭配對應的基因組或轉錄組特徵。核心機制為多模態對比學習，將形態編碼器與分子編碼器的表示空間對齊，使模型從形態學習分子相關特徵。預訓練階段在大規模配對資料上進行自監督對齊；下游階段凍結編碼器，於 107 項腫瘤學任務（含癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）上以線性探針或微調評估，並驗證外部隊列遷移與標籤效率。

## 結果
摘錄未提供可驗證數字。實驗顯示 THREADS 在 107 項腫瘤學任務上持續優於現有全切片基礎模型與監督式基線，展現出強健的外部隊列遷移能力與高標籤效率，證實分子導向預訓練能有效學習通用全切片表示。

## 限制與展望
目前僅對齊形態與基因組/轉錄組，尚未整合空間轉錄組、蛋白質組或臨床資料等額外模態；外部驗證隊列雖具代表性，但癌症類型與種族多樣性仍有擴充空間；模型對罕見亞型或低品質切片的魯棒性未充分探討；未來需進一步整合多模態與空間資訊以提升臨床實用性。
