# 論文 05：Multi-Spectrum Human Detection And Autonomous Maritime Rescue System

- 日期：2026-11-01
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
本研究針對海灘遊客因潮汐與離岸流導致溺水風險高、傳統人力巡救反應速度有限之問題，現有監控系統多缺乏即時自動偵測與主動派遣救援載具之整合機制。本文提出一套結合 AI 物件偵測、邊緣運算與自主導航機器人之海灘安全系統，旨在建立即時威脅偵測、自動觸發救援艇派遣、多方通報與資料回溯之完整閉環，以降低人力負擔並縮短黃金救援時間，貢獻在於將 YOLOv8 部署於 Jetson Nano 邊緣裝置，搭配虛擬門檻線判斷與自主救援艇協同運作，形成端到端之主動防護架構。

## 方法
問題設定與輸入輸出：系統以海灘沿岸攝影機即時影像串流為輸入，輸出為落水者偵測框、是否跨越虛擬門檻線之觸發訊號、自主救援艇導航指令與緊急通報資訊。整體架構：包含邊緣偵測節點、岸端控制中介、自主救援艇三大子系統。核心模組與演算法機制：邊緣節點採用 YOLOv8 物件偵測模型於 Jetson Nano 執行推論，持續掃描影像並輸出遊客邊界框；設定虛擬「門檻線」作為危險區域邊界，當偵測到遊客邊界框與門檻線相交或跨越時，即判定為潛在落水事件。資料前處理與表示：影像串流經解碼、調整大小後餵入 YOLOv8，模型輸出類別信心度與邊界框座標，門檻線以像素座標多邊形表示。訓練目標與損失：摘錄未提及模型訓練細節、損失函數或最佳化策略，僅說明使用預訓練之 YOLOv8。推論與執行流程：偵測觸發後，岸端系統自動派遣配備先進導航能力之自主救援艇，救援艇接收即時位置更新並規劃避障路徑前往目標；同步發送通知予救生員與相關機關。關鍵差異：相較傳統被動監控或純人力巡救，本系統整合邊緣 AI 即時偵測、虛擬邊界觸發邏輯與自主機器人實體救援，形成感知-決策-行動閉環。

## 結果
摘錄未提供可驗證數字。文中僅定性描述系統能持續掃描即時影像、於遊客跨越門檻線時自動派遣救援艇、具備避障導航與多方通報功能，並預期透過資料記錄支援事後分析與模型持續優化，但無實驗數據、比較基線、消融研究或具體效能指標（如偵測準確率、響應時間、救援成功率等）可供驗證。

## 限制與展望
資料與評估限制：摘錄未揭露訓練/測試資料集來源、規模、環境條件（光照、天氣、遮蔽）及評估指標，無法判斷偵測魯棒性。方法限制：YOLOv8 於 Jetson Nano 推論速度、功耗與熱穩定性未量化；虛擬門檻線設定靜態，可能不適應潮汐變化；自主救援艇導航演算法、避障機制、通訊延遲與可靠度缺乏技術細節。部署風險：邊緣裝置長期戶外運維、無線通訊干擾、法規合規與誤觸發責任歸屬未討論。後續研究建議：補充實地實驗數據、動態門檻線自適應、多感測器融合、系統級效能基準測試與安全性驗證。
