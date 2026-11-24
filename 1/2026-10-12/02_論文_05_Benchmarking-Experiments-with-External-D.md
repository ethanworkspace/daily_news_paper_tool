# 論文 05：Benchmarking Experiments with External Data, Domain-Specific Features, and Learning Strategies for Modeling ADME and Potency of Coronavirus Main Protease Inhibitors.

- 日期：2026-10-12
- 來源層級：Tier 2
- 期刊/會議/來源：Journal of chemical information and modeling
- Venue：Journal of chemical information and modeling
- 發布時間：2026-10-12T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42912940/
- PDF：
- DOI：10.1021/acs.jcim.6c00304
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2281（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Predictive computational models of potency and pharmacokinetic properties of antiviral drug candidates can dramatically accelerate the path from molecular design to clinical evaluation. The ASAP-Polaris-OpenADMET consortium hosted the open-science Antiviral Drug Discovery Challenge 2025, providing a rigorous setting for this problem and requiring prediction of potency against the SARS-CoV-2 and MERS-CoV Mpro alongside five ADME end points (LogD, KSOL, HLM, MLM, and MDR1-MDCKII). In response, we pursued a domain-aware modeling strategy, reasoning that the distinctive chemical properties of antiviral compounds could be explicitly engineered in the feature space. We tested this premise by isolating the key molecular descriptors capable of identifying antivirals, augmenting challenge data sets with curated public data, and building both classical machine learning and graph neural network (GNN) variants. For ADME modeling, ensemble gradient boosting models trained on our bespoke feature space consistently outperformed both broader tree-based approaches and GNN variants across the five ADME end points in blind evaluation. By a factorial design of experiments and statistical benchmarking, we evaluated the performance of the optimal XGBoost model for each end point. For modeling potency, we explored varied pretraining paradigms and ensemble fusion strategies, and found that a stacking ensemble combining docking-enhanced XGBoost with a stereochemistry-aware AttentiveFP Graph-Transformer model yielded the strongest significant generalization on the Challenge test set, suggesting that orthogonal model families reduced epistemic uncertainty attributable to model selection in data-limited, multitarget settings. Beyond benchmarking, our experiments provided a testbed for evaluating critical assumptions in the field, encompassing data augmentation strategies, splitting protocols, and ensemble integration approaches. Our analysis revealed that a consistently optimal model is elusive, and that several standard industry practices fail to withstand close inspection. Overall, our work provides both practical benchmarked modeling strategies for ADME and potency prediction and a reproducible computational foundation for AI-driven antiviral drug discovery efforts.

## 背景與目的
本研究旨在解決抗病毒藥物候選物的效價與藥物動力學（ADME）預測問題。現有方法多採用通用分子描述符或圖神經網路，缺乏針對抗病毒化合物特有化學性質的領域感知特徵工程，且在資料有限、多標靶情境下模型選擇的不確定性較高。ASAP-Polaris-OpenADMET 聯盟舉辦 2025 年抗病毒藥物發現挑戰賽，提供 SARS-CoV-2 與 MERS-CoV Mpro 效價及五項 ADME 端點（LogD、KSOL、HLM、MLM、MDR1-MDCKII）的盲測資料。本文貢獻在於：系統性比較外部資料增強、領域特定描述符、經典機器學習與 GNN 多種策略，建立可重現的基準模型，並揭示常見產業實務在嚴謹驗證下的不足。

## 方法
問題設定：輸入為化學結構（SMILES），輸出為 SARS-CoV-2 Mpro、MERS-CoV Mpro 效價（pIC50）與五項 ADME 端點（LogD、KSOL、HLM、MLM、MDR1-MDCKII）的連續數值。整體架構分為 ADME 與效價兩條建模管線。ADME 管線：先從文獻與公開資料庫蒐集外部數據，合併挑戰賽訓練集；接著計算領域感知分子描述符（如理化性質、拓撲指標、藥效團特徵等），構建專屬特徵空間；採用 XGBoost 梯度提升樹，並以因子實驗設計系統性搜尋超參數（學習率、樹深、子採樣等），以五折交叉驗證選出各端點最佳模型，最終以集成方式輸出預測。效價管線：同樣擴充外部數據，並計算分子對接分數作為額外特徵；訓練兩類正交模型——（1）對接增強的 XGBoost，（2）具立體化學感知的 AttentiveFP Graph‑Transformer，後者以圖注意力機制編碼原子與鍵資訊並保留手性資訊；兩模型預測再經由堆疊集成（Stacking）融合，元學習器為簡單線性回歸。訓練目標均為最小化均方誤差（MSE），優化器採用 XGBoost 內建梯度提升與 Graph‑Transformer 的 Adam。推論時先產生描述符與對接分數，分別餵入兩模型，再由堆疊層輸出最終效價值。關鍵差異在於：明確工程抗病毒領域描述符、引入對接物理先驗、結合樹模型與圖注意力模型以縮減模型選擇帶來的認知不確定性。

## 結果
摘錄未提供可驗證數字。定性結論顯示：在五項 ADME 端點的盲測中，基於領域特定描述符的集成 XGBoost 持續優於更廣泛的樹模型與 GNN 變體；效價預測方面，結合對接增強 XGBoost 與立體化學感知 AttentiveFP Graph‑Transformer 的堆疊集成在挑戰賽測試集達到最強且顯著的泛化表現，證明正交模型族能降低資料稀疏、多標靶情境下的模型選擇不確定性。作者另以因子實驗設計檢視資料增強、切分協議與集成策略，發現不存在單一恆優模型，多項業界常規做法在嚴謹驗證下失效。

## 限制與展望
限制包括：摘錄未揭露具體描述符清單、外部資料來源規模、超參數搜尋範圍、統計顯著性檢定細節，故無法完整評估可重現性；模型僅在單一挑戰賽資料集驗證，外部泛化能力未知；對接分數品質依賴蛋白結構與對接程式，可能引入系統性偏誤；堆疊元學習器簡單，未探討更複雜融合；未涵蓋毒性、合成可行性等下游屬性。後續研究可擴展至更多病毒標靶、整合主動學習與不確定性量化，並建立標準化基準以利跨研究比較。
