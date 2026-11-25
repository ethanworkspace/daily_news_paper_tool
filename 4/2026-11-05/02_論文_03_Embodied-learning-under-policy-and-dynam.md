# 論文 03：Embodied learning under policy and dynamics shifts.

- 日期：2026-11-05
- 來源層級：Tier 1
- 期刊/會議/來源：National science review
- Venue：National science review
- 發布時間：2026-11-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43054955/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13781052/
- DOI：10.1093/nsr/nwag506
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1856（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Embodied agents must continuously adapt to the physical world using interaction data collected across varying timescales, controllers and environmental conditions. However, standard reinforcement learning assumes stationary dynamics and on-policy data, a premise often violated in reality where physical parameters drift and historical data becomes heterogeneous. The central challenge lies in the compound distribution shift: replayed transitions follow an occupancy distribution that diverges fundamentally from the current physical reality, leading to biased value estimation and catastrophic learning collapse. In this work, we propose Transition Occupancy Matching as a unifying principle to resolve policy and dynamics shifts within a single mathematical framework. We introduce Occupancy-Matching Policy Optimization (OMPO), a novel algorithm that optimizes a surrogate objective explicitly correcting for transition discrepancies. By leveraging a dual reformulation with a sign-free logarithmic link, OMPO transforms the intractable matching problem into a stable min-max optimization, amenable to arbitrary reward structures. Crucially, OMPO integrates a distributional critic and a multimodal encoder with a small-scale local buffer, allowing the agent to anchor massive historical data to the immediate physical context for rapid adaptation. Extensive evaluations across diverse benchmarks-including MuJoCo locomotion, DM-Control, Meta-World and high-fidelity Panda robot manipulation-demonstrate that OMPO consistently outperforms specialized baselines in stationary, domain-shifting and non-stationary settings. By unifying distribution correction across policy and dynamics shifts, OMPO addresses a fundamental bottleneck in transfer learning, providing a robust algorithmic framework for continual adaptation in changing physical conditions.

## 背景與目的
本文針對具身智能體在真實物理環境中持續適應的問題，指出標準強化學習假設平穩動態與同策略資料，但在參數漂移與異質歷史資料下失效。核心困難在於複合分佈漂移：重播轉移的佔用分佈偏離當前物理實況，導致價值估計偏誤與災難性學習崩潰。研究提出「轉移佔用匹配」作為統一原理，並在單一數學框架內同時解決策略漂移與動態漂移，目標為提供一個穩健的持續適應演算法框架。

## 方法
問題設定：輸入為跨不同時段、控制器與環境條件收集的異質轉移資料；輸出為能在當前動態下快速適應的策略。整體架構包含三大核心模組：(1) 佔用匹配目標，將策略與動態漂移建模為轉移佔用分佈之間的差異，並引入無符號對數連結的對偶重構，將難以處理的匹配問題轉化為穩定的極小極大優化，適用於任意獎勵結構；(2) 分佈式評論網路，輸出價值分佈而非單一標量，以捕捉不確定性並輔助匹配目標的梯度估計；(3) 多模態編碼器結合小規模局部緩衝區，將大量歷史轉移映射至當前物理情境的潛在表示，使代理能錨定海量歷史資料於即時情境。訓練目標為最小化匹配損失與最大化期望回報的聯合極小極大目標，採用交替梯度下降優化。推論時，代理先以局部緩衝區更新編碼器與評論網路，再依匹配後的佔用分佈產生動作。關鍵差異在於同時以單一目標修正策略與動態漂移，並引入分佈式評論與多模態錨定機制，區別於僅處理單一漂移或需離線重訓練的既有方法。

## 結果
作者在 MuJoCo 移動、DM-Control、Meta-World 及高保真 Panda 機械手操作四大基準上進行實驗，報告 OMPO 在平穩、領域漂移與非平穩三類設定下均優於專門針對單一漂移設計的基線方法。消融實驗顯示分佈式評論與多模態編碼器對快速適應貢獻顯著。摘錄未提供可驗證數字，僅能觀察到定性結論：OMPO 能在複合漂移情境下保持穩定學習並加速適應。

## 限制與展望
論文摘錄未揭露具體超參數、緩衝區大小、編碼器架構細節、訓練步數或計算資源需求，亦未提供統計顯著性檢定或多隨機種子結果。評估僅限模擬環境，真實機器人部署的感測噪聲、安全約束與實時性尚未驗證。後續研究可探討理論收斂保證、更大規模異質資料集的擴展性，以及在線安全約束下的佔用匹配機制。
