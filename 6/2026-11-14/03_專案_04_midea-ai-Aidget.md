# GitHub 專案 04：midea-ai/Aidget

- 日期：2026-11-14
- URL：https://github.com/midea-ai/Aidget
- 描述：Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources.
- Stars：186  |  Forks：33  |  Language：Python
- License：Apache-2.0
- Topics：asr, deep-learning, dsp, hifi5, inference, inference-engine, mcu, pruning, resrep, rtos, simd, tflm, wakeup
- 更新時間：2026-11-02T05:01:44+00:00
- 配對論文：
- 品質分數：4/10 [thin_readme]

## 在做什麼
Aidget（AI Edge Toolbox）是由美的集團開發的推理引擎，專門針對計算與記憶體資源受限的邊緣處理器（如 MCU）設計。其目標是讓深度學習模型（例如語音辨識、喚醒詞偵測）能在這類低功耗裝置上高效運行，提供模型壓縮、量化、剪枝、SIMD 優化以及與 RTOS 的整合等工具，使嵌入式軟體工程師或 IoT 產品開發者能在資源受限的平台上部署 AI 功能。

## 技術
專案主要使用 Python 進行工具鏈開發，可見的技術包括 TensorFlow Lite for Microcontrollers（tflm）作為推理後端、模型剪枝與量化（pruning、resrep）以減少參數與運算量、SIMD 指令集加速、針對 DSP/Hifi5 架構的優化內核、支援即時作業系統（RTOS）的任務調度介面、以及針對語音應用的 ASR 與喚醒（wakeup）功能模組。這些技術均來自專案標籤與簡介中可直接觀察到的內容。

## 架構
Aidget 的架構可大致分為三層：第一層是模型準備階段，負責載入原始深度學習模型並進行剪枝、量化、重新參數化（resrep）等優化，產生適合微控制器的 TensorFlow Lite 模型；第二層是程式碼產生與平台適配階段，根據目標 MCU 的指令集（SIMD）、DSP/Hifi5 特性生成對應的推理核心，並提供 RTOS 任務包裝介面，使模型能以執行緒或任務形式運行；第三層是執行階段，負責在設備上載入模型、進行輸入預處理（如語音特徵提取）、呼叫推理引擎執行前向計算，並輸出結果（如辨識文字或喚醒事件）。由於 README 摘錄內容有限，上述流程僅基於可見的技術標籤（asr, tflm, pruning, simd, rtos, hifi5, wakeup 等）進行合理推斷，未涉及未在文件中明確說明的具體效能數字或部署細節。

## README 摘錄（節選）
```text

```
