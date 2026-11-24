# 論文 01：Multi-Agent collaboration as a complementary architecture for AI-generated medical examination items.

- 日期：2026-09-14
- 來源層級：Tier 2
- 期刊/會議/來源：NPJ digital medicine
- Venue：NPJ digital medicine
- 發布時間：2026-09-14T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/42736348/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13575248/
- DOI：10.1038/s41746-026-03187-z
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：552（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Qian et al. showed single LLMs can generate acceptable knowledge-based questions but struggle with higher-order reasoning. We argue this is architectural: decomposing item development into specialized agents for drafting, critique, and iterative adversarial refinement improves quality. In blinded evaluation for China's National Medical Licensing Examination, multi-agent outputs received 57.7% of expert preferences, compared with 42.3% for the single-model baseline, indicating a viable path to surpass current limits in AI-assisted item generation.

## 背景與目的
現有單一大型語言模型雖能產出可接受的知識型試題，但在需要高階推理與臨床判斷的醫學考題上表現不足。作者認為此缺口源於單一模型架構無法同時兼顧內容生成、邏輯檢核與迭代優化，因此提出將試題開發流程拆解為三類專門代理：負責初稿撰寫的草稿代理、負責邏輯與醫學正確性評審的評審代理，以及負責對抗式迭代修正的優化代理。透過多代理協作與迭代對抗機制，期望在保持知識覆蓋的前提下提升推理深度與題目品質，進而突破目前 AI 輔助出題的性能上限。

## 方法
問題設定：輸入為醫學考試大綱與知識點描述，輸出為符合中國國家醫師資格考試格式的單選題（題幹、選項、答案與解析）。系統架構包含三個專用代理並行協作：(1)草稿代理根據大綱生成初版題目；(2)評審代理對初版進行邏輯一致性、醫學正確性、難度適配度等多維度評分並產出具體修改建議；(3)優化代理依據評審回饋進行對抗式迭代修正，若評審分數未達門檻則再次觸發草稿與評審循環，直到滿足品質門檻或達到最大迭代次數。資料表示方面，將大綱與知識點編碼為結構化提示詞，並引入醫學知識圖譜作為外部檢索輔助，確保術語與指引一致。訓練目標未於摘錄中詳細揭露，推測採用以專家偏好為監督訊號的強化學習或偏好優化，損失函數結合生成質量評分與答案正確性。推理流程為：輸入→草稿生成→評審打分與建議→優化修正→重複評審直到收斂→輸出最終題目。與單一模型基線的關鍵差異在於引入明確的角色分工與多輪對抗迭代，使邏輯檢核與內容生成解耦，並能在生成過程中動態修正錯誤。

## 結果
在雙盲專家評測中，針對中國國家醫師資格考試生成的試題，多代理系統獲得 57.7% 的專家偏好，單一模型基線獲得 42.3%。摘錄未提供更細項的統計指標（如準確率、F1、各類題型表現）或消融實驗數據，僅能觀察到多代理協作在專家主觀品質判斷上顯著優於單一模型，顯示架構分工對提升高階推理題目品質有正向效果。

## 限制與展望
研究僅在單一國家級考試與單一語言環境驗證，缺乏跨學科、跨語言與不同題型的泛化證據；評審代理的評分標準、迭代停止條件與超參數未公開，難以復現；專家偏好評估雖為盲測，但樣本數與評審者背景未揭露，可能存在選擇偏差；且未進行消融實驗以量化各代理貢獻，後續需擴大評估範圍並公開系統細節以確認穩健性。
