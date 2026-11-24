# 論文 04：Resistive memory-based neural differential equation solver for score-based diffusion model.

- 日期：2026-10-28
- 來源層級：Tier 1
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-05-12T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42120416/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13376740/
- DOI：10.1038/s41467-026-72900-z
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1127（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
While AI-generated content (AIGC) strives to replicate human imagination, current models like score-based diffusion remain slow and energy-intensive. This inefficiency stems from conventional digital computers, where physically separated storage and processing units cause data-transfer bottlenecks, and discrete operations disrupt naturally continuous generation dynamics. Here we show a brain-inspired, analog in-memory computing system that overcomes these limitations. By employing resistive memory, our system integrates storage and computation to act as a time-continuous neural differential equation solver. We experimentally validate our solution with 180 nm resistive memory in-memory computing macros. While maintaining generative quality equivalent to the software baseline, our system accelerated both unconditional and conditional generation tasks, by factors of 69.0 and 116.5, respectively, compared to advanced digital hardware. Furthermore, it reduced energy consumption by 31.5% and 52.0%, respectively. Our approach expands the horizon for hardware solutions in edge computing for generative AI applications.

## 背景與目的
當前 AI 生成內容（AIGC）以分數基擴散模型為主流，但其在傳統數位電腦上執行時面臨嚴重的資料搬移瓶頸與離散運算對連續生成動態的干擾，導致推理速度緩慢且能耗高昂。現有方法多依賴 von Neumann 架構，記憶體與運算單元物理分離，難以滿足邊緣裝置對即時、低功耗生成的需求。本文旨在提出一種類腦、類比的記憶體內運算系統，利用電阻式記憶體將儲存與計算融合，實現時間連續的神經微分方程求解器，以突破上述效能與能效限制，並為生成式 AI 在邊緣端的部署開闢新路徑。

## 方法
問題設定為以類比電路直接求解分數基擴散模型對應的神經微分方程（Neural ODE），輸入為隨機雜訊，輸出為生成樣本。系統整體架構採用電阻式記憶體（Resistive Memory, ReRAM）交叉陣列作為記憶體內運算巨集，將權重以電導值儲存於記憶體元件中，並在同一物理位置執行矩陣向量乘法與非線性激活，實現儲存與計算的原地融合。核心模組包含：(1) 類比電流域的積分電路，模擬連續時間動態；(2) 可程式化電導陣列，編碼神經網路參數；(3) 類比非線性單元（如電壓控制電流源）實現活化函數。資料表示採用類比電壓/電流訊號，直接對應神經網路的狀態變數，無需數位量化。訓練階段於軟體端完成，獲得的參數再映射至電阻陣列；推理階段則由類比電路自發演化，依據微分方程動態產生輸出，形成時間連續的求解流程。與現有數位加速器相比，關鍵差異在於：(i) 消除資料搬移，記憶體即運算單元；(ii) 以類比動態直接實現連續時間 ODE 求解，避免離散時間步進帶來的誤差與延遲；(iii) 採用 180 nm 製程的 ReRAM 巨集進行實驗驗證，展示硬體層面的可行性。

## 結果
實驗結果顯示，在保持生成品質與軟體基線相當的前提下，該系統於無條件生成任務中較先進數位硬體加速 69.0 倍，條件生成任務加速 116.5 倍；能量消耗分別降低 31.5% 與 52.0%。摘錄未提供更詳細的定量指標（如 FID、IS、吞吐率、功率數值）或消融實驗數據，僅能觀察到定性結論：類比記憶體內運算能大幅提升速度與能效，且不犧牲生成品質。

## 限制與展望
僅依摘要資訊，無法確認系統在大規模網路、多晶片整合、製程變異、長期可靠度、精度損失與溫度漂移等實際部署挑戰上的表現。評估僅限於 180 nm ReRAM 巨集與特定擴散模型，缺乏與其他類比加速器或混合訊號架構的對比。後續研究需探討：(1) 參數映射與校準流程的自動化；(2) 精度與動態範圍對生成品質的影響；(3) 系統級功耗、面積與擴展性分析；(4) 軟硬體協同優化以支援更複雜的條件生成與多模態任務。
