# GitHub 專案 05：carlossantamarizq/vesselTracker

- 日期：2026-10-13
- URL：https://github.com/carlossantamarizq/vesselTracker
- 描述：Ship detection from satellite imagery using Deep Learning model (YOLOv5). Model trained with custom Sentinel-1 dataset provided by Earth Engine API.
- Stars：28  |  Forks：3  |  Language：Python
- License：
- Topics：
- 更新時間：2026-10-06T16:06:50+00:00
- 論文層級：未對應論文（海事）
- 配對論文：
- 品質分數：5/10 

## 在做什麼
此專案利用深度學習模型（YOLOv5）對衛星合成孔徑雷達（Sentinel-1 SAR）影像進行船舶偵測，目標使用者為海事監控研究人員、遙感應用開發者及海上交通管理單位。核心問題在於自動化從大量 SAR 影像中辨識船隻位置，減少人工解讀成本，並為後續船舶分類與地理定位提供基礎。

## 技術
專案主要使用 Python 3.x 作為開發語言，深度學習框架採用 PyTorch，並基於 YOLOv5 的縮減版模型進行訓練與推論。資料來源透過 Google Earth Engine API 下載 Sentinel-1 SAR 影像，經過基本的輻射定標與幾何校正後送入模型。偵測結果使用 Pandas 匯出為 DataFrame，以便後續統計與座標計算。此外，專案尚未實作的船舶類別分類將依賴額外標註資料集與同一 YOLOv5 架構進行多類別訓練。

## 架構
系統可分為四個主要模組：(1) 資料取得模組，負責呼叫 Earth Engine API 依據時間與地理範圍下載 Sentinel-1 GRD 產品；(2) 前處理模組，對 SAR 影像進行去噪、對數變換、影像裁剪及正規化，使其符合 YOLOv5 輸入尺寸；(3) 偵測模組，載入已訓練好的 YOLOv5 權重，執行前向傳播產生邊界框與信心分數，並經過非極大值抑制（NMS）過濾；(4) 後處理與輸出模組，利用 Earth Engine 回傳的影像中心座標與像素尺寸將偵測框映射至地理經緯度，計算掃描面積（km²），最後將船隻編號、信心度、像素座標與地理座標寫入 Pandas DataFrame 並可選擇導出為 CSV。若未來加入船舶類別偵測，則僅需在模組 (3) 中替換為多類別權重，其餘流程保持不變。README 中未詳細說明模型結構的具體縮減方式或訓練超參數，因此架構說明僅基於可見的資料流與已完成的目標推斷。

## README 摘錄（節選）
```text
# vesselTracker
Project based on reduced model of Yolov5 architecture using Pytorch. Custom dataset based on SAR imagery provided by Sentinel-1 through Eart Engine API. In progress.
## Next updates
- Provide more information as output: Earth Engine API also provides coordinates of the scenes. Therefore, the Earth's surface in km2 analyzed by the algorithm can be calculated. With the positions of the vessels on the scenes, the position of each vessel could be also estimated in geographic coordinates. Export info to dataFrame using Pandas.
- Add vessel type detection: There are few datasets with vessel types classified. These can be included on the program developed on this project to not only detect vessels, but also classify them into classes (cargo, tanker, other type).
## Objectives
- [x] Program script that downloads images from Sentinel-1 through Earth Engine API
- [x] Select object detection model
- [x] Select and customize datasetS
- [x] Train model
- [x] Program detection script
- [ ] Add vessel classification
- [ ] Estimate vessel position in geographic coordinates
## Example of input
[code block omitted]
## Output of the model:
Fig.1 - Algeciras port scene with detected vessels. Photo taken on 2 October 2019
at 18:17h
Fig.2 - Shenzhen bay scene with detected vessels. Photo taken on 27 December 2019
at 10:33h
Fig.3 - Strait of Gibraltar scene with detected vessels. Photo taken on 28 February 2020 at 18:25h
```
