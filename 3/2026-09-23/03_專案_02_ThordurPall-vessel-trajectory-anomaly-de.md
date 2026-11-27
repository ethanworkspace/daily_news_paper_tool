# GitHub 專案 02：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-09-23
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
本專案利用深度學習中的變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，以區分正常捕魚活動與異常事件，目標使用者為海事監管機構、研究人員及漁業安全分析師，核心問題是自動識別可疑或違規船舶軌跡。

## 技術
專案以 Jupyter Notebook 為開發環境，主要使用 Python 與深度學習框架（如 TensorFlow/Keras 或 PyTorch）實作變分遞迴神經網路，處理 AIS 資料時提供連續與離散（一熱編碼後分箱）兩種輸入表示，並實驗將 VRNN 的生成分佈從高斯切換為高斯混合模型（GMM），同時引入地理相關的 a contrario 規則進行異常分數計算。

## 架構
資料流程始於原始 AIS 日誌的讀取與清洗，接著依據經緯度、時間戳與速度等特徵產生連續軌跡序列或離散的一熱向量序列；這些序列喂入 VRNN，網路由編碼器捕捉時序依賴、潛在變數學習高斯（或 GMM）分佈，解碼器重建輸入以計算重建機率；根據重建機率與地理位置相關的 a contrario 規則得到異常分數，最後設定閾值標記異常船舶軌跡。若需更詳細的模組劃分，README 未提供完整圖表，僅能根據上述描述推斷。

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
