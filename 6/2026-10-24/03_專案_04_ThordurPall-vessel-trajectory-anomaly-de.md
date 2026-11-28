# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-24
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
本專案利用變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，學習正常漁船行為的機率分布，透過重建 likelihood 與地理相依的 a contrario 偵測規則，識別異常船舶軌跡（如非法漁業或安全事件），目標使用者為海事監管機構、漁業管理單位及從事異常偵測研究的資料科學家。

## 技術
實作以 Python 撰寫的 Jupyter Notebook 為主，使用深度學習框架（如 TensorFlow/Keras 或 PyTorch）構建 VRNN 模型。輸入資料採用 AIS 軌跡的離散箱化 one-hot 向量或連續數值兩種表示方式，模型的生成分布可切換為高斯或混合高斯（GMM），並搭配地理相依的 a contrario 偵測規則進行異常分數計算。

## 架構
資料流程始於原始 AIS 資料的讀取與清理，接著依據選擇的表示方式（離散或連續）產生對應的時間序列特徵。這些特徵送入 VRNN，網路由編碼器捕捉時序依賴、潛在變數學習高斯或 GMM 分布，解碼器重建軌跡並計算重建 likelihood。然後依據船舶所在經緯度套用地理相依的 a contrario 規則，將低 likelihood 轉換為異常分數，最後透過視覺化與評估腳本驗證模型在丹麥漁船及更大區域的泛化能力與不同輸入表示、分布選擇的影響。

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
