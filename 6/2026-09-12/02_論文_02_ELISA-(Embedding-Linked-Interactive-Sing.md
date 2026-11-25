# 論文 02：ELISA (Embedding-Linked Interactive Single-cell Agent): an interpretable hybrid generative Artificial Intelligence agent for expression-grounded discovery in single-cell genomics.

- 日期：2026-09-12
- 來源層級：Tier 2
- 期刊/會議/來源：Briefings in bioinformatics
- Venue：Briefings in bioinformatics
- 發布時間：2026-09-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42721440/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13561307/
- DOI：10.1093/bib/bbag501
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1865（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here, we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies single-cell generative pretrained transformer expression embeddings with biomedical bidirectional encoder representations from transformers-based semantic retrieval and large-language model (LLM)-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoring across 60+ gene sets, ligand-receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation, all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer, a classical lexical retriever (BM25), and a random baseline in cell type retrieval (combined permutation test, $p < 2\times 10^{-5}$ for each), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for mean reciprocal rank). ELISA replicates published biological findings (mean composite score 0.88), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery.

## 背景與目的
單細胞 RNA 定序 (scRNA-seq) 資料轉化為機制性生物假設仍是關鍵瓶頸，現有代理式 AI 缺乏直接存取轉錄體表徵，而表徵基礎模型對自然語言不透明。本文提出 ELISA，整合單細胞生成式預訓練 Transformer 表徵嵌入、生物醫學 BERT 語義檢索與大型語言模型 (LLM) 解釋，構建可解釋的互動式單細胞發現框架，旨在填補資料探索與生物發現間的鴻溝。

## 方法
問題設定：輸入為單細胞表徵嵌入（由生成式預訓練 Transformer 產生）與使用者查詢（基因特徵、自然語言概念或混合）。輸出為細胞類型檢索排名、路徑活性評分、配體-受體交互預測、條件感知比較分析與細胞比例估計。整體架構包含三大層：(1) 嵌入層，直接使用預訓練表徵，不存取原始計數矩陣；(2) 查詢分類與路由模組，自動判斷查詢類型並分派至基因標記評分、語義匹配或倒數排名融合管線；(3) 分析模組集，涵蓋 60 多組基因集的路徑活性評分、280 多對經策展的配體-受體交互預測、條件感知比較分析及細胞類型比例估計。核心演算法機制為倒數排名融合 (RRF) 結合詞彙與語義分數，並由 LLM 依據檢索結果生成具依據的假設。資料前處理僅涉及將單細胞資料轉為預訓練模型的嵌入向量，摘錄未說明具體特徵選取或正規化細節。訓練目標與損失函數：摘錄未提供預訓練或微調階段的損失函數、最佳化策略。推論流程：使用者查詢 → 分類器 → 對應管線計算分數 → RRF 融合 → 排序輸出 → 分析模組計算下游指標 → LLM 解釋生成假設。關鍵差異：與 CellWhisperer、BM25 等僅依賴詞彙或單一模態檢索不同，ELISA 融合表徵嵌入、語義檢索與 LLM 推理，且所有分析直接在嵌入空間運作，無需原始計數矩陣。

## 結果
實驗跨越六個涵蓋發炎性肺病、兒童與成人癌症、類器官、健康組織與神經發育的 scRNA-seq 資料集。ELISA 在細胞類型檢索上顯著優於 CellWhisperer、BM25 與隨機基線（合併排列檢定 p < 2×10⁻⁵），基因特徵查詢的平均倒數排名效應量 Cohen's d = 5.98。複現已發表生物發現的平均綜合得分為 0.88。並能透過具依據的 LLM 推理產生候選假設。摘錄未提供更細緻的數值指標（如各資料集單獨 MRR、召回率等）。

## 限制與展望
資料限制：僅在六個資料集驗證，缺乏大規模獨立測試集與跨平台泛化證據。方法限制：所有分析僅基於嵌入向量，未使用原始計數矩陣可能遺失表達量細節；查詢分類器、RRF 融合權重、LLM 提示設計等超參數未揭露。評估限制：僅報告綜合指標與排列檢定，缺乏統計功效分析、消融實驗細節。部署風險：LLM 生成假設可能產生幻覺，需專家審核。後續研究方向：擴展更多組織類型、引入多模態資料、公開完整訓練細節與消融實驗以強化可重現性。
