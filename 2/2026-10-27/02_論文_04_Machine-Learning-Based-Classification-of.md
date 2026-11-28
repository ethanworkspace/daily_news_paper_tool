# 論文 04：Machine Learning-Based Classification of Kelvin Wakes and Plunging Waves from Simulated Sea Surface Data

- 日期：2026-10-27
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
本研究旨在解決海洋波浪現象中船舶產生的 Kelvin 航跡與自然傾倒破碎波的自動化區分問題，這對海上監視、海岸工程與環境監測至關重要。現有方法多針對單一波型，如利用 Radon/Hough 變換、CFAR 或 CNN 偵測船舶航跡，或以電磁散射模型分析破碎波，但缺乏能在同一框架下同時辨識兩者的機器學習方案。本文提出基於模擬海面數據的統一分類框架，填補此研究缺口。

## 方法
方法包含三大部分：(1) 波型模擬與數據生成：Kelvin 航跡依經典船舶波理論建模，船舶參數設定為長 137.202 m、半寬 8.31 m、吃水 8.732 m、航速 9 m/s，於 50×500 網格產生 400 筆純淨航跡並加入 ±10–30% 噪聲變異；傾倒波依實驗室先前的電磁散射框架，採用 CWMFSM 兩尺度模型（大尺度三角切面由蒙地卡羅生成，小尺度毛細波為正弦波產生布拉格散射），結合光線追蹤處理多路徑散射、物理光學計算被照切面散射場，最後以頻域後向散射場（方程式 7）輸出，取 t16 時刻（破碎階段最大曲率）並設 45% 混合機率產生 400 筆樣本。(2) 特徵工程：對所有樣本先加高斯噪聲（σ=0.20），再擷取 30 維統計、空間與頻域特徵，含平均值、標準差、百分位數、偏度、峰度、區域統計、梯度描述子與 FFT 係數，並進行正規化。(3) 分類器訓練與評估：採分層 75/25 切分訓練/測試集，分別訓練 SVM、XGBoost 與隨機森林，以準確率、精確率、召回率、F1 分數、ROC-AUC 及混淆矩陣評估。

## 結果
實驗結果顯示三種分類器在測試集上的準確率分別為 92.5%（SVM）、93%（XGBoost）與 94%（隨機森林），作者並指出對應的精確率、召回率、F1 分數與 ROC-AUC 均證實效能穩健；然而摘錄未提供這些指標的具體數值，僅能觀察到隨機森林表現最佳、三者差異較小的定性結論。

## 限制與展望
本研究僅使用合成模擬數據，未以真實 SAR 或光學影像驗證，且僅針對 Kelvin 航跡與傾倒波兩類，樣本數 800 筆相對較少；模擬假設如 Kelvin 航跡不含海面粗糙度、傾倒波固定 t16 時刻與 45% 混合機率、高斯噪聲 σ=0.20 等，可能無法涵蓋真實海況的多樣性；僅比較三種傳統機器學習模型，未探討深度學習或集成策略；後續研究建議引入實測數據、擴充波型類別、增加樣本量並評估模型在不同海況下的泛化能力。
