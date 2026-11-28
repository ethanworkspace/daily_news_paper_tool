# GitHub 專案 01：notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15

- 日期：2026-11-20
- URL：https://github.com/notsodubeyous/IoT-Network-Intrusion-Detection-System-UNSW-NB15
- 描述：Network Intrusion Detection based on various machine learning and deep learning algorithms using UNSW-NB15 Dataset
- Stars：210  |  Forks：49  |  Language：Jupyter Notebook
- License：MIT
- Topics：classification, cybersecurity, decision-tree-classifier, deep-learning, iot, iot-security, keras, knn, linear-regression, logistic-regression, machine-learning, mlp-classifier, multilayer-perceptron, network-intrusion-detection, network-security, random-forest, supervised-learning, svm-classifier, tensorflow, unsw-nb15
- 更新時間：2026-11-11T17:45:53+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.1109/milcis.2015.7348942
- 品質分數：10/10 [paper_paired, implementation_signals]

## 在做什麼
本專案利用 UNSW-NB15 資料庫，針對物聯網（IoT）環境中的網路流量進行入侵偵測。透過多種機器學習與深度學習模型（決策樹、K‑近鄰、線性回歸、SVM、邏輯回歸、多層感知器等），實現二元與多類別攻擊分類，協助安全分析人員、IoT 系統開發者及學術研究者快速識別異常流量、評估模型效能，並提供完整的資料前處理、特徵選取與模型訓練流程，以降低智慧城市網路遭受惡意入侵的風險。

## 技術
該專案以 Python 為主要程式語言，在 Jupyter Notebook 環境中實作。使用 scikit‑learn 提供的決策樹、K‑近鄰、線性回歸、SVM、邏輯回歸、隨機森林與多層感知器（MLPClassifier）等演算法，並引用 Keras/TensorFlow 進行深度學習實驗。資料處理階段運用 pandas、numpy 讀取與清理 UNSW‑NB15 CSV，透過 pd.get_dummies 對 proto、service、state 進行 one‑hot 編碼，使用 MinMaxScaler 對 58 個數值欄位做正規化，並以 LabelEncoder 將 label 與 attack_cat 編碼。特徵選取採用 Pearson 相關係數，保留與目標欄位相關係數大於 0.3 的變數，最終得到二元類別 15 個特徵與多類別 16 個特徵。資料切分採用隨機抽樣，二元類別 80% 訓練 / 20% 測試，多類別 70% 訓練 / 30% 測試。所有模型訓練與評估皆在 Notebook 中以程式碼 cell 形式呈現，可直接在 Google Colab 或本機 Jupyter 上執行。

## 架構
專案的執行流程可分為五個主要階段。首先，讀取原始 UNSW_NB15.csv 與特徵說明檔，進行缺失值刪除與資料型別轉換。其次，對 proto、service、state 三個類別欄位執行 one‑hot 編碼，並將得到的 19 個新欄位合併回主資料框，使特徵總數升至 61；接著對 58 個數值欄位使用 MinMaxScaler 進行正規化。第三階段，依據目標變數建立二元類別（normal/abnormal）與多類別（9 種攻擊類別＋正常）兩個資料副本，分別進行 LabelEncoder 編碼，並以 Pearson 相關係數篩選特徵，得到 bin_data（15 特徵）與 multi_data（16 特徵）。第四階段，將二元資料隨機切分為 80% 訓練 / 20% 測試，多類別資料切分為 70% 訓練 / 30% 測試。最後，在各訓練集上依序訓練決策樹、K‑近鄰、線性回歸、SVM、邏輯回歸、隨機森林與多層感知器等模型，並在對應測試集上計算準確率、平均絕對誤差、均方誤差、根均方誤差與 R² 分數，結果直接在 Notebook 中顯示。若未依照此順序執行，可能會因欄位遺失或型別不匹配而產生錯誤。

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
