# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-06
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
此專案利用深度學習中的變分遞迴神經網路（VRNN）針對歷史 AIS 船舶軌跡進行異常偵測，區分合法漁船活動與異常事件。目標使用者包括海事監管機構、漁業管理單位及研究人員，他們需透過自動化方法識別可疑航行行為，以提升海上安全與資源管理效率。核心問題在於如何從時序性的 AIS 資料中學習正常軌跡分布，並依地理位置調整異常判斷門檻。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作深度學習模型。核心模型為變分遞迴神經網路（VRNN），負責學習 AIS 軌跡的機率分布並計算重建似然度。根據輸入表現方式，支援離散（one‑hot 分箱後的向量）與連續兩種 AIS 資料表示。在生成分布上可切換單一高斯或高斯混合模型（GMM）。異常偵測階段採用地理相關的 a contrario 規則，以補償學習分布的位置依賴性。此外，專案引用了 Kristoffer Vinther Olesen 的工具函式庫進行資料預處理與軌跡處理。

## 架構
根據 README 的說明，專案大致可分為四個主要流程：首先是資料準備階段，載入歷史 AIS 軌跡並依據選擇的表現方式（離散或連續）進行編碼；其次是 VRNN 模型訓練階段，網路學習軌跡序列的條件機率分布，並根據選擇的高斯或 GMM 生成分布輸出重建機率；第三階段是似然度計算與異常分數產生，利用 VRNN 的重建似然度作為正常度指標；最後是地理依賴的 a contrario 偵測規則，根據船隻所在位置的統計特性動態設定異常閾值，從而產生最終的異常判斷。由於 README 未提供具體的程式碼目錄結構或模組劃分說明，以上架構描述僅基於文件中所述的方法步驟進行推斷。

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
