# 論文 02：Hyperbolic Large Language Models

- 日期：2026-11-14
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
大型語言模型（LLM）在多領域表現優異，但現有模型多在歐幾里得平坦空間學習 token 嵌入，難以捕捉真實世界數據中普遍存在的非歐幾里得層級結構（如蛋白質網絡、語言句法樹、知識圖譜等）。雙曲幾何因其負曲率特性，能以指數級空間增長自然建模樹狀層級，且在低維即具高表達容量，成為增強語義表達與多尺度推理的潛在表示空間。本文旨在系統梳理將雙曲幾何融入 LLM 的最新進展，提出四大類技術分類，並建立數學與架構框架，為後續研究奠基。

## 方法
本文將雙曲 LLM（HypLLM）歸類為四類：(1) 經指數/對數映射的雙曲 LLM，利用 exp/log map 在切空間與雙曲流形間轉換，保留歐氏運算便利性；(2) 雙曲微調模型，在預訓練歐氏 LLM 基礎上，將部分層或嵌入映射至雙曲空間進行微調；(3) 完全雙曲 LLM，全模型參數與運算均在雙曲流形（如 Lorentz 模型）上進行，採用 Lorentz 變換與雙曲注意力機制，避免切空間投影損失；(4) 雙曲狀態空間模型，將 Mamba 等 SSM 架構推廣至雙曲空間，利用雙曲線性遞歸捕捉長距依賴。 基礎幾何方面，採用 Poincaré 球模型（ℬⁿ_r）與 Lorentz 模型（ℒⁿ⁺¹_r）兩種同構表示。Poincaré 球以開單位球為定義域，度量張量含共形因子 λ_x=2/(1-‖x‖²)，測地線為弧線，適合梯度優化；Lorentz 模型將雙曲空間嵌入 (n+1) 維閔可夫斯基時空，採用 Minkowski 內積 ⟨x,y⟩_L=-x₀y₀+∑xᵢyᵢ，測地距離有閉式解，數值穩定性較佳。兩模型可經由座標映射互換。 核心運算為指數映射 exp_x: T_xℳ→ℳ 與對數映射 log_x: ℳ→T_xℳ，連接流形與切空間。以 Poincaré 球為例，exp_x(v)=x⊕_r tanh(λ_x‖v‖/(2r))·(rv/‖v‖)，其中 ⊕_r 為 Möbius 加法；log_x(y) 則為逆運算。優化採用黎曼優化（如 Riemannian SGD、Riemannian Adam）或投影歐氏更新，確保參數保持於流形上。 輸入為 token 序列，輸出為下一 token 分布或下游任務標籤。架構上，Transformer 版本將注意力機制的查詢/鍵/值投影至雙曲空間，採用雙曲內積計算注意力分數；SSM 版本則在雙曲空間定義狀態轉移矩陣與輸入投影。關鍵差異在於完全雙曲模型全程保持負曲率幾何，而混合模型僅在嵌入或特定層引入雙曲操作。

## 結果
摘錄未提供可驗證數字。文中定性指出：雙曲嵌入在詞彙蕴含預測、詞相似度、類比與上位詞檢測上優於歐氏對應模型；Nickel & Kiela 實驗顯示 5 維雙曲模型優於 200 維歐氏模型於 WordNet 名詞層級；預訓練 LLM 內部嵌入呈現冪律分佈（α≈1.9）與 δ-雙曲性（≈0.08–0.12），實證支持雙曲幾何與語言表示的天然契合。基準測試部分（第 4 節）於摘錄中未給出具體指標。

## 限制與展望
目前研究面臨：(1) 缺乏統一評測基準與標準化指標，難以跨模型公平比較；(2) 雙曲運算（如 Möbius 加法、指數/對數映射）計算開銷較大，數值穩定性在高維或極端曲率下仍具挑戰；(3) 完全雙曲 Transformer 的注意力機制在雙曲空間的理論性質（如梯度流動、收斂性）尚待深入分析；(4) 多模態融合時，視覺/音頻特徵與文本雙曲表示的對齊策略尚未成熟；(5) 大規模預訓練資源需求高，現有開源實現多為小規模驗證。後續方向包括：建立標準化 HypLLM 基準、開發高效雙曲核算子、探索曲率自適應機制、以及在蛋白質摺疊、知識圖譜推理等層級密集任務上的大規模實證。
