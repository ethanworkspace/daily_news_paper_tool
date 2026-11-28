# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-11-18
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
Trident 是一套用於合成孔徑雷達（SAR）影像中偵測海上船艦的生產等級監控系統，結合 Lee 斑點噪聲濾波與 YOLOv8‑OBB（定向邊界框）模型。其目標使用者為海上監控單位、遙感研究人員及國防單位，核心問題在於 SAR 影像乘法性斑點噪聲與船艦任意方向導致傳統水平框偵測效果不佳，Trident 透過噪聲抑制與旋轉框提升偵測準確度與實用性。

## 技術
技術採用 Python 3、PyTorch 與 Ultralytics YOLOv8‑OBB 實作，核心包含 Lee 斑點濾波器（假設乘法噪聲 I = R × N，自適應權重保邊緣）、資料前處理（濾波、正規化、轉換為 YOLO OBB 格式）、模型訓練與推論（支援 yolov8n/s/m/l/x‑obb 變體）、配置檔案（config.yaml）以及結果輸出（四個角點、中心、寬高、角度、信心度）。資料來源為 SSDD 資料集（COCO JSON 轉 YOLO OBB），訓練/驗證分別為 4,716 與 1,346 張影像。

## 架構
系統架構分為四個主要模組：1️⃣ 資料載入與前處理（讀取 SAR 影像、應用 Lee 濾波、正規化、轉換為 YOLO OBB 標註）；2️⃣ 模型層（YOLOv8‑OBB backbone + neck + head，負責旋轉框預測）；3️⃣ 訓練/評估腳本（依據 config.yaml 進行優化、學習率調度、損失計算與 mAP 評估）；4️⃣ 推論腳本（載入權重、對濾波後影像執行前向傳播、後處理非極大值抑制、輸出包含四個角點、中心、寬高、角度與信心度的 JSON/CSV）。資料流為：原始 SAR → Lee 濾波 → 正規化 → YOLOv8‑OBB 預測 → NMS → 結果後處理 → 輸出。若 README 未詳細說明訓練細節，則上述流程基於所述 pipeline、快速開始與模型變體描述進行合理推斷。

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
