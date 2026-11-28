# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-11
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
本專案實作基於變分遞迴神經網路（VRNN）的船舶軌跡異常偵測系統，利用歷史 AIS 資料區分合法漁船活動與異常事件，目標使用者為海事監管單位、研究人員與資料科學家，核心問題在於如何建立能捕捉時空依賴性的生成模型，並以地理相關的 a contrario 規則判定軌跡似然低於閾值的異常行為。

## 技術
專案以 Python 撰寫，主要以 Jupyter Notebook 進行實驗與視覺化；深度學習框架推論為 PyTorch（或 TensorFlow，依據 util 檔案），實作變分遞迴神經網路（VRNN）模型，包含編碼器、先驗與後驗網路以及解碼器；資料處理使用 pandas、numpy 進行 AIS 資料清理、離散/連續特徵編組；評估與視覺化則依賴 matplotlib、seaborn；專案亦引用 Kristoffer Vinther Olesen 提供的工具函式庫進行軌跡投影與基礎運算。

## 架構
資料流程始於原始 AIS 檔案的讀取，經過清理與過濾後，依照設定選擇離散（one‑hot 分箱）或連續表示方式產生輸入序列；接著將序列饋入 VRNN，模型在每個時間步學習後驗分布並重建輸入，透過 ELBO 條件最大化進行訓練；訓練完成後，對新軌跡計算重建似然值，並根據各地理格子的經驗分布應用 a contrario 偵測規則，將低於門檻的軌跡標記為異常；架構圖示中可見資料前處理 → VRNN 編碼‑解碼 → 似然計算 → 地理依賴規則 → 警報輸出。README 未提供具體超參數或硬體需求，因此上述架構推論僅基於說明與程式碼目錄結構。

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
