# GitHub 專案 01：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

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
本專案利用 UNSW‑NB15 資料集，針對物聯網 (IoT) 網路流量進行入侵偵測。透過比較多種機器學習與深度學習模型（決策樹、K‑近鄰、線性回歸、SVM、邏輯回歸、多層感知器、隨機森林等），建構二元與多類別的攻擊分類器，協助安全研究人員、IoT 系統開發者及教學人員快速評估不同演算法在真實流量中的偵測效能，解決 IoT 環境中流量特徵高維、攻擊類別多樣且標註不平衡的核心問題。

## 技術
專案以 Python 為主要語言，在 Jupyter Notebook 或 Google Colab 環境中執行。資料處理使用 pandas、numpy 進行讀取與清理，Matplotlib 繪圖，pickle 儲存模型。特徵工程包括對 proto、service、state 欄位進行 one‑hot 編碼，使用 MinMaxScaler 對 58 個數值欄位做正規化，並以 LabelEncoder 將標籤轉為數值。特徵選擇採用 Pearson 相關係數，保留與目標標籤相關係數大於 0.3 的欄位，使二元資料從 61 維降至 15 維，多類別資料從 69 維降至 16 維。模型方面，調用 scikit‑learn 提供的 DecisionTreeClassifier、KNeighborsClassifier、LinearRegression、SVC（線性核）、LogisticRegression、MLPClassifier 與 RandomForestClassifier，並在同一 Notebook 中依序訓練與評估。評估指標包括 Accuracy、MAE、MSE、RMSE 與 R2。

## 架構
資料流程始於讀取原始 UNSW_NB15.csv 與特徵說明檔，先刪除缺失值，將資料型態依據特徵檔轉換。接著對三個類別欄位 proto、service、state 進行 one‑hot 編碼，並移除原始欄位，使特徵數增加至 61。然後對全部 58 個數值欄位使用 MinMaxScaler 進行正規化。根據需求建立二元與多類別兩份資料副本：二元版將 label 欄位標準為 normal/abnormal 並以 LabelEncoder 編碼；多類別版則對 attack_cat 欄位進行九類標籤編碼，並同樣進行 one‑hot 編碼。特徵選擇階段，利用 Pearson 相關係數篩選與目標標籤相關係數 >0.3 的欄位，得到 bin_data（15 特徵）與 multi_data（16 特徵）。隨機切分資料集，二元採 80% 訓練 / 20% 測試，多類別採 70% 訓練 / 30% 測試。每個模型在對應的訓練集上進行 fit，接著在測試集上計算 Accuracy、MAE、MSE、RMSE、R2 等指標，結果直接在 Notebook 中輸出。整個流程依序執行，避免因資料洩漏或順序錯誤導致錯誤。

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
