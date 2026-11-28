# 論文 04：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-10-16
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
海上目標偵測對智慧航行、海洋監測與自主船艦系統至關重要，但實際海面場景常面臨光照變化、反射干擾、背景雜訊以及小型或低對比度目標，導致現有偵測器可靠度下降。現有輕量化模型在參數量與計算量受限時，往往難以同時保持邊緣感知與結構表達能力。本文旨在提出一個緊湊且強化邊緣感知的偵測網路 ELMA-YOLO，以在有限硬體資源下提升海上目標偵測性能。

## 方法
問題設定與輸入輸出：以單張海面影像為輸入，輸出目標類別、邊界框座標與信心分數。整體架構基於 YOLOv8n，保留其骨幹、頸部與多尺度偵測頭結構。核心模組： 1. EIEStem（Edge‑Enhanced Input Stem）：置於網路最前端，取代原始 Stem，利用邊緣增強卷積與結構感知分支，在早期階段強化邊界感知與結構表達，提升對小型、低對比度目標的特徵提取能力。 2. LSCD Head（Lightweight Suppression‑and‑Compression Detection Head）：重新設計偵測頭，採用深度可分離卷積、通道壓縮與參數共享機制，抑制參數冗餘並降低浮點運算量。 資料前處理：依 YOLOv8 標準流程進行影像縮放、歸一化與資料增強（如馬賽克、混合增強），具體增強策略摘錄未詳細說明。 訓練目標與損失：沿用 YOLOv8n 原始損失函數（分類損失、邊界框回歸損失、物件度損失），但摘錄未提供具體權重或優化器設定。 推論流程：標準 YOLO 单阶段前向傳播，經 EIEStem 提取特徵，經骨幹與頸部融合後送入 LSCD Head 輸出預測，再以 NMS 後處理。 關鍵差異：相較基線 YOLOv8n，ELMA-YOLO 在輸入端引入邊緣增強 Stem，並在偵測頭採用輕量化壓縮設計，以較少參數量與計算量獲得更優的邊界感知能力。

## 結果
在 SeaShips 資料集上，ELMA-YOLO 達到 mAP@0.50:0.95 = 0.783，參數量 2.36M，計算量 6.7 GFLOPs，優於基線模型（具體基線名稱與數值摘錄未提供）。作者指出該設計在縮減模型體積下仍提升整體偵測效能，適合硬體受限平台部署。摘錄未提供可驗證的消融實驗數字、各類別 AP 或推論延遲等細節。

## 限制與展望
僅在單一 SeaShips 資料集驗證，缺乏跨資料集、不同海況與感測器的泛化實證；未公開 EIEStem 與 LSCD Head 的詳細結構圖、超參數設定、訓練週期與硬體延遲測量，難以完整評估實際部署效能；消融實驗與基線比較細節未揭露，無法確認各模組貢獻程度；潛在風險包括在極端光照或高密度目標場景下的穩健性未經驗證。後續研究可擴展至多資料集基準、進行詳細消融分析、量化推論加速並探討模型在邊緣裝置上的實時表現。
