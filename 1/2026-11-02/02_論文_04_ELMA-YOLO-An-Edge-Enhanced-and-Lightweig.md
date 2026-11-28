# 論文 04：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-11-02
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
本研究針對海洋目標檢測在智慧航行、海洋監視與自主船舶系統中的關鍵需求，指出實際海面場景中光照變化、反射干擾、背景雜亂以及小型或低對比度目標常導致檢測可靠性下降。現有方法在邊緣感知與結構表達上仍有不足，且模型龐大難以部署於硬體資源受限平台。本文旨在提出一個輕量化且邊緣增強的檢測器 ELMA-YOLO，以在保持高檢測性能的同時大幅降低參數量與計算量，填補輕量化海洋目標檢測的缺口。

## 方法
ELMA-YOLO 基於 YOLOv8n 架構進行改進，主要包含兩大核心模組：(1) EIEStem（Edge-Enhanced Input Stem）置於網路輸入階段，旨在強化邊緣感知與結構化特徵表示，提升對小型、低對比度目標的邊界建模能力；(2) LSCD Head（Lightweight Suppression of Channel Redundancy Detection Head）取代原始檢測頭，透過通道壓縮與特徵融合機制抑制參數冗餘，降低計算複雜度。整體架構保留 YOLOv8n 的骨幹與頸部結構，僅在輸入莖與檢測頭進行替換，維持單階段檢測流程。輸入為海面影像，輸出為目標類別與邊界框。訓練目標採用 YOLOv8 原始損失函數（含分類、邊界框回歸與目標度損失），最佳化策略未於摘錄中說明。推論時直接前向傳播，無額外後處理。與既有輕量化方法相比，關鍵差異在於針對海洋場景的邊緣增強輸入莖與參數高效的檢測頭設計，但摘錄未提供詳細模組內部結構、特徵維度或訓練超參數。

## 結果
實驗於 SeaShips 資料集進行，ELMA-YOLO 達到 mAP@0.5:0.95 0.783，參數量 2.36M，計算量 6.7 GFLOPs。作者宣稱優於基線模型（未具體列出基線名稱與數值）的整體檢測性能，驗證了該設計在更小模型體積下提升識別能力，適合硬體受限平台部署。摘錄未提供可驗證的基線比較數字、消融實驗結果、不同目標尺度的表現或定性案例分析，僅能觀察到定性結論：模型在輕量化前提下保持較高檢測精度。

## 限制與展望
依目前可取得資料，無法確認實驗的完整基線模型清單、消融研究細節、不同海況（如霧、雨、夜間）的泛化能力、實際嵌入式裝置上的推理延遲與功耗表現。方法僅在 SeaShips 單一資料集驗證，缺乏跨資料集評估；EIEStem 與 LSCD 具體結構未公開，難以復現與分析其邊緣增強機制；未討論極小目標、密集目標或遮擋場景的失效模式。後續研究可擴展至多資料集基準、針對邊緣裝置進行量化與加速測試、探討模組對不同海洋目標類別的適應性。
