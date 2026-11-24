# 論文 04：Precision Drug Discovery in the Era of Artificial Intelligence: A Critical Review.

- 日期：2026-09-14
- 來源層級：Tier 2
- 期刊/會議/來源：Annual review of pharmacology and toxicology
- Venue：Annual review of pharmacology and toxicology
- 發布時間：2026-09-08T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42710027/
- PDF：
- DOI：10.1146/annurev-pharmtox-060325-010428
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1184（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Traditional drug development suffers from high costs, low success rates, and patient response variability. Precision drug discovery seeks to overcome these limitations by targeting specific genetic and molecular mechanisms but faces challenges in integrating cross-scale, multimodal biomedical data. Recent advances in artificial intelligence (AI), especially deep learning, provide powerful tools to navigate these complexities. This review surveys representative AI methods across four core stages of precision drug discovery: (a) target identification and validation using omics-, drug-, and structure-based approaches; (b) structure- and sequence-guided virtual screening of active compounds; (c) individualized drug response prediction integrating cell-line, single-cell, and multimodal data; and (d) AI-enabled toxicology and safety modeling to anticipate adverse liabilities and improve translational success. We further highlight a paradigm shift toward autonomous scientific agents capable of causal reasoning and end-to-end experimental guidance. Finally, we discuss persistent challenges, including data bias, limited interpretability, and in silico-to-wet lab translation.

## 背景與目的
傳統藥物開發面臨高成本、低成功率與患者反應異質性等瓶頸。精準藥物發現旨在鎖定特定基因與分子機制以突破限制，但整合跨尺度、多模態生物醫學資料仍具挑戰。近年人工智慧（AI），特別是深度學習，提供強大工具應對此類複雜性。本文為綜述文章，旨在系統梳理精準藥物發現四大核心階段的代表性 AI 方法，並凸顯向具備因果推理與端到端實驗指導能力的自主科學智能體範式轉移，同時指出資料偏差、可解釋性不足與 in silico 到濕式實驗轉譯等持續挑戰，為領域提供關鍵技術地圖與未來方向指引。

## 方法
本綜述採取結構化調查法，將精準藥物發現流程劃分為四大核心階段，分別蒐集並歸納代表性 AI 方法：（a）標靶鑑定與驗證：涵蓋組學基礎、藥物基礎與結構基礎三類途徑，利用多組學資料整合、藥物標靶關聯網絡與蛋白質結構預測等技術識別疾病關鍵標靶；（b）結構與序列導向的虛擬篩選：結合蛋白質三維結構或氨基酸序列資訊，運用深度學習模型（如圖神經網絡、Transformer）預測化合物結合親和力與活性，加速先導化合物發現；（c）個體化藥物反應預測：整合細胞株、單細胞測序與多模態臨床資料，建構多任務或遷移學習模型，捕捉患者異質性並預測藥物敏感性與抗藥性；（d）AI 賦能毒理與安全性建模：利用化學結構特徵、代謝途徑與表型資料，預測脱靶效應、心臟毒性、肝毒性等不良反應，提升轉譯成功率。除階段性方法外，本文另識別出一範式轉移：自主科學智能體結合因果推理與實驗規劃模組，可自動生成假設、設計實驗並迭代優化，實現端到端發現流程。綜述並未提出單一統一模型架構，而是以階段性任務為導向，對比各方法在資料表示（圖、序列、影像、表格）、模型選擇（CNN、GNN、Transformer、自編碼器）、訓練目標（分類、回歸、對比學習、生成式目標）與驗證策略上的異同，勾勒技術演進脈絡。

## 結果
摘錄未提供可驗證數字。本綜述定性總結指出：AI 方法已滲透精準藥物發現全流程，四大階段均有代表性深度學習模型展現優於傳統計算手法的預測性能；自主科學智能體雖處早期，但展現因果推理與實驗閉環潛力，有望重塑發現範式；然而資料偏差（如族群代表性不足、批次效應）、模型可解釋性受限（黑盒決策難獲監管接受）、以及計算預測與濕式實驗驗證間的轉譯鴻溝，仍為阻礙臨床落地的關鍵瓶頸。

## 限制與展望
本綜述作為二手文獻綜合，受限於被引用原始研究的實驗設計與報告品質，未進行統一基準下的量化比較；資料層面，現有公開資料集多存在選擇偏差、樣本量不足與標註噪聲，限制模型泛化；方法層面，多模態融合策略缺乏標準化，因果推理模組多停留於理論或小規模驗證；評估層面，缺乏跨機構、前瞻性的濕式實驗驗證框架；部署層面，法規科學對 AI 決策透明度與可重現性要求尚未完全對接。後續研究需聚焦：建構高品質、多元化且標準化的基準資料集；發展內建因果機制與不確定性量化的可解釋架構；建立 in silico 預測至臨床試驗的持續驗證管線；並推動監管科學與 AI 治理的共同演進。
