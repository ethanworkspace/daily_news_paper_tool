# 論文 02：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

- 日期：2026-11-10
- 來源層級：Tier 3
- 期刊/會議/來源：ArXiv
- Venue：ArXiv
- 發布時間：2025-11-28T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/4f5e2ad858550bbf00e905658115717e459499ea
- PDF：
- DOI：10.48550/arxiv.2511.23402
- arXiv：2511.23402
- 影響指標：N/A (preprint)
- 影響指標來源：preprint (not peer-reviewed journal/conference)
- 引用數：11
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2511.23402
- 全文字數：54671（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/anonymous-1742/Quantized-TinyLLaVA
- 配對 Repo：anonymous-1742/Quantized-TinyLLaVA

## 摘要
Multimodal foundation models are increasingly trained on sensitive data across domains such as finance, biomedicine, and personal identifiers. However, this distributed setup raises serious privacy concerns due to the need for cross-partition data sharing. Split learning addresses these concerns by enabling collaborative model training without raw data exchange between partitions, yet it introduces a significant challenge: transmitting high-dimensional intermediate feature representations between partitions leads to substantial communication costs. To address this challenge, we propose Quantized-TinyLLaVA, a multimodal foundation model with an integrated communication-efficient split learning framework. Our approach adopts a compression module that quantizes intermediate feature into discrete representations before transmission, substantially reducing communication overhead. Besides, we derive a principled quantization strategy grounded in entropy coding theory to determine the optimal number of discrete representation levels. We deploy our framework in a two-partition setting, with one partition operating as the client and the other as the server, to realistically simulate distributed training. Under this setup, Quantized-TinyLLaVA achieves an approximate \textbf{87.5\%} reduction in communication overhead with 2-bit quantization, while maintaining performance of the original 16-bit model across five benchmark datasets. Furthermore, our compressed representations exhibit enhanced resilience against feature inversion attacks, validating the privacy of transmission. The code is available at https://github.com/anonymous-1742/Quantized-TinyLLaVA.

## 背景與目的
多模態基礎模型在金融、生物醫學等敏感領域訓練需求增長，但分散式資料共享引發隱私與法規疑慮。分割學習雖能在不交換原始資料下協同訓練，卻因需傳輸高維中間特徵導致龐大通訊開銷，且面臨特徵反轉攻擊的隱私風險。現有分割學習框架（如 Randomized Top-K、SplitFC）未在真實分割場景評估通訊速度，亦未建構於多模態基礎模型之上。本文提出 Quantized-TinyLLaVA，整合通訊高效的分割學習框架，採用壓縮模組將中間特徵量化為離散表示，並基於熵編碼理論推導最佳離散層級數，旨在大幅降低通訊成本同時保持模型性能與隱私魯棒性。

## 方法
模型架構基於 TinyLLaVA：視覺塔（ViT 或 CNN）輸入影像輸出 patch 特徵 [B,N,d]；連接器（MLP）將視覺特徵映射至語言空間；各模態專屬壓縮器（視覺/語言壓縮器）對中間特徵進行壓縮與重建；語言模型接收嵌入序列輸出預測。資料壓縮採用兩種方法：1) FSQ：以 tanh 縮放特徵至 (-1,1)，依離散層級 d 四捨五入得整數索引，傳輸索引至伺服器端重建，反向傳播採用直通估計器（STE）近似梯度。2) RD-FSQ 改進 FSQ：(a) 線性縮放替代 tanh，先將特徵裁剪至 [μ-3σ, μ+3σ] 再線性映射至 (-1,1)，緩解飽和與雙峰分布導致的碼本利用率低問題；(b) 引入失真正則化承諾損失 L_comm = 1 - cos(((d-1)/2)e, sg(z))，以餘弦相似度約束量化前後向量差異，減少四捨五入誤差並改善梯度估計。另將 QLoRA 的 4-bit 正規浮點與區塊雙重量化推廣至任意位寬，應用於中間特徵量化。分割學習部署於雙分區：客戶端執行前向至切割層，發送量化索引；伺服器重建特徵完成前向、計算損失、反向傳播至切割層並回傳梯度。理論上以熵編碼推導最佳離散層級準則，消除試誤依賴。

## 結果
Quantized-TinyLLaVA 在 2-bit 量化下實現約 87.5% 通訊開銷減少，且在五個基準資料集上維持原始 16-bit 模型性能。RD-FSQ 與 QLoRA 於評估方法中達到最高預測準確率，RD-FSQ 另具最強特徵反轉攻擊抵抗力。理論最佳離散層級準則經實證驗證。實驗涵蓋端到端訓練與實際分割學習場景，量測傳輸時間與通訊開銷；系統性分析不同壓縮方法對隱私保護的影響，證明框架對隱私威脅的魯棒性。摘錄未提供可驗證的具體準確率數字、資料集名稱與規模、基線模型細節。

## 限制與展望
僅於雙分區設定驗證，未擴展至多方分割學習；熵編碼理論準則的完整推導與適用條件未詳述；量化位寬對不同下游任務的影響缺乏細粒度分析；特徵反轉攻擊實驗未涵蓋其他隱私攻擊（如屬性推論、模型反轉）；STE 梯度近似可能影響收斂穩定性；程式碼與實驗細節（硬體、訓練超參數）未公開驗證。後續研究可探索更大規模多模態模型、自適應位寬分配、形式化隱私保證及跨異質裝置部署。
