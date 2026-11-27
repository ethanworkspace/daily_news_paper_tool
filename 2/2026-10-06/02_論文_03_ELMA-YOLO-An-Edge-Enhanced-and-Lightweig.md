# 論文 03：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-10-06
- 來源層級：Tier 1（頂級期刊）（海事）
- 期刊/會議/來源：2026 IEEE International Conference on Pattern Recognition, Machine Vision and Artificial Intelligence (PRMVAI)
- Venue：2026 IEEE International Conference on Pattern Recognition, Machine Vision and Artificial Intelligence (PRMVAI)
- 發布時間：2026-05-01T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/aee3735205693015ec24e2c56bccda49ef4b4b6c
- PDF：
- DOI：10.1109/prmvai70103.2026.11605595
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：957（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Robust perception of maritime targets is critical for intelligent navigation, ocean surveillance, and autonomous vessel systems. In practical sea-surface scenes, illumination changes, reflection interference, cluttered backgrounds, and small or low-contrast targets often degrade detection reliability. Our work presents ELMA-YOLO, a compact detector built on YOLOv8n. The network incorporates EIEStem to strengthen boundary-aware and structural representations at the input stage, and introduces LSCD head to suppress parameter redundancy and lower computational cost. Experiments on SeaShips demonstrate that ELMA-YOLO obtains an mAP.50:.95 of 0.783 with 2.36M parameters and 6.7 GFLOPs, outperforming the baseline models in overall detection performance. These results verify that the proposed design improves recognition capability with a smaller model footprint, making it suitable for efficient maritime target detection on hardware-limited platforms.

## 背景與目的
海上目標偵測對智慧航行、海洋監測與自主船舶系統至關重要，但實際海面場景常面臨光照變化、反射干擾、雜亂背景以及小型或低對比度目標，導致偵測可靠度下降。現有輕量化偵測器在邊緣感知與參數效率間仍有提升空間。本文旨在提出一個緊湊且強化邊緣特徵的檢測器 ELMA-YOLO，以在有限硬體資源下提升海上目標辨識能力。

## 方法
問題設定為單張海面影像輸入，輸出目標邊界框與類別。整體架構基於 YOLOv8n，並在輸入階段引入 EIEStem 模組，專門強化邊緣感知與結構化表徵，使網路更能捕捉目標輪廓；在偵測頭部採用 LSCD head，設計目標為抑制參數冗餘並降低計算量。資料前處理與特徵表示沿用 YOLOv8n 標準流程（縮放、歸一化、資料增強），訓練目標與損失函數未於摘錄中詳細說明，推測仍採用 YOLO 系列的多任務損失（分類、邊界框回歸、物件度）。推論流程與 YOLOv8n 一致，僅在 Stem 與 Head 替換為提出模組。關鍵差異在於：(1) EIEStem 提供邊緣增強的初始特徵；(2) LSCD head 以輕量化設計減少參數與 FLOPs，並在整體偵測性能上優於基線模型。

## 結果
在 SeaShips 資料集上，ELMA-YOLO 達到 mAP@0.50:0.95 = 0.783，參數量 2.36M，計算量 6.7 GFLOPs，整體偵測表現優於基線模型。摘錄未提供可驗證的逐類別 mAP、推論速度或消融實驗數字，僅能觀察到定性結論：提出的邊緣增強 Stem 與輕量化 Head 能在更小模型體積下提升辨識能力。

## 限制與展望
僅在單一 SeaShips 資料集驗證，缺乏跨資料集、不同海況與光照條件的泛化評估；未公開訓練超參數、損失函數細節、消融實驗與實際硬體部署延遲，難以全面判斷實用性；EIEStem 與 LSCD head 內部結構未於摘錄揭露，無法確認其具體創新點與計算權衡；後續研究可擴展至多模態融合、更大規模基準測試與邊緣裝置實測。
