# 論文 04：Artificial Intelligence for the Verification of Nasogastric Tube Position in Chest Radiographs: A Systematic Review.

- 日期：2026-10-01
- 來源層級：Tier 2
- 期刊/會議/來源：Cureus
- Venue：Cureus
- 發布時間：2026-10-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43075324/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13792418/
- DOI：10.7759/cureus.118520
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：2090（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Nasogastric tube (NGT) malposition is a significant patient-safety concern, and chest radiography is commonly used to confirm tube position before the tube is used. This systematic review evaluated the diagnostic performance and clinical usefulness of artificial intelligence (AI) systems in assessing NGT or related enteric feeding-tube position on radiographs. PubMed, Embase via Ovid, IEEE Xplore, and the National Health Service (NHS) Knowledge and Library Hub were searched from inception up to September 1, 2026, with additional backward and forward citation searching. Studies were included if they evaluated AI-based assessment of tube position on radiographs, and risk of bias and applicability were assessed using appropriate tools. A total of 131 records were identified, 32 duplicates were removed, and 99 records were screened. Nineteen reports were sought for retrieval, three could not be retrieved, 16 underwent full-text assessment, and 13 studies were included. Most studies were retrospective, and one was a prospective silent NHS validation. Task-specific AI models generally performed well in internal or development datasets, and some external studies reported area under the receiver operating characteristic curve (AUROC) values above 0.90. However, performance was inconsistent across different hospitals and datasets, and several studies were limited by small numbers of unsafe tubes, class imbalance, selected patient groups, and the reuse of the same public datasets or related models. In the prospective NHS study, sensitivity for unsafe NGT position was 86.5% and negative predictive value (NPV) was 98%, although false-negative cases and AI processing failures still occurred. General-purpose multimodal large language models (LLMs) performed poorly, with sensitivity for abnormal NGT position ranging from 0% to 18.4%. Overall, AI may be useful for triage and clinical decision support, but current evidence does not support autonomous NGT verification. Further prospective, independent, multicentre studies in representative clinical populations are needed.

## 背景與目的
鼻胃管（NGT）錯置為重大病人安全隱憂，胸部 X 光為常規確認手段，但人工判讀存在誤差與延遲。現有文獻缺乏對 AI 系統評估 NGT 管位診斷效能與臨床實用性的系統性整合。本研究旨在透過系統性回顧，檢視 AI 於胸部 X 光判讀 NGT 或相關餵食管位之表現，並評估偏倚風險與適用性，以釐清 AI 是否可輔助或取代人工判讀。貢獻在於首次系統性綜合 13 項研究，指出任務特定 AI 模型在內部資料表現良好、部分外部驗證 AUROC 超過 0.90，但跨機構表現不一；通用多模態大型語言模型（LLM）表現極差；現有證據不支持自主驗證，需更多前瞻性多中心研究。

## 方法
本系統性回顧依 PRISMA 指引執行。搜尋來源包含 PubMed、Embase (Ovid)、IEEE Xplore 及 NHS Knowledge and Library Hub，檢索期間自建庫至 2026 年 9 月 1 日，並輔以前向與後向引文搜尋。納入標準為評估基於 AI 之管位判讀研究；排除非原始研究、非影像評估等。兩位獨立審查者進行標題/摘要篩選與全文評估，分歧由第三人仲裁。使用適當工具（摘錄未明確工具名稱）評估偏倚風險與適用性。篩選流程：131 筆記錄，去除 32 重複後 99 篩選，尋求 19 全文，3 篇無法取得，16 篇全文評估，最終納入 13 研究。多數為回顧性設計，僅 1 項為前瞻性 NHS 靜默驗證。資料綜合採描述性統計，報告 AUROC、敏感度、陰性預測值（NPV）等指標；未進行元分析。關鍵分層比較：任務特定 AI 模型（如 CNN 為主）與通用多模態 LLM（如 GPT-4V 等）分開分析。

## 結果
任務特定 AI 模型在內部/開發資料集表現良好，部分外部研究報告 AUROC > 0.90。然而，跨醫院與資料集表現不一致，主要受限於不安全管位樣本數少、類別不平衡、選擇性病患群、重複使用相同公共資料集或相關模型。前瞻性 NHS 研究顯示：不安全 NGT 管位敏感度 86.5%、NPV 98%，但仍出現假陰性與 AI 處理失敗。通用多模態 LLM 表現極差，異常管位敏感度僅 0%~18.4%。作者結論：AI 可作為分流與臨床決策輔助，但現有證據不支持自主 NGT 驗證；需進一步前瞻性、獨立、多中心、代表性臨床族群研究。

## 限制與展望
納入研究多為回顧性、單中心、樣本量小、不安全管位事件稀少、類別不平衡，且部分重複使用公共資料集，易導致過度擬合與泛化能力高估。系統性回顧本身未執行元分析，異質性高；搜尋截止 2026 年 9 月，可能遺漏最新研究；偏倚評估工具未明確說明。通用 LLM 評估研究極少，結論受限。潛在風險包括假陰性導致臨床傷害、AI 處理失敗造成判讀延遲。後續研究建議：大規模前瞻性多中心驗證、標準化評估指標與報告規範、探討 AI 整合臨床工作流程之安全性與成本效益。
