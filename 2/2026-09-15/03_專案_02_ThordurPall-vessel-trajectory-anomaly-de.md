# GitHub 專案 02：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-09-15
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
本專案針對歷史 AIS 軌跡資料，利用變異循環神經網路（VRNN）學習正常漁船行為的機率分布，進而以重建 likelihood 判斷異常軌跡，目標使用者為海事安全研究員、資料科學家與漁業管理單位，核心問題是在缺乏標註異常樣本的情況下，如何有效區分合法漁作與可疑事件。

## 技術
專案以 Jupyter Notebook 為開發環境，使用 Python 進行資料讀取、清理與特徵工程；採用變異循環神經網路（VRNN）建模軌跡序列，透過編碼器-解碼器結構產生潛在變數的高斯或混合高斯分布，以計算重建機率；異常偵測則採用地理相關的 a contrario 規則，根據位置依賴的分布調整門檻。程式碼部分參考 Kristoffer Vinther Olesen 的工具函式，負責 AIS 資料的格式轉換與基本統計。

## 架構
資料流程始於原始 AIS 訊息的讀取，經過時間對齊與軌跡切分，產生均勻取樣的經緯度序列；依照實驗需求，將序列轉換為離散的 one‑hot 分箱向量或保留連續的浮點數值作為模型輸入；接著，VRNN 編碼器逐時步更新隱藏狀態並產生潛在變數的分布參數，解碼器根據採樣的潛在變數重建下一個軌跡點，計算重建對數機率作為正常度分數；最後，利用 a contrario 規則將分數與特定海域的經驗分布比較，設定位置依賴的警報門檻，標記超過門檻的點為異常。整個流程在 Jupyter Notebook 中以實驗腳本形式呈現，便於參數調整與結果視覺化。

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
