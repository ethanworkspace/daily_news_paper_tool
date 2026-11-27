# GitHub 專案 04：avaapm/marveldataset2016

- 日期：2026-09-27
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
此專案提供一個 Python 腳本 (MARVEL_Download.py)，用於從網路上下載 MARVEL 2016 海船圖像資料庫，並產生對應的中繼檔案，以支援船舶分類、驗證、檢索與辨識等四種常見電腦視覺任務。目標使用者為從事船舶圖像研究的學術研究者與開發者，核心在解決取得大規模標註海船影像與任務劃分的門檻。

## 技術
專案主要使用 Python 3 撰寫，核心腳本 MARVEL_Download.py 透過內建的 threading 模組實現多執行緒平行下載（NUMBER_OF_WORKERS 可設），利用 urllib 或 requests 進行 HTTP GET 取得圖像，依設定的 IMAGE_HEIGHT、IMAGE_WIDTH 與 ORIGINAL_SIZE 進行尺寸調整（或保留原始大小），將下載的圖片依照 meta 資料夾結構儲存，最後產生 FINAL.dat 檔案，其中每行補充了對應的本地路徑。資料流僅涉及檔案讀寫與網路 I/O，未顯示依賴第三方深度學習框架。

## 架構
使用流程為：使用者先選擇對應的 .dat 檔案（如 VesselClassification.dat 或 IMOTrainAndTest.dat），在 MARVEL_Download.py 中取消註解該檔案的引用，執行腳本。腳本讀取 .dat 每一行，解析 vessel ID、set index 等欄位，根據 ID 組合下載 URL，利用 NUMBER_OF_WORKERS 執行緒平行下載圖像，將圖片存放於腳本所在目錄下的 meta 資料夾（例如 W1_1/993293.jpg），並在記憶體中累積路徑。下載完成後，腳本將原始 .dat 的每行追加對應的圖片路徑，輸出為 FINAL.dat，供後續任務使用。分類、驗證、檢索與辨識等任務則分別讀取各自的 .dat 檔案（如 VesselVerificationTest.dat、ChiTrain.dat 等）以及必要的 IMOTrainAndTest.dat，根據其中的索引進行特徵 extraction、距離計算或模型訓練。若 README 未明確說明特定模型或訓練流程，則此部分為基於檔案說明的合理推斷。

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
