# 論文 02：AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- 日期：2026-11-20
- 來源層級：Tier 3
- 期刊/會議/來源：arXiv
- Venue：arXiv preprint
- 發布時間：2026-11-19T17:57:59+00:00
- URL：http://arxiv.org/abs/2611.26510v1
- PDF：https://arxiv.org/pdf/2611.26510v1.pdf
- DOI：
- arXiv：2611.26510
- 影響指標：N/A (preprint)
- 影響指標來源：arXiv preprint (not peer-reviewed journal/conference)
- 引用數：0
- 解析程度：fulltext / html
- 全文來源：https://arxiv.org/html/2611.26510
- 全文字數：54790（pages=0, ocr_pages=0）
- GitHub/Code：https://github.com/RUCAIBox/AutoMaster
- 配對 Repo：RUCAIBox/AutoMaster

## 摘要
Task success alone does not specify which behaviors post-training should reinforce. Even successful teacher trajectories can contain unsupported assumptions, unproductive repetition, or superficial verification. We propose Skill-FT (Skill-Guided Fine-Tuning), which uses natural-language skills to suppress undesirable habits and elicit underrepresented effective behaviors during teacher rollouts, then fine-tunes a target model on the resulting trajectories. We introduce AutoMaster, an autonomous post-training system in which an LLM agent develops these interventions through trajectory analysis, skill design, data selection, and feedback from rollouts and target-model evaluation. Across Terminal, Search, and software engineering tasks with 4B and 9B target models, AutoMaster improves mean performance over Vanilla SFT on successful unguided teacher trajectories by 1.42-8.99 percentage points, with the teacher, task pool, training set size, and SFT recipe held fixed. Together with the ablations and trajectory analyses, these results suggest that behavioral shaping can make a fixed model a more effective teacher. We further find that retaining skill instructions during SFT yields higher mean performance than removing them across all six settings, despite their absence at evaluation and identical supervised outputs. These findings suggest that preserving skill context as part of a training demonstration can support better behavioral internalization.

## 背景與目的
本文針對後訓練階段中「任務成功」無法完整指定應強化行為的問題，指出即使成功的教師軌跡仍可能包含未經支持的假設、無效重複或表面驗證等不良習慣，且理想行為在未引導軌跡中常被低估。研究提出 Skill-FT（技能引導微調）與 AutoMaster 自主後訓練系統，旨在以自然語言技能引導教師生成更優質的示範軌跡，並保留技能指令於訓練輸入中，使學生模型內化更有效的行為模式，從而在固定教師、任務池、訓練資料量與 SFT 配方不變的條件下提升學生表現。

## 方法
AutoMaster 採用雙層迴圈架構。內層迴圈由 LLM 代理（Codex 中的 GPT-6 Astra）負責：先檢視訓練任務與初始教師/學生軌跡，發現需抑制的壞習慣與缺乏的好行為；設計自然語言技能（附加於系統提示詞），並在小規模試驗中驗證技能是否能誘導預期行為且不引入新問題；根據試驗軌跡修訂技能內容與適用範圍，再擴大至批次教師推演，並依任務結果與展示行為挑選示範資料（亦可保留未引導但行為良好的教師軌跡）。外層迴圈：每輪從相同初始學生檢查點（Qwen3.5-4B/9B）以標準 SFT 微調於內層選出的軌跡，訓練輸入保留教師推演時使用的技能指令；評估時學生不使用生成技能，依基準官方協議執行。代理接收評估分數與軌跡，比對歷史技能、教師推演與訓練集，決定下一輪是否修訂技能、調整任務覆蓋或重新選擇示範。基礎設施透過 Model Context Protocol (MCP) 存取任務、提交教師推演與 SFT 作業；推演與評估在共享沙箱叢集並行執行；SFT 完成後自動排程評估，SGLang 直接從共享檢查點存儲載入權重；實驗記錄將每輪學生的評估、檢查點、訓練集與技能關聯，支援代理追溯與決策。教師模型固定為 DeepSeek-V4-Pro-Preview，任務池為 Terminal-Bench 2.1、BrowseComp Lite-185、Doc2Repo 各隨機抽樣 1,000 任務，訓練集固定 512 條成功軌跡。

## 結果
在 Terminal、Search、軟體工程三領域、4B 與 9B 兩種學生模型共六組設定中，AutoMaster 相較於 Vanilla SFT（隨機抽樣未引導成功教師軌跡）平均提升 1.42–8.99 個百分點。消融實驗顯示，在所有六組設定中，保留技能指令於 SFT 訓練輸入的表現均優於移除技能指令，即使評估階段不提供技能。軌跡分析進一步說明技能引導能改善教師行為弱點，即便雙方均達到任務成功。摘錄未提供各基準具體數值與統計顯著性細節。

## 限制與展望
實驗僅涵蓋三個領域、兩種學生模型規模、單一固定教師模型與固定訓練集大小，且依賴專有模型（GPT-6 Astra、DeepSeek-V4-Pro-Preview）作為代理與教師，復現性受限。基礎設施與 MCP 介面細節未完全公開，可能影響他人部署。技能設計由 LLM 代理自動生成，潛在偏誤與穩定性未深入探討。後續研究可擴展至更多任務、更大模型、不同教師與更多樣的技能表示，並系統性評估技能保留對行為內化的機制。
