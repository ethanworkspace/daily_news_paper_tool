# GitHub 專案 03：avaapm/marveldataset2016

- 日期：2026-09-14
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
此專案提供一個 Python 腳本 (MARVEL_Download.py) 用於從網路上下載 MARVEL 2016 資料集，該資料集包含大量船舶圖像，適用於船舶分類、驗證、檢索與識別等電腦視覺研究。目標使用者為需要此資料集進行實驗的學術研究者與開發者，核心問題在於取得並組織資料集的過程較為繁瑣，透過該腳本可自動化下載、依照 .dat 檔案的說明建立對應的資料夾結構，並產生含完整路徑的 FINAL.dat 檔案，方便後續模型訓練與評估。

## 技術
專案主要使用 Python 3，核心為 MARVEL_Download.py 腳本。腳本內部利用多執行緒 (NUMBER_OF_WORKERS = 10) 進行平行下載，透過 urllib 或 requests (依實際程式碼而定) 從 URL 取得圖像，並依據設定的 IMAGE_HEIGHT、IMAGE_WIDTH、ORIGINAL_SIZE 等參數決定是否保留原始尺寸或統一調整至 256×256。下載後的圖像會被放置在與腳本同目錄的資料夾中，並依照輸入的 .dat 檔案 (如 VesselClassification.dat、IMOTrainAndTest.dat 等) 產生對應的 FINAL.dat，其中每行最後一欄為圖像的本地路徑。未見額外的深度學習框架或模型訓練程式碼。

## 架構
系統架構簡單，主要包含三個部分：(1) 輸入的 .dat 檔案，描述船舶 ID、類別、訓練/測試索引等資訊；(2) MARVEL_Download.py 腳本，讀取 .dat 檔案，根據每行組合下載 URL，啟動多執行緒進行圖像下載，並將圖像存放在本地目錄下的子資料夾中；(3) 輸出的 FINAL.dat 檔案，其格式與輸入 .dat 相同，僅在每行末尾追加對應圖像的完整路徑。資料流程為：讀取 .dat → 建立下載任務 → 平行下載圖像 → 儲存圖像 → 產生 FINAL.dat。由於 README 未提供腳本的原始碼細節，以上架構推斷僅基於說明中的參數與檔案說明，若腳本內部實作有所不同則需參考原始程式碼以確認。

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
