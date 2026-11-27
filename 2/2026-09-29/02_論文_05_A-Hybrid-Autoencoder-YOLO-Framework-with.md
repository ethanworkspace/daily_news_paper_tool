# 論文 05：A Hybrid Autoencoder YOLO Framework with Spatial Regularization for Rapid Small Maritime Object Detection.

- 日期：2026-09-29
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
海港監控、船舶追蹤與海上安全需要可靠的海事物件偵測，但現有方法面臨兩大困境：類別極度不平衡（IMO 號碼僅佔標註物件 1.2%）與空間不一致（預測的 IMO 常落在船體外）。標準偵測器與傳統類別平衡策略無法同時解決，導致研究驗證與實務表現脫節。本文提出混合自編碼器‑YOLO 架構，結合重建引導學習與可微分空間正則化，首次同步處理類別不平衡與空間不一致，旨在提升 IMO 偵測精度並保持即時推論速度。

## 方法
問題設定為雙類別偵測：船舶與 IMO 號碼，輸入為海事影像，輸出為兩類別的邊界框與類別機率。整體架構採用共享的 YOLOv8 編碼器，分別接上偵測頭（輸出船舶與 IMO 的框與分數）與輔助重建解碼器（SkipDecoder，採 U‑Net 風格跳躍連接），使編碼器同時學習判別特徵與影像重建特徵。核心模組包含：1) 重建損失（如 MSE 或 L1）引導編碼器保留精細紋理，緩解 IMO 樣本稀少導致的特徵退化；2) 空間限制損失，利用預測的船舶框與 IMO 框，強制每個 IMO 框幾何上落在對應船舶框內，損失可微分並僅依賴預測框；3) 課程式權重排程，先進行自編碼器預訓練（僅重建損失），再進入聯合優化階段，逐步增加空間損失權重。訓練目標為偵測損失（CIoU + 分類交叉熵）+ 重建損失 + 空間限制損失的加權和。推論時僅保留偵測頭，解碼器被丟棄，因此推論速度不受重建分支影響。與既有方法關鍵差異在於：同時引入重建輔助任務與幾何正則化，並以課程學習平衡兩者，首次在單一框架內解決類別不平衡與空間不一致。

## 結果
在 297 張標註影像（五折交叉驗證，保留 47 張測試集）上，完整模型於測試集達到 IMO AP50‑95 50.1%、Precision 97.8%、F1‑score 94.6%，較基線 YOLOv8s 分別提升 +7.8、+6.5、+5.2 個百分點。消融實驗顯示重建輔助貢獻 +4.5 pp AP50‑95，空間正則化貢獻 +3.3 pp。船舶 AP50‑95 從 77.0% 降至 55.6%，作者認為在 IMO 為唯一船舶識別碼的前提下可接受。推論延遲為 8.0 ms/張（NVIDIA A100），較 YOLOv8s 10.0 ms 快 20%。與 RetinaNet、Faster R‑CNN、DETR、EfficientDet 等主流偵測器（皆以 COCO 預訓練骨幹微調）比較，最高 IMO AP50‑95 僅 42.3%，凸顯任務難度與本方法優勢。

## 限制與展望
資料集規模較小（297 張），且僅涵蓋特定港口場景，泛化能力需在更多海域、光照、天氣條件驗證。船舶偵測 AP 明顯下降，顯示共享編碼器在雙任務間存在權衡，未來可探索任務特定解碼器或多尺度特徵融合。空間限制損失依賴預測框，早期訓練階段框品質差可能產生噪聲梯度，課程權重排程的超參數敏感度未詳細分析。論文未公開程式碼與完整超參數，復現性受限。後續研究可擴大標註資料、引入弱監督或自監督策略，並評估於邊緣裝置即時部署的功耗與延遲表現。
