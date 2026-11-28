# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-21
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
本專案利用變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，學習正常漁船活動的分布，進而以重建似然與地理相關的 a contrario 規則偵測異常航跡，目標使用者為海事研究員、資料科學家與漁業監管單位，核心問題是區分合法漁撈與異常事件。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作 VRNN 模型，透過自訂的 util 模組處理 AIS 資料（包括經緯度、速度、航向等特徵），支援連續與離散（one‑hot binning）兩種輸入表示，模型訓練採用最大似然或變分下界，並在推論階段計算重建機率；異常判斷則結合地理依賴的 a contrario 規則設定動態閾值。

## 架構
資料流程始於原始 AIS 檔案，經 util 模組清洗、切割軌跡段並產生特徵張量（連續或離散一熱向量），送入 VRNN 編碼器產生潛在分布（高斯或 GMM），解碼器重建軌跡並計算對數似然作為正常度分數；接著依據船隻所在經緯度格子，應用地理相關的 a contrario 規則將分數轉換為異常 p‑值，最後根據設定的顯著水準旗標異常段落。整個流程可在 Notebook 中以 célula 形式逐步執行，方便實驗不同輸入表示與分布假設。

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
