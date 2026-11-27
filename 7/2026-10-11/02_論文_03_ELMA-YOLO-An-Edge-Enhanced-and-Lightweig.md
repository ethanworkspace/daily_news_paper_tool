# 論文 03：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-10-11
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
海上目標偵測在智慧航行、海洋監視與自主船舶系統中至關重要。實際海面場景常面臨光照變化、反射干擾、雜亂背景以及微小或低對比度目標，導致現有偵測器可靠度下降。現有輕量化模型在邊緣感知與參數效率間難以取得平衡。本文旨在提出一個緊湊偵測器 ELMA-YOLO，基於 YOLOv8n，透過改進輸入階段與檢測頭，提升邊緣感知與結構表達，同時抑制參數冗餘，以適應硬體資源受限平台。

## 方法
問題設定為單階段海上目標物件偵測，輸入為海面影像，輸出為目標類別與邊界框。整體架構沿用 YOLOv8n 的骨幹網路、頸部特徵融合與檢測頭結構，並在兩處引入創新模組： 1. EIEStem（輸入階段增強模組）：置於網路最前端，專門強化邊緣感知與結構化表達，使模型對低對比度、小目標的邊界資訊更敏感。具體操作細節（如卷積核大小、注意力機制或邊緣提取策略）於摘錄中未說明。 2. LSCD Head（輕量化結構化檢測頭）：取代原始 YOLOv8n 的檢測頭，設計目標為抑制參數冗餘並降低計算量，採用更精簡的卷積組合與特徵聚合方式，具體層數、通道數與連接方式未於摘錄揭露。 資料前處理、特徵表示、訓練目標（如 CIoU Loss、分類交叉熵等）與最佳化策略（學習率排程、資料增強）在提供文本中均未提及。推論流程遵循標準 YOLO 前向傳播：影像經 EIEStem、骨幹、頸部、LSCD Head 輸出預測框。關鍵差異在於輸入端加入邊緣增強與檢測頭輕量化，旨在以更少參數（2.36M）與算力（6.7 GFLOPs）達到更高 mAP。

## 結果
在 SeaShips 資料集上，ELMA-YOLO 達到 mAP@0.50:0.95 = 0.783，模型參數量 2.36M，計算量 6.7 GFLOPs。作者宣稱整體偵測表現優於基線模型（YOLOv8n 及其他基線），但摘錄未提供基線具體數值以供驗證。定性結論顯示：輕量化設計兼顧邊緣感知與參數效率，適合硬體受限平台部署。

## 限制與展望
僅在單一 SeaShips 資料集驗證，缺乏跨資料集、不同海況與目標尺度的泛化實證。EIEStem 與 LSCD Head 的內部結構、超參數設定、訓練損失函數細節未公開，難以復現與深入分析。未報告實際推論延遲、功耗或嵌入式裝置部署結果。消融實驗與各模組貢獻度量缺失，無法確認邊緣增強與輕量化頭部的相對效益。後續研究可擴展至多場景資料、提供完整模組細節與硬體實測，並探討模型在極端光照與雜訊下的魯棒性。
