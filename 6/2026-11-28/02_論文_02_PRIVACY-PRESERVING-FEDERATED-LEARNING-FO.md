# 論文 02：PRIVACY-PRESERVING FEDERATED LEARNING FOR CYBERSECURITY IN DISTRIBUTED CLOUD NETWORKS

- 日期：2026-11-28
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：International Journal of Engineering Research and Science & Technology
- Venue：International Journal of Engineering Research and Science & Technology
- 發布時間：2026-11-14T00:00:00+00:00
- URL：https://ijerst.org/index.php/ijerst/article/view/4842
- PDF：https://ijerst.org/index.php/ijerst/article/download/4842/4470
- DOI：
- arXiv：
- 影響指標：2yr_mean_citedness=0.14, h_index=16, i10_index=23 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: International Journal of Engineering Research and Science & Technology
- 引用數：0
- 解析程度：fulltext / pdf+ocr
- 全文來源：https://ijerst.org/index.php/ijerst/article/download/4842/4470
- 全文字數：24931（pages=11, ocr_pages=1）
- GitHub/Code：
- 配對 Repo：

## 摘要
Distributed cloud networks pose many security and privacy issues coupled by complex cyber threats, that need to be handled, not only in the realm of data security and privacy, but also to collaborate on threat detection. This research paper looks at the benefits and hurdles signifying Privacy-Preserving Federated Learning (PPFL) in the area of Cybersecurity through distributed machine learning systems. It evaluates differential privacy, secure aggregation and homomorphic encryption possibilities for protecting the sensitive information of a network and offers collaborative intrusion detection. The proposed framework evaluates cyber security issues based on publicly available cyber security datasets incorporating accuracy, precision, recall, F1 score, communication overhead, computation efficiency and adversarial resilience. The results of the analysis indicate the potential of PPFL to provide both privacy protection and cybersecurity performance. Scalable federated architectures are recommended in the study where secure, reliable and privacy protected distributed cloud architectures are developed.

## 背景與目的
分散式雲端網路面臨複雜網路威脅，傳統集中式機器學習需集中敏感資料，引發隱私與法規風險。聯邦學習雖讓節點本地訓練、僅上傳模型參數，但仍易受梯度反轉、成員推論、投毒、後門與拜占庭攻擊。現有研究多單獨探討差分隱私、同態加密、安全聚合等機制，缺乏在分散式雲端環境下整合多重隱私增強技術、對抗韌性、通訊效率與擴展性的綜合框架。本文旨在實驗驗證隱私保護聯邦學習（PPFL）於分散式雲端網路入侵偵測中的可行性，並評估隱私保護與偵測性能的平衡。

## 方法
研究採量化實驗設計，使用公開網路流量資料集 CIC‑IDS2017、CSE‑CIC‑IDS2018 與 UNSW‑NB15 作為次級資料。系統架構包含多個分散式雲端節點，各節點在本地以相同模型架構（未於摘錄中指定具體分類器）對正常流量與多類攻擊進行訓練，原始資料不離開節點。全域聚合伺服器採用聯邦平均（FedAvg）演算法，並結合安全聚合機制以防止單一節點模型更新洩露。隱私保護層面分別評估差分隱私、同態加密與安全多方計算/安全聚合的組合效果。評估指標涵蓋準確率、精確率、召回率、F1‑score、假陽性率、通訊開銷（MB）與計算時間（秒/資源利用率）。實驗對比三種架構：集中式學習、傳統聯邦學習與隱私保護聯邦學習（PPFL），並以描述性統計與比較性能分析解釋結果。推論階段各節點載入全域模型進行本地入侵偵測，無需上傳原始流量。

## 結果
實驗顯示集中式模型最高準確率 98.20%，傳統聯邦學習 96.80%，PPFL 95.60%，F1‑score 約 95.50%。各攻擊類別 F1 分別為 DDoS 96.80%、連接埠掃描 96.65%、惡意軟體 93.20%、資料外洩 92.10%。隱私機制比較：協同聯邦學習達 98% 隱私保護；同態加密隱私保護 96% 但計算複雜度 32%；PPFL 綜合表現為測試準確率 95.60%、計算負擔 25%。通訊方面，傳統 FL 耗 1,250 MB，集中式 2,400 MB，PPFL 每輪額外約 1,000 MB，但集中式通訊量比 PPFL 多 34.17%，延遲 PPFL 165 ms 對集中式 180 ms。擴展性測試：5 節點準確率 94.80%，20 節點 95.60%，25 節點略降至 95.30%，訓練時間 395 秒、資源利用率 81%。整體評估 PPFL 隱私保護 98%、對抗韌性 91%，優於其他兩架構；假設檢定顯示隱私保護、對抗韌性、通訊效率顯著改善（p<0.05），但偵測準確率未達顯著（p>0.05）。

## 限制與展望
本研究僅採三個公開資料集，未涵蓋真實雲端異構流量與非 IID 分佈的完整情境；PPFL 引入同態加密與安全聚合導致計算與通訊額外開銷，且在節點數超過 20 時準確率略降、資源利用率升高。假設檢定顯示偵測準確率未顯著優於基線，主要優勢在隱私與安全指標。未來需探討更輕量化隱私機制、自適應聚合策略、非 IID 資料下的模型收斂與對抗攻擊防禦，並驗證於實際分散式雲端部署。
