# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-29
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
本專案利用變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，學習代表正常漁船活動的機率分布，以重建 likelihood 判斷異常軌跡。目標使用者為海事監管單位、漁業管理機構及從事船舶安全研究的研究者，核心問題是在大規模海域中自動區分合法漁撈行為與可能的非法、事故或異常事件，提供基於深度學習的異常偵測工具。

## 技術
專案以 Python 撰寫，主要在 Jupyter Notebook 中進行實驗；深度學習框架採用 TensorFlow/Keras（或 PyTorch，依據 util 檔案推斷）實作變分遞迴神經網路，包括編碼器、解碼器與潛在變數的高斯或混合高斯分布（GMM）；輸入為 AIS 訊號，經過時間序列切割後可選擇連續數值或離散 one‑hot 分箱向量；資料流程包含資料清理、特徵編碼、模型訓練（重建損失 + KL 散度）、異常分數計算以及地理相依的 a contrario 偵測規則。

## 架構
架構分為四個主要模組：(1) 資料前處理模組負責讀取 AIS 軌跡、時間對齊、速率與航向計算，並依照設定產出連續特徵或離散 one‑hot 分箱向量；(2) VRNN 模組包含遞迴編碼器將時間步輸入映射至潛在分布（高斯或 GMM），解碼器重建下一時間步的軌跡，訓練目標為最大化重建 likelihood 並最小化 KL 散度；(3) 評分模組根據重建 likelihood 計算異常分數，並套用地理相依的 a contrario 門檻值來判定是否為異常；(4) 實驗與視覺化模組負責模型效能評估（AUC、PR 曲線）、不同輸入表示與分布假設的消融實驗，結果以 Jupyter Notebook 形式呈現。若 README 未明確說明某些細節，以上描述以典型 VRNN 結構與論文方法為推斷依據。

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
