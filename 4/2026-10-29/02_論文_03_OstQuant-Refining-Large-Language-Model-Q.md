# 論文 03：OstQuant: Refining Large Language Model Quantization with Orthogonal and Scaling Transformations for Better Distribution Fitting

- 日期：2026-10-29
- 來源層級：Tier 3
- 期刊/會議/來源：ArXiv
- Venue：International Conference on Learning Representations
- 發布時間：2025-01-23T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/fbfa1d0ec0074478311196fc667cb7bae276c8f1
- PDF：
- DOI：10.48550/arxiv.2501.13987
- arXiv：2501.13987
- 影響指標：N/A (preprint)
- 影響指標來源：preprint (not peer-reviewed journal/conference)
- 引用數：117
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2501.13987
- 全文字數：89282（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/BrotherHappy/OSTQuant
- 配對 Repo：BrotherHappy/OSTQuant

## 摘要
Post-training quantization (PTQ) has emerged as a widely adopted technique for compressing and accelerating Large Language Models (LLMs). The major challenge in LLM quantization is that uneven and heavy-tailed data distributions can expand the quantization range, thereby reducing bit precision for most values. Recent methods attempt to eliminate outliers and balance inter-channel differences by employing linear transformations; however, they remain heuristic and are often overlook optimizing the data distribution across the entire quantization space.In this paper, we introduce Quantization Space Utilization Rate (QSUR), a novel metric that effectively assesses the quantizability of transformed data by measuring the space utilization of the data in the quantization space. We complement QSUR with mathematical derivations that examine the effects and limitations of various transformations, guiding our development of Orthogonal and Scaling Transformation-based Quantization (OSTQuant). OSQuant employs a learnable equivalent transformation, consisting of an orthogonal transformation and a scaling transformation, to optimize the distributions of weights and activations across the entire quantization space. Futhermore, we propose the KL-Top loss function, designed to mitigate noise during optimization while retaining richer semantic information within the limited calibration data imposed by PTQ. OSTQuant outperforms existing work on various LLMs and benchmarks. In the W4-only setting, it retains 99.5\% of the floating-point accuracy. In the more challenging W4A4KV4 configuration, OSTQuant reduces the performance gap by 32\% on the LLaMA-3-8B model compared to state-of-the-art methods. \href{https://github.com/BrotherHappy/OSTQuant}{https://github.com/BrotherHappy/OSTQuant}.

## 背景與目的
大型語言模型（LLM）部署面臨記憶體與計算龐大需求，離線量化（PTQ）成為主流壓縮加速技術。然而權重與激活分布呈現不均勻、重尾特性，導致量化範圍擴大、有效位精度下降。現有方法（如 SmoothQuant、Quarot）採用線性變換消除離群值、平衡通道差異，但屬啟發式且未針對整個量化空間優化分布。本文提出量化空間利用率（QSUR）度量可量化性，並推導數學分析各變換效果與限制，進而發展 OSTQuant，旨在透過可學習等價變換全域優化分布，提升量化精度並保持泛化能力。

## 方法
方法核心包含三部分：(1) QSUR 指標：定義資料集合在量化超立方體空間中佔據體積比例，利用協方差矩陣特徵值分解計算橢球體積與量化空間體積，證明 QSUR 與量化精度正相關。(2) OSTQuant 架構：為每個全連接層分配一組可學習等價變換對——正交變換矩陣（約束於 Stiefel 流形）與縮放變換向量。正交變換調整特徵方向、平衡均值；縮放變換調整特徵值尺度、減小特徵值差異。兩者聯合優化權重與激活在整個量化空間的分布。優化過程中，變換對及其逆矩陣融合回原層，保持計算圖不變，避免區塊重建帶來的過擬合。(3) 損失與優化：針對 PTQ 校準資料稀少（如 1000 筆）問題，提出 KL-Top 損失，僅使用全精度模型輸出前 k 大機率 logits 計算 KL 散度，保留豐富語義並抑制長尾噪聲。優化器採用 RiemannAdam，利用一階資訊在 Stiefel 流形上更新正交矩陣。推論時僅需融合後的量化權重與激活，無額外開銷。

## 結果
實驗顯示 OSTQuant 在多種 LLM 與基準上優於現有方法。W4 僅量化權重設定下保留 99.5% 浮點精度；更具挑戰的 W4A4KV4 設定下，在 LLaMA-3-8B 上將效能差距較 SOTA 縮減 32%。W4A16 保留超過 99.5% 精度，W4A4KV4 維持至少 96% 原始效能。量化 LLaMA-3-8B 於 A800 GPU 僅需 20 分鐘。QSUR 正規化值與 Zero-Shot 精度保留率呈正相關，驗證指標有效性。摘錄未提供可驗證數字之詳細消融實驗數值。

## 限制與展望
依目前可取得資料，無法確認完整消融實驗與超參數敏感度分析。潛在限制包括：(1) 依賴小規模校準集（≤1000 筆），KL-Top 的 k 值選擇可能影響泛化；(2) 需在 Stiefel 流形上優化正交矩陣，訓練穩定性與收斂速度受 RiemannAdam 超參數影響；(3) 僅在 LLaMA 系列模型與 Zero-Shot 基準驗證，其他架構（如 MoE、多模態）效果未知；(4) 未提供實際硬體部署延遲與能耗測量；(5) 為預印本，尚未經同行審查。後續研究可探索更大校準集、硬體感知量化及擴展至其他模型家族。
