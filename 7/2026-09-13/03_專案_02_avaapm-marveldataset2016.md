# GitHub 專案 02：avaapm/marveldataset2016

- 日期：2026-09-13
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案提供一個 Python 腳本 MARVEL_Download.py，用於從網路下載 MARVEL 2016 海船圖像資料集，並自動建立資料夾結構與對應的標註檔（FINAL.dat），使研究者能直接取得用於船舶分類、驗證、檢索與辨識等任務的圖像與中繼資料，解決資料取得與組織的門檻問題。

## 技術
該腳本使用 Python 3 標準庫（如 urllib、os、threading）實作多執行緒下載，透過設定 NUMBER_OF_WORKERS 控制平行數量，可調整 IMAGE_HEIGHT、IMAGE_WIDTH、MAX_NUM_OF_FILES_IN_FOLDER 等參數，下載後依照輸入的 .dat 檔案（VesselClassification.dat、IMOTrainAndTest.dat 等）在腳本所在目錄建立 meta 資料夾，並將每筆圖像的相對路徑附加為最後一欄，產出 FINAL.dat 檔案。

## 架構
執行流程為：使用者先選擇對應的 .dat 檔案並取消註解，腳本讀取檔案中的每一行（vessel ID、set index、class label、class label name 等欄位），根據 vessel ID 從線上來源下載圖像，利用多執行緒將圖像存放至以 set index 與 class label 為基礎的資料夾結構中，下載完成後在原始 .dat 每行末追加對應的相對路徑，寫入 FINAL.dat。此檔案可直接作為後續分類、驗證、檢索或辨識任務的輸入；若需進行驗證、檢索或辨識，則必須先產出 IMOTrainAndTest.dat 的 FINAL.dat，因為其他任務的 .dat 檔案僅提供相對索引，依賴該完整路徑檔案來定位實際圖像。若 README 未明確說明多執行緒細節或錯誤處理，以上架構推斷基於所述參數與檔案流程描述。

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
