# GitHub 專案 03：tsinghua-fib-lab/LLM_for_Polarization

- 日期：2026-10-19
- URL：https://github.com/tsinghua-fib-lab/LLM_for_Polarization
- 描述：Official implementation for “Emergence of polarization in networks of large language model agents”
- Stars：14  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-19T07:10:21+00:00
- 配對論文：https://doi.org/10.1038/s41467-026-78228-y
- 品質分數：8/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
此專案模擬大型語言模型（LLM）代理在社交網路中的互動，研究其如何導致觀點極化（polarisation）。目標使用者為計算社會科學、AI 安全與政策研究者，旨在提供可重現的實驗平台，以探討代理間的訊息傳遞、狀態更新與網路結構對極化現象的影響。

## 技術
專案主要以 Python 實作，包含 run.py（模擬入口）、simulate.py（基線模擬）、simulate_debiased.py（去偏模擬）與 utils.py（LLM 提示與工具函式）。LLM 呼叫透過 OpenAI API 進行，需在 utils.py 中設定 API 金鑰與模型參數。繪圖部份依賴 pandas、numpy、matplotlib 與 seaborn，讀取 CSV 與 pickle 形式的儲存資料，產出 PDF 圖表。

## 架構
架構上，run.py 作為執行入口，會載入 source_data 中的網路初始化檔案（edges.csv、data_ID2Net_ID.csv、user_message_generate.json）以及對應議題的 epoch-level 互動資料（pkl）。接著呼叫 simulate.py（或 simulate_debiased.py）進行代理狀態更新的迭代過程；每一步中，utils.py 負責構造提示、呼叫 LLM 取得回應，並根據回應更新 source 與 target node 的 opinion state（-2 至 2）。模擬結果會被寫入暫存的 DataFrame，之後可由 figures/* 下的 Jupyter notebook 讀取本地 CSV 數據，繪製主要圖表與補充資訊的 PDF。由於 README 未提供細部類別圖或模組依賴圖，上述流程為基於檔案說明的合理推斷。

## README 摘錄（節選）
```text
# LLM for Polarization
Code and data for **Emergence of polarization in networks of large language model agents**, in principle accepted by *Nature Communications*.
This repository contains the simulation code, source data, and curated figure data/code used for the main-text and Supplementary Information figures.
## Repository Structure
- `run.py`: example entry point for launching a simulation.
- `simulate.py`: baseline simulation code.
- `simulate_debiased.py`: self-regulated/debiased simulation code.
- `utils.py`: LLM prompting and simulation utilities.
- `source_data/`: network initialization files and source interaction data.
- `figures/figure1` to `figures/figure4`: main-text figure data, plotting notebooks, and generated panel PDFs.
- `figures/SI`: Supplementary Information result tables, plotting notebook, and generated panel PDFs.
## Source Data
`source_data/Data_WS_2000/` contains the original network initialization files used by the simulation code:
- `edges.csv`
- `data_ID2Net_ID.csv`
- `user_message_generate.json`
`source_data/Partisan Alignment/`, `source_data/Gun Control/`, and `source_data/Abortion Ban/` contain epoch-level interaction data for the three main topics. Each `epoch_run*.pkl` file is a pandas DataFrame where each row is a directed interaction with:
- `source node Id`
- `target node Id`
- `source node state`
- `target node state`
Opinion states are coded from `-2` to `2`. See `source_data/README.md` and `source_data/metadata.csv` for details.
## Figure Data and Code
Each figure folder includes a plotting notebook, minimal CSV data, and generated panel PDFs:
- `figures/figure1/figure1_codes.ipynb`
- `figures/figure2/figure2_codes.ipynb`
- `figures/figure3/figure3_codes.ipynb`
- `figures/figure4/figure4_codes.ipynb`
- `figures/SI/SI_codes.ipynb`
The main-text figure notebooks are designed to be run from their own folders, reading local files from `data/` and writing PDFs to `output/`. The SI notebook reads local files from `figures/SI/data/` and writes PDFs to `figures/SI/figures/`.
The curated data files are aggregated result tables for the plotted panels. They are intended to cover the figure outputs, while the epoch-level source interaction data for the three main topics are kept under `source_data/`.
## Environment
The original simulation environment used:
[code block omitted]
For plotting the curated figure notebooks, a modern Python environment with `pandas`, `numpy`, `matplotlib`, and `seaborn` is sufficient.
## Installation
[code block omitted]
To run simulations, configure your OpenAI API key and model settings in `utils.py`.
## Running the Demo Simulation
`run.py` provides an example configuration for the Partisan Alignment setting. By default, it uses:
[code block omitted]
Run:
[code block omitted]
For a network with around 4,000 relationships and 1,000 agents, a full simulation may take several hours depending on model latency and API tier.
## Drawing Main-Text Figures
Run a figure notebook from its folder. For example:
[code block omitted]
The same pattern applies to `figure2`, `figure3`, and `figure4`.
## Drawing Supplementary Figures
Run:
[code block omitted]
The SI folder includes grouped CSV files for SI panels derived from the original Figure 1, Figure 2, Figure 4, intervention, NC experiment, argument-extraction, and affection/perception notebooks. See `figures/SI/README.md` for the file groups.
## License
This project is licensed under the MIT License. See `LICENSE` for details.
```
