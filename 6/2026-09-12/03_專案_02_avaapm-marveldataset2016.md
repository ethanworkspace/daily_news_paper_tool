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
此專案提供 MARVEL 2016 資料集的下載腳本與說明，使研究者能取得大型海事船舶圖像資料，以進行船舶分類、驗證、檢索與辨識等電腦視覺任務。主要使用者為從事船舶圖像分析的學術研究者與開發者，核心問題在於取得統一格式、具備標註資訊的船舶圖像集以及相應的資料索引檔(.dat)，以便直接用於實驗。

## 技術
專案以 Python 實作主要下載腳本 MARVEL_Download.py，使用標準函式庫進行網路請求、檔案 I/O 與多執行緒（NUMBER_OF_WORKERS 參數控制平行下載數量）。透過讀取 .dat 檔案（如 VesselClassification.dat、IMOTrainAndTest.dat 等）取得圖像 URL 與標籤，依設定的 IMAGE_HEIGHT、IMAGE_WIDTH、ORIGINAL_SIZE 等參數將圖像儲存至本機資料夾，並產生包含完整路徑的 FINAL.dat 檔案。未見額外的第三方框架或模型。

## 架構
架構包含：(1) 輸入 .dat 檔案（描述船舶 ID、集合索引、類別標籤等）；(2) MARVEL_Download.py 讀取該檔案，以多執行緒方式下載對應圖像，依設定建立資料夾階層；(3) 下載完成後產出 FINAL.dat，在原始 .dat 每行末追加圖像完整路徑；(4) 依不同任務（船舶分類、驗證/檢索/辨識）使用對應的 .dat 檔案與 FINAL.dat 進行後續處理。資料流為：.dat → 下載腳本 → 圖像檔案 + FINAL.dat → 下游訓練/評估腳本。若 README 未明確說明腳本內部實作細節，則上述流程為基於可見內容的合理推斷。

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
