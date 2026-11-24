# GitHub 專案 02：avaapm/marveldataset2016

- 日期：2026-09-18
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案提供 MARVEL 2016 海事船舶圖像資料集的下載與組織工具，透過 MARVEL_Download.py Python 腳本讀取對應的 .dat 檔案，自動從網路抓取船舶圖片並依照分類、驗證、檢索或辨識任務建立資料夾結構與 FINAL.dat 索引檔，方便研究者直接用於電腦視覺實驗。目標使用者為從事船舶辨識、圖像分類與檢索的學術研究人員與開發者。

## 技術
技術上採用 Python 3 實作，使用標準庫（urllib、os、threading）進行多執行緒下載（NUMBER_OF_WORKERS 可調），解析 .dat 中的船舶 ID、集合索引、類別標籤及 IMO 編號等欄位，依設定的 IMAGE_HEIGHT/IMAGE_WIDTH 或原始尺寸下載圖片，存放於層級資料夾，最後產生包含完整路徑的 FINAL.dat 檔案，支援船舶分類、驗證、檢索與辨識五種任務的資料準備流程。

## 架構
架構方面，主要模組為 MARVEL_Download.py，內部包含參數設定區、檔案解析函式（讀取 VesselClassification.dat、IMOTrainAndTest.dat 等）、多執行緒下載函式（依船舶 ID 建立 URL、儲存路徑），以及寫入結果索引函式（產生 FINAL.dat）。資料流程為：使用者選取對應的 .dat → 腳本解析每列取得 vessel ID 與其他標註 → 透過 NUMBER_OF_WORKERS 執行緒並行下載圖片至本地資料夾 → 下載完成後，將每筆紀錄的路徑附加至原始欄位後輸出為 FINAL.dat，此檔案可直接被後續的訓練或評估腳本讀取，用於分類、驗證、檢索或辨識等任務。若需進行驗證、檢索或辨識，則需先產生 IMOTrainAndTest.dat 對應的 FINAL.dat，再根據其中的索引使用 VesselVerification*.dat、Chi*/Euc*.dat 或 Recognition 資料夾內的 .dat 檔案進行配對。由於 README 未詳細說明多執行緒實作細節與錯誤處理，上述架構推斷主要基於腳本註解與參數說明。

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
