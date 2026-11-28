# 論文 05：PGNet: Progressive Feature Alignment and Gaussian Geometric-Consistency Assignment for Ship Detection in Complex Maritime Environments.

- 日期：2026-10-17
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
船舶偵測在海上交通、國防與海洋資源管理中至關重要，但真實環境常出現雲霧遮蔽、海面雜波與光照不均，導致特徵表徵退化；現有樣本指派策略未考慮細長船舶對旋轉角度的高敏感度，使許多高品質候選框在微小角度偏移下被判定為負樣本。本文旨在同時優化特徵表徵與樣本指派，提出 PGNet，以提升複雜海洋環境下的偵測魯棒性與泛化能力。

## 方法
PGNet 採用雙軌並行設計：(1) 漸進式對齊預融合特徵金字塔網路。首先在多尺度特徵圖之間引入自適應空間對齊模組，利用可變形卷積或幾何變換將不同解析度特徵對齊至統一參考尺度，消除空間錯位；接著透過漸進式特徵交互機制，由低層至高層逐階段融合語義與細節資訊，並在每階段加入通道注意力與空間注意力，緩解語義不一致問題。輸出為對齊後的多尺度特徵金字塔，供後續偵測頭使用。(2) 高斯幾何一致性指派策略。傳統 IoU 指派對旋轉框極度敏感，本文建立以高斯分布建模的幾何一致性分數，同時考慮預測框與真值框的重疊度（IoU）與中心點對齊誤差，將兩者以加權高斯核融合為單一指派分數。訓練階段以該分數為正負樣本判準，並搭配標準的分類損失（如 Focal Loss）與回歸損失（如 Smooth‑L1 或 CIoU Loss）進行端到端優化。推論時直接使用偵測頭輸出的旋轉框，無額外後處理。關鍵差異在於：特徵端採用自適應多尺度對齊與漸進融合，指派端引入高斯幾何一致性同時建模重疊與中心對齊，專門緩解細長船舶的角度敏感問題。

## 結果
實驗於 HRSC2016、SCCOS、FGSRCS 三資料集進行。FGSRCS 上 mAP 達 88.8%（+1.7%）；SCCOS 上 mAP 87.52%、Recall 91.84%（分別 +0.5% 與 +1.43%）；HRSC2016 上 mAP@50:95 為 70.39%（+1.22%）。結果顯示 PGNet 在多種複雜海洋場景下均優於現有方法，具備較強的魯棒性與泛化能力。

## 限制與展望
本文僅在三個公開船舶資料集驗證，未涵蓋極端天氣、多感測器融合或即時部署場景；高斯幾何一致性指派的超參數（如高斯核帶寬）敏感度未詳細分析；漸進式對齊模組增加計算量，可能影響嵌入式平台推理速度。後續研究可擴展至更大規模、多模態資料，並探索輕量化架構與自適應超參數學習。
