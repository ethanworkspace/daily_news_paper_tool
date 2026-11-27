# 論文 05：PGNet: Progressive Feature Alignment and Gaussian Geometric-Consistency Assignment for Ship Detection in Complex Maritime Environments.

- 日期：2026-10-01
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Annals of the New York Academy of Sciences
- Venue：Annals of the New York Academy of Sciences
- 發布時間：2026-10-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42924538/
- PDF：
- DOI：10.1111/nyas.70428
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1493（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Deep learning has advanced remote sensing object detection, with ship detection drawing attention due to its importance in maritime traffic, defense, and marine resource management. However, real-world scenarios often involve cloud and fog occlusion, sea clutter, and uneven illumination, which degrade feature representation. Moreover, existing sample assignment strategies fail to account for the high-angle sensitivity of slender ships, causing many potentially high-quality proposals to be assigned as negative samples under slight rotational deviations. To address these issues, we propose PGNet, a robust ship detection framework that jointly optimizes feature representation and sample assignment. Specifically, a progressive aligned pre-fusion feature pyramid network is designed to alleviate spatial misalignment and semantic inconsistency via adaptive multi-scale spatial alignment and progressive feature interaction. Meanwhile, a Gaussian geometric consistency assignment strategy is introduced, which jointly models overlap and center alignment to alleviate the high-angle sensitivity problem for slender ships. Experiments on the HRSC2016, SCCOS, and FGSRCS datasets demonstrate that PGNet consistently outperforms existing methods, achieving a mean average precision (mAP) of 88.8% (+1.7%) on FGSRCS, 87.52% mAP and 91.84% recall (+0.5% and +1.43%) on SCCOS, and 70.39% mAP 50 : 95 (+1.22%) on HRSC2016, indicating robustness and generalization in complex maritime environments.

## 背景與目的
深度學習已大幅推進遙感目標偵測，船舶偵測因在海上交通、國防與海洋資源管理的關鍵角色而受矚目。然而真實海洋環境常伴隨雲霧遮蔽、海面雜波與光照不均，導致特徵表徵退化；現有樣本指派策略未考慮細長船舶對旋轉角度的高度敏感，使得微小角度偏差即將潛在高品質候選框判定為負樣本。本文旨在同時優化特徵表徵與樣本指派，提出 PGNet 框架，以解決空間錯位、語義不一致與高角度敏感度問題，提升複雜海況下的偵測魯棒性與泛化能力。

## 方法
PGNet 包含兩大核心模組： 1. 漸進式對齊預融合特徵金字塔網路（Progressive Aligned Pre‑fusion FPN）：針對多尺度特徵圖的空間錯位與語義不一致，採用自適應多尺度空間對齊機制，先將不同層級特徵對齊至統一參考尺度，再透過漸進式特徵交互逐層融合高層語義與低層細節，減少資訊損失並強化船舶目標的表徵。 2. 高斯幾何一致性指派策略（Gaussian Geometric‑Consistency Assignment）：傳統 IoU 指派對細長船舶的旋轉極為敏感，本策略聯合建模候選框與真實框的重疊度與中心點對齊，以高斯函數將幾何一致性轉化為連續的指派權重，使微小角度偏移仍能獲得正樣本權重，緩解高角度敏感問題。 整體流程為：骨干網路提取多尺度特徵 → 經漸進式對齊預融合 FPN 輸出增強特徵圖 → 偵測頭產生候選框 → 以高斯幾何一致性指派計算正負樣本權重 → 配合標準分類與回歸損失進行端到端訓練。與既有方法相比，關鍵差異在於同時從特徵融合與樣本指派兩面著手，並針對細長船舶的幾何特性設計專用指派函數。

## 結果
作者在 HRSC2016、SCCOS 與 FGSRCS 三個公開資料集上驗證 PGNet。結果顯示：FGSRCS 達 mAP 88.8%（較基線 +1.7%）；SCCOS 達 mAP 87.52% 且 Recall 91.84%（分別 +0.5% 與 +1.43%）；HRSC2016 達 mAP@50:95 70.39%（+1.22%）。實驗證明 PGNet 在雲霧、海面雜波與光照不均等複雜海況下，持續優於現有方法，展現較佳的魯棒性與泛化能力。

## 限制與展望
目前摘錄僅提供整體 mAP 與 Recall 數值，缺乏訓練細節（如損失函數權重、學習率排程、資料增強策略）、計算成本（參數量、推理速度）、消融實驗各模組貢獻、以及對不同感測器（SAR、光學）與不同解析度的泛化驗證。此外，高斯幾何一致性指派的超參數敏感度、極端遮蔽情況下的表現、以及部署於邊緣裝置的可行性均未說明。後續研究可進一步探討輕量化設計、多模態融合與更完整的消融分析，以全面評估方法在實務部署上的優劣。
