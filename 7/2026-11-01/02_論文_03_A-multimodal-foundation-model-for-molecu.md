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
本研究旨在解決計算病理學中現有基礎模型多僅在patch層級運作，或以影像為基礎的目標、粗略組織標籤、病理報告等主觀且機構間異質的監督訊號學習切片層級表示的問題。這類方法難以捕捉腫瘤微環境與分子特徵的深層關聯，限制了模型在癌症亞型分級、治療反應預測與生存分析等下游任務的泛化能力。本文提出THREADS，透過將H&E染色切片形態學與基因組/轉錄組特徵進行多模態對齊，學習通用的全切片表示，並在超過47,000張切片上預訓練，建立分子導向預訓練的有效性。

## 方法
THREADS採用多模態對齊架構，輸入為H&E染色全切片影像與對應的基因組或轉錄組剖面。模型核心在於將形態學特徵與分子特徵映射至共同潛在空間，透過對比學習或類似的對齊目標（摘錄未具體說明損失函數細節），使切片表示蘊含分子層面的生物學資訊。預訓練資料集包含超過47,000張H&E切片，涵蓋多種癌症類型。下游任務採用凍結編碼器或微調方式，於107項腫瘤學任務評估，包括癌症亞型分級、腫瘤微環境特徵化、治療反應預測與生存分析。與現有全切片基礎模型及監督式基線比較，THREADS展現優越的遷移能力與標籤效率。具體架構模組（如視覺編碼器、分子編碼器、融合機制）、訓練超參數、優化策略等技術細節在摘錄中未提供。

## 結果
作者報告THREADS在107項腫瘤學任務上持續優於領先的全切片基礎模型與監督式基線，並展現出強健的外部隊列遷移能力與高標籤效率。任務涵蓋癌症亞型分級、腫瘤微環境特徵化、治療反應預測及生存分析。然而，摘錄未提供可驗證的具體數值指標（如AUC、準確率、C-index等），亦未列出具體基線模型名稱與統計顯著性檢定結果，僅能觀察到定性上的優越結論。

## 限制與展望
依目前可取得資料，無法確認模型在不同種族、機構掃描設備、染色批次變異下的穩健性；預訓練資料規模雖達47,000切片，但癌症類型分佈、分子數據品質與對齊完整性未揭露。評估任務雖多達107項，但缺乏外部驗證隊列的詳細描述與統計功效分析。方法僅整合H&E形態與基因組/轉錄組，未納入空間轉錄組、蛋白質組或臨床結構化資料，多模態擴展性待證實。部署層面，計算資源需求、推論延遲與臨床整合流程均未討論。後續研究可探索更多樣分子模態、空間資訊融合及前瞻性臨床驗證。
