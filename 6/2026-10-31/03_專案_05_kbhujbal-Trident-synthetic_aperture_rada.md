# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-10-31
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
本專案構建了一套生產等級的海上監控系統，專門針對合成孔徑雷達（SAR）影像中的船隻進行偵測。系統結合 Lee 斑點濾波器去除雷達特有的乘法雜噪，並使用 YOLOv8‑OBB（定向邊界框）模型來捕捉船隻的任意方向。目標使用者包括海上監控分析師、遙感研究員、海岸防衛與國防單位，核心問題在於 SAR 影像的斑點噪聲與船隻非水平姿勢導致傳統偵測方法失效。

## 技術
專案主要使用 Python 3、PyTorch 框架與 Ultralytics 提供的 YOLOv8‑OBB 實作。資料流程包括：下載 SSDD 資料集、將其轉換為 YOLO OBB 格式、應用 Lee 濾波器進行斑點噪聲抑制、訓練模型（支援 yolov8n/s/m/l/x 變體）以及進行推論。設定透過 config/config.yaml 調整，輸出包含旋轉框的四個角點、中心座標、寬高、角度與信心度。

## 架構
系統架構可劃分為四個主要模組：(1) 前處理模組負責讀取 SAR 影像並執行 Lee 斑點濾波，以減少乘法噪聲而保持邊緣資訊；(2) 資料載入模組讀取已轉換為 YOLO OBB 格式的 SSDD 資料集，並進行標準化與增強；(3) 模型採用 YOLOv8‑OBB 骨幹（基於 PyTorch），透過訓練迴圈學習船隻的定向邊界框表示；(4) 推論模組在濾波後影像上執行偵測，解析模型輸出的八個座標（四個角點）並計算中心、寬高、旋轉角度與信心度，最後以 JSON 或 CSV 形式輸出。由於 README 未提供詳細的類別圖或執行流程圖，上述架構推斷基於典型 YOLOv8 訓練/推論管道與專案所述組件。

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
