# 論文 01：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-09-21
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
針對海灘遊客面臨潮汐與離岸流等隱性溺水風險，現有救生機制多依賴人工巡視與被動通報，難以在事發初期即時偵測並快速介入。本研究旨在整合人工智慧、機器人與無線通訊技術，建構一套即時威脅偵測與自主海上救援系統，透過邊緣運算裝置部署物件偵測模型，自動判斷遊客是否越過虛擬安全界線，並觸發無人救生艇自主導航執行救援，同時同步通知救生員與相關單位，期望大幅縮短反應時間、降低人力負擔，並透過資料記錄支援事後分析與模型持續優化，建立主動式海灘安全防護架構。

## 方法
系統整體架構包含三大層級：感知層、決策控制層與執行層。感知層部署沿岸攝影機，即時串流影像輸入至 NVIDIA Jetson Nano 邊緣運算裝置，運行 YOLOv8 物件偵測模型持續掃描畫面中的人體目標；模型輸出為邊界框與類別信心度，系統據此計算目標質心位置，並與預先設定的虛擬「臨界線」進行幾何關係判斷，一旦偵測到遊客穿越該線即判定為潛在溺水事件。決策控制層位於岸端主控系統，接收偵測觸發訊號後，自動派遣配備自主導航模組的無人救生艇，並透過無線通訊下發目標座標與即時更新的遊客位置；救生艇內建避障演算法與路徑規劃機制，依據即時感測資料（如 GPS、IMU、超音波/雷達）動態調整航向，確保繞越障礙物並以最短安全路徑抵達目標。執行層包含救生艇的推進與操控系統，執行導航指令並回傳狀態。同步地，岸端系統透過通訊協定即時推送警報至救生員手持裝置與指揮中心，確保人力介入同步啟動。全程關鍵事件（偵測時間、觸發座標、艇隻軌跡、救援結果）自動寫入資料庫，供事後複盤與 YOLOv8 微調訓練使用。與傳統純人工巡邏或固定監控錄影相比，本系統關鍵差異在於：邊緣端即時推論與虛擬界線觸發機制、岸艇協同的閉迴路自主導航、以及資料驅動的持續學習迴路。

## 結果
摘錄未提供可驗證數字。依文本描述，系統預期具備即時偵測、自主派遣、避障導航與多方通報等功能，可在遊客越界瞬間啟動救援流程，縮短黃金救援時間；資料記錄機制可支援事後分析與模型迭代，形成正向循環。然而，缺乏實驗數據（如偵測準確率、誤報率、救援成功率、平均反應時間、環境干擾下的鲁棒性指標）與基線比較，無法量化評估實際效能。

## 限制與展望
依目前可取得資料，無法確認具體實驗驗證細節。潛在限制包括：YOLOv8 在強光、陰影、浪花遮蔽、遠距離小目標等複雜海灘場景下的偵測穩定性；Jetson Nano 算力對高解析度多攝影機串流即時推論的負載上限；無線通訊在海洋環境中的延遲、封包遺失與頻譜干擾風險；自主導航於大浪、強風、漂流物密集水域的避障與定位可靠度；虛擬臨界線設定的普適性與誤觸發風險；以及系統整合部署的維運成本、法規合規與隱私保護問題。後續研究建議進行實地場域測試、量化效能指標、探索輕量化模型與邊緣訓練策略、強化多感測器融合與通訊彈性，並建立標準化評估基準。
