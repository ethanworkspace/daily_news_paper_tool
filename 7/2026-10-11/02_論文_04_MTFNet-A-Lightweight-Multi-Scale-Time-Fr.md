# 論文 04：MTFNet: A Lightweight Multi-Scale Time-Frequency Neural Network for Multi-Class Event Recognition in DAS-Based Perimeter Security.

- 日期：2026-10-11
- 來源層級：Tier 2
- 期刊/會議/來源：Sensors (Basel, Switzerland)
- Venue：Sensors (Basel, Switzerland)
- 發布時間：2026-10-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42944260/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13708884/
- DOI：10.3390/s26206398
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1761（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Distributed Acoustic Sensing (DAS) has emerged as a pivotal technology for perimeter security. However, existing DAS event recognition methods have inherent limitations. Single-domain modeling has limited feature representation, while conventional multi-domain fusion methods require converting one-dimensional signals into two-dimensional images. This conversion adds computational overhead and may discard part of the original phase and amplitude information. In addition, the robustness of lightweight recognizers under low signal-to-noise ratio (SNR) conditions remains insufficiently examined. This paper proposes a lightweight multi-scale time-frequency network (MTFNet) for direct processing of one-dimensional DAS signals. The model adopts a parallel time-frequency dual-branch architecture. The time-domain branch utilizes a lightweight 1D Inception-ResNet variant to capture short-term impulse features and long-range temporal dependencies via multi-scale parallel convolutions and residual connections. The frequency-domain branch performs multi-scale segmented spectral analysis to extract complementary discriminative information at diverse time and frequency resolutions, followed by a lightweight attention-free fusion module for effective time-frequency feature fusion. Experimental results on a self-built dataset covering Wind, Facility Noise, Hammering, Sawing, and Walking events show that MTFNet achieves a recognition accuracy of 99.55% with 0.12 M parameters, outperforming SVM, 1D-CNN, TCN, MS 1D-CNN, CNN-BiLSTM, and attention-based multimodal fusion methods. It maintains an accuracy of 94.06% at an SNR of 0 dB, demonstrating its robustness against additive white Gaussian noise (AWGN) and practical engineering application potential.

## 背景與目的
本研究針對分散式聲學感測（DAS）在周界安防應用中，現有單域建模特徵表達有限，傳統多域融合需將一維訊號轉為二維影像，增加計算開銷且可能損失相位與振幅資訊，且輕量化模型在低訊雜比（SNR）下的魯棒性尚未充分驗證等問題。提出輕量化多尺度時頻網路（MTFNet），直接處理一維 DAS 訊號，旨在以極少參數量實現高精度多類別事件辨識，並強化低 SNR 環境下的表現。

## 方法
MTFNet 採用平行時頻雙分支架構，直接處理一維 DAS 原始訊號。時域分支為輕量化 1D Inception-ResNet 變體，包含多尺度平行卷積核（如 1×1、3×3、5×5 等）與殘差連結，可同步擷取短時衝激特徵與長距時序相依性。頻域分支執行多尺度分段頻譜分析，將訊號分段並以不同窗長進行短時傅立葉變換（STFT）或類似頻譜估計，獲得多解析度時頻表示，提取互補判別資訊。雙分支輸出特徵經由輕量化無注意力融合模組（如逐元素加權或串接後經 1×1 卷積）進行有效時頻特徵融合，避免傳統方法將一維訊號轉為二維影像所帶來的計算開銷與相位、振幅資訊損失。整體模型參數量僅 0.12 M，屬極輕量化設計，適合邊緣部署。摘錄未提及具體損失函數、優化器或訓練超參數。

## 結果
實驗於自建資料集（含 Wind、Facility Noise、Hammering、Sawing、Walking 五類事件）進行。MTFNet 以 0.12 M 參數量達 99.55% 辨識準確率，優於 SVM、1D-CNN、TCN、MS 1D-CNN、CNN-BiLSTM 及注意力型多模態融合等基線。在 SNR 0 dB 的加性白高斯雜訊（AWGN）下仍保持 94.06% 準確率，展現較強抗雜訊魯棒性與工程應用潛力。摘錄未提供混淆矩陣、各類別 F1 分數、訓練時間或推論延遲等細節數字。

## 限制與展望
主要限制：僅於自建五類別資料集驗證，資料多樣性與規模未揭露；雜訊測試僅含 AWGN，缺乏非平穩雜訊、多路徑干擾等真實場景驗證；未報告推論延遲、記憶體佔用及邊緣部署實測；缺乏與更多輕量化 SOTA 模型比較；跨光纖長度、不同佈設環境的泛化能力未探討。後續可擴充資料集、引入多樣雜訊、進行實時部署評估並分析可解釋性。
