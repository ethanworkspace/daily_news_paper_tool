# 論文 05：PGNet: Progressive Feature Alignment and Gaussian Geometric-Consistency Assignment for Ship Detection in Complex Maritime Environments.

- 日期：2026-10-12
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
深度學習已大幅推進遙感目標檢測，船舶檢測因海上交通、國防與海洋資源管理的重要性而受關注。然而真實海洋環境常伴隨雲霧遮蔽、海面雜波與光照不均，導致特徵表徵退化；現有樣本分配策略未考慮細長船舶的高角度敏感性，使得微小旋轉偏差即將潛在高品質候選框判定為負樣本。本文旨在聯合優化特徵表徵與樣本分配，提出 PGNet 以提升複雜海洋場景下的檢測魯棒性與泛化能力。

## 方法
PGNet 包含兩大核心模組：(1) 漸進式對齊預融合特徵金字塔網路（Progressive Aligned Pre‑fusion FPN），針對多尺度特徵的空間錯位與語義不一致，採用自適應多尺度空間對齊機制，先在各層級進行幾何對齊，再透過漸進式特徵交互逐步融合高層語義與低層細節，減輕遮蔽與雜波造成的特徵退化；(2) 高斯幾何一致性分配策略（Gaussian Geometric‑Consistency Assignment），將候選框與真實框的重疊度（IoU）與中心點對齊度聯合建模為高斯分布，根據幾何一致性機率動態決定正負樣本標籤，緩解細長船舶在微小旋轉下被誤判為負樣本的問題。整體架構採用單階段檢測器為基礎，輸入影像經骨干網路提取多尺度特徵，送入上述預融合 FPN 獲得對齊後的特徵圖，再經檢測頭輸出類別與旋轉邊界框；訓練目標包含分類損失、邊界框回歸損失與分配策略產生的樣本權重損失，採用標準 SGD/Adam 最佳化。推論時直接使用訓練好的網路進行前向傳播，無額外後處理。與既有方法相比，關鍵差異在於同時解決特徵對齊與角度敏感分配，且皆在特徵金字塔層級完成，無需額外注意力模組。

## 結果
在三個公開資料集上實驗顯示：FGSRCS 達 mAP 88.8%（+1.7%）；SCCOS 達 mAP 87.52% 且 Recall 91.84%（分別 +0.5% 與 +1.43%）；HRSC2016 達 mAP@50:95 70.39%（+1.22%）。結果證明 PGNet 在雲霧、雜波與光照變化等複雜海洋環境下具備較佳的檢測精度與召回率，並展現跨資料集的泛化能力。

## 限制與展望
本文僅提供摘要層級的實驗數字，缺乏詳細消融實驗、計算量與推理速度分析，亦未說明訓練資料增強、超參數設定與硬體環境。高斯幾何一致性分配的超參數敏感度、極端遮蔽下的表現、以及部署於邊緣裝置的可行性仍待進一步驗證。後續研究可擴展至更多旋轉角度分佈、多模態融合（如 SAR+光學）與輕量化架構設計。
