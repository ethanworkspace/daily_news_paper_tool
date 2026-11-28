# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-11-20
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
Trident 是一個生產等級的海上監控系統，專門針對合成孔徑雷達（SAR）影像中的船隻進行偵測。系統結合 Lee speckle 濾波器去除雷達特有的乘法雜 noise，並使用 YOLOv8‑OBB（Oriented Bounding Box）模型來檢測任意方向的船艦。目標使用者包括海上監控分析師、遙感研究員、海岸防衛與國防單位，他們需要在高雜訊的 SAR 影像中快速、準確地定位船隻。核心問題在於 SAR 影像的 speckle 雜 noise 會使船隻呈現為噪點叢集，且船隻方向隨機，傳統水平邊界框難以有效捕捉。

## 技術
專案主要使用 Python 3、PyTorch 框架與 Ultralytics YOLOv8‑OBB 實作偵測模型。資料流程先以 Lee speckle 濾波器處理單通道 SAR 影像，假設觀測值 I = R × N，透過局部平均與變異數計算自適應權重以保留邊緣而抑制乾擾。濾波後的影像轉換為張量輸入 YOLOv8‑OBB，模型輸出四個歸一化角點（x1y1…x4y4）定義旋轉矩形，並附帶類別與信心分數。專案提供 config.yaml 供調整濾波參數、模型尺寸（n/s/m/l/x）與訓練超參數，並已將 SSDD 資料集轉換為 YOLO OBB 格式（COCO → YOLO）。

## 架構
系統架構可分為三個主要模組：(1) 前處理模組 — — 讀取 SAR 影像，套用 Lee speckle 濾波器以降低乘法雜 noise；(2) 偵測模組 — — 使用 YOLOv8‑OBB backbone（基於 Ultralytics 實作）對濾波後特徵圖進行前向傳播，產生旋轉邊界框預測；(3) 後處理模組 — — 將模型輸出的歸一化角點轉換為實際圖像座標，寬高、中心點與旋轉角度，並輸出包含 confidence 的 JSON 或 CSV。資料流為：原始 SAR 圖 → Lee 濾波 → 張量正規化 → YOLOv8‑OBB 前向推理 → 後處理座標轉換 → 最終偵測結果。README 未詳細說明模型內部結構或訓練循環細節，因此架構描述僅基於可見的資料流與模組說明。

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
