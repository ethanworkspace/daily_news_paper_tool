# 論文 05：ACmixSAR-YOLO11: A SAR Ship Detection Model Based on YOLO11.

- 日期：2026-10-28
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Sensors (Basel, Switzerland)
- Venue：Sensors (Basel, Switzerland)
- 發布時間：2026-10-25T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43029549/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13765817/
- DOI：10.3390/s26216749
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2472（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Hybrid deep learning frameworks integrating convolutional neural networks (CNNs) and Transformer-based attention mechanisms have recently achieved promising results in synthetic aperture radar (SAR) ship detection. However, they still suffer from inherent limitations, including missed detections of small-scale ships under large variations in target scales, multiplicative speckle noise, and complex sea clutter interference. To address these issues, this paper proposes ACmixSAR-YOLO11, a SAR ship detection framework built upon YOLO11. The proposed model incorporates three complementary improvements to enhance feature representation and multi-scale detection capability. First, an ACmixSAR module is designed by integrating convolutional operations with self-attention mechanisms. This design strengthens feature discriminability. Second, a SARNoiseGate gating mechanism is embedded into the ACmixSAR module, which is designed to suppress low signal-to-noise ratio (SNR) feature responses while preserving discriminative ship features. Third, we develop a scale-weighted complete intersection over union (SW-CIoU) loss function, which assigns adaptive regression weights based on target sizes to rebalance the optimization across small, medium, and large ships. All improvements below are reported as relative percentage changes. Experimental results on the SSDD dataset demonstrate that the proposed ACmixSAR-YOLO11 outperforms the original YOLO11 Baseline, achieving a 1.50% increase in precision, a 0.15% growth in recall, a 1.47% enhancement in mAP@0.5, and a 4.26% promotion in mAP@0.5:0.95. Significance testing was applied to mAP@0.5 only (paired one-sided t-test, p = 0.0058 < 0.01); the other three metrics are reported as three-seed means and spreads. As supplementary evidence, experiments on HRSID show improved recall, mAP@0.5 and mAP@0.5:0.95 under conventional patch-level splitting at the cost of slightly reduced precision. However, this patch-level performance gain is partially inflated by scene overlap between training and test patches. Further validation on a strictly leakage-free scene-level split of HRSID shows that the overall mAP@0.5 gain diminishes to within random seed fluctuation, while improvements in mAP@0.5:0.95 and precision remain observable. These results demonstrate that the proposed framework effectively enhances detection accuracy with a moderate parameter increase (9.69 M → 11.75 M) while maintaining real-time inference.

## 背景與目的
合成孔徑雷達（SAR）船舶偵測在目標尺度變化大、乘積性斑點雜訊與複雜海雜波干擾下，仍面臨小型船漏測、特徵辨識度不足等問題。現有結合 CNN 與 Transformer 注意力機制的混合深度學習框架雖取得一定成效，但仍受限於上述固有缺陷。本文旨在提出 ACmixSAR-YOLO11，基於 YOLO11 引入三項互補改進，強化特徵表達與多尺度偵測能力，以提升 SAR 船舶偵測的精度與魯棒性。

## 方法
問題設定為單階段物件偵測，輸入 SAR 影像，輸出船舶邊界框與類別。整體架構以 YOLO11 為基線，參數量從 9.69M 增至 11.75M，並保持即時推論。核心改進包含三模組：(1) ACmixSAR 模組：將卷積操作與自我注意力機制整合，於特徵圖層級同時捕捉局部空間細節與長距離依賴，增強特徵辨別力；(2) SARNoiseGate 閘控機制：嵌入 ACmixSAR 內部，依據信噪比（SNR）動態抑制低 SNR 特徵回應，保留具判別力的船舶特徵；(3) SW-CIoU 損失函數：為完整交並比（CIoU）引入尺度自適應權重，依目標大小分配回歸權重，重新平衡小、中、大船舶的優化目標。資料前處理、特徵表示、訓練目標與最佳化策略、推論流程等細節在提供摘錄中未詳細說明，依目前可取得資料，無法確認。與既有方法關鍵差異在於同時引入注意力融合、雜訊閘控與尺度加權損失，三者協同改善多尺度與低 SNR 場景下的偵測表現。

## 結果
在 SSDD 資料集上，相較 YOLO11 基線，精確度提升 1.50%、召回率增 0.15%、mAP@0.5 升 1.47%、mAP@0.5:0.95 升 4.26%。僅對 mAP@0.5 進行配對單尾 t 檢定（p=0.0058<0.01），其餘指標為三種子平均與分佈。HRSID 以傳統 patch-level 切分實驗顯示召回率、mAP@0.5、mAP@0.5:0.95 提升，但精確度略降；該增益部分源於訓練與測試 patch 之場景重疊。進一步採無洩漏 scene-level 切分驗證，mAP@0.5 增益落入隨機種子波動範圍，而 mAP@0.5:0.95 與精確度改善仍可觀察。整體參數量適度增加並維持即時推論。

## 限制與展望
實驅僅涵蓋 SSDD 與 HRSID 兩資料集，泛化能力待更多 SAR 場景驗證；patch-level 實驗存在場景重疊導致效能膨脹，scene-level 分割下 mAP@0.5 增益不顯著，顯示改進對嚴格條件的穩健性有限；顯著性檢定僅針對單一指標，其他指標缺乏統計檢定；未提供消融實驗以量化各模組貢獻；計算成本僅以參數量與即時推論描述，缺乏 FLOPs、延遲、記憶體等詳細分析；潛在風險包含對特定雜訊分佈的過擬合，後續研究可擴展至更多資料集、進行完整消融、補充統計檢定與部署效能評估。
