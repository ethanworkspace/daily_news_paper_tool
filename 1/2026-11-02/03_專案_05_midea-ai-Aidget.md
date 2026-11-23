# GitHub 專案 05：midea-ai/Aidget

- 日期：2026-11-02
- URL：https://github.com/midea-ai/Aidget
- 描述：Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources.
- Stars：186  |  Forks：33  |  Language：Python
- License：Apache-2.0
- Topics：asr, deep-learning, dsp, hifi5, inference, inference-engine, mcu, pruning, resrep, rtos, simd, tflm, wakeup
- 更新時間：2026-11-02T05:01:44+00:00
- 配對論文：
- 品質分數：4/10 [thin_readme]

## 在做什麼
本專案名為 Aidget（AI Edge Toolbox），由美的集團開發，針對計算與記憶體資源受限的邊緣處理器（如 MCU）提供輕量級推論引擎。其目標使用者為嵌入式 AI 開發者與物聯網產品工程師，旨在解決深度學習模型在低功耗、低資源硬體上難以直接執行的問題，透過模型壓縮、指令集優化與硬體加速等技術，使語音喚醒、ASR 等應用能在資源受限的端側設備上實現低延遲推論。

## 技術
技術上，Aidget 以 Python 作為腳本與工具鏈語言，核心推論引擎則 likely 使用 C/C++ 實作，以支援 TensorFlow Lite for Microcontrollers（TFLM）模型格式。專案主題涵蓋語音識別（ASR）、深度學習、數位訊號處理（DSP）、Hifi5 DSP 架構、模型剪枝（pruning）、重新參數化（resrep）、即時作業系統（RTOS）整合、SIMD 指令向量化以及喚醒詞偵測（wakeup）。這些顯示其透過模型壓縮、硬體加速與指令集優化來達到在低資源 MCU 上的高效推論。

## 架構
由於提供的 README 摘錄內容不足，無法直接從文件中確定 Aidget 的具體模組劃分與資料流程。僅根據專案主題可推斷，其架構可能包含模型載入與 TFLM 解析階段、模型剪枝與重新參數化模組、SIMD 優化的核心運算核心、DSP/Hifi5 加速單元、RTOS 任務調度與唤醒詞偵測流程，但這些僅為基於主題的推論，實際架構仍需參考完整原始碼或文件方能確認。

## README 摘錄（節選）
```text

```
