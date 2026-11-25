# GitHub 專案 01：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

- 日期：2026-11-13
- URL：https://github.com/notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15
- 描述：Network Intrusion Detection based on various machine learning and deep learning algorithms using UNSW-NB15 Dataset
- Stars：210  |  Forks：49  |  Language：Jupyter Notebook
- License：MIT
- Topics：classification, cybersecurity, decision-tree-classifier, deep-learning, iot, iot-security, keras, knn, linear-regression, logistic-regression, machine-learning, mlp-classifier, multilayer-perceptron, network-intrusion-detection, network-security, random-forest, supervised-learning, svm-classifier, tensorflow, unsw-nb15
- 更新時間：2026-11-11T17:45:53+00:00
- 配對論文：https://doi.org/10.1109/milcis.2015.7348942
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
此專案構建基於 UNSW‑NB15 資料集的 IoT 網路入侵偵測系統，透過多種機器學習與深度學習演算法（決策樹、K‑鄰近、線性回歸、SVM、邏輯回歸、多層感知器）進行二元及多類別攻擊分類，旨在協助安全研究人員與網路管理員快速識別異常流量，提升 IoT 環境的威脅偵測能力。目標使用者包括資安研究員、IoT 系統開發者以及網路安全分析師。

## 技術
專案使用 Python 實作，筆記本以 Jupyter Notebook / Google Colab 為執行環境，主要依賴 scikit‑learn 提供的分類器（DecisionTreeClassifier、KNeighborsClassifier、LinearRegression、SVC、LogisticRegression、MLPClassifier），搭配 pandas、numpy 進行資料處理，matplotlib 視覺化，pickle 儲存模型。資料前處理包括缺失值移除、資料型別轉換、對 proto、service、state 三個類別欄位進行 one‑hot 編碼、MinMax 標準化、LabelEncoder 編碼目標標籤，並以 Pearson 相關係數 (>0.3) 進行特徵選擇，得到 binary 資料集 15 個特徵與 multi‑class 資料集 16 個特徵。

## 架構
資料流程先載入 UNSW_NB15.csv 與特徵說明檔，移除空值後轉換欄位型別，對 proto、service、state 進行 one‑hot 編碼並合併，得到 61 個特徵；接著使用 MinMaxScaler 對 58 個數值欄位進行正規化。根據 label 與 attack_cat 建立二元與多類別資料集，分別以 LabelEncoder 編碼目標，並對 multi‑class 進行 one‑hot 編碼 attack_cat。利用 Pearson 相關係數選擇與目標相關度 >0.3 的特徵，binary 得 15 個、multi‑class 得 16 個特徵。隨機切分資料（binary 80%/20%，multi‑class 70%/30%），將訓練集輸入各個分類器進行訓練，然後在測試集上計算 Accuracy、MAE、MSE、RMSE、R² 等評估指標。若 README 未說明模型儲存或推論部署，則僅可推論為在筆記本內完成訓練與評估。

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
