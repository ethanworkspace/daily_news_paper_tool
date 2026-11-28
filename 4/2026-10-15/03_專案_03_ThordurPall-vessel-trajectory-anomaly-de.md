# GitHub 專案 03：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-10-15
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
此專案針對漁船 AIS 軌跡資料，利用變分循環神經網路（VRNN）學習軌跡分布，進而以重建似然判斷異常行為；結合地理相關的 a contrario 檢測規則，評估模型在丹麥漁船區域的表現、更大區域的泛化能力、不同輸入表示（離散 vs 連續）以及高斯分布與混合高斯分布對產生分布的影響。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作變分循環神經網路（VRNN），可能依賴 PyTorch 或 TensorFlow 框架進行序列建模與變分推論；資料處理階段利用 pandas、numpy 進行 AIS 清洗、時間切片與離散/連續特徵編裝；模型訓練與評估則透過 matplotlib 視覺化重建誤差與 a contrario 門檻；此外，參考 Kristoffer Vinther Olesen 的 util 函式庫提供軌跡投影、地理格點劃分等輔助功能。

## 架構
根據 README 可見的流程，首先將原始 AIS 軌跡進行清洗與時間對齊，依據經緯度將全球劃成地理格子；接著依照選擇的輸入表示（離散：一熱編碼後分箱 concatenated vector；或連續：經度、緯度、速度、航向等）產生序列張量；序列送入 VRNN，其中編碼 RNN 產生隱藏狀態，從中採樣潛在變數，解碼 RNN 重建輸入序列，訓練目標為重建負對數似然加上 KL 散度；訓練完成後，對每個地理格子計算重建似然分布，利用 a contrario 規則設定異常門檻；最終對新軌跡計算重建似然，低於門檻則標記為異常。由於 README 未提供詳細圖表或模型結構圖，上述架構推斷基於典型 VRNN 與論文描述。

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
