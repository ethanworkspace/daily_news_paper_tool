# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-16
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
此專案針對漁船的自動識別系統（AIS）軌跡資料，利用深度學習中的變異循環神經網路（VRNN）建立軌跡的機率分布，進而透過重建 likelihood 與地理相關的 a contrario 偵測規則來辨識正常漁撈行為與異常事件。目標使用者為海事監控研究者、漁業管理單位及從事異常偵測演算法的開發者，核心問題在於如何有效區分合法漁船活動與潛在的非法或異常航行行為。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作變異循環神經網路（VRNN）來模擬 AIS 軌跡的分布。根據 README，程式碼引用了 Kristoffer Vinther Olesen 提供的 util 函式庫，並採用深度學習框架（如 PyTorch 或 TensorFlow）進行模型訓練與推論。資料處理方面，涉及 AIS 資料的清洗、離散/連續表示方式的轉換以及地理依存的偵測規則實作。

## 架構
專案架構大致可分為四個主要部分：(1) 資料前處理模組，負責讀取原始 AIS 資料、進行軌跡切割、離散或連續特徵編製；(2) VRNN 模型定義與訓練模組，實作變異循環神經網路，學習軌跡的機率分布並計算重建 likelihood；(3) 偵測規則模組，基於所學分布應用地理相關的 a contrario 規則來設定異常閾值；(4) 評估與實驗模組，透過 Jupyter Notebook 進行模型在丹麥漁船上的效能分析、更大區域的泛化測試、不同輸入表示方式的影響評估以及從高斯分布改為 GMM 生成分布的實驗。由於 README 未提供詳細的目錄結構或模組間的具體介面，以上說明乃基於典型深度學習專案組織與文件中提及的內容所作的合理推論。

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
