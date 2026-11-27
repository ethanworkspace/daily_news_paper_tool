# GitHub 專案 02：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-02
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
本專案利用變異循環神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，以區分正常捕魚活動與異常事件。目標包括在丹麥海域評估 VRNN 性能、測試其在較大區域的泛化能力、比較離散與連續輸入表示的影響，以及探討將 VRNN 的生成分布從高斯改為混合高斯模型（GMM）的效果。服務對象為海事監管、漁業管理及相關研究人員。

## 技術
專案以 Jupyter Notebook 為開發環境，使用 Python 實作變異循環神經網路（VRNN）。模型訓練與評估依賴常見的科學計算與深度學習套件（如 NumPy、Pandas、Matplotlib 以及 PyTorch 或 TensorFlow），處理 AIS 資料時會進行軌跡切割、時間序列編碼，並提供離散（one‑hot 分箱）與連續兩種輸入形式。此外，程式碼引用了 Kristoffer Vinther Olesen 提供的工具函式庫，以協助資料讀取與基本運算。

## 架構
架構上，資料流程首先從原始 AIS 檔案讀取經緯度、時間戳與船速等欄位，經過清洗與軌跡切割後，依據選擇的表示方式產生離散的 one‑hot 分箱向量或連續的歸一化數值序列。這些序列輸入 VRNN，網路由循環編碼器產生潛在變數的分布（高斯或 GMM），再由解碼器重建輸入序列；透過重建機率計算似然值，進而套用地理相關的 a contrario 規則判定異常分數。最後，評估腳本會統計重建誤差、ROC 曲線與精準率‑召回率，以驗證模型在不同設定下的表現。README 未提供詳細圖表，以上說明基於文中描述與常見 VRNN 結構進行合理推斷。

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
