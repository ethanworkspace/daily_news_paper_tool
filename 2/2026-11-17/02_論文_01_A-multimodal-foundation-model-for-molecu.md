# 論文 01：A multimodal foundation model for molecular and morphologic data in oncology.

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
本研究旨在解決計算病理學中現有基礎模型多僅於切片層級運作，或依賴影像級目標、粗略組織標籤或病理報告學習切片級表示的問題。這些方法受限於機構間標註不一致與敘述主觀性。THREADS 提出以分子導向的預訓練策略，將 H&E 染色切片形態學與基因組/轉錄組特徵對齊，學習通用全切片表示，並在 107 項腫瘤學任務上驗證，確立分子引導預訓練的有效性。

## 方法
問題設定：輸入為 H&E 全切片影像與對應的基因組/轉錄組剖面，輸出為通用全切片向量表示。整體架構採用雙編碼器設計，分別編碼形態學影像與分子特徵，再透過跨模態對齊機制將兩者映射至共享潛在空間。核心模組包含影像編碼器（處理切片級 patch 聚合）、分子編碼器（處理高維基因表達），以及對齊損失（如對比學習或相似度最大化）以強制形態與分子語義一致。資料前處理將超過 47,000 張 H&E 切片切割為 patch，提取視覺特徵；分子資料經標準化後作為監督信號。訓練目標為最小化跨模態距離，優化策略採用大規模自監督預訓練。推論時僅需影像編碼器即可產生全切片表示，支援下游分類、生存分析等任務。關鍵差異在於以分子剖面作為預訓練監督，而非傳統影像級自監督或病理報告標籤，從而獲得更具生物學意義的表示。

## 結果
摘錄未提供可驗證數字。作者報告 THREADS 在 107 項腫瘤學任務（癌症亞型分級、腫瘤微環境特徵化、治療反應預測、生存分析）上持續優於領先的全切片基礎模型與監督式基線，並展現強健的外部隊列遷移能力與高標籤效率。定性結論顯示分子導向預訓練能有效學習通用全切片表示。

## 限制與展望
依目前可取得資料，無法確認具體限制。潛在限制包括：預訓練隊列癌症類型多樣性與樣本平衡度未說明；分子資料來源與批次效應處理缺失；評估任務未列出具體基線名稱與統計顯著性；計算資源需求、推論延遲與部署可行性未討論；罕見癌症與不同染色協議泛化能力待驗證。後續方向為擴展更多模態並強化外部驗證。
