# 論文 02：Hyperbolic Large Language Models

- 日期：2026-11-12
- 來源層級：Tier 2
- 期刊/會議/來源：SIAM Review
- Venue：SIAM Review
- 發布時間：2026-11-12T00:00:00+00:00
- URL：https://doi.org/10.1137/25m1795248
- PDF：https://arxiv.org/pdf/2509.05757
- DOI：10.1137/25m1795248
- arXiv：2509.05757
- 影響指標：2yr_mean_citedness=7.85, h_index=253, i10_index=1463 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: SIAM Review
- 引用數：16
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2509.05757
- 全文字數：111664（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/sarangp2402/Hyperbolic-LLM-Models
- 配對 Repo：sarangp2402/Hyperbolic-LLM-Models

## 摘要
Large language models (LLMs) have achieved remarkable success and demonstrated superior performance across various tasks, including natural language processing (NLP), weather forecasting, biological protein folding, text generation, and solving mathematical problems. However, many real-world data exhibit highly non-Euclidean latent hierarchical anatomy, such as protein networks, transportation networks, financial networks, brain networks, and linguistic structures or syntactic trees in natural languages. Effectively learning intrinsic semantic entailment and hierarchical relationships from these raw, unstructured input data using LLMs remains an underexplored area. Due to its effectiveness in modeling tree-like hierarchical structures, hyperbolic geometry—a non-Euclidean space—has rapidly gained popularity as an expressive latent representation space for complex data modeling across domains such as graphs, images, languages, and multimodal data. Here, we provide a comprehensive and contextual exposition of recent advancements in LLMs that leverage hyperbolic geometry as a representation space to enhance semantic representation learning and multiscale reasoning. Specifically, the paper presents a taxonomy of the principal techniques of hyperbolic LLMs (HypLLMs) in terms of four main categories: (1) hyperbolic LLMs through exp/log maps; (2) hyperbolic fine-tuned models; (3) fully hyperbolic LLMs; and (4) hyperbolic state-space models. We also explore crucial potential applications and outline future research directions. A repository of key papers, models, datasets, and code implementations is available at https://github.com/sarangp2402/Hyperbolic-LLM-Models .

## 背景與目的
大型語言模型（LLM）在歐氏空間學習 token 嵌入，難以捕捉真實世界數據中普遍存在的非歐氏層級結構（如蛋白質網絡、語言句法樹）。雙曲幾何因負曲率特性，能以指數級增長空間自然建模樹狀層級，且在低維即具高表示容量，成為增強語義表徵與多尺度推理的潛在空間。現有研究雖在圖神經網絡、詞嵌入等領域引入雙曲幾何，但如何系統整合至 LLM 仍分散於文獻中。本文旨在提供首個全面綜述，建立雙曲 LLM（HypLLM）的數學與架構框架，提出四大類技術分類法，並探討基準測試、應用與未來方向，填補領域空白。

## 方法
本文為綜述論文，方法層面著重於建立 HypLLM 的理論基礎與技術分類法。問題設定：輸入為原始非結構化數據（文本、圖、多模態），輸出為雙曲流形上的層級語義表徵，目標在保持語義蘊含與樹狀結構。整體架構分四類：(1) 經指數/對數映射的雙曲 LLM：利用 exp/log map 在切空間與雙曲流形間轉換，將歐氏注意力機制投影至雙曲空間，保留 Transformer 架構並引入黎曼優化；(2) 雙曲微調模型：預訓練歐氏 LLM 參數固定，僅將嵌入層或輸出層映射至雙曲空間（如 Poincaré 球或 Lorentz 模型）進行微調；(3) 完全雙曲 LLM：全模型參數（注意力、前饋網絡、層歸一化）皆定義於雙曲流形，採用 Lorentz 變換或陀螺向量運算實現端到端雙曲計算，避免切空間往返；(4) 雙曲狀態空間模型：將 Mamba 等 SSM 架構推廣至雙曲空間，利用雙曲線性遞歸捕捉長程依賴。核心模組包括：雙曲表示模型（Poincaré 球與 Lorentz 雙曲面），二者同構且可經坐標映射互換；指數映射 exp_x(v) 將切向量 v 沿測地線映回流形，對數映射 log_x(y) 將流形點投影回切空間，支撐梯度下降與注意力計算；Möbius 加法與 Lorentz 內積定義雙曲空間的向量運算與距離度量。資料表示採用詞頻符合 Zipf 定律的冪律分布（α≈1.9）與 δ-雙曲性（≈0.08–0.12）作為語言固有雙曲結構的實證依據。訓練目標沿用語言建模損失，但優化器需為黎曼優化（如 Riemannian Adam）或投影歐氏更新，確保參數停留於流形。推理流程：輸入嵌入→雙曲編碼器→雙曲注意力/狀態轉移→雙曲解碼器→經對數映射回切空間輸出機率。關鍵差異在於完全雙曲模型消除混合歐氏/雙曲操作的數值不穩定，且理論上保證層級結構無失真嵌入。

## 結果
摘錄未提供可驗證數字。本文為綜述，主要貢獻在於建立 HypLLM 的四大類分類法、整理雙曲幾何數學基礎（Poincaré 球、Lorentz 模型、exp/log map、黎曼優化）、彙總跨領域應用（NLP、視覺、多模態）並指出基準測試缺乏標準化、評估指標不一致等問題。定性結論顯示：雙曲幾何與語言固有層級結構高度吻合，完全雙曲架構在理論上優於混合方法，但實際部署面臨數值穩定性、計算效率與現有硬體生態兼容性的挑戰。

## 限制與展望
本文作為綜述，未提出新實驗，缺乏統一基準下的量化比較；現有 HypLLM 研究多基於小規模模型或特定任務，大規模預訓練的可行性與擴展律尚未驗證。雙曲運算（如 arcosh、Möbius 加法）計算開銷大，且對數值精度敏感，現有 GPU 加速庫支援有限。評估體系碎片化，缺乏專門針對層級推理、多尺度泛化的標準基準。未來方向包括：開發高效雙曲核算子、設計雙曲專用預訓練目標、建立統一評估套件、探索雙曲幾何與提示工程、對齊技術的結合，以及解決雙曲空間中長序列的記憶效率問題。
