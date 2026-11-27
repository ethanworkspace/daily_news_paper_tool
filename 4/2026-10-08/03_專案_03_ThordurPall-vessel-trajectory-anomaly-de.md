# GitHub 專案 03：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-08
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
此專案利用深度學習中的變異循環神經網路（VRNN）對船舶自動識別系統（AIS）軌跡進行異常偵測，區分正規漁船活動與可疑事件（如非法捕魚、航行違規）。目標使用者為海事監管機構、漁業管理單位及研究人員，核心問題在於如何從歷史 AIS 資料中學習正常軌跡分布，並以機率重建 likelihood 與地理相關的 a contrario 規則判斷異常軌跡。

## 技術
專案以 Python 為主要開發語言，使用 Jupyter Notebook 進行實驗與可視化。核心模型為變異循環神經網路（VRNN），負責學習 AIS 軌跡的機率分布並計算重建 likelihood。資料處理方面，利用 pandas、numpy 讀取與清洗 AIS 資料，並探索離散（one‑hot binning）與連續兩種輸入表示方式。評估則透過 matplotlib 繪製結果圖表。README 未明確指出深度學習框架，僅說模型建構於 VRNN。

## 架構
根據 README，專案大致可分為四個階段：(1) 資料擷取與前處理，將原始 AIS 訊息轉換為時間序列特徵；(2) 建構 VRNN 模型，訓練階段學習軌跡的生成分布（Gaussian 或 GMM）；(3) 利用訓練好的模型計算每條軌跡的重建 likelihood，並結合地理依賴的 a contrario 偵測規則設定異常門檻；(4) 透過視覺化與定量指標（如 AUC、Precision‑Recall）評估模型在丹麥漁船及較大 ROI 上的表現。由於 README 未提供詳細圖表或模組名稱，以上架構推斷依據為文本描述與圖片說明，若需更細部的模組劃分則資訊不足。

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
