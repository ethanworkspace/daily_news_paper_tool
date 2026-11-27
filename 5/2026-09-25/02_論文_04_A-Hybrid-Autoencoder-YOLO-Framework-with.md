# 論文 04：A Hybrid Autoencoder YOLO Framework with Spatial Regularization for Rapid Small Maritime Object Detection.

- 日期：2026-09-25
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Journal of imaging
- Venue：Journal of imaging
- 發布時間：2026-09-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42783857/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13608120/
- DOI：10.3390/jimaging12090433
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2940（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Maritime object detection is essential for port-based surveillance, ship tracking, and maritime security. However, practical implementation encounters two primary challenges: significant class imbalance (IMO identification numbers represent only 1.2% of labelled objects) and spatial inconsistency (predicted IMO numbers often appear beyond ship boundaries). Standard detectors and conventional class-balancing strategies fail to adequately address these difficulties, resulting in a persistent mismatch between research validation and practical performance. We present a hybrid autoencoder-YOLO framework with variable spatial regularisation. To the best of our understanding, this is the first methodology to simultaneously address class imbalance and spatial inconsistency in maritime IMO detection via reconstruction-guided learning and differentiable spatial regularisation. The model uses a YOLOv8 encoder shared by both a detection head (designed for ships and IMO numbers), and an auxiliary reconstruction decoder (a SkipDecoder with U-Net-style skip connections). A unique spatial limitation loss provides the physical restriction that each IMO number must be within a ship's bounding box, using only anticipated boxes. Training occurs in two phases: autoencoder pretraining on the marine dataset, followed by phased joint optimisation with a curriculum schedule for the spatial weighting. In a dataset of 297 annotated images (utilising five-fold cross-validation with a 47-image preserved test set), our comprehensive model achieved 50.1% IMO AP50-95, 97.8% IMO precision, and 94.6% IMO F1-score on the test set, beating the baseline YOLOv8s by +7.8 percentage points, +6.5 percentage points, and +5.2 percentage points, respectively. Ablation studies indicate that reconstruction instruction improves IMO AP50-95 by +4.5 percentage points, while spatial regularisation adds +3.3 percentage points. Although ship detection results in a small compromise (ship AP50-95 decreases from 77.0% to 55.6%), this appears to be practically acceptable given the essential role of IMO numbers as unique ship IDs. Significantly, inference speed improves by 20% (8.0 ms per image on an NVIDIA A100 GPU) relative to YOLOv8s (10.0 ms). Comparisons with leading detectors (RetinaNet, Faster R-CNN, DETR, EfficientDet), all initialised with standard COCO-pretrained backbones and fine-tuned on our dataset, reveal that none achieve an IMO AP50-95 exceeding 42.3%, highlighting the task's challenge and the accuracy of our design. The proposed framework shows potential to address the gap in practical implementation through reconstruction-based feature learning accompanied by a specified geometric baseline. It is precise, accurate, and fast, aligns with specific physics, and shows promise for real-time maritime surveillance applications, though we acknowledge the need for additional thorough verification across many operational environments.

## 背景與目的
海事物體偵測對港口監控、船舶追蹤與海上安全至關重要，但實務部署面臨兩大挑戰：類別不平衡（IMO 號碼僅佔標註物件 1.2%）與空間不一致性（預測的 IMO 號碼常落在船舶邊界框外）。現有偵測器與傳統類別平衡策略難以同時解決這兩問題，導致研究驗證與實際效能持續落差。本文提出混合式自編碼器-YOLO 架構，結合可變空間正則化，旨在透過重建引導學習與可微分空間正則化，同步解決類別不平衡與空間不一致，縮小實務落差。

## 方法
模型採用 YOLOv8 編碼器作為共享骨幹，分別連接偵測頭（負責船舶與 IMO 號碼兩類別）與輔助重建解碼器（SkipDecoder，採 U-Net 風格跳躍連接）。核心創新在於空間限制損失，僅利用預測框即可強制每個 IMO 號碼必須落在對應船舶邊界框內，提供物理幾何約束。訓練分兩階段：第一階段在海事資料集上進行自編碼器預訓練，學習領域特徵表示；第二階段採課程式權重排程進行聯合優化，逐步增加空間正則化權重，使偵測與重建任務協同收斂。推論時僅保留偵測頭，解碼器被捨棄，不增加額外計算負擔。與既有方法相比，關鍵差異在於同時引入重建輔助任務與可微分空間幾何約束，並以課程學習平衡兩者權重。

## 結果
於 297 張標註影像（五折交叉驗證保留 47 張測試集）實驗，完整模型在測試集達 IMO AP50-95 50.1%、精確度 97.8%、F1-score 94.6%，較基線 YOLOv8s 分別提升 +7.8、+6.5、+5.2 個百分點。消融實驗顯示重建指導貢獻 +4.5 pp，空間正則化貢獻 +3.3 pp。船舶偵測 AP50-95 從 77.0% 降至 55.6%，作者認為在 IMO 號碼作為唯一船舶識別碼的前提下可接受。推論速度 8.0 ms/張（NVIDIA A100），較 YOLOv8s 10.0 ms 快 20%。對比 RetinaNet、Faster R-CNN、DETR、EfficientDet（皆以 COCO 預訓練骨幹微調），最高 IMO AP50-95 僅 42.3%，凸顯任務難度與本方法優勢。

## 限制與展望
資料集規模較小（297 張），僅以五折交叉驗證加單一保留測試集評估，泛化能力有待更大規模、多環境驗證。船舶偵測效能顯著下降（AP50-95 降 21.4 pp），可能影響下游追蹤任務。空間限制損失僅依賴預測框，若偵測框本身偏移大，約束效果可能受限。論文亦承認需在更多實務操作環境進一步嚴格驗證，且未探討極端天氣、遮擋、不同解析度等條件下的魯棒性。
