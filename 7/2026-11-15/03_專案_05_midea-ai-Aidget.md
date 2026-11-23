# GitHub 專案 05：midea-ai/Aidget

- 日期：2026-11-15
- URL：https://github.com/midea-ai/Aidget
- 描述：Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources.
- Stars：186  |  Forks：33  |  Language：Python
- License：Apache-2.0
- Topics：asr, deep-learning, dsp, hifi5, inference, inference-engine, mcu, pruning, resrep, rtos, simd, tflm, wakeup
- 更新時間：2026-11-02T05:01:44+00:00
- 配對論文：
- 品質分數：4/10 [thin_readme]

## 在做什麼
Aidget 是美的集團針對資源受限的邊緣處理器（如 MCU、DSP）所開發的推論引擎工具箱，主要服務於需要在設備端執行語音喚醒、語音識別（ASR）或其他深度學習任務的嵌入式開發者與產品工程師。它的目標是解決這類設備在計算能力、記憶體與功耗上的瓶頸，提供經過剪枝、SIMD 優化以及適配 RTOS 的輕量級推論框架，使模型能在毫瓦級功耗下完成即時推論。

## 技術
專案主要使用 Python 進行建置與腳本開發，核心推論引擎基於 TensorFlow Lite Micro（tflm）實現，支援深度學習模型的離線推論。透過模型剪枝（pruning）與 SIMD 指令向量化，降低運算量與記憶體佔用；同時針對 MCU/DSP 平台提供 RTOS 友善的介面，並整合 HIFI5 DSP 的加速庫。專案涵蓋語音喚醒（wakeup）、語音識別（ASR）等常見邊緣 AI 應用的範例與工具鏈。

## 架構
根據 README 摘錄未提供詳細架構說明，僅從專案描述與 Topics 推斷：Aidget 可能包含（1）模型轉換與優化階段（將訓練好的 TensorFlow/Keras 模型經過剪枝、量化後轉為 TFLite Micro 格式）；（2）引擎執行階段（載入 TFLite Micro 模型，透過 SIMD 優化的核心運算子在 MCU/DSP 上執行推論）；（3）平台適配層（針對不同 RTOS、HIFI5 DSP 或通用 MCU 提供抽象介面，負責記憶體管理、中斷與任務調度）；（4）應用範例層（提供語音喚醒、ASR 等 demo，示範如何在資料流中接收音訊、進行前處理、呼叫推論引擎並輸出結果）。由於缺少原始 README，以上架構僅為基於可見技術主題的合理推斷，實際結構可能有所不同。

## README 摘錄（節選）
```text

```
