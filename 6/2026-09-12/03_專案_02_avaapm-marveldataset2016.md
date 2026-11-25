# GitHub 專案 02：avaapm/marveldataset2016

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
本專案提供一個 Python 腳本 MARVEL_Download.py，用於從網路上下載 MARVEL 2016 海船圖像資料集，並依照資料集的標註檔 (.dat) 產生對應的圖片路徑檔 FINAL.dat，方便研究者直接取得用於船舶分類、驗證、檢索與辨識等任務的圖像與中繼資料。目標使用者為需要大規模海船圖像資料進行電腦視覺或遙感研究的學術研究者與開發者，核心在於解決手動搜尋與組織該資料集的繁瑣過程。

## 技術
該專案以 Python 3 為主要語言，核心腳本 MARVEL_Download.py 內建多執行緒下載機制（NUMBER_OF_WORKERS 控制平行執行緒數），透過 urllib 或 requests（依實際程式碼而定）從指定 URL 下載 JPEG 圖片，並依照設定的 IMAGE_HEIGHT、IMAGE_WIDTH 與 ORIGINAL_SIZE 參數決定是否保留原始尺寸。下載後，圖片會被放置在與腳本同目錄的資料夾中，形成類別或任務對應的子資料夾結構，最後產生 FINAL.dat 檔案，其格式與輸入的 .dat 相同，僅在每行最後加入完整的本地檔案路徑。未見使用特定深度學習框架或模型，僅為資料準備工具。

## 架構
執行流程如下：使用者先編輯 MARVEL_Download.py，取消註解想要使用的 .dat 檔案（例如 VesselClassification.dat 或 IMOTrainAndTest.dat），設定下載參數（工作執行緒數、圖片尺寸、是否保留原始尺寸、是否只下載圖片）。腳本讀取選定的 .dat 檔，逐行解析出 vessel ID、set index、class label 等欄位，根據 ID 構造對應的下載 URL。接著啟動 NUMBER_OF_WORKERS 個工作執行緒，各執行緒負責從 URL 下載圖片並儲存至本地資料夾，資料夾命名依照資料集的 meta 結構（例如 W1_1/ 下的子資料夾）。所有圖片下載完成後，腳本在每行原始資料後附加本地圖片完整路徑，寫入 FINAL.dat 檔案。若後續任務（如船舶驗證、檢索或辨識）需要參考 IMOTrainAndTest.dat 的索引，則必須先產生該檔案的 FINAL.dat 版本，才能正確使用對應的 .dat 檔。由於 README 未提供詳細的程式碼或類別圖，以上架構說明僅基於文件中描述的參數與流程推斷。

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
