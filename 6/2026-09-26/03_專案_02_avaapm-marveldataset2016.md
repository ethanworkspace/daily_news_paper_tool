# GitHub 專案 02：avaapm/marveldataset2016

- 日期：2026-09-26
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案提供一個 Python 腳本，用於從網路下載 MARVEL 2016 海船圖像資料集，並依照資料集的 .dat 索引檔案自動建立對應的資料夾結構與 FINAL.dat 路徑檔案，方便研究人員進行船舶分類、驗證、檢索與辨識等任務。

## 技術
主要使用 Python 3 標準庫，透過 MARVEL_Download.py 腳本實作多執行緒下載（NUMBER_OF_WORKERS 可設），支援自訂圖片尺寸、每個資料夾最大檔案數，並根據 VesselClassification.dat、IMOTrainAndTest.dat 等索引檔案產生對應的圖片與中繼資料。未見額外框架或模型。

## 架構
腳本首先讀取使用者指定的 .dat 檔案，解析每列的船舶 ID、集合索引、類別標籤等資訊；接著啟動多個工作執行緒，根據 URL 規則下載對應的船舶圖片，並將圖片儲存於以類別或任務為基礎的層級資料夾中；下載完成後，在每列後附加實際檔案路徑，產生 FINAL.dat 檔案，使後續訓練或評估腳本能直接讀取圖片路徑與標籤。資料流為：.dat → 下載 → 圖片檔案 + FINAL.dat。若需更細部模型訓練則需自行搭配其他程式。

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
