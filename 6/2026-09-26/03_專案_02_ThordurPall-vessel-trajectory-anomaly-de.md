# GitHub 專案 02：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-09-26
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
本專案利用深度學習方法構建基於軌跡的變分遞迴神經網路（VRNN），以歷史 AIS 資料區分合法漁船活動與異常事件，目標使用者為海事監控研究者、漁業管理單位及海上安全分析師，核心問題在於提升異常偵測的準確性與泛化能力。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作 VRNN 模型，基於 TensorFlow/Keras（或 PyTorch）構建編碼器‑解碼器結構，潛在變數採用高斯分布或混合高斯分布（GMM），輸入採用連續經緯度或離散的一熱編碼分箱向量，透過自訂 util 檔案處理 AIS 資料清洗、軌跡切割與特徵工程，最後以重建似然計算異常分數。

## 架構
資料流程始於原始 AIS 資料的讀取與清洗，接著依據經緯度進行時間序列切割，產生連續或離散（一熱分箱）的輸入序列；這些序列饋入 VRNN 編碼器，產生時間步潛在變數的分布參數，解碼器則重建輸入序列並計算重建似然；根據地理位置依樣的 a contrario 規則設定閾值，將低似然的序列標記為異常；最後透過視覺化與評估指標（如 AUC、Precision‑Recall）驗證模型在丹麥漁船及更大 ROI 的表現。

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
