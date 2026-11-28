# GitHub 專案 05：kbhujbal/Trident-synthetic_aperture_radar_maritime_vessel_detection_yolov8

- 日期：2026-11-06
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
本專案提供一套生產級的海上監控系統，專門針對合成孔徑雷達（SAR）影像中的船隻進行偵測。系統結合 Lee speckle 濾波器去除雷達特有的乘法雜訊，並使用 YOLOv8‑OBB（Oriented Bounding Box）模型來偵測任意方向的船艦。目標使用者包括遙感研究人員、海事監控工程師、國防與海上安全相關單位，他們需要在高雜訊、船隻方向不固定的 SAR 影像中快速、準確地取得船隻位置與姿態。核心問題在於 SAR 影像的斑點噪聲會掩蓋船隻特徵，且傳統水平邊界框無法有效擬合旋轉的船體，導致偵測漏報或誤報。

## 技術
該專案以 Python 3 為主要開發語言，基於 PyTorch 框架與 Ultralytics 提供的 YOLOv8‑OBB 實作旋轉邊界框偵測模型。資料前處理採用 Lee speckle 濾波器（乘法噪聲模型 I = R × N）來降低 SAR 影像的雜訊同時保持邊緣資訊。訓練流程使用經過 COCO JSON 轉換為 YOLO OBB 格式的 SSDD 資料集（4,716 訓練、1,346 驗證影像），透過 config/config.yaml 調整超參數、濾波器窗口大小與模型尺寸（ yolov8n/s/m/l/x‑obb）。模型訓練與推論皆採用標準的 Ultralytics API，支援單張圖片與批次推論，輸出包含四個角點座標、中心、寬高、旋轉角度與信心度的 OBB 結果。此外，專案提供 Dockerfile 與腳本方便在 Kaggle 或本地 GPU 環境中快速部署。

## 架構
系統架構可分為四個主要階段：首先，原始 SAR 影像經過 Lee speckle 濾波器進行雜訊抑制，產生濾波後的灰度圖；其次，濾波後影像與對應的標註經過轉換工具產生 YOLO OBB 格式的資料集（類別、四個歸一化角點座標）；第三階段是模型訓練，使用 Ultralytics YOLOv8‑OBB 在 PyTorch 上進行前向傳播、損失計算（包含分類、回轉框回歸與置信度）與反向傳播，依據 config.yaml 中的超參數（學習率、批次大小、濾波器窗口等）進行優化；最後是推論階段，載入最佳權重對新影像先做 Lee 濾波，再喂入 YOLOv8‑OBB 模型，得到旋轉邊界框的四個角點、中心座標、寬高、角度與信心度，結果以 JSON 或文字檔案輸出。由於 README 未詳細說明後處理（如非極大值抑制、座標反歸一化）與模型導出步驟，此部分屬於合理推斷。

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
