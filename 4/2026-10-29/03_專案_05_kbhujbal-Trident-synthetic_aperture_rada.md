# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-10-29
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
本專案提供一套生產等級的海上監控系統，專門針對合成孔徑雷達（SAR）影像中的船隻進行偵測。系統結合 Lee speckle 濾波器去除雷達特有的乘法雜訊，並使用 YOLOv8‑OBB（Oriented Bounding Box）模型偵測任意方向的船艦。目標使用者為海上監控人員、遙感研究者、海巡與國防單位，核心問題在於 SAR 影像的斑點噪聲與船艦方向不固定導致傳統偵測方法失效。

## 技術
專案以 Python 為主要開發語言，基於 PyTorch 框架與 Ultralytics YOLOv8‑OBB 實現旋轉邊界框偵測。資料流程包括載入 SAR 影像、應用 Lee 濾波器（假設乘法噪聲模型 I = R × N）進行 speckle 去噪，然後送入 YOLOv8‑OBB 進行訓練或推論。模型支援多種規模（n、s、m、l、x），可透過 config/config.yaml 調整超參數、資料路徑與訓練設定。訓練使用 SSDD 資料集（COCO 格式轉換為 YOLO OBB），並提供 Kaggle 下載與預處理腳流程。

## 架構
系統架構可分為三個主要模組：前處理模組負責讀取 SAR 影像並執行 Lee speckle 濾波，以減少乘法雜訊同時保留船隻邊緣；模型模組採用 YOLOv8‑OBB，輸出四個標準化角點（x1y1…x4y4）代表旋轉矩形，並附帶類別、寬高、中心點、角度與信心分數；後處理模組將模型輸出轉換為可讀的 JSON 格式，包含 corners、center、width、height、angle、confidence。資料流程為：原始 SAR 影像 → Lee 濾波 → YOLOv8‑OBB 推論/訓練 → 結果後處理 → 輸出偵測框。若 README 未詳細說明訓練循環與硬體需求，則此部分為基於可見內容的合理推斷。

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
