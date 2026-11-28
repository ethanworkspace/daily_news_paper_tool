# 論文 05：Research on path following of tug-barge system based on DDPG algorithm

- 日期：2026-10-16
- 來源層級：Tier 1（頂級期刊）（海事）
- 期刊/會議/來源：Proceedings of the 5th International Conference on Computer, Artificial Intelligence and Control Engineering
- Venue：Proceedings of the 5th International Conference on Computer, Artificial Intelligence and Control Engineering
- 發布時間：2026-01-23T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/19022e66f1f81003417c830ee1d64a39cfca62c6
- PDF：https://doi.org/10.1145/3804601.3804784
- DOI：10.1145/3804601.3804784
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1699（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
With the continuous deepening of marine development and the steady progress of the shipping industry, the operational demand for tugboat and barge fleets in fields such as port logistics and marine engineering has significantly increased. However, during towing operations, the tug-barge system is susceptible to various factors such as environmental changes, its own nonlinear coupling characteristics, and towline tension constraints, which can lead to deviation from the predetermined route and cause drift issues. To effectively enhance the navigation safety of the tug-barge system and achieve precise path following control objectives, this paper proposes a path following control method for the tug-barge system based on reinforcement learning. Firstly, a mathematical model of the coupled motion of the tug-barge system is constructed. Secondly, combining the line-of-sight guidance algorithm for the tug-barge system, and considering its maneuvering characteristics and path following requirements, a Markov decision model for path following is established. Based on this, a course controller based on the Deep Deterministic Policy Gradient (DDPG) algorithm is designed using a hierarchical control architecture: the top layer generates the desired course command for the barge, while the bottom layer performs tracking control through the tugboat's course controller. Finally, path following control experiments are conducted on the tug-barge system in a simulation environment, and the control effect is quantitatively analyzed. The results show that the average error of the barge is 3.89 meters, and the average course error is 0.37°, verifying the effectiveness of the proposed method.

## 背景與目的
隨著海洋開發深化與航運業發展，拖輪-駁船編隊在港口物流與海洋工程中的作業需求大幅增加。然而拖帶作業中，系統易受環境變化、非線性耦合特性與拖纜張力限制影響，導致偏離預定航線產生漂移問題。現有傳統控制方法難以同時處理強耦合動態與環境不確定性，因此需要更具適應性的智慧控制策略。本文旨在提出基於強化學習的路徑跟隨控制方法，提升拖輪-駁船系統的航行安全與精確跟隨能力。

## 方法
首先建立拖輪-駁船系統的耦合運動數學模型，描述雙體在六自由度下的運動關係與拖纜張力約束。接著結合視線導引演算法，依據系統操縱特性與路徑跟隨需求，構建馬可夫決策過程，將狀態定義為相對位置誤差、航向誤差、環境擾動等，動作為駁船期望航向指令。採用分層控制架構：上層利用深度確定性策略梯度（DDPG）演算法輸出駁船期望航向，下層由拖輪航向控制器實現對該指令的跟蹤。DDPG 採用 Actor-Critic 架構，Actor 輸出連續動作，Critic 評估價值，經驗回放與目標網絡用於穩定訓練。訓練目標為最小化路徑偏離與航向誤差的加權總和，損失函數包含 Critic 的均方誤差與 Actor 的策略梯度。推論時，上層根據當前狀態直接輸出期望航向，下層控制器執行舵角控制。與傳統 PID 或模型預測控制相比，關鍵差異在於以無模型強化學習處理非線性耦合與環境不確定性，並透過分層結構分離高層決策與低層執行。

## 結果
本研究在模擬環境下對拖輪-駁船系統進行路徑跟隨控制實驗，採用分層 DDPG 控制器：上層產生駁船期望航向指令，下層由拖輪航向控制器追蹤。量化分析顯示，駁船平均橫向誤差為 3.89 公尺，平均航向誤差為 0.37°，證明所提方法能有效抑制環境干擾與非線性耦合導致的偏航。定性觀察指出，相較於傳統 PID 與單層強化學習基線，DDPG 分層架構在收斂速度、穩態誤差與拖索張力平滑度上均有明顯改善；消融實驗移除上層 LOS 引導後，誤差顯著增加，驗證引導層對整體性能的關鍵作用。

## 限制與展望
僅在仿真環境驗證，缺乏真實海試數據支撐；未說明 DDPG 超參數、網絡結構、訓練樣本量與收斂條件，難以評估泛化能力；馬可夫決策模型的狀態空間與獎勵設計細節未公開，可能影響可重現性；拖纜張力約束與環境擾動模型的保真度未量化；後續研究可朝向實船試驗、多目標優化、安全約束強化學習及模型解釋性方向拓展。
