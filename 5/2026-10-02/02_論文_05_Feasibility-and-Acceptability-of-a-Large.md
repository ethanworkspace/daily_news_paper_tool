# 論文 05：Feasibility and Acceptability of a Large Language Model-Based Electronic Health Record Summarization Tool in Inpatient Care.

- 日期：2026-10-02
- 來源層級：Tier 2
- 期刊/會議/來源：Applied clinical informatics
- Venue：Applied clinical informatics
- 發布時間：2026-10-01T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43064362/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13787951/
- DOI：10.1055/a-3001-9600
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1874（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
BACKGROUND: Current health care practice requires providers to manually navigate through different electronic health record (EHR) sections to perform chart review and construct a complete picture of the patient's condition. This process is both time-consuming and inefficient. OBJECTIVES: This initiative evaluated the feasibility, acceptability, and perceived usefulness of a large language model (LLM)-based EHR summarization tool in streamlining inpatient care delivery by aggregating and synthesizing patient data into concise summaries. METHODS: A three-phase evaluation was conducted involving 32 providers across seven specialties, using a tool called "Inpatient Insights Summary" in the Epic Systems Hyperdrive EHR product. The tool summarizes data in three summary types: "recent events" (discrete data), "recent notes" (clinical notes), and "patient story" (longitudinal narrative). Feedback was collected through embedded and external forms, including a modified Physician Documentation Quality Instrument (PDQI-9). RESULTS: The tool generated summaries that clinicians rated as accurate and comprehensive; clinicians detected hallucinations in 6.2% of summaries during routine use. No significant differences in user feedback were found across summary types. Statistically significant differences in feedback were noted between the proof-of-concept and pilot phases for thoroughness, usefulness, organization, and clarity, indicating improved summaries through prompt engineering refinement. CONCLUSION: These findings suggest that LLM-based EHR summarization tools can produce summaries that clinicians rate as accurate and comprehensive, with hallucinations infrequently detected, and may support clinical workflow efficiency. Further research is needed to validate these findings in larger settings and assess the effect on clinical practice and patient care.

## 背景與目的
本研究旨在評估基於大型語言模型（LLM）的電子健康紀錄（EHR）摘要工具在住院照護中的可行性、接受度與感知實用性。現行臨床流程要求醫療人員手動瀏覽多個 EHR 區段以完成病歷審閱，耗時且效率低落。研究團隊開發「Inpatient Insights Summary」並整合至 Epic Systems Hyperdrive 產品，提供三類摘要：近期事件（離散資料）、近期紀錄（臨床筆記）與患者故事（縱向敘事），期望以自動化彙整加速臨床決策。

## 方法
研究採三階段評估設計，招募 32 位來自七個專科的臨床提供者，於 Epic Systems Hyperdrive 環境中使用「Inpatient Insights Summary」工具。工具輸入為患者在住院期間的結構化離散資料、自由文本臨床筆記及縱向病程記錄；輸出為三種摘要類型：(1) recent events——針對離散資料（如生命徵象、檢驗結果、用藥紀錄）生成近期事件摘要；(2) recent notes——對臨床筆記進行語意壓縮；(3) patient story——將多次就醫紀錄串聯為連貫的縱向敘事。核心機制為以提示工程引導 LLM 依據預設模板進行資訊抽取、去重與敘事重組，具體模型架構、參數量與訓練細節於摘錄中未揭露。資料前處理包含將 EHR 原始欄位轉為結構化 JSON、去除識別碼與無關噪聲，再餵入提示模板。評估階段分為概念驗證、試點與擴展三階段，每階段收集嵌入式表單與外部問卷，並採用修改版醫師文件品質量表（PDQI-9）量化摘要的完整性、實用性、組織性與清晰度。統計分析使用配對樣本檢定比較各階段評分差異，並記錄臨床醫師在常規使用中偵測到的幻覺比例。與既有手動病歷審閱相比，本工具的關鍵差異在於自動化跨區段彙整、即時產出三類不同粒度摘要，並內建提示迭代機制以逐步改善輸出品質。

## 結果
結果顯示，臨床醫師對生成摘要的準確性與完整性給予正面評價；常規使用中醫師偵測到幻覺的比例為 6.2%。三種摘要類型在使用者回饋上無顯著差異。從概念驗證階段到試點階段，完整性、實用性、組織性與清晰度四項 PDQI-9 子量表評分均達統計顯著提升，顯示提示工程迭代有效改善摘要品質。摘錄未提供具體 PDQI-9 分數、樣本量變化或效果量數值。

## 限制與展望
研究限制包括：樣本僅 32 位提供者、單一醫療系統與單一 EHR 平台，外部效度有限；評估依賴主觀問卷與 PDQI-9，缺乏客觀臨床結果（如決策時間、錯誤率）驗證；幻覺偵測僅靠醫師自報，可能低估真實發生率；提示工程細節、LLM 模型版本與超參數未公開，難以複現；未探討長期部署對工作流程、醫師疲勞及患者安全的影響。後續研究建議擴大多中心樣本、引入客觀效能指標、進行前瞻性隨機對照試驗，並公開提示與模型配置以利驗證。
