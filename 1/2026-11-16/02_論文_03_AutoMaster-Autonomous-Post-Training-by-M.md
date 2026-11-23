# 論文 03：AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- 日期：2026-11-16
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
現有後訓練常以任務成功的教師軌跡進行監督微調，但任務成功無法指定應強化哪些行為；成功軌跡仍可能包含未經支持的假設、無效重複或表面驗證等不良習慣，且理想行為在成功軌跡中可能代表性不足。本文提出 Skill-FT 利用自然語言技能引導教師行為，並設計 AutoMaster 自主後訓練系統，透過軌跡分析、技能設計、資料選擇與學生模型評估回饋迭代優化，旨在使固定教師模型成為更有效的教師，並探討保留技能指令對學生內化行為的影響。

## 方法
問題設定：給定固定教師模型 π_T、固定訓練任務池與初始學生檢查點 θ_0，目標是透過技能引導教師產生優質示範，再對學生進行 SFT。輸入為任務 x 與基礎系統提示 p，輸出為教師軌跡 τ。核心模組：Skill-FT 將自然語言技能 s 附加至系統提示（p⊕s），引導教師在 rollout 時抑制不良習慣、誘發未充分呈現的有效行為。AutoMaster 採雙層迴圈：內層由 LLM 代理分析初始教師與學生軌跡，設計候選技能，進行小規模試驗 rollout，根據軌跡行為修訂技能與適用範圍，再擴大至批次 rollout 並依任務結果與示範行為挑選訓練集 D_r；外層以相同 θ_0 為起點對 D_r 執行標準 SFT，訓練時保留教師使用的技能指令於輸入中，評估時則移除技能。資料表示：每筆訓練樣本包含系統提示（含技能）、用戶查詢、教師動作與環境回饋序列。訓練目標為標準交叉熵損失的 SFT，優化策略為固定學習率與批次大小（論文未詳細列出超參數）。推論流程：學生模型在評估基準上直接生成動作，不接收技能。關鍵差異：傳統 Vanilla SFT 僅使用未引導的成功軌跡，而 AutoMaster 主動塑造教師行為並保留技能上下文，實現行為層面的干預與內化。基礎設施透過 MCP 介面提交 rollout 與 SFT 作業，共享檢查點存儲與隔離沙箱叢集支援並行執行。

## 結果
實驗在 Terminal-Bench 2.1、BrowseComp Lite-185、Doc2Repo 三基準上，使用 Qwen3.5-4B/9B 作為學生、DeepSeek-V4-Pro-Preview 為教師。AutoMaster 相較 Vanilla SFT（512 條未引導成功軌跡）在六種設定下平均提升 1.42–8.99 個百分點。消融顯示：在 SFT 時保留技能指令優於移除技能指令，於所有六種設定均獲得更高平均表現，且評估階段均不提供技能。軌跡分析進一步說明技能引導如何修正教師的未支持假設、重複與表面驗證等弱點。摘錄未提供更細粒度的數值或統計顯著性。

## 限制與展望
本文為預印本，僅在三個領域、兩種模型規模驗證，教師模型固定為 DeepSeek-V4-Pro-Preview，技能設計依賴 GPT-6 Astra 代理，基礎設施與 MCP 介面可能限制可重現性；評估未包含測試時技能，且未報告超參數細節、訓練成本與統計顯著性。後續研究可擴展至更多任務、模型與教師，探討技能自動發現的穩健性、技能指令保留的最佳策略，以及對長程推理與安全性的影響。
