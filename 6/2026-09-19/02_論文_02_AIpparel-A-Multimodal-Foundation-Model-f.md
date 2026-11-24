# 論文 02：AIpparel: A Multimodal Foundation Model for Digital Garments

- 日期：2026-09-19
- 來源層級：Tier 1
- 期刊/會議/來源：2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- Venue：2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
- 發布時間：2025-06-10T00:00:00+00:00
- URL：https://www.semanticscholar.org/paper/d5b17f95e1d63ecf3ba0cee690464550da9ab833
- PDF：https://arxiv.org/pdf/2412.03937
- DOI：10.1109/cvpr52734.2025.00762
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：31
- 解析程度：fulltext / pdf
- 全文來源：https://arxiv.org/pdf/2412.03937
- 全文字數：96952（pages=27, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Apparel is essential to human life, offering protection, mirroring cultural identities, and showcasing personal style. Yet, the creation of garments remains a time-consuming process, largely due to the manual work involved in designing them. To simplify this process, we introduce AIpparel, a multimodal foundation model for generating and editing sewing patterns. Our model fine-tunes state-of-the-art large multimodal models (LMMs) on a custom-curated large-scale dataset of over 120,000 unique garments, each with multimodal annotations including text, images, and sewing patterns. Additionally, we propose a novel tokenization scheme that concisely encodes these complex sewing patterns so that LLMs can learn to predict them efficiently. AIpparel achieves state-of-the-art performance in single-modal tasks, including text-to-garment and image-to-garment prediction, and enables novel multimodal garment generation applications such as interactive garment editing. The project website is at https: //georgenakayama.github.io/AIpparel/.

## 背景與目的
服裝設計與製版過程高度依賴人工，耗時且需專業知識。現有基於深度學習的縫紉圖樣生成方法多為單一模態（如僅支援文字、圖像或 3D 點雲），難以整合多模態輸入，且缺乏大規模多模態標註資料集。本文旨在建立首個多模態縫紉圖樣基礎模型 AIpparel，解決資料稀缺與模型擴展兩大瓶頸，貢獻包含：(1) 構建 GCD-MM，擴充最大公開縫紉圖樣資料集 GCD，新增超過 12 萬件服裝的文字描述、渲染圖像與編輯指令；(2) 設計高效的縫紉圖樣 Tokenization 方案，將複雜幾何編碼為簡潔 Token 序列；(3) 在 LLaVA 1.5-7B 上微調，實現文字、圖像與圖樣的多模態生成與編輯。

## 方法
方法分為資料構建與模型微調兩階段。 1. 多模態資料集 GCD-MM：基於程序生成的 GCD 資料集，利用規則演算法從設計參數產生短標題（服裝類型、特徵），再餵給 GPT-4o 連同渲染圖生成詳細自然語言描述，減少幻覺。編輯標註則使用 GarmentCode 程式抽象，手動定義長度調整、領型變更、帽袖增減等編輯操作，並以模板產生對應文字指令，形成成對編輯樣本。 2. 縫紉圖樣 Tokenization：將圖樣表示為面板集合與縫合資訊。引入四個特殊 Token 標記服裝與面板的起迄（<SoG>, <EoG>, <SoP>, <EoP>），面板名稱用 LLaVA 文字 tokenizer 編碼，面板剛體變換以 <R> Token 表示。邊類型（直線、二/三次貝茲曲線、圓弧）各對應起始與閉合 Token（<L>/<cL> 等）。縫合關係以標籤 Token 集合 {<t1>…<tM>, <tN>} 標記於邊上，未縫合邊用 <tN>。頂點座標與 3D 變換以位置嵌入方式注入 Token 序列，避免固定長度零填充導致的上下文爆炸。 3. 微調目標與流程：以 LLaVA 1.5-7B 為基座，輸入多模態（文字、圖像、既有圖樣 Token），自回歸預測輸出 Token 序列，解碼後得到可直接用於布料模擬的縫紉圖樣。訓練目標包含離散 Token 預測與連續參數（頂點座標、變換）的回歸損失，採用標準交叉熵與 L2 損失聯合最佳化。推理時依多模態條件自回歸採樣生成 Token 序列，再解碼為幾何圖樣。

## 結果
摘錄未提供可驗證數字。作者報告 AIpparel 在單模態任務（文字生成圖樣、圖像生成圖樣）達到最先進效能，且以較大幅度超越既有基線；同時展示多模態新應用，如語言指導的互動式圖樣編輯。定性上，生成圖樣幾何複雜度高、多樣性佳，並可直接輸入布料模擬產生 3D 服裝。

## 限制與展望
資料集為程序生成合成資料，可能無法完全涵蓋真實服裝的幾何變異與材質行為；Tokenization 雖簡潔，但對極高頂點數或特殊拓撲結構的表達能力仍有上限；微調基於 LLaVA 1.5-7B，繼承其語言與視覺偏誤，且未探討更大規模基座模型的擴展性；評估僅限於模擬環境，缺乏實體製版與穿著測試驗證；編輯指令模板化，自然語言泛化能力有待進一步驗證。後續研究可朝真實掃描資料融合、更豐富編輯語義、以及端到端可微分模擬優化方向發展。
