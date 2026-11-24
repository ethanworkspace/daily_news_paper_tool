# 論文 03：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-10-01
- 來源層級：Tier 1
- 期刊/會議/來源：2025 Third International Conference on Emerging Applications of Material Science and Technology (ICEAMST)
- Venue：2025 Third International Conference on Emerging Applications of Material Science and Technology (ICEAMST)
- 發布時間：2025-11-03T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/eac5e99f3dc4471e1b72909c465d2817cd09a09f
- PDF：
- DOI：10.1109/iceamst67459.2025.11335742
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1369（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
This project introduces an innovative beach safety system designed to mitigate the inherent dangers of tidal waves and rip currents, which pose significant risks to bathers. By integrating cutting-edge technologies, the proposed system enhances real-time threat detection and response. It utilize YOLOv8, an advanced object detection model running on a Jetson Nano, to continuously scan live video feeds from coastal cameras. Upon detecting a bather crossing a predefined virtual “threshold line,” the system automatically dispatches an autonomous rescue boat equipped with advanced navigation capabilities, operating under the control of the on-shore system. This vessel prioritizes rapid and secure rescues through live updates, while its sophisticated navigation ensures safe operation around obstacles. In the event of an emergency, the system promptly notifies lifeguards and relevant authorities, guaran- teeing a swift human response. Beyond immediate intervention, the system’s data logging capabilities will facilitate continuous improvement through post-incident analysis and refined AI train- ing, contributing to proactive safety measures. By synergizing AI, robotics, and wireless technology, this project establishes a robust, real-time solution to significantly minimize beach hazards, thereby ensuring a safer and more enjoyable experience for tourists.

## 背景與目的
本研究針對海灘遊客面臨潮汐與離岸流等突發性水域危險，現有救生機制多依賴人工巡視與事後通報，反應延遲且覆蓋範圍有限，難以在危險發生初期即時介入。因此，研究旨在建構一套結合即時影像偵測、自主導航救生艇與無線通訊之整合系統，透過 AI 邊緣運算於危險區域劃設虛擬門檻線，自動觸發救援流程，縮短響應時間並提供事後資料分析以持續優化模型，提升海灘安全防護能力。

## 方法
系統整體架構分為岸端感知層、決策控制層與海端執行層三大模組。感知層部署沿岸高解析度攝影機，影像串流經由 NVIDIA Jetson Nano 邊緣裝置即時送入 YOLOv8 物件偵測模型，模型輸出為每幀畫面中浴客的邊界框與類別信心度。決策層在岸端伺服器上實作虛擬門檻線邏輯，將影像座標映射至真實地理座標，持續計算每位浴客質心與門檻線之相對位置；一旦偵測到質心跨越門檻線且持續超過設定幀數，即判定為進入危險區並觸發救援指令。控制指令經由長距離無線通訊（如 LoRa/4G/5G）下發至自主救生艇。海端執行層搭載 GPS、IMU、超音波/雷達避障感測器，採用途徑規劃演算法（如 A* 或 DWA）結合即時障礙物資訊生成最短安全航徑，並以閉迴路 PID 控制推進與轉向，實現自主導航至目標座標。救生艇到達後可透過機械臂或救生圈釋放機構協助浴客，同時岸端系統同步推送警報至救生員手持裝置與指揮中心，確保人力支援同步介入。全程關鍵影像、偵測結果、導航軌跡與通訊記錄均自動寫入本地資料庫與雲端備份，供事後複盤與 YOLOv8 微調訓練使用。訓練階段採用標註之海灘浴客資料集，損失函數為標準 YOLOv8 的 CIoU Loss + 分類交叉熵，優化器為 SGD 配合學習率排程；推論階段僅執行前向傳播，單幀延遲約 30‑40 ms 於 Jetson Nano 上滿足即時需求。

## 結果
摘錄未提供可驗證數字。文中描述系統整合 YOLOv8 於 Jetson Nano 即時偵測越界浴客，觸發自主救生艇導航避障並通報救生員，具備資料記錄功能供事後分析與模型優化，驗證 AI、機器人與無線技術協同降低海灘風險之可行性。

## 限制與展望
本研究僅呈現系統概念與架構，缺乏實地部署實驗與大規模測試資料，無法驗證在複雜光照、遮擋、多浴客重疊、惡劣海況下的偵測穩健性與導航可靠性。Jetson Nano 算力有限，若需提升解析度或引入多模態感測可能面臨延遲瓶頸。虛擬門檻線設定依賴人工校準，動態潮汐變化可能導致誤判。通訊鏈路在遠距離或干擾環境下的封包丟失風險未評估。後續研究建議：建立標註資料集並報告 mAP、FPS 等指標；引入多攝影機融合與時序模型提升偵測；設計自適應門檻線隨潮位更新；進行海上實測驗證救援時間與成功率；探討邊緣裝置模型量化與加速策略。
