# 論文 01：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

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
多模態基礎模型在金融、生物醫學等敏感領域訓練時，常面臨跨分區資料共享的隱私與法規限制。分割學習雖能在不交換原始資料下協同訓練，但需傳輸高維中間特徵，導致通訊開銷大增，且易受特徵反轉攻擊洩露隱私。現有分割學習框架（如 Randomized Top-K、SplitFC）未在真實分割場景評估通訊速度，亦未針對多模態基礎模型設計，且缺乏對隱私攻擊的完整評估。本文提出 Quantized-TinyLLaVA，整合壓縮模組對中間特徵量化為離散表示，並基於熵編碼理論推導最佳離散層級，在雙分區模擬下以 2-bit 量化達約 87.5% 通訊減量，同時在五個基準資料集保持 16-bit 模型性能，並驗證壓縮表示對特徵反轉攻擊的增強韌性。

## 方法
模型架構基於 TinyLLaVA：視覺塔（ViT 或 CNN）輸出影像塊特徵 [B,N,d]；連接器（MLP）將視覺特徵映射至語言空間；各模態專用壓縮器（視覺壓縮器、語言壓縮器）對中間特徵量化壓縮；語言模型接收嵌入序列輸出預測。分割學習設定為雙分區：客戶端執行前向至切割層，傳送量化索引；伺服端重建特徵完成前向、計算損失、反向傳播梯度至切割層並回傳。資料壓縮採兩種方法：(1) FSQ：以 tanh 縮放特徵至 (-1,1)，按離散層級 d 四捨五入得整數索引，傳輸索引，伺服端反向縮放重建；使用直通估計器（STE）近似梯度。(2) RD-FSQ：改進 FSQ 之飽和與碼本利用率不足。採線性縮放：先將特徵裁剪至 [μ-3σ, μ+3σ]，再映射至 (-1,1)；引入失真正則化承諾損失 L_comm = 1 - cos((d-1)/2 * e, sg(z))，以餘弦相似度約束量化誤差，確保梯度估計準確。並擴展 QLoRA 的 4-bit 正規浮點與區塊雙重量化至任意位寬，應用於中間特徵量化。另依熵編碼理論推導最佳離散層級準則，消除試誤調參。訓練目標包含任務損失與 RD-FSQ 的承諾損失聯合最佳化。

## 結果
作者報告在雙分區分割學習設定下，2-bit 量化可達約 87.5% 通訊開銷減量，且在五個基準資料集上維持與原始 16-bit 模型相當的性能。RD-FSQ 與 QLoRA 在評估方法中達到最高預測準確率，RD-FSQ 另具最強特徵反轉攻擊防禦能力。實驗涵蓋端到端訓練與實際分割學習場景，量測傳輸時間與通訊開銷；理論最佳離散層級準則經實證驗證。摘錄未提供可驗證的具體準確率數字、傳輸時間數值或各資料集名稱，僅能觀察到定性結論：壓縮方法有效降低通訊成本並增強隱私保護。

## 限制與展望
論文為預印本（ArXiv），未經同行審查。評估僅限五個未具名基準資料集，且分割學習模擬僅雙分區，未涵蓋多方真實部署。壓縮方法在極低位寬下的性能權衡未詳細探討。隱私評估僅針對特徵反轉攻擊，其他攻擊（如模型反轉、成員推論）未測試。熵編碼理論準則假設特定分布，泛化性待驗證。程式碼連結為匿名 GitHub，缺乏完整復現細節。摘錄未提供具體實驗數字（如準確率、延遲、通訊量），無法量化比較。後續研究可擴展至多方分割、更多攻擊模型、自適應位寬分配及理論分析。
