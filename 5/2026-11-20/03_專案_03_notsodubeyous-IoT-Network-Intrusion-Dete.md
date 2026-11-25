# GitHub 專案 03：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

- 日期：2026-11-20
- URL：https://github.com/notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15
- 描述：Network Intrusion Detection based on various machine learning and deep learning algorithms using UNSW-NB15 Dataset
- Stars：210  |  Forks：49  |  Language：Jupyter Notebook
- License：MIT
- Topics：classification, cybersecurity, decision-tree-classifier, deep-learning, iot, iot-security, keras, knn, linear-regression, logistic-regression, machine-learning, mlp-classifier, multilayer-perceptron, network-intrusion-detection, network-security, random-forest, supervised-learning, svm-classifier, tensorflow, unsw-nb15
- 更新時間：2026-11-11T17:45:53+00:00
- 配對論文：https://doi.org/10.1109/milcis.2015.7348942
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
本專案利用 UNSW‑NB15 資料集，針對 IoT 場景下的網路入侵偵測問題，實作多種機器學習與深度學習模型（決策樹、K‑近鄰、線性回歸、線性 SVM、邏輯回歸、多層感知器）進行二元與多分類攻擊辨識，目標使用者為資安研究人員、IoT 系統開發者以及希望透過 Notebook 快速驗證入侵偵測演算法的學習者。核心在於透過資料前處理、特徵選擇與模型訓練流程，評估不同算法在 UNSW‑NB15 上的偵測效能，提供可重現的實驗基礎。

## 技術
專案以 Python 為主要語言，以 Jupyter Notebook 形式呈現，依賴 scikit‑learn、pandas、numpy、matplotlib、pickle 等庫進行資料處理與模型訓練；實作的演算法包括決策樹、K‑近鄰、線性回歸、線性 SVM、邏輯回歸與多層感知器（MLPClassifier），資料流程經過一熱編碼、欄位正規化、標籤編碼、Pearson 相關特徵選擇，最後以 80/20 或 70/30 分割進行訓練與測試。

## 架構
架構分為五個主要步驟：(1) 載入 UNSW‑NB15 原始 CSV 與特徵說明檔；(2) 資料前處理 – 移除空值、依特徵檔轉換資料型別、對 proto、service、state 進行 one‑hot 編碼、使用 MinMaxScaler 對 58 個數值欄位正規化；(3) 特徵抽取 – 計算 Pearson 相關係數，保留與目標 label 相關係數 >0.3 的欄位，產生 bin_data（15 特徵）與 multi_data（16 特徵）；(4) 資料切分 – 二元採 80% 訓練/20% 測試，多分類採 70%/30%；(5) 模型訓練與評估 – 分別對 bin_data 與 multi_data 訓練決策樹、K‑NN、線性回歸、線性 SVM、邏輯回歸與 MLP，計算準確率、MAE、MSE、RMSE、R2 等指標。整個流程在 Notebook 中依序執行，以確保結果可重現。

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
