# 論文 04：Integrating Artificial Intelligence With PPE: A Smart Boiler Suit Framework for Maritime Survey Applications

- 日期：2026-11-21
- 來源層級：Tier 1（頂級期刊）（海事）
- 期刊/會議/來源：Safety Science and Technology
- Venue：Safety Science and Technology
- 發布時間：2026-10-30T00:00:00+00:00
- URL：https://doi.org/10.1002/sst3.70059
- PDF：https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/sst3.70059
- DOI：10.1002/sst3.70059
- arXiv：
- 影響指標：2yr_mean_citedness=0.00, h_index=3, i10_index=0 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Safety Science and Technology
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1075（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Marine surveyors are routinely exposed to complex hazards, chemical, ergonomic, and physical, within dynamic environments such as ships and offshore platforms. Existing personal protective equipment (PPE) provides only basic safeguards and remains largely reactive. This paper proposes the design and conceptual architecture of an AI‐enhanced smart PPE boiler suit specifically optimized for marine and offshore class surveyors. The proposed system is envisioned to leverage embedded sensor networks, edge/cloud artificial intelligence analytics, and real‐time communications for continuous hazard detection, predictive risk mitigation, and streamlined survey workflows. We detail a proposed system architecture, outline pathways for functional prototyping, and critically examine anticipated challenges, establishing a robust roadmap for future multidisciplinary research and industry adoption. No physical prototype has been constructed at this stage; all scenarios and performance figures presented herein are theoretical and intended to guide future empirical validation.

## 背景與目的
海事檢測人員在船舶與離岸平台等動態環境中，長期面臨化學、人因工學與物理等複合危害。現有個人防護裝備（PPE）僅提供基礎防護，屬於被動反應模式，缺乏即時感測與預測能力，難以在作業過程中主動降低風險。本文旨在提出一套結合人工智慧的智慧型鍋爐服（boiler suit）概念架構，專為海事與離岸級檢測人員設計，期望透過嵌入式感測網路、邊緣/雲端 AI 分析與即時通訊，實現持續危害偵測、預測性風險緩解與檢測流程優化，為後續多領域研究與產業落地建立路線圖。

## 方法
本文提出的智慧型鍋爐服系統架構包含四大層級：(1) 感測層：於服裝內部與外部佈建多模態感測器網路，涵蓋氣體濃度、溫濕度、揮發性有機物等環境感測器，以及心率、體溫、姿態、加速度等生理與動作感測器，採用低功耗無線協定（如 BLE、Thread）將原始訊號傳輸至邊緣節點。 (2) 邊緣計算層：內嵌微控制器或單晶片執行資料前處理、雜訊濾波、特徵擷取與輕量級異常偵測（如門檻判斷、簡單分類器），並負責本地即時警報與關鍵事件標記，以降低頻寬需求。 (3) 雲端 AI 層：邊緣節點透過 5G/衛星/船載 Wi-Fi 將關鍵特徵上傳至雲端，雲端部署深度學習模型（如時序 CNN、Transformer）進行多源資料融合、危害模式辨識與風險預測，並支援模型線上更新與聯邦學習以保護隱私。 (4) 應用與決策層：提供行動裝置或頭戴式顯示器介面，呈現即時危害等級、預測風險熱區、作業建議與自動記錄報表，並與既有檢測管理系統整合以優化工作流程。全系統採模組化設計，支援功能原型逐步驗證，並規劃電源管理、資料安全與法規遵循等跨領域考量。

## 結果
本文為概念性設計研究，摘錄未提供可驗證數字。研究提出 AI 強化智慧鍋爐服架構，包含嵌入式感測網路、邊緣/雲端 AI 分析與即時通訊三大核心模組。定性結論顯示，相較現有僅提供基礎防護且屬被動反應的傳統 PPE，本架構可實現連續危害偵測、預測性風險緩解與檢驗流程優化，將防護模式轉向主動預警。消融觀察方面，論文批判性檢視電源續航、環境耐久度、海上通訊可靠性、多模態資料融合延遲及法規認證等五大落地挑戰，並規劃原型開發、實驗驗證與跨域合作路徑，為後續實證研究奠定基礎。

## 限制與展望
主要限制在於：(1) 尚無實體原型，所有架構細節、感測器選型、通訊協定、AI 模型結構與訓練策略均屬概念設計，缺乏實測數據支撐。(2) 電源續航、抗震動、防水防腐蝕等海事環境適應性未經驗證。(3) 資料隱私、網路安全、法規認證（如 SOLAS、IACS）與多廠商互操作性尚未具體規劃。(4) 評估指標僅停留於理論預期，缺乏基線比較與消融實驗。後續研究需著重於原型製作、現場試驗、模型輕量化與標準化流程建立。
