# 論文 05：ELMA-YOLO: An Edge-Enhanced and Lightweight Network for Maritime Object Detection

- 日期：2026-10-20
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
海上目標偵測在智慧航行、海洋監測與自主船舶系統中扮演關鍵角色，但實際海面場景常面臨光照變化、反射干擾、背景雜訊以及微小或低對比度目標，導致偵測可靠度下降。現有輕量化偵測器在參數量與計算量受限時，往往難以兼顧邊緣感知與結構特徵表達。本文提出 ELMA-YOLO，基於 YOLOv8n 設計，引入 EIEStem 強化輸入階段的邊緣感知與結構表示，並以 LSCD head 抑制參數冗餘、降低計算成本，旨在以更小模型體積達到更高偵測性能，適合硬體資源受限平台部署。

## 方法
問題設定為單張海面影像的多類別物件偵測，輸入為 RGB 影像，輸出為邊界框與類別信心度。整體架構沿用 YOLOv8n 的骨幹與頸部，並在兩處進行改良：(1) EIEStem 置於網路輸入端，旨在提升邊緣感知與結構特徵的表達能力，具體模組結構、卷積核大小、注意力機制等細節摘錄未提供，無法確認；(2) LSCD head 取代原始偵測頭，設計目標為減少參數冗餘與浮點運算，具體採用何種深度可分離卷積、群組卷積或知識蒸餾策略，摘錄同樣未說明。訓練目標推測沿用 YOLO 系列的損失函數（如 CIoU loss、分類交叉熵、物件度損失），但摘錄未明確列出損失權重、優化器、學習率排程等超參數。推論流程與 YOLOv8n 一致，經骨幹、頸部、EIEStem 與 LSCD head 後輸出預測框。與既有方法的關鍵差異在於輸入端加入邊緣增強模組、偵測頭採用輕量化設計，其餘組件保持不變。

## 結果
在 SeaShips 資料集上，ELMA-YOLO 達到 mAP@0.5:0.95 = 0.783，模型參數量 2.36M，計算量 6.7 GFLOPs，優於基線模型（具體基線名稱與數值摘錄未提供）。摘錄未提供可驗證的消融實驗數字、各類別 AP、推論延遲或不同解析度下的表現，僅能觀察到整體偵測性能在輕量化條件下有所提升。

## 限制與展望
實驅僅在單一 SeaShips 資料集驗證，缺乏跨資料集、不同海況、不同感測器的泛化性證據；未公開 EIEStem 與 LSCD head 的詳細結構、超參數設定與訓練細節，難以復現與深入分析；未報告實際部署於邊緣裝置的延遲、功耗與記憶體佔用；缺少消融實驗以量化各模組貢獻；潛在風險包括在極端光照或高密度目標場景下性能退化。後續研究可擴展至多資料集評估、模組細節公開、硬體實測與更完整的消融分析。
