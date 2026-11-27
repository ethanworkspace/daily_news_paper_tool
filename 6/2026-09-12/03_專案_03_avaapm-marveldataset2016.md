# GitHub 專案 03：avaapm/marveldataset2016

- 日期：2026-09-12
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案提供一個 Python 腳本 (MARVEL_Download.py) 用於從網路上下載 MARVEL 2016 海船圖像資料集，並依照資料集的 .dat 檔案結構將圖像組織成資料夾階層，產生含完整路徑的 FINAL.dat 檔案，以支援後續的船舶分類、驗證、檢索與辨識任務。目標使用者為電腦視覺與海洋資訊研究者，核心問題是取得及準備大規模標註海船影像以進行實驗。

## 技術
專案主要使用 Python 3，核心為 MARVEL_Download.py 腳本。腳本透過多執行緒 (NUMBER_OF_WORKERS = 10) 並行下載圖像，可設定圖像尺寸 (IMAGE_WIDTH/HEIGHT)、是否保留原始尺寸 (ORIGINAL_SIZE)、每個資料夾最大檔案數 (MAX_NUM_OF_FILES_IN_FOLDER) 以及是否僅下載圖像 (JUST_IMAGE)。下載後依照輸入的 .dat 檔案 (如 VesselClassification.dat、IMOTrainAndTest.dat 等) 產生對應的 FINAL.dat，其中每行加入圖像完整路徑作為最後一欄。未見額外的第三方函式庫或模型，僅靠 Python 標準庫進行 HTTP 下載與檔案操作。

## 架構
系統架構簡單：使用者先準備對應的 .dat 檔案（訓練/測試索引、類別標籤、IMO 編號等），執行 MARVEL_Download.py。腳本讀取 .dat 檔案，根據每列的 vessel ID 從預定義的 URL 下載圖像，利用多執行緒加速。下載的圖像被存放在腳本所在目錄下的 meta 資料夾結構中，並產生 FINAL.dat 檔案，其格式與輸入 .dat 相同，只是多了一欄路徑。此 FINAL.dat 可直接用於後續的船舶分類 (VesselClassification)、驗證/檢索/辨識 (IMO Train/Test 集及其衍生 .dat 檔案)。若需進行船舶辨識，則需先解壓 Recognition.zip，其中依船型分類的子資料夾提供各折的 train/test .dat 檔案。架構中未見明確的模型訓練或推論元件，僅為資料準備管線。

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
