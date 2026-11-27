# 論文 05：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-10-11
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
本研究針對海灘游客面臨潮汐與離岸流等突發性水域危險，現有救生機制多依賴人工巡邏與事後通報，反應速度有限且難以全天候覆蓋。論文指出缺乏即時、自動化之偵測與救援聯動系統，導致溺水風險居高不下。因此，本文目標在建構一套結合 AI 物件偵測、邊緣運算與自主救生艇之即時安全系統，以縮短發現至救援之時間差距，並透過資料記錄支援事後分析與模型持續優化，提升整體海灘安全防護能力。

## 方法
系統整體架構分為四大模組：(1) 影像擷取與邊緣推論模組，部署 YOLOv8 物件偵測模型於 NVIDIA Jetson Nano 邊緣裝置，實時讀取沿岸攝影機串流，輸出游客邊界框與類別信心度；(2) 虛擬門檻判斷模組，預先在影像座標系定義一條「門檻線」，當偵測到游客邊界框中心點跨越該線即觸發警報；(3) 自主救生艇調度與導航模組，岸端控制器經無線通訊向救生艇下發目標座標，救生艇搭載自主導航演算法（含避障、路徑規劃與即時定位），依據即時回傳之游客位置動態更新航向，執行快速且安全之接近與救援動作；(4) 通報與資料記錄模組，事件觸發時同步推送通知至救生員手持裝置與管理後台，並將影像幀、偵測結果、艇隻軌跡與時間戳記寫入資料庫，供事後複盤與模型再訓練使用。推論流程為：影像串流 → YOLOv8 推論 → 門檻判斷 → 觸發調度 → 無線下發目標 → 救生艇自主航行 → 同步通報與記錄。與傳統人工巡邏相比，關鍵差異在於全自動化偵測‑決策‑執行閉環、邊緣低延遲推論以及資料閉環支援持續改進。

## 結果
摘錄未提供可驗證數字。論文僅以文字描述系統能「顯著降低海灘危險」並建立「穩健即時解決方案」，並提及資料記錄可支援事後分析與模型優化，但未呈現具體偵測準確率、救援成功率、反應時間、誤報率或與基線方法之量化比較。因此僅能觀察到定性結論：系統整合 AI 偵測與自主艇具備端到端自動化潛力，實際效能仍待實驗驗證。

## 限制與展望
受限於摘錄資訊，缺乏實驗數據集、評估指標、硬體效能基準、環境干擾（光照、浪高、遮擋）與通訊可靠性之實測結果；模型版本、訓練資料來源、超參數設定未揭露，難以重現。部署層面未討論電力續航、法規合規、多艇協同與大規模海灘擴展性。後續研究需補充完整實證、消融實驗與長期現場驗證。
