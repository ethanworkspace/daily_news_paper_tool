# GitHub 專案 03：avaapm/marveldataset2016

- 日期：2026-09-16
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 論文層級：未對應論文（海事）
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案提供一個 Python 腳本，用於從網路下載 MARVEL 2016 船舶影像資料集，並產生對應的中繼檔案（.dat），以支援船舶分類、驗證、檢索與辨識等五種任務。目標使用者為需要大規模船舶影像進行電腦視覺研究的學者與開發者，核心問題在於取得標註完整且結構化的船舶資料，以便進行模型訓練與評估。

## 技術
專案主要使用 Python 3，核心腳本 MARVEL_Download.py 透過標準庫（urllib、os、threading）實作多執行緒下載，參數包括工作執行緒數、圖片尺寸、是否保留原始大小等。下載後會依照輸入的 .dat 檔案（如 VesselClassification.dat、IMOTrainAndTest.dat 等）在每行末附加本地檔案路徑，產生 FINAL.dat。資料流程僅涉及 HTTP 下載與本地檔案寫入，未使用額外框架或深度學習模型。

## 架構
執行流程為：使用者先選取對應的 .dat 檔案並取消註解，接著執行 MARVEL_Download.py；腳本讀取 .dat 檔案的每一行，解析船舶 ID、集合索引、類別標籤等欄位，根據 ID 從預定義的 URL 下載對應影像，利用 NUMBER_OF_WORKERS 設定的執行緒平行進行下載，下載完成後將影像存放於與腳本同目錄的資料夾中，並建立 meta 資料夾結構；最後在每行原始資料後附加本地路徑，寫入至 FINAL.dat。後續任務（分類、驗證、檢索、辨識）則直接讀取該 FINAL.dat 或原始 .dat 檔案，依照所需的索引與標籤進行資料載入與模型訓練。由於 README 未提供更詳細的模組圖或非同步訊息流，以上架構說明僅基於腳本說明與檔案結構的推斷。

## README 摘錄（節選）
```text
# marveldataset2016
This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
Author: Erhan Gundogdu
Last Update: 09/28/2016
CITATION:
If you use MARVEL in your research, please cite:
@PROCEEDINGS {MARVEL,
author = "Gundogdu E., Solmaz B, Yucesoy V., Koc A.",
title = "Marvel: A Large-Scale Image Dataset for Maritime Vessels",
year = "2016",
organization = "Asian Conference on Computer Vision (ACCV)"
}
This document is to explain the use of MARVEL and its metadata and to download it from the web.
(0) Downloading MARVEL dataset:
In order to download the MARVEL dataset, 'MARVEL_Download.py' Python script must be run with the appropriate
.dat file, i.e. Uncomment the related dat file: 'VesselClassification.dat' for Vessel Classification,
'IMOTrainAndTest.dat' for Vessel Verification/Retrieval/Recognition tasks.
Default values and explanation of the download parameters inside MARVEL_Download.py are:
NUMBER_OF_WORKERS = 10 ## Number of threads that will be working in parallel
MAX_NUM_OF_FILES_IN_FOLDER = 5000 ## Maximum number of files in a folder
IMAGE_HEIGHT = 256 ## image height unless ORIGINAL_SIZE = 1
IMAGE_WIDTH = 256 ## image width unless ORIGINAL_SIZE = 1
ORIGINAL_SIZE = 0 # 1 for yes, 0 for no
JUST_IMAGE = 1 # 1 for yes, 0 for no
The images are downloaded to the location of MARVEL_Download.py with a meta folder structure.
Once the download is finished, the vessel images are distributed in a meta folder structure.
The output filename is FINAL.dat, which has the same structure as the input XXX.dat file except for appended path names
as the last column of each line.
e.g. one line from input IMOTrainAndTest.dat file: '993293,1,1,Container Ship'
and one line from output FINAL.dat file: '993293,1,1,Container Ship,path\to\your\folder\W1_1\993293.jpg'
(1) Vessel Classification:
VesselClassification.dat is the corresponding file for vessel classification.
Each line carries the information related to the training and the test images in the following structure:
vessel ID, set index, class label, class label name
vessel ID: is the ID consistent with the url name in the corresponding website and helps us to download the image.
set index: 1 or 2 (1 for training and 2 for test)
class label: vessel type label enumeration (from 1 to 26)
class label name: the name of the class label given in our paper
(2) IMO Training and Test Sets:
IMOTrainAndTest.dat is the corresponding file containing information of IMO train and test sets defined in the paper.
Each line carries the information related to the IMO train and the test images in the following structure:
vessel ID, set index, class label, class label name, IMO Number
vessel ID: is the ID consistent with the url name in the corresponding website and helps us to download the image.
set index: 1 or 2 (1 for training and 2 for test)
class label: vessel type label enumeration (from 1 to 26)
class label name: the name of the class label given in our paper
IMO number: is International Maritime Organization number of the corresponding vessel taken from the website
Note: The IMO Train and test sets contain 400K images in total and Vessel Verification/Retrieval/Recognition set indices
are based on the ordering of these 400K image list.
(3) Vessel Verification:
VesselVerificationTest.dat and VesselVerificationTrain.dat are the vessel verification task related .dat files.
In each file, every line corresponds to the indices of the pairs of images for positive and negative examples.
As stated in the paper, a positive example is a pair of images belonging to the same vessel
and a negative example is a pair of images belonging to different vessels. These pairs are randomly sampled from
the IMO train and test sets.
Each line has the following structure:
vessel index 1, vessel index 2, set index
vessel index 1/2: the index of the vessels withi
```
