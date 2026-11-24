# 論文 05：Pruning random resistive memory for optimizing analog AI.

- 日期：2026-10-28
- 來源層級：Tier 1
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-01-10T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/41519952/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC12858861/
- DOI：10.1038/s41467-025-67960-6
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1154（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
The rapid expansion of AI models has intensified concerns over energy consumption. Analog in-memory computing with resistive memory offers a promising, energy-efficient alternative, yet its practical deployment is hindered by programming challenges and device non-idealities. Here, we propose a software-hardware co-design that trains randomly weighted resistive-memory neural networks via edge-pruning topology optimization. Software-wise, we tailor the network topology to extract high-performing sub-networks without precise weight tuning, enhancing robustness to device variations and reducing programming overhead. Hardware-wise, we harness the intrinsic stochasticity of resistive-memory electroforming to generate large-scale, low-cost random weights. Implemented on a 40 nm resistive memory chip, our co-design yields accuracy improvements of 17.3% and 19.9% on Fashion-MNIST and Spoken Digit, respectively, and a 9.8% precision-recall AUC improvement on DRIVE, while reducing energy consumption by 78.3%, 67.9%, and 99.7%. We further demonstrate broad applicability across analog memory technologies and scalability to ResNet-50 on ImageNet-100.

## 背景與目的
隨著 AI 模型規模快速擴大，能耗問題日益嚴峻。類比記憶體內運算利用電阻式記憶體（RRAM）可大幅降低能量消耗，但實際部署受限於程式化困難與器件非理想特性。本文旨在提出軟硬體協同設計，透過邊緣剪枝拓撲優化訓練隨機權重的電阻式記憶體神經網路，解決精確權重調整與程式化開銷大的缺口，提升對器件變異的魯棒性並降低能耗。

## 方法
問題設定：輸入為原始資料（影像、語音等），輸出為分類或檢測結果。整體架構採用隨機加權的電阻式記憶體神經網路，硬體端利用電阻式記憶體電成形（electroforming）的本質隨機性，直接產生大規模、低成本的隨機權重，避免精密程式化。軟體端引入邊緣剪枝拓撲優化，從隨機權重網路中搜尋並保留高性能子網路，無需微調權重即可獲得良好表現，增強對器件變異的容忍度並減少程式化開銷。核心模組包含：(1) 隨機權重生成模組，利用電成形隨機性；(2) 拓撲剪枝演算法，根據邊緣重要性移除冗餘連結；(3) 推理流程，僅在保留的子網路上進行類比矩陣向量乘法。訓練目標與損失函數、最佳化策略、資料前處理與特徵表示等細節在摘錄中未說明。與既有方法的關鍵差異在於結合硬體隨機權重生成與軟體拓撲剪枝，實現免精確程式化的類比推理。

## 結果
在 40 nm 電阻式記憶體晶片上實測：Fashion-MNIST 準確率提升 17.3%，Spoken Digit 提升 19.9%，DRIVE 精確率-召回率 AUC 提升 9.8%。能耗分別降低 78.3%、67.9% 與 99.7%。另展示跨類比記憶體技術的通用性，並能擴展至 ResNet-50 在 ImageNet-100 上的實驗。摘錄未提供更多基線模型名稱、詳細數值或統計顯著性分析。

## 限制與展望
摘錄缺乏訓練超參數、損失函數、優化器、資料增強、剪枝比率、硬體變異模型等關鍵實驗細節，無法評估方法在不同噪聲條件、大規模資料集或即時推理延遲下的表現。僅在三個基準測試呈現結果，缺少與主流數位或類比基線的全面比較。器件層面的長期可靠度、溫度漂移、製程變異對隨機權重分布的影響未討論。後續研究需補充完整實驗設定、擴大基線比較、探討大規模部署的系統級能耗與面積權衡。
