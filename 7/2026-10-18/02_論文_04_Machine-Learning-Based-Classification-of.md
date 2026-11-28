# 論文 04：Machine Learning-Based Classification of Kelvin Wakes and Plunging Waves from Simulated Sea Surface Data

- 日期：2026-10-18
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
海洋波浪現象的精確分類對海上監視、海岸工程與環境監測至關重要。現有研究多針對單一波浪類型（如 Kelvin 船尾波或衝破波）進行偵測，缺乏在同一框架下自動區分兩者的方法；傳統線性特徵提取（如 Radon、Hough 變換）難以同時捕捉兩類波浪的紋理與頻域差異。真實遙感資料取得成本高且參數受限，難以進行受控實驗。本文旨在建立首個基於模擬海面資料的機器學習統一分類框架，利用合成資料集與多維特徵，比較 SVM、XGBoost、Random Forest 三種分類器，實現 Kelvin 船尾波與衝破波的自動辨識，並系統評估其在分層抽樣下的分類性能，驗證模擬資料與特徵工程結合的有效性，為海上偵察與海岸監測提供可行技術路徑。

## 方法
問題設定為二元分類：輸入為模擬海面資料（50×500 網格），輸出為 Kelvin 船尾波或衝破波類別。整體流程包含三階段：(1) 波浪建模與模擬：Kelvin 波依經典船波理論（Lord Kelvin 1887），以點擾動產生橫向與發散波，尖角 16°–19.5°，船舶參數長 137.202 m、半寬 8.31 m、吃水 8.732 m、航速 9 m/s，生成無海面粗糙度的純淨波型；衝破波採用電磁散射框架，先用 CWMFSM 以蒙地卡羅法產生大尺度切面，小尺度毛細波以正弦波描述並產生 Bragg 散射，再以光線追蹤處理多路徑散射，物理光學計算被照亮切面散射場，最後在頻域計算後向散射場。(2) 資料生成與預處理：各類別各 400 筆，Kelvin 波加入 ±10–30% 噪聲變異，衝破波取自 t16 時刻資料集並以 45% 混合機率產生；全體樣本再疊加高斯噪聲 σ=0.20。(3) 特徵工程與分類：提取 30 維統計（均值、標準差、百分位數、偏度、峰度）、空間（區域統計、梯度描述子）與頻域（FFT 係數）特徵，經正規化後以分層 75/25 切分訓練/測試集，分別訓練 SVM、XGBoost、Random Forest 三種監督式分類器，評估指標含準確率、精確率、召回率、F1、ROC-AUC 及混淆矩陣。推論時對新樣本同樣預處理、抽取特徵並餵入已訓練模型輸出類別。關鍵差異在於首創統一機器學習框架，結合物理基模擬與手工多域特徵，區別於既有單一波浪偵測或深度學習方法。

## 結果
實驗報告三分類器在測試集上的準確率分別為 SVM 92.5%、XGBoost 93%、Random Forest 94%，並指出精確率、召回率、F1 分數與 ROC-AUC 等指標均顯示穩健表現（摘錄未提供可驗證數字）。定性結論顯示：基於模擬資料與 30 維手工特徵的傳統機器學習方法已能有效區分 Kelvin 船尾波與衝破波，驗證了自動化波浪類型辨識在海上監視與海岸監測應用的可行性。

## 限制與展望
資料層面僅涵蓋單一航速（9 m/s）、固定網格與特定噪聲設定的合成樣本，缺乏真實 SAR 影像驗證，泛化能力未知；方法層面僅比較三種傳統分類器，未探討深度學習或端到端特徵學習；特徵為人工設計，可能遺漏高階紋理資訊；樣本總數 800 筆較小，易產生過擬合風險；評估僅採單一分層切分，未進行交叉驗證或不同海況下的鲁棒性測試。後續研究建議擴充真實多源遙感資料、增加波浪類別、引入深度網絡並進行大規模跨場景實驗。
