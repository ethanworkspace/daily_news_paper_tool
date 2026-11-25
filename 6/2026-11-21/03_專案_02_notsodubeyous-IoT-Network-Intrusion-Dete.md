# GitHub 專案 02：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

- 日期：2026-11-21
- URL：https://github.com/notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15
- 描述：Network Intrusion Detection based on various machine learning and deep learning algorithms using UNSW-NB15 Dataset
- Stars：210  |  Forks：49  |  Language：Jupyter Notebook
- License：MIT
- Topics：classification, cybersecurity, decision-tree-classifier, deep-learning, iot, iot-security, keras, knn, linear-regression, logistic-regression, machine-learning, mlp-classifier, multilayer-perceptron, network-intrusion-detection, network-security, random-forest, supervised-learning, svm-classifier, tensorflow, unsw-nb15
- 更新時間：2026-11-11T17:45:53+00:00
- 配對論文：https://doi.org/10.1109/milcis.2015.7348942
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
此專案利用 UNSW‑NB15 資料集，針對物聯網環境的網路流量進行入侵偵測。透過多種機器學習與深度學習模型（決策樹、K‑鄰近、線性回歸、線性 SVM、邏輯回歸、多層感知器），實作二元與多類別攻擊分類，協助安全研究人員、IoT 系統開發者與教學人員快速評估不同演算法在真實攻擊場景下的偵測效能，解決 IoT 網路中異常流量辨識與攻擊類別預測的核心問題。

## 技術
專案以 Python 為主要語言，在 Jupyter Notebook 環境中實作。使用 scikit‑learn 提供的 DecisionTreeClassifier、KNeighborsClassifier、LinearRegression、SVC（linear kernel）、LogisticRegression、MLPClassifier 等模型；資料處理依賴 pandas、numpy 進行讀取與清理，透過 matplotlib 視覺化結果，使用 pickle 儲存模型。前置步驟包括缺失值刪除、資料型別轉換、對 proto、service、state 欄位進行 one‑hot 編碼、MinMax 標準化數值欄位、LabelEncoder 對標籤編碼，並以 Pearson 相關係數 (>0.3) 進行特徵選擇，得到 binary 資料集 15 個特徵與 multi 資料集 16 個特徵。

## 架構
資料流程先載入 UNSW_NB15.csv 與特徵說明檔，接著刪除空值、轉換資料型別，對三個類別欄位做 one‑hot 編碼後合併，得到 61 個特徵。接著對 58 個數值欄位使用 MinMaxScaler 正規化。根據任務建立二元標籤（normal/abnormal）與多類別標籤（9 種攻擊類別），分別產生 bin_data 與 multi_data，並以 LabelEncoder 編碼目標。利用 Pearson 相關係數篩選特徵，binary 保留 15 個、multi 保留 16 個特徵。隨機切分資料集（binary 80%/20%，multi 70%/30%），依序訓練 Decision Tree、K‑Nearest Neighbor、Linear Regression、Linear SVM、Logistic Regression、Multi‑Layer Perceptron 六種模型，並在測試集上計算 Accuracy、MAE、MSE、RMSE、R2 等評估指標。整個流程必須依照 Notebook 中給定的儲存格順序執行，以避免因變數未定義而產生錯誤。若 README 未明確說明某些細節（例如模型超參數調整依據），則以上描述為基於可見步驟的合理推斷。

## README 摘錄（節選）
```text
# IoT-Network-Intrusion-Detection-System-UNSW-NB15
Network Intrusion Detection based on various Machine learning and Deep learning algorithms using UNSW-NB15 Dataset
## Blog
>## Cyberattacks Detection in IoT-based Smart City Network Traffic (https://now-its-abhi.medium.com/cyberattacks-detection-in-iot-based-smart-city-network-traffic-c874588c5f6c?source=friends_link&sk=62e0269e428b8658163a0c0d842d1151)
## Prerequisites
- Sklearn
- Pandas
- Numpy
- Matplotlib
- Pickle
## Running the Notebook
The notebook can be run on
- Google Colaboratory
- Jupyter Notebook
## Instructions
- To run the code, user must have the required Dataset on their system or programming environment.
- Upload the notebook and dataset on Jupyter Notebook or Google Colaboratory.
- Click on the file with .ipynb extension to open the notebook. To run complete code at once press Ctrl + F9
- To run any specific segment of code, select that code cell and press Shift+Enter or Ctrl+Shift+Enter
> **Caution - The code should be executed in the given order for best results without encountering any errors.**
## Datasets
- **UNSW_NB15.csv** - Original Dataset
- **UNSW_NB15_features.csv** - 49 features with the class label. These features are described in UNSW-NB15_freatures.csv file.
- **bin_data.csv** - CSV Dataset file for Binary Classification
- **multi_data.csv** - CSV Dataset file for Multi-class Classification
## Machine Learning Models
- Decision Tree Classifier
- K-Nearest-Neighbor Classifier
- Linear Regression Model
- Linear Support Vector Machine
- Logistic Regression Model
- Multi Layer Perceptron Classifier
- Random Forest Classifier
## Data Preprocessing
- Dataset had **45 attributes** and **175341 rows**.
- After dropping null values Dataset had **45 attributes** and **81173 rows**.
- Data type of attributes is converted using provided datatype information from features dataset.
- ### One-hot-encoding
- Categorical Columns **'proto'**, **'service'**, **'state'** are one-hot-encoded using **pd.get_dummies()** and these 3 attributes are removed afterwards.
- **data_cat** Dataframe had **19 attributes** after one-hot-encoding.
- **data_cat** is concatenated with the main **data** dataframe.
- Total attributes of **data** dataframe - **61**
- ### Data Normalization
- **58 Numeric Columns** of DataFrame is scaled using **MinMax Scaler**.
- ### Binary Classification
- A copy of DataFrame is created for Binary Classification.
- **'label'** attribute is classified into two categories **'normal'** and **'abnormal'**.
- **'label'** is encoded using **LabelEncoder()**, encoded labels are saved in **'label'**.
- Binary dataset - **81173 rows**, **61 columns**
- ### Multi-class Classification
- A copy of DataFrame is created for Multi-class Classification.
- **'attack_cat'** attribute is classified into **9** categories **'Analysis'**, **'Backdoor'**, **'DoS'**, **'Exploits'**, **'Fuzzers'**, **'Generic'**, **'Normal'**, **'Reconnaissance'**, **'Worms'**
- **attack_cat** is encoded using **LabelEncoder()**, encoded labels are saved in **label**.
- **attack_cat is one-hot-encoded'**.
- Multi-class Dataset - **81173 rows**, **69 columns**
- ### Feature Extraction
- No. of attributes of **'bin_data'** - **61**
- No. of attributes of **'multi_data'** - **69**
- **Pearson Correlation Coefficient** method is used for feature extraction.
- The attributes with **more than 0.3** correlation coefficient with the target attribute **label** were selected.
- No. of attributes of **'bin_data'** after feature selection - **15**
- **'rate'**, **'sttl'**, **'sload'**, **'dload'**, **'ct_srv_src'**, **'ct_state_ttl'**, **'ct_dst_ltm'**, **'ct_src_dport_ltm'**, **'ct_dst_sport_ltm'**, **'ct_dst_src_ltm'**, **'ct_src_ltm'**, **'ct_srv_dst'**, **'state_CON'**, **'state_INT'**, **'label'**
- No. of attributes of **'multi_data'** after feature selection - **16**
- **'dttl'**, **'swin'**, **'dwin'**, **'tcprtt'**, **'synack'**, **'ackdat'**, **'label'**, **'proto_tcp'**, **'proto_udp'**, **'
```
