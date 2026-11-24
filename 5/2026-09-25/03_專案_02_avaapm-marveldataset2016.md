# GitHub 專案 02：avaapm/marveldataset2016

- 日期：2026-09-25
- URL：https://github.com/avaapm/marveldataset2016
- 描述：This repository is to download the MARVEL dataset 2016 for the publication "Gundogdu E., Solmaz B, Yucesoy V., Koc A., Marvel: A Large-Scale Image Dataset for Maritime Vessels, Asian Conference on Computer Vision (ACCV), 2016".
- Stars：64  |  Forks：23  |  Language：Python
- License：
- Topics：
- 更新時間：2026-08-29T14:08:52+00:00
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案提供一個 Python 腳本 MARVEL_Download.py，用於從網路下載 MARVEL 2016 海船圖像資料集，並依照不同任務（船舶分類、驗證、檢索、辨識）所需的 .dat 檔案產生對應的 FINAL.dat，其中每行包含圖像路徑與標籤。目標使用者為電腦視覺與海運領域的研究者，他們需要大規模標註的船舶圖像來訓練與評估深度學習模型。核心問題在於取得且組織好此資料集的下載與中繼檔案，以便直接用於後續的實驗。

## 技術
專案主要使用 Python 3，核心為 MARVEL_Download.py 腳本。該腳本透過可設定的 NUMBER_OF_WORKERS 參數啟用多執行緒下載，支援自訂圖片尺寸（IMAGE_HEIGHT、IMAGE_WIDTH）與是否保留原始大小（ORIGINAL_SIZE）。下載後，圖像會依照 meta 資料夾結構儲存，並產生 FINAL.dat 檔案，其中每行將原始 .dat 資料附加上對應的本地檔案路徑。腳本同時讀取 VesselClassification.dat、IMOTrainAndTest.dat 等任務特定的 .dat 檔案，以產生對應的訓練/測試清單。

## 架構
架構方面，專案包含以下主要元素：(1) MARVEL_Download.py 下載腳本，負責讀取輸入的 .dat 檔案、透過多執行緒從指定 URL 下載圖像並建立資料夾結構；(2) 各種任務的 .dat 檔案（VesselClassification.dat、IMOTrainAndTest.dat、VesselVerificationTrain/Test.dat、Chi*/Euc* 檔案、Recognition 子資料夾中的 trainSplit_X 檔案），它們定義了圖像的 ID、所屬集合（訓練/測試）、類別標籤及 IMO 編號等資訊；(3) 下載完成後，腳本會在每個圖像對應的資料夾中產生 FINAL.dat，其中最後一欄為本地路徑，使得後續的訓練或評估程式可以直接讀取此檔案以取得圖像與標籤。由於 README 僅說明下載與檔案格式，未提供模型訓練或推論的程式碼，因此架構描述僅基於可見的下載流程與資料組織。

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
