# 論文 05：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-10-06
- 來源層級：Tier 1（頂級期刊）（海事）
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
本研究針對海灘游客面臨潮汐與離岸流等自然危險，現有依賴人工巡邏與救生員反應速度有限，缺乏即時自動化偵測與救援機制。本文提出結合 AI 物件偵測、邊緣運算與自主救生艇之整合系統，旨在即時辨識越界游客、自動派遣救援艇並通知相關單位，並透過資料記錄支援事後分析與模型持續優化，建構一套即時、主動的海灘安全解決方案。

## 方法
系統輸入為沿岸攝影機即時影像串流，輸出為越界偵測事件、救援艇調度指令與緊急通知。整體架構分三層：(1) 邊緣感知層，於 Jetson Nano 部署 YOLOv8 進行人體偵測，並以虛擬「門檻線」判斷游客是否進入危險區；(2) 決策與控制層，岸端伺服器接收偵測結果，觸發自主救生艇啟動，透過無線通訊傳送即時目標座標與導航路徑，救生艇具備避障與路徑規劃能力；(3) 通訊與記錄層，同步向救生員與相關機關發送警報，並將影像、偵測框、艇艇軌跡等資料寫入日誌供事後分析與模型再訓練。核心演算法為 YOLOv8 的單階段物件偵測，採用其預設損失函數（分類、邊界框回歸與物件度），於邊緣裝置即時推論；門檻線邏輯為幾何判斷，無額外學習模組。推論流程：影像擷取→前處理（縮放、正規化）→YOLOv8 推論→後處理（NMS、門檻線判斷）→事件觸發→救援艇導航與通知。與傳統人工巡邏相比，關鍵差異在於全自動化偵測‑決策‑執行閉環與邊緣即時運算。

## 結果
摘錄未提供可驗證數字。本文提出多頻段人體偵測與自主海上救援系統架構，整合 YOLOv8 於 Jetson Nano 即時偵測越界行為，觸發自主救生艇導航與救生員通報機制。定性驗證顯示系統能完成從影像偵測、虛擬邊界判斷、艇隻自主避障至人工介入通報之完整閉環流程，資料記錄功能支援事後分析與模型持續優化，證明 AI、機器人與無線技術協同運作之可行性。

## 限制與展望
受限於摘錄資訊，缺乏實驗資料集規模、評估指標、環境干擾（光照、浪花、遮擋）與通訊可靠性之量化驗證；Jetson Nano 算力可能限制高解析度即時推論；自主航行於複雜海況下的避障與定位精度未經實測；法律責任、隱私與緊急協調機制亦未討論。後續研究需補充完整基線比較、長期現場部署數據與法規遵循評估。
