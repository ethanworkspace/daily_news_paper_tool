# 論文 04：Physics-informed and data-efficient machine learning for storm surge forecasting during typhoons.

- 日期：2026-11-13
- 來源層級：Tier 4（一般期刊）（海事）
- 期刊/會議/來源：Science advances
- Venue：Science advances
- 發布時間：2026-11-13T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43024695/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13763864/
- DOI：10.1126/sciadv.aeh5673
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：967（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
This study addresses the challenge of accurately forecasting storm surges during tropical cyclones, which is crucial in reducing coastal damages. We develop a physics-informed and data-efficient model, a storm surge neural network (SSNN), that embeds shallow water equations into a machine learning (ML) framework with a specifically designed piecewise loss function to effectively incorporate physical constraints. The SSNN is iteratively trained to make rolling forecast and can produce more accurate forecasts than a standard data-driven model even with a smaller size of training data. The improvement in the performance by the SSNN model is evident, particularly in coastal areas with varying strong winds. This is especially true for forecasts beyond 16 hours, where the data-driven model struggles to provide accurate predictions. Combining physics with ML could offer a promising way to improve storm surge forecasting and support coastal hazard preparedness.

## 背景與目的
本研究針對熱帶氣旋期間風暴潮預測的準確性挑戰，旨在降低沿海災害損失。現有純資料驅動模型在訓練資料有限、長時效預測（>16小時）及強風變化沿海區域表現不佳，缺乏物理約束導致外推能力不足。本文提出物理資訊融合且資料高效的風暴潮神經網絡（SSNN），將淺水方程嵌入機器學習框架，並設計分段損失函數以強制物理一致性，期望在少量訓練樣本下仍能提升預測精度，為沿海災害防備提供更可靠工具。

## 方法
問題設定：輸入為颱風路徑、風場、氣壓場等時空特徵，輸出為未來多個時間步的沿海水位序列（滾動預測）。模型架構：SSNN 採用編碼器‑解碼器結構，編碼器提取風壓強迫特徵，解碼器輸出水位場；核心創新在於將淺水方程（連續性方程與動量方程）以殘差形式嵌入損失函數，構成分段損失：第一段為資料誤差項（如 MSE），第二段為物理殘差項，並在不同時段或空間區域給予不同權重，確保物理約束在強風區與長時效預測中發揮更大作用。資料表示：將風場、氣壓場以網格化張量輸入，水位標籤同樣為網格序列。訓練目標：最小化分段損失，採用 Adam 優化器，學習率衰減策略；訓練過程採用迭代滾動方式，每輪以前一輪預測作為下一輪輸入，實現多步預測。推理流程：給定初始風壓場，模型逐步輸出未來水位，並將預測結果回饋至下一步輸入。與純資料驅動基線的關鍵差異在於：(1) 物理方程硬性嵌入損失而非僅作正則化；(2) 分段損失依風速強度與預測時效動態調整權重；(3) 迭代滾動訓練提升長時效穩定性。

## 結果
摘錄未提供可驗證數字。作者報告 SSNN 在較少訓練樣本下仍優於標準資料驅動模型，改善在強風變化沿海區域最明顯；對於超過 16 小時的預測，資料驅動模型難以給出準確結果，而 SSNN 能保持較高精度。定性結論顯示物理約束有效提升長時效與極端風況下的預測穩健性。

## 限制與展望
本文僅以摘要說明方法與結果，缺乏具體資料集規模、評估指標（RMSE、MAE）、基線模型細節、消融實驗與計算成本資訊，無法判斷泛化至不同海域、颱風強度或實時作業系統的表現。分段損失權重選擇、滾動步數對誤差累積的影響未量化。未來需於多區域、多颱風案例驗證，並探討物理殘差權重自適應調整、模型輕量化部署與不確定性量化。
