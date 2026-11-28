# GitHub 專案 03：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-20
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
此專案利用變體遞迴神經網路（VRNN）對歷史 AIS 軌跡進行建模，學習正常漁船行為的分布，進而以重建機率與地理相關的 a contrario 規則辨識異常航跡，目標是協助海上監控與漁業管理偵測可疑或非法活動。

## 技術
專案以 Jupyter Notebook 為開發環境，使用 Python 實作 VRNN 模型；輸入為 AIS 軌跡點，可選擇離散（one‑hot 分箱）或連續表示；VRNN 的產生分布可切換為單一高斯或混合高斯（GMM）；利用重建似然計算異常分數，並採用地理依賴的 a contrario 門檻進行決策；程式碼參考 Kristoffer Vinther Olesen 的 util 函式庫。

## 架構
架構包含：1) 數據載入與預處理（AIS 清理、時間軸對齊、離散/連續編碼）；2) VRNN 模型（編碼器循環網路產生潛在均值與變異數、解碼器重建軌跡）；3) 條件損失函數（負對數似然＋KL 散度）；4) 異常評估（重建機率低於地理相關的 a contrario 門檻標記為異常）；5) 實驗腳本（針對丹麥漁船、較大 ROI、不同輸入表示、分布類型進行消融）。README 未提供詳細模組圖，上述流程根據所述目標與方法推斷。

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
