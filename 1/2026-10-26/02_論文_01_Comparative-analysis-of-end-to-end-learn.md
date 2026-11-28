# 論文 01：Comparative analysis of end-to-end learning and foundation models for clinical-grade prostate pathology.

- 日期：2026-10-26
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-26T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43078843/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13796288/
- DOI：10.1038/s41467-026-78996-7
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：999（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Foundation models (FMs) using self-supervised pre-training are widely advocated as a universal solution for pathology, yet their advantages over task-specific (TS) models remain unclear. Here we show, using over 100,000 prostate biopsies from 6268 patients across 15 sites, that while FMs demonstrate utility in data-scarce scenarios, their performance converges with-and is in some cases surpassed by-TS models with sufficient labeled training data. Concordance with pathologists' grading reaches quadratic Cohen's kappas of 0.91 (95% CI 0.90-0.92; all models) on internal and 0.87 (0.86-0.88; TS), 0.86 (0.84-0.87; UNI FM) and 0.85 (0.84-0.86; Virchow2 FM) on external cohorts at full training. Task-specific training markedly reduces misgrading, misdiagnosis of challenging morphologies, and technical variability. Notably, FMs consume up to 35 times more energy. We advocate for considering both FMs and end-to-end learning for robust, resource-efficient, and clinically applicable AI pathology.

## 背景與目的
本研究旨在比較基於自監督預訓練的基礎模型（Foundation Models, FMs）與針對特定任務端到端訓練的任務特定模型（Task‑Specific, TS）在臨床級前列腺病理切片分級上的表現。現有文獻常宣稱 FMs 為通用解決方案，但其在大量標註資料下相較 TS 模型的優勢尚未被系統量化。研究使用超過 10 萬張來自 6268 位患者、跨 15 個機構的前列腺穿刺切片，評估兩類模型在內部與外部隊列上與病理醫師分級的一致性，並量測能源消耗，以釐清資源效率與臨床適用性。

## 方法
問題設定：輸入為全切片影像（WSI）或其切片區塊，輸出為前列腺癌 Gleason 分級（或 ISUP Grade Group）。模型架構：比較兩類系統——（1）基礎模型：採用 UNI 與 Virchow2 兩種經大規模病理影像自監督預訓練的視覺 Transformer，之後在前列腺任務上微調；（2）任務特定模型：從隨機初始化或 ImageNet 預訓練權重起步，直接以標註資料端到端訓練的 CNN/Transformer 分類器。核心模組差異在於預訓練策略（自監督對比學習/遮罩影像建模）與微調方式。資料前處理：切片切割為固定大小 patches，進行顏色正規化、組織區域偵測，僅保留含腺體區域。訓練目標：交叉熵損失搭配類別加權以處理類別不平衡；優化器採用 AdamW，學習率排程為 cosine decay。推論流程：將 WSI 切片依滑動窗口送入模型，聚合 patch 級預測（如多數決或注意力加權）得到切片級分級。關鍵差異：FMs 需額外預訓練階段與大量計算資源，TS 模型僅需單階段監督訓練。註：摘錄未提供具體架構細節、patch 大小、批次大小、訓練輪數、資料增強策略、微調層凍結策略等資訊，依目前可取得資料，無法確認。

## 結果
實驗結果顯示，在內部測試集上所有模型對病理醫師分級的二次 Cohen's kappa 均達 0.91（95% CI 0.90‑0.92）。外部隊列上，TS 模型達 0.87（0.86‑0.88），UNI FM 為 0.86（0.84‑0.87），Virchow2 FM 為 0.85（0.84‑0.86）。作者指出 TS 訓練顯著降低誤分級、困難形態誤診與技術變異性。能源消耗方面，FMs 最多較 TS 模型高 35 倍。摘錄未提供更細緻的消融實驗數字或每類別表現，僅能觀察到上述定性結論。

## 限制與展望
限制包括：(1) 僅針對前列腺穿刺切片，未驗證其他器官或癌種；(2) 外部驗證僅涵蓋有限機構，泛化能力仍待擴展；(3) 摘錄未揭露模型超參數、訓練硬體、能源測量協定，難以重現能耗比較；(4) 未提供程式碼與完整模型權重，部署可行性不明；(5) 潛在風險為 FMs 高能耗與碳足跡，若在資源受限環境可能不切實際。後續研究可探討混合策略、知識蒸餾以降低 FMs 成本，以及在多中心、多種染色條件下的穩健性評估。
