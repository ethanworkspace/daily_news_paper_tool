# 論文 01：An all-in-one foundation model for multimodal medical image restoration and enhancement

- 日期：2026-10-21
- 來源層級：Tier 1
- 期刊/會議/來源：Nature Machine Intelligence
- Venue：Nature Machine Intelligence
- 發布時間：2026-10-13T00:00:00+00:00
- URL：https://doi.org/10.1038/s42256-026-01310-z
- PDF：
- DOI：10.1038/s42256-026-01310-z
- arXiv：
- 影響指標：2yr_mean_citedness=36.01, h_index=187, i10_index=954 (OpenAlex)
- 影響指標來源：OpenAlex source summary_stats: Nature Machine Intelligence
- 引用數：1
- 解析程度：fulltext / html
- 全文來源：https://doi.org/10.1038/s42256-026-01310-z
- 全文字數：42941（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/caoluyang0830/All-in-One-Medical-Image-Restoration
- 配對 Repo：caoluyang0830/All-in-One-Medical-Image-Restoration

## 摘要
（無摘要）

## 背景與目的
醫學影像品質對臨床診斷與下游 AI 分析至關重要，但常規影像常受雜訊、運動偽影、低對比度、低劑量採集或模態特有偽影降解。現有方法多為針對單一任務或模態的專用模型，缺乏跨模態統一處理能力。本文提出 AMIFound，旨在建立一個全能基礎模型，針對電腦斷層、磁振造影、正子發射斷層、內視鏡、超音波、眼底造影與 X 光等七大醫學模態，統一處理七類代表性降解模式，提升低品質臨床影像品質並保留臨床關鍵資訊，強化下游醫療 AI 工作流程。

## 方法
AMIFound 採用共享編碼器與動態路由專家修復池架構。輸入為七大模態（CT、MRI、PET、內視鏡、超音波、眼底、X 光）含七類降解模式的配對影像；輸出為增強後影像。模型於 376 萬對高品質與降解配對影像訓練，資料源自 TCIA、OpenNeuro、NITRC、Grand Challenge、Synapse、Kaggle、GitHub 等公開資料庫，涵蓋 MRI 34 組、CT 37 組、X 光 6 組、內視鏡 5 組、皮膚鏡 4 組、眼底 4 組、超音波 2 組、PET 1 組資料集。共享編碼器同時擷取模態與降解線索；動態路由機制依輸入特徵選擇專家修復路徑，實現自適應增強。資料前處理與載入管線參考 MoCE-IR、PromptIR、AirNet 實作。訓練目標針對單一與複合降解設計專用管線，以 PyTorch 實現。推論時編碼器提取特徵，路由模組分配專家，專家池並行或串聯處理，輸出修復影像。關鍵差異在於跨模態共享表示學習與輸入自適應的專家動態路由，區別於固定架構的任務專用或通用模型。

## 結果
跨七大模態實驗顯示，AMIFound 在全參考影像品質指標、臨床醫師主觀評估、複合降解魯棒性測試及真實臨床降解影像上，均優於 38 個任務專用與通用基線。視覺比較（圖 3）與醫師評分（圖 4）證實其修復效果。增強影像進一步提升 44 項疾病偵測任務、非小細胞肺癌腫瘤分期預測與生存風險分層表現，改善個體級預後排序（圖 6）。摘錄未提供可驗證數字，但定性結論為：跨模態一致超越基線、複合降解魯棒、臨床下游任務獲益明顯。

## 限制與展望
依目前可取得資料，無法確認完整限制。潛在限制包括：訓練資料僅來自公開資料集，可能存在選擇偏誤與模態不平衡；合成降解模式能否完整涵蓋真實臨床複雜降解尚待驗證；基礎模型規模龐大，部署算力需求高；未見前瞻性臨床試驗驗證；對未見模態或新型降解的泛化能力未量化。後續研究可朝真實世界多中心驗證、輕量化部署、持續學習適應新模態與降解方向推進。
