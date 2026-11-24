# 論文 02：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

- 日期：2026-10-13
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
多模態基礎模型在金融、生醫、個人識別等敏感領域訓練需求增長，但分散式資料共享引發隱私與法規顧慮。分割學習雖能在不交換原始資料下協同訓練，卻因高維中間特徵傳輸產生龐大通訊開銷，且面臨特徵反轉攻擊的隱私風險。現有分割學習框架（如 Randomized Top-K、SplitFC）未在真實分割場景評估通訊速度，亦未充分驗證隱私攻擊魯棒性，更未建構於多模態基礎模型之上。本文提出 Quantized-TinyLLaVA，整合通訊高效的分割學習框架，採用壓縮模組將中間特徵量化為離散表示，並基於熵編碼理論推導最佳離散層級數，於雙分區設定下實現約 87.5% 通訊開銷降低（2-bit 量化）且保持原 16-bit 模型在五個基準資料集上的性能，同時壓縮表示對特徵反轉攻擊展現更強韌性。

## 方法
模型架構基於 TinyLLaVA，包含四大組件：(1) 視覺塔：接收影像 [B,C,H,W]，輸出 patch 特徵序列 [B,N,d]，可為 ViT 或 CNN。(2) 連接器：MLP 將視覺特徵映射至語言特徵空間 [B,N,D]。(3) 壓縮器：各模態專屬壓縮模組，支援可學習編碼器-解碼器或固定量化/稀疏化演算法，於分割點前壓縮中間特徵。(4) 語言模型：接收嵌入序列輸出預測。 資料壓縮方法： - FSQ：以 tanh 縮放特徵至 (-1,1)，依離散層級 d 進行對稱或非對稱四捨五入，傳輸整數索引，伺服端重建。因四捨五入不可微，採直通估計器 (STE) 近似梯度。 - RD-FSQ：改進 FSQ 兩大缺失。① 線性縮放：先將特徵裁剪至 [μ-3σ, μ+3σ]，再線性映射至 (-1,1)，避免 tanh 飽和導致碼本利用率低與梯度消失。② 失真正則化：引入承諾損失 L_comm = 1 - cos((d-1)/2 * e, sg(z))，以餘弦相似度約束量化前後向量差異，減少四捨五入誤差並改善梯度估計。 - QLoRA 擴展：將 4-bit 正規浮點數與區塊雙重量化推廣至任意位寬，應用於中間特徵量化。 分割學習流程：客戶端執行前向至切割層，經壓縮器量化後傳輸離散索引；伺服端解碼重建特徵，完成前向、計算損失、反向傳播至切割層，梯度經壓縮器（或直接）回傳客戶端更新參數。 理論準則：基於熵編碼理論推導最佳離散表示層級數，消除反覆試誤，提升可信度與可解釋性。

## 結果
作者在五個基準資料集上比較 RD-FSQ、QLoRA、FSQ、Randomized Top-K 稀疏化及無分割學習的原始模型。結果顯示 RD-FSQ 與 QLoRA 達到最高預測準確率，且 RD-FSQ 對特徵反轉攻擊具最強防禦能力。在實際分割學習場景下，2-bit 量化可實現約 87.5% 通訊開銷減少，同時維持與 16-bit 原模型相當的性能；並測量傳輸時間與通訊開銷，驗證通訊效率提升。理論推導的最佳離散層級準則經實證驗證有效。摘錄未提供可驗證的具體準確率數字、傳輸時間數值或各資料集名稱，僅能觀察到定性結論：RD-FSQ 在準確率與隱私魯棒性上雙贏，量化位寬降低不顯著損害任務表現。

## 限制與展望
論文為 ArXiv 預印本，未經同行審查。實驗僅於雙分區分割學習設定，未探討多客戶端或異質資料分佈。五個基準資料集未具體命名，且缺乏詳細數值指標（如準確率、F1、傳輸延遲），難以獨立驗證。壓縮方法僅在 TinyLLaVA 架構驗證，泛化至其他多模態模型（如 LLaVA、Flamingo）未知。隱私評估僅針對特徵反轉攻擊，未涵蓋模型反轉、屬性推論等其他攻擊。理論最佳層級準則的假設條件（如特徵分佈）未在摘錄中完整描述，可能限制適用範圍。程式碼連結為匿名倉庫，長期可用性不確定。後續研究可擴展至多方分割學習、更全面的隱私威脅模型、以及與其他量化感知訓練方法的系統性比較。
