# GitHub 專案 03：ThordurPall/vessel-trajectory-anomaly-detection

- 日期：2026-11-21
- URL：https://github.com/ThordurPall/vessel-trajectory-anomaly-detection
- 描述：Vessel Trajectory Anomaly Detection Using Deep Learning Methods
- Stars：10  |  Forks：4  |  Language：Jupyter Notebook
- License：
- Topics：
- 更新時間：2026-06-29T07:54:22+00:00
- 配對論文：https://arxiv.org/abs/1912.00682
- 品質分數：7/10 [paper_paired, stale_seed]

## 在做什麼
此專案利用深度學習方法構建變分遞迴神經網路（VRNN）模型，以歷史 AIS 軌跡資料辨識合法漁船活動與異常事件（如非法捕魚），目標使用者為海事監管單位、研究人員與資料科學家，核心在於評估模型在丹麥漁船區域的表現、更大區域的泛化能力、不同輸入表示（離散vs連續）以及生成分布從高斯轉為 GMM 的影響。

## 技術
專案以 Jupyter Notebook 為主要開發環境，使用 Python 實作深度學習模型。核心模型為變分遞迴神經網路（VRNN），負責學習 AIS 軌跡的機率分布並計算重建似然度。異常偵測則採用地理相關的 a contrario 規則，以針對位置依賴的分布進行門檻設定。程式碼參考 Kristoffer Vinther Olesen 的 util 函式庫，涉及資料前處理、離散/連續特徵編碼以及模型訓練與評估腳本。具體使用的深度學習框架（如 PyTorch 或 TensorFlow）在 README 中未明確說明。

## 架構
資料流程始於原始 AIS 檔案的讀取與清洗，接著依據離散或連續表示方式產生對應的輸入張量（例如 one‑hot 編碼的離散箱或原始經緯度速度序列）。這些輸入饋送至 VRNN 模型，模型由編碼器捕獲時間依賴性、潛在變數產生高斯或 GMM 分布，以及解碼器重建軌跡。訓練時最大化重建似然度（或最小化負對數似然），驗證階段根據重新建機率計算異常分數。最後套用地理相關的 a contrario 規則，將分數與位置依賴的門檻比較，判定是否為異常軌跡。整個流程在 Jupyter Notebook 中以逐步儲存格呈現，方便實驗不同輸入表示與分布假設。

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
