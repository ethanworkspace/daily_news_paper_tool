# GitHub 專案 03：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-14
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
本專案利用深度學習中的變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，學習代表正常漁船活動的機率分布，進而以重建似然度判斷異常軌跡。目標使用者為海事監管機構、漁業管理單位及研究人員，核心問題是如何在大規模 AIS 資料中自動辨識非法捕撈、轉移或其他異常船舶行為，減少人工審查成本並提升偵測及時性。

## 技術
技術實作以 Python 為主語言，透過 Jupyter Notebook 進行互動式開發與實驗。模型核心採用變分遞迴神經網路（VRNN），實作框架可能為 PyTorch 或 TensorFlow，輔以 NumPy、Pandas 處理 AIS 資料，Matplotlib/Seaborn 視覺化軌跡與重建誤差。資料流程包括原始 AIS 清洗、時間序列切分、離散或連續特徵編碼，送入 VRNN 進行編碼‑採樣‑解碼，最後以重建對數似然計算異常分數。

## 架構
架構分為四個主要模組：(1) 資料前處理模組，負責讀取原始 AIS 訊息，剔除錯誤點，依船舶 ID 與時間戳切分軌跡，並依需求產生離散（one‑hot binning）或連續（正規化經緯度、速率、航向）特徵序列；(2) VRNN 建模模組，包含編碼 RNN（捕捉過去觀測）、潛在變數採樣（從高斯或 GMM 分布）、解碼 RNN（重建未來觀測），訓練目標為重建負對數似然加上 KL 散度；(3) 異常評分模組，對每條軌跡計算重建對數似然，並依據地理位置的 a contrario 規則設定動態門檻，將低於門檻的軌跡標記為異常；(4) 評估與視覺化模組，使用 AUC、Precision‑Recall、F1 等指標驗證模型在丹麥漁船資料與更大 ROI 的泛化能力，並繪製重建誤差分布與異常軌跡圖表。由於 README 未提供具體程式碼細節，上述流程乃基於論文描述與典型 VRNN 實作的合理推斷。

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
