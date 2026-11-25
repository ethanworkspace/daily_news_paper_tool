# GitHub 專案 01：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

- 日期：2026-11-14
- URL：https://github.com/notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15
- 描述：Network Intrusion Detection based on various machine learning and deep learning algorithms using UNSW-NB15 Dataset
- Stars：210  |  Forks：49  |  Language：Jupyter Notebook
- License：MIT
- Topics：classification, cybersecurity, decision-tree-classifier, deep-learning, iot, iot-security, keras, knn, linear-regression, logistic-regression, machine-learning, mlp-classifier, multilayer-perceptron, network-intrusion-detection, network-security, random-forest, supervised-learning, svm-classifier, tensorflow, unsw-nb15
- 更新時間：2026-11-11T17:45:53+00:00
- 配對論文：https://doi.org/10.1109/milcis.2015.7348942
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
本專案利用 UNSW-NB15 資料集，實作多種機器學習與深度學習模型（決策樹、KNN、線性回歸、SVM、邏輯回歸、MLP 等），進行二元及多類別網路入侵偵測，旨在協助 IoT 場景中的網路流量異常識別與威脅預警，服務對象為資安研究人員、IoT 系統開發者與安全運維人員。

## 技術
專案以 Python 為主要語言，以 Jupyter Notebook 為開發環境，引用 scikit-learn、pandas、numpy、matplotlib 與 pickle 進行資料讀取、前處理與模型訓練；資料經過缺失值移除、類別欄位 one‑hot 編碼、LabelEncoder 編碼、MinMax 標準化以及 Pearson 相關係數特徵選取；接著使用決策樹、KNN、線性回歸、SVM、邏輯回歸與 MLP 等模型分別進行二元及多類別入侵偵測，並報告準確率、MAE、MSE、RMSE 與 R² 等評估指標。

## 架構
資料流程始於讀取 UNSW_NB15.csv 與特徵說明檔，先移除空值，將 proto、service、state 欄位進行 one‑hot 編碼後合併，得到 61 個特徵；接著依據 label 或 attack_cat 建立二元與多類別資料集，對數值欄位使用 MinMax Scaler 進行正規化；利用 Pearson 相關係數選取與目標高於 0.3 的特徵，得到 bin_data（15 特徵）與 multi_data（16 特徵）；隨機切分訓練/測試集（二元 80/20，多類別 70/30），分別訓練決策樹、KNN、線性回歸、SVM、邏輯回歸與 MLP 模型，最後計算準確率、MAE、MSE、RMSE 與 R² 等指標來評估模型在入侵偵測上的效能。

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
