# 論文 04：A multimodal foundation model for molecular and morphologic data in oncology.

- 日期：2026-11-10
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
現有計算病理基礎模型多在patch層級運作，或使用影像目標、粗略組織標籤、病理報告學習切片層級表示，這些標籤跨機構差異大且具主觀性。本研究旨在解決如何學習通用全切片表示的問題，提出THREADS，透過將組織形態學與基因組/轉錄組特徵對齊，實現分子導向的預訓練策略，以獲取更具泛化能力的全切片嵌入，支援癌症亞型分級、微環境特徵化、治療反應預測與生存分析等多樣腫瘤學任務。

## 方法
問題設定：輸入為成對的H&E染色全切片影像與對應的基因組/轉錄組剖面，輸出為通用全切片向量表示。模型整體採用雙編碼器架構（依目前可取得資料，無法確認具體編碼器類型），分別處理形態學影像與分子數據，核心機制為跨模態對齊，將形態特徵空間映射至分子特徵空間，使切片表示蘊含分子層級資訊。資料前處理方面，使用超過47,000張H&E切片及其配對分子剖面進行預訓練。訓練目標為形態與分子模態的對齊（摘錄未明確說明損失函數形式，如對比損失或生成式目標）。推理階段僅需影像編碼器即可產生切片嵌入，下游任務以線性探針或微調方式適應107項腫瘤學任務。關鍵差異在於以分子剖面作為監督信號，替代傳統影像級自監督目標或粗略標籤，實現分子導向的全切片表示學習。

## 結果
摘錄未提供可驗證數字。作者報告THREADS在107項腫瘤學任務（含癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）上，持續優於領先的全切片基礎模型與監督式基線，並展現出強健的外部隊列遷移能力與高標籤效率。定性結論顯示分子導向預訓練能有效學習通用全切片表示，且在多樣下游任務具備優異泛化表現。

## 限制與展望
目前資料未揭露架構細節、超參數、基線名稱、評估指標、消融實驗或計算資源。潛在限制：依賴成對影像-分子數據獲取難、分子模態僅限基因組/轉錄組、缺乏空間與臨床模態、外部驗證多樣性未量化、部署效能未知。後續方向如作者所述，擴展多模態、空間與臨床數據，並需驗證臨床實用性與公平性。
