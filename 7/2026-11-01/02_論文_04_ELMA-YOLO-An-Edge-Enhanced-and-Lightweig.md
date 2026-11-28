# 論文 04：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-11-01
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
海上目標感知對智慧航行、海洋監視與自主船舶系統至關重要。實際海面場景中，光照變化、反射干擾、雜亂背景以及小型或低對比度目標常降低偵測可靠性。現有方法在邊緣感知與輕量化之間難以取得平衡，導致在資源受限平台上部署困難。本文旨在提出一個緊湊偵測器 ELMA-YOLO，基於 YOLOv8n 引入 EIEStem 強化輸入階段的邊緣感知與結構表達，並以 LSCD head 抑制參數冗餘與降低計算成本，以提升海上目標偵測效能並縮減模型體積。

## 方法
本文提出 ELMA-YOLO，以 YOLOv8n 為基礎骨幹。核心改進包含兩大模組：(1) EIEStem：置於網路輸入階段，旨在強化邊緣感知與結構化表達能力，使模型能更有效捕捉海面目標的邊界與結構特徵；(2) LSCD head：取代原始偵測頭，設計目標為抑制參數冗餘並降低計算量，以達成輕量化。整體架構維持 YOLOv8n 的單階段偵測流程，輸入影像經 EIEStem 提取特徵，再經骨幹網路與頸部網路，最後由 LSCD head 輸出偵測結果。摘錄未提供具體的模組內部結構（如卷積核大小、注意力機制、特徵融合方式）、資料前處理細節、特徵表示方式、訓練目標與損失函數形式、最佳化策略（學習率、排程、資料增強）、推論流程細節，亦未說明與既有輕量化 YOLO 變體的關鍵架構差異。因此僅能確認上述兩模組的設計動機與高層定位，詳細技術機制依目前可取得資料無法確認。

## 結果
實驗於 SeaShips 資料集進行，ELMA-YOLO 達到 mAP@0.50:0.95 為 0.783，參數量 2.36M，計算量 6.7 GFLOPs。作者宣稱整體偵測表現優於基線模型，驗證所提設計在縮減模型體積下仍能提升辨識能力，適合硬體受限平台部署。摘錄未提供基線模型名稱、基線數值、消融實驗結果、不同 IoU 閾值下的 mAP、各類別表現、推論速度（FPS）或部署平台實測數據，故無法進行量化比較分析。

## 限制與展望
依目前可取得資料，本研究僅在 SeaShips 單一資料集驗證，缺乏跨資料集泛化能力評估；未提供消融實驗以量化 EIEStem 與 LSCD head 的個別貢獻；未揭露訓練超參數、資料增強策略與損失函數細節，難以復現；未報告實際邊緣裝置（如 Jetson、嵌入式 GPU）上的推論延遲與功耗，輕量化實效尚待實證；潛在風險包含在極端光照、濃霧、高海浪等未涵蓋場景下的魯棒性未知。後續研究可擴展至多資料集基準、完整消融分析、實機部署測試，並探討模組在其他海上任務（如目標追蹤、語意分割）的遷移性。
