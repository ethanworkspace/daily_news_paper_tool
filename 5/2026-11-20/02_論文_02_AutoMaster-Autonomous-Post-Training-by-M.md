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
論文指出任務成功並不代表教師軌跡中的行為都值得強化，成功軌跡仍可能包含未經驗證的假設、無效重複或表面驗證。因此提出 Skill-FT 與 AutoMaster，透過自然語言技能引導教師行為，並在學生微調時保留技能指令，以改善行為內化。

## 方法
AutoMaster 採雙層迴圈：內層由 LLM 代理分析教師與學生初始軌跡，設計自然語言技能並附加於系統提示，進行小規模試驗滾軸驗證行為變化，再擴大批次滾軸並篩選具價值軌跡；外層以固定教師、任務池、訓練集大小與 SFT 配方，從同一初始檢查點微調學生，評估時不提供技能，並依學生表現決定下一輪技能修訂與資料選擇。

## 結果
在 Terminal、Search、軟體工程三領域、4B 與 9B 兩種模型共六組設定中，AutoMaster 平均表現優於 Vanilla SFT 1.42–8.99 個百分點；且在所有六組設定中，微調時保留技能指令均優於移除指令，即使評估時不提供技能。消融實驗與軌跡分析顯示行為塑形能使固定教師更有效。

## 限制與展望
實驗僅涵蓋三個基準與兩種模型規模，教師、任務池、訓練集大小與 SFT 配方固定，泛化性有待驗證；技能設計依賴 LLM 代理可能引入偏誤；技能指令保留效果的機制需進一步實證。
