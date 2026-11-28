# GitHub 專案 05：gy65896/DeepSORVF

- 日期：2026-11-28
- URL：https://github.com/gy65896/DeepSORVF
- 描述：[TITS 2023] Method-Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways
- Stars：65  |  Forks：13  |  Language：Jupyter Notebook
- License：CC0-1.0
- Topics：ais, data-fusion, detection, multi-model, pytorch, tracking, video
- 更新時間：2026-11-23T08:43:19+00:00
- 論文層級：未對應論文（海事）
- 配對論文：
- 品質分數：7/10 [implementation_signals]

## 在做什麼
DeepSORVF 是一種基於深度學習的簡易線上即時船舶資料融合方法，主要目標是將 AIS 與影像來源的船舶軌跡進行異步匹配，進而融合 AIS 資訊與視覺目標，以提升內陸水域船舶交通監控的準確度與穩定性。該方法同時提出一種先驅知識驅動的反遮蔽技術，在遮蔽情境下仍能提供可靠的船舶追蹤結果。適用於從事海事監測、 multimodal 資料融合、船舶偵測與追蹤研究的學者與工程師。

## 技術
專案以 Python 3.7 為基礎，使用 PyTorch 1.13.1 與 CUDA 11.7 進行深度學習模型訓練與推論。偵測階段採用 YOLOX（權重 YOLOX-final.pth），追蹤則基於 DeepSORT（需 ckpt.t7 權重）。資料處理方面引用 easydict、geopy、pyproj、fastdtw、pandas 與 numpy 進行座標轉換、軌跡匹配與統計。核心融合模組為一個深度學習網路，實現異步軌跡匹配；此外，結合 AIS 與影像的運動特徵提出先驅知識驅動的反遮蔽方法，以提升遮蔽場景下的追蹤穩定性。

## 架構
系統流程可分為三個主要階段：首先，從輸入的影片與 AIS 日誌分別提取特徵——影片經 YOLOX 偵測船體目標，再由 DeepSORT 追蹤取得 video‑based 軌跡；AIS 資料則經 geopy/pyproj 轉換為經緯度軌跡。其次，將兩種軌跡送入深度學習的異步軌跡匹配網路，透過時間對齊與特徵融合產出對應的船舶身份與狀態。最後，利用先驅知識驅動的反遮蔽模組，結合 AIS 與影像的運動特徵（速度、方向等）對被遮蔽目標進行修正，輸出最終的融合追蹤結果。整個流程在 main.py 中協調運行，可透過 draw_org.py 視覺化 AIS 軌跡（藍線）、偵測框（紅框）與融合結果（黑字)。由於 README 未提供詳細網路結構圖，上述架構推斷基於所述模組與流程描述。

## README 摘錄（節選）
```text
# [TITS 2023] DeepSORVF: Deep Learning-based Simple Online and Real-Time Vessel Data Fusion Method
(https://ieeexplore.ieee.org/abstract/document/10159572)
(https://gy65896.github.io/projects/TITS2023_DeepSORVF/index.html)
(https://github.com/gy65896/FVessel)
(README_zh-CN.md)
(https://www.python.org/)
(https://pytorch.org/)
--- 
>** Asynchronous Trajectory Matching-Based Multimodal Maritime Data Fusion for Vessel Traffic Surveillance in Inland Waterways**
> Yu Guo (https://scholar.google.com/citations?user=klYz-acAAAAJ&hl=zh-CN), Ryan Wen Liu (http://mipc.whut.edu.cn/index.html) * , Jingxiang Qu (https://scholar.google.com/citations?user=9zK-zGoAAAAJ&hl=zh-CN), Yuxu Lu (https://scholar.google.com/citations?user=XXge2_0AAAAJ&hl=zh-CN), Fenghua Zhu * , Yisheng Lv
> (* Corresponding Author)
> IEEE Transactions on Intelligent Transportation Systems
> **Introduction:** *In this work, we first extract the AIS- and video-based vessel trajectories, and then propose a deep learning-enabled asynchronous trajectory matching method (named DeepSORVF) to fuse the AIS-based vessel information with the corresponding visual targets. In addition, by combining the AIS- and video-based movement features, we also present a prior knowledge-driven anti-occlusion method to yield accurate and robust vessel tracking results under occlusion conditions.*
## Flowchart
The architecture of the proposed deep learning-based simple online and real-time vessel data fusion method.
The flowchart of anti-occlusion tracking method for video-based vessel trajectory extraction.
## Environment
* Python3.7
* easydict 1.11
* geopy 2.4.1
* pyproj 3.2.1
* fastdtw 0.3.4
* pytorch 1.13.1
* cuda 11.7
* pandas 1.3.5
* numpy 1.21.6
## Running
* Save ckpt.t7 (https://drive.google.com/file/d/1QdIP5TEDALJnnpqwjXwvL1J_GoseTK9D/view?usp=share_link) to `DeepSORVF/deep_sort/deep_sort/deep/checkpoint/` folder.
* Save YOLOX-final.pth (https://drive.google.com/file/d/1mhah7ZzP8oAUuSMR96Or9UvqkXe-AMuS/view?usp=share_link) to `DeepSORVF/detection_yolox/model_data/` folder.
* Set data dir by `parser.add_argument("--data_path", type=str, default = './clip-01/', help='data path')`.
* Run `main.py`.
#### `draw_org.py` is used to simultaneously visualize the ais-based trajectory (blue line), target detection box (red box), and fusion results (black text). It can be enabled by modifying `import draw` in `main.py` to `import draw_org`.
#### Test Data: clip-01 (https://drive.google.com/file/d/1Bns1jAW1ImL-FeCQBvIUcrO0hjYLIB5K/view?usp=share_link)
## FVessel: Benchmark Dataset for Vessel Detection, Tracking, and Data Fusion
The FVessel (https://github.com/gy65896/FVessel) benchmark dataset is used to evaluate the reliability of AIS and video data fusion algorithms, which mainly contains 26 videos and the corresponding AIS data captured by the HIKVISION DS-2DC4423IW-D dome camera and Saiyang AIS9000-08 Class-B AIS receiver on the Wuhan Segment of the Yangtze River. To protect privacy, the MMSI for each vessel has been replaced with a random number in our dataset. As shown in Figure 1, these videos were captured under many locations (e.g., bridge region and riverside) and various weather conditions (e.g., sunny, cloudy, and low-light).
Some samples of the FVessel dataset, which contains massive images and videos captured on the bridge region and riverside under sunny, cloudy, and low-light conditions.
## Performance on FVessel_V1.0 (https://github.com/gy65896/FVessel)
|Name|MOFA (%)|IDP (%)|IDR (%)|IDF (%)
| :-: | :-: | :-: | :-: | :-: |
video-01 (https://github.com/gy65896/DeepSORVF/assets/48637474/a3d4a688-e97b-4fdf-b0be-ecc536e41134)|79.94|89.35|90.76|90.05
video-02 (https://github.com/gy65896/DeepSORVF/assets/48637474/d52b4388-aa8f-4293-9898-2a7913d600df)|73.19|83.27|91.60|87.23
video-03 (https://github.com/gy65896/DeepSORVF/assets/48637474/182ae077-dc8f-4773-bb04-499aa0eee90e)|96.45|99.23|97.20|98.20
video-04 (https://github.com/gy65896/DeepSORVF/assets/48637474/1509e058-fa36-4cfd-8cd5-c00d12a
```
