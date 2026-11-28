# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-18
- URL：https://github.com/ThordurPall/vessel-trajectory-anomaly-detection
- 描述：Vessel Trajectory Anomaly Detection Using Deep Learning Methods
- Stars：10  |  Forks：4  |  Language：Jupyter Notebook
- License：
- Topics：
- 更新時間：2026-06-29T07:54:22+00:00
- 論文層級：未對應論文（海事）
- 配對論文：https://arxiv.org/abs/1912.00682
- 品質分數：7/10 [paper_paired, stale_backfill]

## 在做什麼
本專案利用深度學習中的變分遞迴神經網路（VRNN）模型，針對歷史自動識別系統（AIS）船舶軌跡進行異常偵測，以區分合法漁業活動與可疑事件（如非法捕魚、船舶違規）。目標使用者包括海事監管機構、漁業管理單位及研究人員，他們需要依據船舶軌跡判斷是否存在異常行為。核心問題在於如何從時序性的 AIS 資料中學習正常行為的機率分布，並利用重建似然與地理相關的 a contrario 規則判定異常，同時探討不同輸入表示（連續 vs 離散一熱編碼）與生成分布（高斯 vs 混合高斯）對偵測效能的影響。

## 技術
專案以 Python 為主要程式語言，透過 Jupyter Notebook 進行實驗與視覺化。使用深度學習框架建構變分遞迴神經網路（VRNN），包含編碼器、潛在變數分布與解碼器，以學習 AIS 軌跡的時序分布。資料處理階段利用 pandas、numpy 讀取與清理 AIS 訊號，並依照需求製作連續輸入或離散一熱編碼的特徵向量。模型訓練採用最大似然或變分下界優化，異常偵測則根據重建似然計算似然分數，並結合地理依賴的 a contrario 規則設定動態閾值。評估過程中繪製 ROC 曲線、精準率-召回率圖，並利用 matplotlib 進行結果呈現。

## 架構
架構方面，專案可划分為四個主要模組：(1) 資料前處理模組，負責讀取原始 AIS 檔案、過濾無效訊號、進行時間對齊與空間投影，並產生連續或離散（一熱編碼）的時序特徵；(2) VRNN 模型核心，包含循環編碼器將時序輸入映射至潛在變數的平均數與變異數（或混合高斯參數），再經由解碼器重建輸入序列，訓練目標為最大化變分下界；(3) 偵測與評分模組，利用訓練好的 VRNN 計算每個軌跡片段的重建對數似然作為異常分數，並根據該海域的歷史似然分布套用地理依賴的 a contrario 規則決定是否為異常；(4) 實驗與結果模組，透過 Jupyter Notebook 進行不同輸入表示與生成分布（高斯 vs GMM）的對比實驗，繪製學習曲線、ROC 與 Precision-Recall 圖，並輸出定量評估指標。若 README 未提供完整目錄結構，以上說明乃基於典型深度學習專案組織與文件中提及的 util 檔案與 notebook 推斷。

## README 摘錄（節選）
```text
# Vessel Trajectory Anomaly Detection
This is a Git repository accompanying the "Vessel Trajectory Anomaly Detection Using Deep Learning Methods" master project. Based on work done in https://arxiv.org/abs/1912.00682, this project constructs trajectory-based models to discriminate between legitimate fishing vessel activities and anomalous events using historical AIS data. The proposed approach uses a variational recurrent neural network (VRNN) that learns a distribution representing the data that can state the reconstruction likelihood of AIS trajectories. Then for anomaly detection, a geographically-dependent a contrario detection rule is used to account for the fact that the learnt distribution may be location-dependent. The project objectives are to
- Analyse the VRNN-based model performance for fishing vessels around Denmark.
- Evaluate the generalisation of the VRNN-based model to a larger ROI.
- Examine the impact of different input AIS data representations (discrete vs. continuous inputs).
- Assess the impact of switching from a Gaussian to a GMM for the generating distribution of the VRNN.
The following image gives the intuition about the difference between the continuous inputs and the discrete binned concatenated vector of the one-hot vectors:
Please note that some code in this project builds upon excellent work done by Kristoffer Vinther Olesen (in particular the util files). The overall directory structure is as follows:
[code block omitted]
```
