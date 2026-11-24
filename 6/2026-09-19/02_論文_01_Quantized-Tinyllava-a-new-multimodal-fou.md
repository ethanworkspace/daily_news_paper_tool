# 論文 01：Quantized-Tinyllava: a new multimodal foundation model enables efficient split learning

- 日期：2026-09-19
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
本研究針對多模態基礎模型在分散式敏感資料（金融、生醫、個人識別碼）上協同訓練時的隱私與通訊成本問題。現有分割學習雖避免原始資料交換，但需傳輸高維中間特徵，導致通訊開銷大且易受特徵反轉攻擊。論文提出 Quantized-TinyLLaVA，結合量化壓縮模組與基於熵編碼理論的最佳離散表示層級選擇，在雙分區（客戶端/伺服器）設定下實現通訊效率與隱私保護的雙重提升。

## 方法
方法架構基於 TinyLLaVA，包含視覺塔、連接器、壓縮器（視覺壓縮器與語言壓縮器）及大型語言模型。視覺塔輸出影像 patch 特徵，連接器以 MLP 將視覺特徵映射至語言空間。壓縮器於客戶端將中間特徵量化為離散索引傳輸，伺服器端重建特徵供後續模型使用。提出兩種壓縮策略：(1) FSQ：以 tanh 縮放後四捨五入至固定離散層級，採直通估計器（STE）近似梯度；(2) RD-FSQ：改用線性縮放並先將特徵裁剪至 [μ−3σ, μ+3σ] 區間，再引入餘弦相似度承諾損失 L_comm = 1−cos((d−1)/2·e, sg(z)) 以抑制量化失真，並同樣以 STE 反傳梯度。另將 QLoRA 的 4-bit 正規浮點與區塊雙重量化推廣至任意位寬，應用於中間特徵傳輸。並依熵編碼理論推導最佳離散表示層級的理論準則，避免反覆試誤。訓練目標為下游任務損失加上壓縮模組的承諾損失，採用端到端與分割學習兩階段訓練。推論流程：客戶端編碼量化索引傳送，伺服器解碼重建特徵送入語言模型產生預測。關鍵差異在於針對分割學習場景設計的 RD-FSQ 線性縮放與失真正則化，以及理論指導的位寬選擇。

## 結果
實驗在五個基準資料集上進行，比較 RD-FSQ、QLoRA、FSQ、Randomized Top-K 稀疏化與無分割學習的原始 16-bit 模型。結果顯示 RD-FSQ 與 QLoRA 達到最高預測準確度，RD-FSQ 另具最強特徵反轉攻擊防禦能力。在 2-bit 量化下，通訊開銷較 16-bit 基準降低約 87.5%，且模型性能與原始模型持平。論文亦量測實際傳輸時間與通訊量，驗證於端到端訓練與實際分割學習場景下的效率提升。摘錄未提供可驗證的具體數值（如準確率、傳輸時間毫秒數），僅呈現定性結論。

## 限制與展望
限制包括：(1) 僅於雙分區模擬環境驗證，未涵蓋多客戶端、異質資料分佈或真實網路延遲；(2) 理論最佳層級準則假設特徵分佈符合熵編碼模型，實際分佈偏差可能影響最優性；(3) RD-FSQ 的線性縮放與裁剪超參數（如 3σ 界限）敏感度未充分探討；(4) 隱私評估僅針對特徵反轉攻擊，其他攻擊（如模型推理、屬性推論）未測試；(5) 程式碼為匿名發布，缺乏完整復現細節與超參數設定。後續研究可擴展至多方分割學習、自適應位寬分配與更全面的隱私威脅模型。
