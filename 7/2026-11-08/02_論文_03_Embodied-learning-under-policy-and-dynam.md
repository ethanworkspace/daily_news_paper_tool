# 論文 03：Embodied learning under policy and dynamics shifts.

- 日期：2026-11-08
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
本研究針對具身智能體在真實物理環境中持續適應的問題。標準強化學習假設環境動態平穩且資料為同策略，但實際上物理參數漂移、控制器變更導致歷史資料分布異質，造成轉移佔據分布與當前現實偏離，進而產生價值估計偏差與災難性遺忘。現有方法多針對單一類型分布漂移（策略或動態）設計專用修正，缺乏統一框架。本文提出「轉移佔據匹配」作為統一原理，並發展 Occupancy‑Matching Policy Optimization (OMPO)，旨在單一數學框架內同時修正策略與動態漂移，提供持續適應的演算法基礎。

## 方法
問題設定：智能體需在非平穩動態與異質歷史資料下學習策略，輸入為跨時段、跨控制器收集的轉移樣本，輸出為適應當前物理條件的策略。整體架構採用「轉移佔據匹配」原理，將歷史轉移的佔據分布與當前佔據分布對齊。核心機制為 Occupancy‑Matching Policy Optimization (OMPO)： 1. 代理目標：建立一個修正轉移差異的替代目標，明確補償策略與動態漂移導致的分布偏移。 2. 對偶重構與無符號對數連結：將難以直接優化的匹配問題轉化為穩定的極小極大優化，適用於任意獎勵結構。 3. 分布式評論網路：採用分布式評論以捕捉價值分布的不確定性，提升對漂移環境的魯棒性。 4. 多模態編碼器與小規模局部緩衝區：編碼器整合多源感測資訊，局部緩衝區保存近期真實互動，使大量歷史資料能錨定至即時物理脈絡，實現快速適應。 訓練目標與損失：摘錄未提供具體損失函數形式、優化器設定或超參數。推論流程：於部署時利用局部緩衝區更新編碼器與評論網路，並透過極小極大優化更新策略。與既有方法差異在於單一框架同時處理策略漂移與動態漂移，並引入無符號對數連結實現穩定極小極大優化。

## 結果
作者在 MuJoCo 移動任務、DM‑Control、Meta‑World 以及高保真 Panda 機械手操作等多樣基準上進行實驗，報告 OMPO 在平穩、領域漂移與非平穩三類設定下均持續優於專用基線。摘錄未提供可驗證數字（如具體回報、成功率、樣本效率等），僅能觀察到定性結論：OMPO 能在策略與動態同時漂移時保持穩定學習，並展現快速適應能力。

## 限制與展望
目前可取得資料僅含摘要，缺乏詳細實驗設定、消融研究、計算資源需求、超參數敏感度分析、安全性評估及真實機器人部署細節。因此無法確認方法在極端動態變化、長期持續學習或高維感測噪聲下的表現。後續研究需補充完整實驗數據、理論收斂證明、擴展至多智能體協作場景，並探討實時推論延遲與模型壓縮可行性。
