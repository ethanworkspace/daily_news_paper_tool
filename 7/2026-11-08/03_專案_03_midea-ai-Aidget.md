# GitHub 專案 03：midea-ai/Aidget

- 日期：2026-11-08
- URL：https://github.com/midea-ai/Aidget
- 描述：Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources.
- Stars：186  |  Forks：33  |  Language：Python
- License：Apache-2.0
- Topics：asr, deep-learning, dsp, hifi5, inference, inference-engine, mcu, pruning, resrep, rtos, simd, tflm, wakeup
- 更新時間：2026-11-02T05:01:44+00:00
- 配對論文：
- 品質分數：4/10 [thin_readme]

## 在做什麼
Aidget（AI Edge Toolbox）是美的集團為資源受限的邊緣處理器設計的推理引擎，目標是讓物聯網設備、智慧家電等嵌入式系統能在極低的計算與記憶體預算下執行深度學習模型，主要服務於需要即時語音喚醒、語音識別或其他感知任務的開發者與產品工程師。

## 技術
專案主要使用 Python 進行建置、模型轉換與工具鏈開發；核心推理引擎基於 TensorFlow Lite Micro（tflm），支援模型剪枝（pruning）、量化與稀疏化，以減少模型大小與計算量；利用 SIMD 指令集與 DSP/HiFi5 硬體加速進行向量運算；提供 RTOS 抽象層與 MCU 驅動，使引擎能在 FreeRTOS、Zephyr 等實時作業系統上運行；此外，還內建語音喚醒（wakeup）與自動語音識別（ASR）範例，示範如何將深度學習模型部署到資源受限的邊緣設備。

## 架構
根據 README 摘錄未提供完整細節，架構描述僅根據可見 Topics 進行合理推斷。Aidget 大致可分為四層：(1) 模型優化前端，負責讀取 TensorFlow/Keras 模型，進行剪枝、量化與轉換為 TFLM 格式；(2) 推理執行階段，包含張量運算核心、SIMD/DSP 加速內核與記憶體管理器，專為 MCU 級別的快取與堆疊限制設計；(3) 硬體抽象層（HAL），針對不同 MCU、DSP 或 HiFi5 晶片提供統一的介面，處理時鐘、中斷與 DMA；(4) 作業系統與應用層，提供 RTOS 任務調度範例、唤醒詞偵測與 ASR 管線的範例程式，開發者可在此基礎上實作具體功能。由於原始 README 未說明具體模組名稱或資料流，以上描述僅為基於 Topics 的合理推論。

## README 摘錄（節選）
```text

```
