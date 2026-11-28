# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-11-10
- URL：https://github.com/kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8
- 描述：📡 Production-grade maritime surveillance system for detecting ships in Synthetic Aperture Radar (SAR) imagery using YOLOv8-OBB (Oriented Bounding Boxes) and Lee speckle filtering. Handles the unique challenges of radar imagery: multiplicative noise and arbitrarily-oriented vessels.
- Stars：37  |  Forks：4  |  Language：Python
- License：MIT
- Topics：computer-vision, deep-learning, geospatial, image-processing, maritime-surveillance, object-detection, oriented-bounding-box, pytorch, remote-sensing, satellite-imagery, ship-detection, speckle-noise, ssdd-dataset-processing, synthetic-aperture-radar, ultralytics, yolov8
- 更新時間：2026-10-26T14:48:58+00:00
- 論文層級：未對應論文（海事）
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
本專案提供海上監控系統，利用 YOLOv8-OBB 與 Lee speckle 過濾器，在合成孔徑雷達（SAR）影像中偵測船舶。目標使用者為海上監控人員、遙測研究者與國防單位，解決 SAR 影像中乘法性雜 noise 與船隻任意方向導致的偵測困難。

## 技術
使用 Python 3、PyTorch 與 Ultralytics YOLOv8-OBB 框架；採用 Lee 乾淨過濾器去除 SAR 影像的乘法性 speckle 雜訊；資料流程包括 SSDD 資料集下載、轉換為 YOLO OBB 格式、訓練與推論；支援多種模型尺寸（n/s/m/l/x）以及透過 config.yaml 調整超參數。

## 架構
系統架構分為三個主要模組：(1) 前處理模組，對輸入 SAR 影像執Lee speckle 過濾以降低乘法性雜訊；(2) 偵測模組，使用 YOLOv8-OBB backbone（如 CSPDarknet）提取特徵，經 neck 與 OBB head 產生旋轉框的四個角點、中心、寬高、角度與信心分數；(3) 後處理與輸出模組，將偵測結果轉換為 JSON 格式，包含 corners、center、width、height、angle、confidence。資料流程為：原始 SAR 影像 → Lee 過濾 → YOLOv8-OBB 推論 → 輸出偵測框。若需訓練，則加入資料集準備與訓練迴圈。

## README 摘錄（節選）
```text
# Trident - SAR Maritime Vessel Detection
A production-grade maritime surveillance system for detecting ships in Synthetic Aperture Radar (SAR) imagery using Oriented Bounding Boxes (OBB) and speckle noise filtering.
## Mission
Detect ships in SAR images where vessels appear as noisy "salt-and-pepper" clusters, using:
- **Lee Speckle Filter**: Remove radar-specific multiplicative noise
- **YOLOv8-OBB**: Detect ships with rotated bounding boxes (ships are rarely horizontal)
## Pipeline
## Why This Approach?
### The SAR Challenge
SAR images suffer from "speckle noise" - a granular interference pattern unique to coherent radar imaging. Ships appear as bright clusters mixed with noise, making standard detection difficult.
### Speckle Filtering (The "Secret Sauce")
The Lee filter removes multiplicative radar noise while preserving ship edges:
[code block omitted]
### Why Oriented Bounding Boxes?
Ships sail in arbitrary directions. Axis-aligned boxes waste pixels and overlap:
[code block omitted]
## Sample Detection Results
| Single Ship | Multiple Ships | Complex Scene |
|:-----------:|:--------------:|:-------------:|
| | | |
## Project Structure
[code block omitted]
## Quick Start
### 1. Installation
[code block omitted]
### 2. Kaggle Setup
[code block omitted]
### 3. Download & Prepare Dataset
[code block omitted]
### 4. Train the Model
[code block omitted]
### 5. Run Inference
[code block omitted]
## Configuration
Edit `config/config.yaml` to customize:
[code block omitted]
## Model Variants
| Model | Size | Speed | Accuracy |
|-------|------|-------|----------|
| yolov8n-obb | 3.2M | Fastest | Good |
| yolov8s-obb | 11.2M | Fast | Better |
| yolov8m-obb | 25.9M | Medium | High |
| yolov8l-obb | 43.7M | Slow | Higher |
| yolov8x-obb | 68.2M | Slowest | Highest |
## API Usage
[code block omitted]
## Output Format
Detection results include:
- `corners`: 4 corner points of the rotated box
- `center`: Center coordinates
- `width`, `height`: Box dimensions
- `angle`: Rotation angle in degrees
- `confidence`: Detection confidence
## Dataset: SSDD
The SAR Ship Detection Dataset (SSDD) used in this project:
- **Source**: Kaggle - SARscope Maritime Images (https://www.kaggle.com/datasets/kailaspsudheer/sarscope-unveiling-the-maritime-landscape)
- **Train**: 4,716 images
- **Validation**: 1,346 images
- **Format**: COCO JSON (converted to YOLO OBB)
## Technical Details
### Lee Filter Algorithm
The Lee filter assumes multiplicative noise: `I = R × N`
[code block omitted]
Where:
- `μ` = local mean
- `σ²` = local variance
- `W` = adaptive weight (preserves edges)
### OBB Output Format
YOLO OBB format: `class x1 y1 x2 y2 x3 y3 x4 y4`
Four normalized corner coordinates defining the rotated rectangle.
## License
MIT License - see LICENSE (LICENSE) for details.
## Acknowledgments
- SSDD Dataset (https://www.kaggle.com/datasets/kailaspsudheer/sarscope-unveiling-the-maritime-landscape) creators
- Ultralytics (https://github.com/ultralytics/ultralytics) YOLOv8 team
- Jong-Sen Lee (Lee filter inventor, 1981)
```
