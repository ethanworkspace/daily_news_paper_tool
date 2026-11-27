# 論文 05：A Hybrid Autoencoder YOLO Framework with Spatial Regularization for Rapid Small Maritime Object Detection.

- 日期：2026-09-30
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
海上物件偵測對港口監控、船舶追蹤與海上安全至關重要，但實務上嚴重類別不平衡（IMO 號碼僅佔標註物件 1.2%）與空間不一致（預測 IMO 常落在船體外）兩大挑戰。現有偵測器與傳統類別平衡策略無法同時解決此兩問題，導致研究驗證與實際效能持續落差。本文提出混合自編碼器-YOLO 架構，結合重建引導學習與可微分空間正則化，首次同步處理類別不平衡與空間不一致，旨在提升 IMO 號碼偵測精度並符合物理約束，縮小實務部署鴻溝。

## 方法
問題設定：輸入海上影像，輸出船舶與 IMO 號碼兩類邊界框。整體架構採用共享 YOLOv8 編碼器，分別連接雙任務偵測頭（船舶、IMO）與輔助重建解碼器（SkipDecoder，具 U-Net 風格跳躍連接）。核心模組包含：(1) 重建解碼器，從編碼器特徵重建輸入影像，強化對小目標 IMO 的特徵表達；(2) 空間限制損失，利用預測框強制每個 IMO 框落在對應船舶框內，實現可微分幾何約束。資料前處理：使用 297 張標註影像，採五折交叉驗證並保留 47 張測試集。訓練分兩階段：第一階段自編碼器預訓練（僅重建損失），第二階段聯合優化，結合 YOLOv8 偵測損失、重建損失與空間限制損失，並對空間權重採課程排程逐步增加。推論時僅保留偵測頭，解碼器移除，單張影像 8.0 ms（A100）。關鍵差異：首創以重建引導學習緩解類別不平衡，並以可微分空間正則化解決空間不一致，雙管齊下且無需額外標註。

## 結果
於 47 張測試集上，完整模型達 IMO AP50-95 50.1%、Precision 97.8%、F1 94.6%，較基線 YOLOv8s 分別提升 +7.8、+6.5、+5.2 個百分點。消融顯示重建指導貢獻 +4.5 pp，空間正則化貢獻 +3.3 pp。船舶 AP50-95 從 77.0% 降至 55.6%，作者認為可接受。推論速度 8.0 ms/張，較 YOLOv8s 10.0 ms 快 20%。與 RetinaNet、Faster R-CNN、DETR、EfficientDet 比較，皆無法超過 IMO AP50-95 42.3%，凸顯任務難度與本方法優勢。

## 限制與展望
資料集僅 297 張影像，類別極度不平衡且缺乏多樣環境驗證，泛化能力待確認。船舶偵測精度下降顯著，可能影響下游追蹤。空間限制損失依賴預測框品質，錯誤傳播風險存在。未來需擴大資料、評估不同海況、探討端到端聯合優化與輕量化部署。
