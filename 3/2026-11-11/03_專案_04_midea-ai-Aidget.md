# GitHub 專案 04：midea-ai/Aidget

- 日期：2026-11-11
- URL：https://github.com/midea-ai/Aidget
- 描述：Aidget (AI Edge Toolbox) is an inference engine developed by Midea Group for edge processors with limited compute and memory resources.
- Stars：186  |  Forks：33  |  Language：Python
- License：Apache-2.0
- Topics：asr, deep-learning, dsp, hifi5, inference, inference-engine, mcu, pruning, resrep, rtos, simd, tflm, wakeup
- 更新時間：2026-11-02T05:01:44+00:00
- 配對論文：
- 品質分數：4/10 [thin_readme]

## 在做什麼
Aidget 是由美的集團開發的 AI Edge Toolbox，主要提供一個適合計算與記憶體資源受限的邊緣處理器（如 MCU、DSP）的推論引擎。它針對語音喚醒、語音識別（ASR）以及其他深度學習任務，透過模型壓縮（剪枝、量化）與硬體加速（SIMD、DSP、HiFi5）來實現低延遲、低功耗的即時推論。目標使用者為嵌入式系統開發者、物聯網產品工程師以及需要在資源受限設備上部署 AI 模型的研究人員。

## 技術
專案主要使用 Python 實作工具鏈與腳本，支援 TensorFlow Lite Micro（tflm）作為基礎推論框架，並整合模型剪枝（pruning）與量化技術以降低模型大小與計算量。利用 SIMD 指令集與 DSP（如 HiFi5）進行向量化運算，以提升在 MCU/RTOS 環境下的執行效率。此外，專案提供喚醒詞偵測（wakeup）與 ASR 前處理模組，示範如何在即時語音流上完成特徵提取與推論。

## 架構
根據 README 摘錄與專案 Topics，可推斷 Aidget 的架構包含以下幾個主要模組：(1) 模型優化管線，負責進行剪枝、量化及格式轉換，將訓練好的模型轉為適合 TensorFlow Lite Micro 的格式；(2) 推論執行引擎，內含針對 SIMD、DSP 與 HiFi5 硬體加速的核心函式庫，負責在 MCU/RTOS 平台上執行模型推論；(3) 系統整合層，提供記憶體管理、任務排斷及介面適配，使引擎能在各種 RTOS（如 FreeRTOS）或裸金屬環境中運行；(4) 前端處理模組，包括喚醒詞偵測與語音特徵提取（如 MFCC、濾波器組），將原始音訊轉為引擎可接受的輸入。由於 README 未提供詳細圖表或流程說明，上述架構推斷僅基於可見的技術標籤與典型邊緣推論工具箱的設計原則。

## README 摘錄（節選）
```text

```
