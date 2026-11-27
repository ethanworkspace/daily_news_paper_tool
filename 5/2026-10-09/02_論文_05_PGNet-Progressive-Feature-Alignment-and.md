# 論文 05：PGNet: Progressive Feature Alignment and Gaussian Geometric-Consistency Assignment for Ship Detection in Complex Maritime Environments.

- 日期：2026-10-09
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
船舶偵測在海上交通、國防與海洋資源管理中極為重要，但真實環境常伴隨雲霧遮蔽、海面雜波與光照不均，導致特徵表徵退化；現有樣本指派策略未考慮細長船舶的高角度敏感性，使得微小旋轉偏差即將高品質候選框判定為負樣本。本文提出 PGNet，旨在聯合優化特徵表徵與樣本指派，解決空間錯位、語義不一致與角度敏感三大問題，提升複雜海洋場景下的偵測魯棒性與泛化能力。

## 方法
PGNet 包含兩大核心模組：(1) 漸進式對齊預融合特徵金字塔網路（PA‑PFPN）。該模組在多尺度特徵圖之間引入自適應空間對齊層，先以可變形卷積或幾何變換將不同解析度特徵對齊至統一參考尺度，再透過漸進式特徵交互機制，由粗到細逐層融合語義與細節資訊，緩解空間錯位與語義不一致。(2) 高斯幾何一致性指派策略（GGCA）。傳統指派僅依賴 IoU 重疊，對細長船舶的旋轉極度敏感；GGCA 引入高斯核同時建模候選框與真實框的重疊度與中心點對齊度，將兩者以加權高斯函數融合為一致性分數，作為正負樣本判定依據，降低微小角度偏移導致的誤指派。訓練階段將 PA‑PFPN 輸出的多尺度特徵送入偵測頭，搭配 GGCA 進行樣本指派，損失函數採用標準分類與邊界框回歸損失（論文未詳細列出具體權重）。推論時僅保留 PA‑PFPN 與偵測頭，GGCA 僅用於訓練指派。與現有方法相比，關鍵差異在於同時解決多尺度對齊與角度敏感指派，且採用漸進式交互與高斯幾何一致性雙重機制。

## 結果
實驗於 HRSC2016、SCCOS、FGSRCS 三資料集進行。FGSRCS 上 mAP 達 88.8%（+1.7%）；SCCOS 上 mAP 87.52%、Recall 91.84%（分別 +0.5% 與 +1.43%）；HRSC2016 上 mAP@50:95 為 70.39%（+1.22%）。作者指出 PGNet 在各資料集均優於現有基線，展現於複雜海洋環境下的魯棒性與泛化能力。摘錄未提供詳細消融實驗數值或推理速度。

## 限制與展望
僅在三個船舶偵測資料集驗證，缺乏對其他類別或極端天氣（如強雨、夜間）的測試；論文未公開消融實驗細節、計算量與推理延遲，難以評估部署可行性；GGCA 的高斯核超參數敏感性未討論；程式碼未釋出，復現性受限。後續研究可擴展至多目標類別、引入自適應高斯帶寬、並進行實時部署優化。
