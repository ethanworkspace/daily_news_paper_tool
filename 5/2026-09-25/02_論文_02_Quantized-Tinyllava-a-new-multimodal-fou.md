# 論文 02：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

- 日期：2026-09-25
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
多模態基礎模型在金融、生物醫學等敏感領域訓練時面臨隱私與法規限制，分散式資料無法直接共享。Split learning 雖能在不交換原始資料下協同訓練，但需傳輸高維中間特徵，導致通訊開銷極大；現有稀疏化與量化方法未在真實分割學習場景驗證通訊速度，亦未充分評估特徵反轉攻擊風險，且皆未建構於多模態基礎模型之上。本文提出 Quantized-TinyLLaVA，整合通訊高效的分割學習框架，採用壓縮模組將中間特徵量化為離散表示，並基於熵編碼理論推導最佳離散層級數，在雙分區（客戶端-伺服器）設定下實現約 87.5% 通訊量降低（2-bit 量化）且保持 16-bit 基線性能，同時增強對特徵反轉攻擊的韌性。

## 方法
模型架構基於 TinyLLaVA：視覺塔提取影像 patch 特徵，連接器將視覺特徵映射至語言空間，雙模態專用壓縮器對中間特徵進行壓縮與重建，最後由大型語言模型處理下游任務。壓縮模組支援多種嵌入壓縮技術，重點引入兩種方法：(1) 擴展 QLoRA 的 4-bit 正規浮點數與區塊雙重量化至任意位寬，應用於中間特徵量化；(2) 提出 RD-FSQ（Robust and Distortion-aware Finite Scalar Quantization），改進 FSQ 的三大缺失：以線性縮放取代 tanh 並先將特徵裁剪至 [μ-3σ, μ+3σ] 區間緩解飽和與雙峰分布；引入基於餘弦相似度的承諾損失 L_comm = 1 - cos((d-1)/2 * e, sg(z)) 正則化量化失真，配合直通估計器（STE）近似梯度；量化流程為：客戶端將特徵縮放、量化為整數索引傳輸，伺服端重建特徵。另依熵編碼理論推導最佳離散表示層級的理論準則，消除反覆試誤。實驗在端到端訓練與實際分割學習場景（量化嵌入、測量傳輸時間與通訊開銷）雙軌評估，並系統分析不同壓縮方法對特徵反轉攻擊的隱私防護效果。

## 結果
在五個基準資料集上，RD-FSQ 與 QLoRA 達到最高預測準確率，RD-FSQ 另具最強特徵反轉攻擊抵抗力。Quantized-TinyLLaVA 在 2-bit 量化下實現約 87.5% 通訊開銷減少，性能與原始 16-bit 模型持平。理論推導的最佳離散層級準則經實證驗證。實際分割學習場景測量顯示傳輸時間與通訊量顯著降低。摘錄未提供可驗證的具體準確率數字、傳輸時間毫秒數、基線模型名稱或消融實驗細節，僅能觀察到定性結論：RD-FSQ 兼顧精度與隱私，量化策略理論依據增強可信度。

## 限制與展望
論文為預印本（ArXiv），程式碼匿名發布，缺乏同行審查。實驃僅在雙分區（客戶端-伺服器）模擬，未驗證多節點或異構分區情況。五個基準資料集未具名，無法評估領域覆蓋度。隱私評估僅針對特徵反轉攻擊，未涵蓋模型反轉、屬性推論等其他威脅。理論最佳層級準則雖經驗證，但推導假設與邊界條件未在摘錄中說明。極低位寬（如 1-bit）下的性能-通訊權衡未探討。部署層面未提及異構硬體適配、量化感知訓練成本或線上適應機制。後續研究可擴展至多方分割學習、更全面的隱私威脅模型、自適應位寬分配與硬體加速實現。
