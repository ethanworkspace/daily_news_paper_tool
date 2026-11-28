# GitHub 專案 04：aavek/Aeolus-Ocean

- 日期：2026-11-28
- URL：https://github.com/aavek/Aeolus-Ocean
- 描述：An all-weather, day-and-night, collision avoidance simulator that can be implemented as a digital twin for the autonomous COLREG-compliant navigation of maritime vessels.
- Stars：68  |  Forks：5  |  Language：unknown
- License：BSD-3-Clause
- Topics：autonomous, autonomous-navigation, autonomous-vehicles, boat, collision-avoidance, colreg, computer-vision, graphics, jonswap, machine-learning, marine-robotics, ocean, reinforcement-learning, robotics, simulation, unity, unity3d, vessel, waves
- 更新時間：2026-11-27T06:39:42+00:00
- 論文層級：未對應論文（海事）
- 配對論文：https://arxiv.org/abs/2307.06688
- 品質分數：5/10 [no_language, paper_paired]

## 在做什麼
Aeolus-Ocean 是一個以 Unity 為基礎的海洋模擬環境，專為無人船舶（USV）在各種天候與光照條件下執行符合 COLREG 的自主航行與碰撞避讓而設計。使用深度強化學習（PPO）與模仿學習訓練智慧代理，結合 YOLO‑X 視覺偵測與模擬雷達，提供可作為數位雙胞胎的平台，讓船舶在航向航點時遵守海事規則、避開其他船艦、障礙物與陸地。

## 技術
專案使用 Unity 引擎與 C# 開發模擬環境，透過 Unity ML-Agents Toolkit 實作深度強化學習（PPO）與模仿學習訓練流程。視覺偵測採用 YOLO‑X（Megvii-BaseDetection/YOLOX）進行船舶偵測，並結合模擬雷達資料；海洋環境則以 JONSWAP、Pierson-Moskowitz 或 TMA 修正的波譜模型產生波浪，並搭配 Beaufort 1‑11 風級與海流模擬。陸地透過簡化的聲納類似系統與 Perlin Noise 生成的程序島嶼來表示。資料流程為：相機影像 → YOLO‑X 偵測 → 與雷達融合 → 代理觀測 → PPO 政策網路輸出舵機/推進指令 → Unity 物理引擎更新船體動態。

## 架構
系統主要分為四個模組：(1) 環境模擬器（Unity 場景），負責產生海浪（JONSWAP/Pierson-Moskowitz/TMA）、海流、風級、陸地（Perlin Noise 島嶼）與簡化聲納；(2) 感測器模組，包含船艦相機輸出給 YOLO‑X 進行目標偵測、模擬雷達產生方位與距離資料，以及聲納偵測陸地；(3) 代理觀測與決策模組，將視覺與雷達融合後的向量作為觀測輸入喂給 PPO 政策網路（ML-Agents），輸出舵角與推進指令；(4) 動力學與碰撞模組，利用 Unity 物理引擎計算船體受水力、推進力與環境力的作用，同時依據 COLREG 規則檢測並施加避讓行為。資料流程為：環境產生 → 感測器讀取 → 代理觀測 → 政策推論 → 指令送入船體 → 物理更新 → 回饋給環境。若使用者切換至手動模式，則鍵盤輸入直接覆寫代理指令。

## README 摘錄（節選）
```text
# Aeolus-Ocean
Aeolus Ocean - A simulation environment for the autonomous COLREG-compliant navigation of Unmanned Surface Vehicles using Deep Reinforcement Learning and Maritime Object Detection (http://arxiv.org/abs/2307.06688)
## Description
An all-weather, day-and-night, simulator that can be implemented as a digital twin for the autonomous navigation of maritime vessels as they attempt to reach waypoints while avoiding collisions with other vessels while respecting maritime collision regulations (COLREGs), obstacles and land.
The project consists of an ocean system (Beaufort 1-11) as well as physics algorithms that handle vessel-water interactions and propulsion. Each vessel has its own target acquisition systems. For Object Detection, cameras make use of YOLO-X (https://github.com/Megvii-BaseDetection/YOLOX) to visually locate other vessels on-screen and this data is fused with information extracted from a simulated radar system to detect all other vessels positional data in its environment. Land is detected with a simplified sonar-like system. The navigational guidance of each vessel is controlled by an intelligent Agent that has been trained (as single-agents in the proximity of other single-agents in multiple environments) over a range of different scenarios using Deep Reinforcement Learning (PPO) and Imitation Learning with Unity's Machine Learning Agents Toolkit (ML-Agents (https://github.com/Unity-Technologies/ml-agents)).
Currently, the project is available in binary form. It can be downloaded as a release (https://github.com/aavek/Aeolus-Ocean/releases/tag/v1.11). If there is enough interest in the current work, the source code may become available in the future.
## How to Run
Once you download the release (https://github.com/aavek/Aeolus-Ocean/releases/tag/v1.11), you can safely run the program with
[code block omitted]
. The binary is created directly from Unity's build settings, and Windows might ask you to trust it as it may come from an 'unknown publisher'.
By clicking on the "Simulation" tab in the main-menu you should be presented with the following setup menu.
### Simulation Setup
Each of the controllable setup parameters (default values shown) for the simulation are now described:
| **Environment Parameters** | Description |
| :---: | --- |
| Number of Environments | Number of environments agents will reach waypoints on. In the source code, this is used to train agents in parallel. |
| Agents Per Environment | Each environment will have this many agents in it. NOTE: (Number of Environments) x (Agents Per Environment) must not exceed 32. |
| Environment Spacing | Spacing in meters between consecutive environments. Environments are arranged so they fill, at maximum, a 4x4 grid. |
| Environment Enclosures | Whether to use walls that restrict travel between environments. In the source code, this can speed up training. |
| Ocean Current Factor | Slider that controls how strong ocean currents are in causing the vessel to drift off course. |
| Wave Spectrum | Choose a non-directional wave spectrum (Pierson-Moskowitz, JONSWAP or JONSWAP with Texel MARSEN ARSLOE (TMA) correction). In each case, we use the Hasselmann Directional Spreading function. |
| **Waypoint Parameters** | Description |
| :---: | --- |
| Waypoint Change Distance | Distance in meters to a waypoint that, when reached, causes a new waypoint to be spawned for the current Agent. |
| Show Waypoint Markers | Whether to show graphics for waypoint markers and navigational arrows. |
| Minimum Waypoint Spawn | Minimum distance beyond which a waypoint will spawn from the Environment center as a percentage of the Environment Spacing. This can exceed 1 if you want waypoints to extend beyond the current environment. |
| Maximum Waypoint Spawn | Maximum distance up to which a waypoint will spawn from the Environment center as a percentage of the Environment Spacing. This can exceed 1 for waypoints beyond the current environment. Must be larger than the minimu
```
