# GitHub 專案 02：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-09-14
- URL：https://github.com/ThordurPall/vessel-trajectory-anomaly-detection
- 描述：Vessel Trajectory Anomaly Detection Using Deep Learning Methods
- Stars：10  |  Forks：4  |  Language：Jupyter Notebook
- License：
- Topics：
- 更新時間：2026-06-29T07:54:22+00:00
- 論文層級：未對應論文（海事）
- 配對論文：https://arxiv.org/abs/1912.00682
- 品質分數：7/10 [paper_paired, stale_seed]

## 在做什麼
此專案旨在利用深度學習偵測漁船軌跡異常，針對丹麥海域的歷史 AIS 資料建立基於變分遞迴神經網路（VRNN）的模型，學習軌跡分布並以重建機率判斷異常；並引入地理相關的 a contrario 檢測規則以處理位置依賴性。目標使用者為海事監管、漁業管理與學術研究人員，核心問題在於如何從高維時序 AIS 序列中自動識別非法或異常捕撈行為。

## 技術
專案以 Python 為主，於 Jupyter Notebook 開發，採用 PyTorch 實作 VRNN（含編碼器、解碼器、先驗/後驗分布），支援高斯與高斯混合模型（GMM）兩種生成分布，並比較離散 one-hot 編碼與連續座標兩種輸入表示。資料處理使用 pandas、numpy 進行 AIS 解析、時間對齊與網格化；視覺化與評估則仰賴 matplotlib、seaborn 等套件。

## 架構
架構可分為四大模組：(1) 資料前處理模組 — 讀取原始 AIS CSV，清洗、插值、依經緯度網格離散化或保留連續座標，產生固定長度序列；(2) VRNN 模型模組 — 含遞迴編碼器、潛在變數採樣（高斯或 GMM）、解碼器重建軌跡，訓練目標為 ELBO 最小化；(3) 異常評分模組 — 計算各時間步重建似然，結合地理相關的 a contrario 門檻產生異常分數；(4) 實驗與評估腳本 — 跨不同 ROI、輸入表示與分布假設進行訓練/驗證，輸出 ROC、PR 曲線等指標。README 未詳細列出推論部署流程，故推斷部署細節不足。

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
