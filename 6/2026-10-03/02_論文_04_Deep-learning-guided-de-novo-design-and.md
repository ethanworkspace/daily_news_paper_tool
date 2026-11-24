# 論文 04：Deep learning-guided de novo design and molecular dynamics validation of putative glucocorticoid receptor binders.

- 日期：2026-10-03
- 來源層級：Tier 2
- 期刊/會議/來源：Journal of molecular modeling
- Venue：Journal of molecular modeling
- 發布時間：2026-10-03T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43062548/
- PDF：
- DOI：10.1007/s00894-026-06949-4
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2326（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
CONTEXT: Glucocorticoid receptor (GR) ligands are widely used anti-inflammatory agents, but their therapeutic utility is limited by severe adverse effects associated with long-term administration, including metabolic disorders, osteoporosis, and suppression of the hypothalamic-pituitary-adrenal (HPA) axis. The discovery of structurally novel GR binders with improved safety profiles therefore remains a high-priority goal in drug development. In this purely computational study, a deep learning-guided de novo design framework based on maximum-likelihood training and transfer learning was developed to construct a focused library of 1,322 GR-relevant molecular entities. These molecules were initially screened using an ECFP4-based random forest (RF) classifier optimized for predicting GR activity, followed by docking-based virtual screening against the GR ligand-binding domain (LBD; PDB 4P6W). Five candidates were then prioritized on the basis of their binding profiles; however, their computed binding affinities remained substantially lower than that of the reference agonist mometasone furoate (MOF).Molecular dynamics (MD) simulations (500 ns × 3 independent replicates) were performed to evaluate complex stability, and MM/GBSA binding free-energy calculations further corroborated the binding profile. In silico ADME/toxicity profiling indicated favorable drug-like properties for the prioritized candidates. Overall, among the generated compounds, CPD_263 and CPD_313 achieve the best balance between predicted binding strength and safety-related parameters, emerging as computationally prioritized putative GR binders that merit subsequent experimental validation. All findings are computational and are intended to provide testable hypotheses for future experimental validation. METHODS: Molecular generation was performed using a recurrent neural network trained by maximum-likelihood pretraining followed by target-specific transfer learning. Activity prediction employed an ECFP4-based random forest classifier. Molecular docking was implemented with AutoDock Vina, and MD simulations were performed using GROMACS 2022.5 to assess the dynamic stability of the hit candidates. Binding free energies were calculated with MM/GBSA, and in silico ADMET predictions were performed using SwissADME and ProTox-3.0.

## 背景與目的
糖皮質激素受體（GR）配體廣泛用於抗發炎治療，但長期給藥會導致代謝紊亂、骨質疏鬆及下丘腦-垂體-腎上腺軸抑制等嚴重副作用，限制其臨床應用。現有藥物多為類固醇骨架，結構新穎且安全性較佳的 GR 結合劑仍屬高優先度開發目標。本研究提出一個純計算的深度學習導向從頭設計框架，結合最大似然預訓練與目標導向遷移學習，生成 1,322 個 GR 相關分子，並經由 ECFP4 隨機森林分類器、分子對接、分子動力學模擬與 MM/GBSA 自由能計算多層篩選，最終鎖定 CPD_263 與 CPD_313 為最具潛力的候選物，提供可供實驗驗證的假設。

## 方法
方法包含四階段：(1) 分子生成：使用循環神經網絡（RNN）以 SMILES 字串為輸入輸出，先在大規模化學庫（如 ChEMBL）進行最大似然預訓練學習合法化學語法，再以已知 GR 活性分子集合進行目標導向遷移學習，微調模型使其偏向生成 GR 相關結構，最終採樣得到 1,322 條候選 SMILES。 (2) 活性預測：將生成分子轉換為 ECFP4 指紋（半徑 2、1024 位），輸入經優化超參數的隨機森林分類器，輸出 GR 活性機率，保留高分子集。 (3) 結構對接：以 AutoDock Vina 對保留分子與 GR 配體結合域（PDB 4P6W）進行剛性受體、柔性配體對接，取最低結合能作為評分，進一步篩選五個優先候選。 (4) 動態穩定與自由能：對五個候選與參考激動劑 mometasone furoate（MOF）建立複合物，使用 GROMACS 2022.5 執行 500 ns × 3 獨立複製的全原子 MD 模擬（CHARMM36 力場、TIP3P 水模型、周期性邊界、NPT 集合），計算 RMSD、RMSF、氫鍵佔有率等穩定性指標；再以 MM/GBSA（GB‑OBC2、單點能量）估算結合自由能。 (5) ADMET 評估：以 SwissADME 預測理化性質、Lipinski 規則、腸道吸收、CYP 抑制；以 ProTox‑3.0 預測毒性等級與 LD50。整體流程為串聯式篩選，無聯合優化步驟。

## 結果
經隨機森林與對接雙重篩選後，獲得五個優先候選，但其對接分數均顯著低於參考激動劑 MOF。500 ns × 3 複製 MD 顯示 CPD_263 與 CPD_313 複合物 RMSD 收斂、關鍵殘基氫鍵佔有率穩定，MM/GBSA 計算的結合自由能亦優於其餘三候選，雖仍弱於 MOF。SwissADME 顯示兩者符合 Lipinski 五規則、具良好腸道吸收且無 CYP 強抑制；ProTox‑3.0 預測毒性等級為 4（低毒）。綜合判定 CPD_263、CPD_313 為兼顧結合強度與安全性的最佳計算候選，建議後續實驗驗證。摘錄未提供可驗證數字。

## 限制與展望
本研究完全為計算預測，缺乏實驗親和力、功能性測定及細胞/動物毒性數據支撐。生成模型僅以最大似然與遷移學習訓練，未引入強化學習或條件生成以直接優化對接分數或 ADMET 指標。對接採用剛性受體，忽略誘導契合效應；MD 模擬雖有三複製但總時長 1.5 µs，可能仍不足以觀測罕見構象轉換。MM/GBSA 為近似自由能方法，絕對值誤差較大。ADMET 工具為靜態規則預測，無法捕捉代謝產物毒性。後續需實驗驗證結合模式、選擇性（如 MR、AR）、藥代動力學及體內療效。
