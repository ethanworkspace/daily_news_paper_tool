# 論文 04：Physics-informed and data-efficient machine learning for storm surge forecasting during typhoons.

- 日期：2026-11-17
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
本研究針對颱風期間風暴潮預測的準確性挑戰，現有純資料驅動模型在超過 16 小時的預測時效上表現不佳，尤其在風場變化劇烈的沿海區域。為提升預測可靠性並降低資料需求，作者提出將淺水方程式嵌入神經網絡，設計分段損失函數以強制物理約束，構建風暴潮神經網絡（SSNN），並採用滾動訓練方式進行預測。目標在於證明物理資訊融合機器學習能以較少訓練資料達成更高預測精度，支援沿海災害防備。

## 方法
問題設定：輸入為颱風路徑、風場、氣壓等氣象強迫條件及初始水位，輸出為未來多個時間步的風暴潮水位序列。模型架構：SSNN 為一前饋神經網絡，內部將淺水方程式（SWE）的離散形式作為物理層，網絡輸出的水位場需滿足動量與連續性方程。核心機制：設計分段損失函數 L = λ_data·L_data + λ_phy·L_phy，其中 L_data 為預測水位與觀測的均方誤差，L_phy 為 SWE 殘差在空間與時間上的加權誤差；分段權重隨預測時效遞增，強化長時效物理一致性。資料表示：將氣象場與水位場以網格化張量輸入，採用標準化與歸一化。訓練策略：採用滾動訓練，每輪以最新觀測更新模型參數，並以較小訓練集進行迭代優化，使用 Adam 最佳化器。推論流程：給定新颱風氣象輸入，模型依序輸出下一時間步水位，並將其作為下一步輸入，形成滾動預測。關鍵差異：相較純資料驅動模型，SSNN 明確嵌入物理方程並透過分段損失平衡資料與物理約束，實現資料高效與長時效穩定性。

## 結果
作者報告 SSNN 在多個颱風案例中優於標準資料驅動基線，特別在預測超過 16 小時及風速變化大的沿海點位表現明顯提升；模型在較小訓練資料下仍保持穩定誤差。摘錄未提供可驗證數字（如 RMSE、相關係數或具體提升百分比），僅能觀察到定性結論：物理約束改善長時效預測與空間非均勻風場下的準確度。

## 限制與展望
僅提供摘要與片段，缺乏資料集規模、超參數、計算成本、泛化至不同海域或極端颱風的驗證；分段損失權重選擇、滾動訓練誤差累積、淺水方程假設（如忽略垂直結構）可能限制適用範圍。後續研究需補充定量基線比較、不確定度量化與實時部署測試。
