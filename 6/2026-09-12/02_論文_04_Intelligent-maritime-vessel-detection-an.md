# 論文 04：Intelligent maritime vessel detection and classification toward offshore wind energy zone surveillance using YOLOv11 and explainable hybrid machine learning for autonomous maritime monitoring

- 日期：2026-09-12
- 來源層級：Tier 3（海事頂刊）（海事）
- 期刊/會議/來源：Ocean Engineering
- Venue：Ocean Engineering
- 發布時間：2026-08-13T00:00:00+00:00
- URL：https://doi.org/10.1016/j.oceaneng.2026.127443
- PDF：https://www.sciencedirect.com/science/article/pii/S0029801826032774/pdf
- DOI：10.1016/j.oceaneng.2026.127443
- arXiv：
- 影響指標：2yr_mean_citedness=7.26, h_index=192, i10_index=15505 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Ocean Engineering
- 引用數：1
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1364（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The rapid global expansion of offshore wind energy facilities creates new surveillance challenges within coastal transition regions. Motivated by this, the Offshore Zone Risk Weighted Detection (OZRWD) framework is proposed for offshore surveillance and evaluated on the SeaShips coastal dataset. To overcome sea clutter and structural occlusions, OZRWD YOLOv11 integrates a squeeze and excitation channel attention mechanism. On SeaShips, it achieves 0.971 mAP@0.5, outperforming baseline YOLO variants and significantly enhancing the detection of morphologically challenging categories like fishing boats. Following detection, an XGBoost classifier analyses bounding box attributes to attain 93.7% accuracy. This is paired with SHapley Additive exPlanations (SHAP) to provide auditable, feature level decision transparency, bridging the gap between deep learning perception and maritime regulatory compliance. A novel Zone Risk Scoring (ZRS) module then fuses predicted vessel class, spatial proximity, and detection confidence into a continuous operational risk indicator. With processing times of 12.3 ms per frame, this real time, explainable pipeline represents a viable approach for potential deployment in offshore wind energy areas. Future work may extend this architecture via Multi Agent Reinforcement Learning (MARL) for autonomous patrol coordination.

## 背景與目的
離岸風電設施快速擴展帶來沿海過渡區監控新挑戰，現有目標偵測方法在海面雜波、結構遮蔽與多樣船型下表現不穩，且缺乏可解釋的風險評估機制，難以滿足海事法規合規需求。本文旨在提出離岸區風險加權偵測（OZRWD）框架，結合改良 YOLOv11、可解釋混合機器學習與區域風險評分，實現即時、透明且具操作風險指標的自主海上監控。

## 方法
問題設定：輸入為海岸監視影像，輸出為船舶邊界框、類別、偵測信心與連續風險分數。整體架構分三階段：(1) OZRWD YOLOv11 偵測器，在 YOLOv11 主幹加入 Squeeze‑and‑Excitation 通道注意力模組，強化對海面雜波與結構遮蔽下特徵的自適應加權，訓練目標採用 CIoU 定位損失、分類交叉熵與物件置信度損失的加權和；資料前處理使用 SeaShips 沿海資料集，進行隨機縮放、水平翻轉與色彩抖動增強。(2) 偵測後 XGBoost 分類器，以邊界框屬性（中心座標、寬高、長寬比、偵測信心、類別機率）為特徵，進行二階段精細分類，達 93.7% 準確率；並引入 SHAP 計算各特徵對分類決策的貢獻，提供可稽核的特徵級解釋。(3) 區域風險評分（ZRS）模組，融合預測船舶類別、空間距離風電區邊界與偵測信心，經加權加總產生連續操作風險指標。推論流程為：影像 → YOLOv11 → 邊界框與信心 → XGBoost + SHAP → 類別與解釋 → ZRS → 風險分數。全管線單幀處理約 12.3 ms，滿足即時部署需求。關鍵差異在於將通道注意力嵌入 YOLOv11、引入可解釋 XGBoost+SHAP 二階段分類，並設計風險導向的 ZRS 融合模組。

## 結果
在 SeaShips 資料集上，OZRWD YOLOv11 達到 mAP@0.5 0.971，優於基準 YOLO 變體，尤其對漁船等形態困難類別提升顯著。XGBoost 二階段分類準確率 93.7%，SHAP 提供特徵重要度視覺化，滿足法規可稽核性。ZRS 產出連續風險分數，能反映船舶類別、接近度與信心綜合影響。整體管線單幀 12.3 ms，具備即時監控可行性。

## 限制與展望
實驅僅在 SeaShips 單一沿海資料集驗證，缺乏跨區域、不同海況與多感測器融合的泛化證據；XGBoost 依賴手工邊界框特徵，未探討端到端可學習表示；SHAP 解釋僅限特徵層級，未涵蓋時序或上下文資訊；ZRS 權重設定為啟發式，未經實際事故資料校準；硬體平台與功耗細節未揭露，部署可行性仍待實地測試；後續 MARL 協同巡邏尚未實作。
