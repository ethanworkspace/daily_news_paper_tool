# 論文 01：A multimodal foundation model for molecular and morphologic data in oncology

- 日期：2026-11-21
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature Cancer
- Venue：Nature Cancer
- 發布時間：2026-11-20T00:00:00+00:00
- URL：https://doi.org/10.1038/s43018-026-01252-w
- PDF：https://arxiv.org/pdf/2501.16652
- DOI：10.1038/s43018-026-01252-w
- arXiv：2501.16652
- 影響指標：2yr_mean_citedness=16.75, h_index=147, i10_index=656 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Cancer
- 引用數：134
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2501.16652
- 全文字數：173337（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/prov-gigapath/prov-gigapath
- 配對 Repo：prov-gigapath/prov-gigapath

## 摘要
（無摘要）

## 背景與目的
研究問題：現有病理基礎模型多為 patch encoder，僅能編碼小區域，需額外訓練才能處理 gigapixel 全切片影像（WSI），且缺乏多模態分子數據指導。現有方法在資料稀缺的罕見癌症或治療反應預測任務上表現受限。本文目的：提出 Threads，一個能直接產生任意大小 WSI 通用表示的 slide-level 基礎模型，透過大規模多模態對比學習，將 H&E 切片與配對的基因組/轉錄組特徵對齊，以捕捉組織潛在分子組成。貢獻：構建目前最大的配對多模態資料集 MBTG-47k（47,171 樣本），採用跨模態對比學習預訓練，並在 54 項腫瘤學任務上達到 SOTA，展現優異泛化與標籤效率。

## 方法
Threads 架構包含兩大組件：(1) ROI 編碼器：採用 CONCHv1.5（ViT-Large），於數百萬影像塊經由 ROI 與文字描述的多模態學習預訓練；(2) 切片編碼器：利用注意力機制聚合 tile embeddings 為單一 slide embedding。預訓練資料 MBTG-47k 來自四來源（MGH、BWH、TCGA、GTEx），每樣本含 H&E WSI 及鄰近切片的分子特徵。分子特徵編碼方式：大量 RNA-seq 轉錄組資料（MGH、TCGA、GTEx）以預訓練於 570 萬細胞的單細胞基礎模型編碼；靶向基因面板的 SNV、indel、CNV 基因組資料（BWH）以多層感知機編碼。訓練目標：跨模態對比學習，將 slide embedding 與對應分子 embedding 對齊。下游評估：以線性探針（固定正則化的邏輯回歸）在 54 項任務（臨床亞型分級 8 項、基因突變預測 21 項、IHC 狀態 12 項、治療反應與生存預測 13 項）上評估，指標含 AUC、二次 Cohen's kappa、平衡準確率、c-index。基線模型包括 Prism（Virchow patch encoder + Perceiver）、GigaPath（ViT-Giant + LongNet）、Chief（CTransPath + ABMIL）。另進行外部隊列遷移性驗證與小樣本標籤效率實驗。

## 結果
線性探針整體表現：Threads 較 Prism、GigaPath、Chief 絕對提升 6.3%、9.9%、6.7%（P<<0.001）。各任務族群：臨床亞型分級較 Prism +2.1%、突變預測較 Chief +6.1%、IHC 狀態較 Prism +4.6%、預後較 Prism +8.9%。單一任務層面：Threads 勝過 Prism 44/54、Chief 49/54、GigaPath 54/54。具體指標：乳癌亞型 AUC 98.3%、肺癌亞型 AUC 98.2%、大腸癌分級二次 kappa 91.9%。遷移性測試：9 項外部任務中 8 項優於所有基線，肺癌亞型 98.4% AUC、乳癌亞型 96.5% AUC、ER/PR 狀態 88.5%/79.4% AUC。小樣本治療反應預測（36–183 病例）亦展現優勢。摘錄未提供可驗證的完整數值表格，僅呈現關鍵定量結果。

## 限制與展望
依目前可取得資料，無法確認完整限制條件。推測潛在限制包括：(1) 預訓練依賴配對分子數據，可能難以擴展至缺乏分子剖析的機構或罕見癌種；(2) 資料來源集中於美國特定醫院與公共資料庫，族群多樣性與批次效應未充分討論；(3) 模型規模（ViT-L + 注意力聚合）與計算需求未揭露，部署成本不明；(4) 僅針對 H&E 染色切片，其他染色或數位病理格式泛化性未驗證；(5) 分子模態僅涵蓋大量 RNA-seq 與靶向基因面板，全外顯子組或蛋白質組數據未納入；(6) 缺乏前瞻性臨床驗證與監管級效能評估。後續研究可探索更廣泛分子模態、多中心前瞻驗證、模型壓縮與解釋性增強。
