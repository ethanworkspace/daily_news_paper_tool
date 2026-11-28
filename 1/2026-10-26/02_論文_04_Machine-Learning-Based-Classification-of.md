# 論文 04：Machine Learning-Based Classification of Kelvin Wakes and Plunging Waves from Simulated Sea Surface Data

- 日期：2026-10-26
- 來源層級：Tier 1（頂級期刊）（海事）
- 期刊/會議/來源：International Journal of Innovative Science and Research Technology (IJISRT)
- Venue：International Journal of Innovative Science and Research Technology (IJISRT)
- 發布時間：2026-10-16T00:00:00+00:00
- URL：https://doi.org/10.38124/ijisrt/26oct657
- PDF：https://www.ijisrt.com/assets/upload/files/IJISRT26OCT657.pdf
- DOI：10.38124/ijisrt/26oct657
- arXiv：
- 影響指標：2yr_mean_citedness=0.61, h_index=55, i10_index=262 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: International Journal of Innovative Science and Research Technology (IJISRT)
- 引用數：0
- 解析程度：fulltext / pdf
- 全文來源：https://www.ijisrt.com/assets/upload/files/IJISRT26OCT657.pdf
- 全文字數：39689（pages=10, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The accurate classification of ocean wave phenomena is essential for maritime surveillance, coastal engineering, and environmental monitoring applications. This study addresses the challenge of distinguishing between ship-generated Kelvin wakes and natural plunging breaking waves using machine learning techniques. A synthetic dataset consisting of 800 samples (400 per wave type) is generated under controlled simulation conditions.

## 背景與目的
本研究針對海洋波浪現象中船舶產生的 Kelvin 航跡與自然衝擊型破碎波的自動辨識問題。現有文獻多針對單一波浪類型進行偵測或電磁散射建模，缺乏能在同一框架下區分這兩類波浪的機器學習方法。由於真實遙感資料取得成本高且參數受限，作者採用數值模擬產生可控的合成資料集，旨在建立首個統一的機器學習分類流程，並系統評估多種分類器在模擬海面資料上的表現，以支援海上監視、海岸工程與環境監測等應用。

## 方法
問題設定為二元分類：輸入為模擬海面高度/後向散射場資料（50×500 格點），輸出為 Kelvin 航跡或衝擊型破碎波標籤。整體流程包含三階段：(1) 波浪建模與資料生成：Kelvin 航跡依經典船舶波理論（Lord Kelvin 1887）建模，船舶參數設定為長 137.202 m、半寬 8.31 m、吃水 8.732 m、航速 9 m/s，波高由橫向與發散波疊加並含黏性係數；衝擊型破碎波採用實驗室先前的電磁散射框架，結合 CWMFSM 兩尺度粗糙面模型、毛細波 Bragg 散射、光線追蹤多路徑散射與物理光學近似，計算頻域後向散射場。資料集共 800 筆（各 400 筆），Kelvin 航跡加入 ±10–30% 噪聲變異，衝擊波取自 t16 時刻資料集並以 45% 混合機率生成。(2) 前處理與特徵擷取：先施加高斯雜訊（σ=0.20），再提取 30 維統計、空間與頻域特徵，包含均值、標準差、百分位數、偏度、峰度、區域統計、梯度描述子與 FFT 係數，並進行正規化。(3) 分類器訓練與評估：採分層 75/25 切分訓練/測試集，分別訓練 SVM、XGBoost 與 Random Forest，以準確率、精確率、召回率、F1 分數、ROC-AUC 及混淆矩陣評估。關鍵差異在於首次將兩類波浪的物理模擬、統一特徵集與多種傳統機器學習分類器整合於單一框架中。

## 結果
實驗結果顯示三種分類器在測試集上分別達到 92.5%（SVM）、93%（XGBoost）與 94%（Random Forest）的分類準確率；作者並指出對應的精確率、召回率、F1 分數與 ROC-AUC 指標均證實模型具備穩健表現。摘錄未提供可驗證的精確率、召回率、F1 或 AUC 具體數值，僅能觀察到 Random Forest 表現最佳，三者皆超過 92% 準確率，顯示手工特徵結合傳統分類器在該合成資料上具備可行性。

## 限制與展望
研究限制包括：(1) 僅使用特定模擬條件（單一航速、固定格點、特定噪聲範圍）生成資料，缺乏真實 SAR/光學影像驗證，泛化能力未知；(2) 樣本數僅 800 筆，類別平衡但規模較小，易導致過擬合；(3) 僅評估三種傳統機器學習模型，未探討深度學習或端到端特徵學習；(4) 特徵為人工設計的統計/頻域描述子，可能遺漏關鍵物理紋理資訊；(5) 未考慮海況、風速、雷達頻帶等多變因子對分類的影響。後續研究建議引入實測資料、擴大資料集、嘗試卷積神經網路與多任務學習，並探討不同海況下的魯棒性。
