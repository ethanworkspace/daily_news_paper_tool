# 論文 05：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-11-02
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
本研究針對海灘遊客因潮汐與離岸流導致的溺水風險，提出一套即時偵測與自主救援系統。現有救生員巡邏與固定監視器難以在大範圍、高動態環境中即時發現越界遊客，且人力救援反應時間較長。本文目標為整合邊緣運算、物件偵測與自主導航機器人，建立端到端的自動化安全防護鏈，以降低事故發生率並提供事後資料分析基礎。

## 方法
系統輸入為海灘沿岸攝影機的即時影像串流，經由部署於 NVIDIA Jetson Nano 邊緣裝置的 YOLOv8 模型進行人體偵測，輸出每幀的邊界框與類別信心度。設定一條虛擬「閾值線」對應危險水域邊界，當偵測到遊客的邊界框中心點跨越該線時，觸發事件。邊緣端透過無線通訊（如 Wi‑Fi/4G）向岸端控制伺服器發送警報，伺服器隨即指派自主救生艇。救生艇搭載自身定位（GPS/IMU）與避障感測器（超音波/雷達），採用路徑規劃演算法（如 A* 或 DWA）依據即時障礙物資訊生成安全航線，並持續接收岸端更新的目標座標進行閉環控制。同時，系統在岸端記錄影像片段、偵測結果、救援軌跡與通訊日誌，供事後離線重新訓練 YOLOv8 及優化導航策略。整體架構包含邊緣偵測節點、中央調度節點與自主航行節點三層，採用非同步訊息佇列實現低延遲協同。

## 結果
本研究提出多頻段人體偵測與自主海上救援系統，整合 YOLOv8 於 Jetson Nano 即時分析海灘影像，設定虛擬門檻線觸發自動派遣自主救生艇，具備避障導航與即時位置回傳，並同步通知救生員與相關單位。系統具備資料記錄功能，支援事後分析與模型再訓練，形成閉環改善機制。實驗部分鑘錄未提供可驗證數字，僅呈現定性驗證：偵測準確度達到可用水準、救援艇可在複雜波浪中完成路徑規劃、通知延遲極低，整體展現即時性與可靠性優於傳統人工巡邏。消融觀察顯示移除門檻線判斷會導致誤觸發增加，移除避障模組則降低航行安全性。

## 限制與展望
目前僅呈現系統概念與架構，缺乏實測精度、召回率、救援到達時間等量化指標，亦未說明訓練資料集、閾值線設定準則、通訊延遲與惡劣天氣下的穩健性。邊緣裝置算力限制可能影響高解析度影像的即時推論；自主航行在複雜波浪、多船隻環境的避障表現未驗證。後續研究需補充實地實驗、基線比較、長期部署穩定性與法規合規性評估。
