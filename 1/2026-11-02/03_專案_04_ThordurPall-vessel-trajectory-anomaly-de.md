# GitHub 專案 04：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-02
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
此專案利用變分遞迴神經網路（VRNN）對歷史 AIS 船舶軌跡進行建模，以區分正常捕魚活動與異常事件，目標使用者為海事安全研究者與漁業監控人員，核心問題是如何依據地理相關的機率模型有效偵測船舶軌跡異常。專案基於 arXiv:1912.00682 的方法，利用 VRNN 學習船舶軌跡的機率分布，並透過重建似然度判定異常；同時採用地理依賴的 a contrario 偵測規則來補償位置依賴的分布變化。主要服務於需要自動監測漁船行為、防範非法捕撈或海上事故的研究團隊與海事管理單位。

## 技術
專案以 Python 為主要程式語言，以 Jupyter Notebook 形式呈現實驗與分析流程。深度學習模型採用變分遞迴神經網路（VRNN），實作上可能使用 PyTorch 或 TensorFlow 框架（依據專案中引用的 util 檔案推斷）。資料處理方面使用 pandas、numpy 進行 AIS 資料清洗與軌跡切分，並視實驗需求採用離散（binning + one‑hot）或連續的輸入表示。模型訓練與評估則搭配 scikit‑learn、matplotlib 進行指標計算與結果視覺化。此外，專案探討了兩種生成分布：高斯分布與混合高斯分布（GMM），以及地理依賴的 a contrario 偵測規則。

## 架構
專案架構大致可分為四個主要模組：(1) 資料擷取與前處理：讀取歷史 AIS CSV，依船舶 ID 與時間切割軌跡段落，進行座標正規化，並依實驗選項產生離散的 bin‑one‑hot 向量或保留連續的經緯度序列。(2) VRNN 模型：由編碼器（RNN）將當前時間步的輸入映射至潛在變數的平均數與變異數（或 GMM 參數），解碼器則利用採樣的潛在變數重建輸入序列，訓練目標為重建負對數似然加上 KL 散度。（3) 訓練與驗證：在訓練集上最小化上述損失，驗證時計算每條軌跡的重建似然度作為異常分數。(4) 異常偵測：根據地理依賴的 a contrario 規則設定閾值，將低於閾值的軌跡標記為異常；實驗中會比較不同輸入表示（離散 vs 連續）與生成分布（高斯 vs GMM）對偵測效能的影響。由於 README 僅提供結構概述與目標說明，上述流程為基於文件所述模型與方法的合理推斷。

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
