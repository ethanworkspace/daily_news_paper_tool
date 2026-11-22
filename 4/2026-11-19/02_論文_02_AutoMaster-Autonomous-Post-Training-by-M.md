# 論文 02：AutoMaster: Autonomous Post-Training by Making the Same Model a Better Teacher

- 日期：2026-11-19
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
論文指出僅靠任務成功無法指定後訓練應強化的行為，成功教師軌跡仍可能包含未經支持的假設、無效重複或表面驗證。因此提出 Skill-FT 與 AutoMaster，透過自然語言技能引導教師行為，並自主設計、選擇軌跡進行微調，以提升固定模型作為教師的效能。

## 方法
Skill-FT 將自然語言技能附加至系統提示，引導教師在推演時抑制不良習慣、誘發未充分展現的有效行為。AutoMaster 由 LLM 代理執行雙層迴圈：內層設計技能、進行小規模試推演並修正，篩選具價值軌跡；外層以保留技能指令的軌跡對學生模型進行 SFT，評估時不提供技能，並依學生表現決定下一輪干預。輸入為固定教師、任務池與初始學生檢查點。

## 結果
在 Terminal、Search、軟體工程三類任務上，使用 Qwen3.5-4B/9B 作為學生模型，AutoMaster 相較 Vanilla SFT 平均提升 1.42–8.99 個百分點（教師、任務池、訓練集大小、SFT 配方固定）。保留技能指令進行 SFT 在所有六種設定下均優於移除指令，顯示技能上下文有助行為內化。

## 限制與展望
實驗僅涵蓋三個基準與兩種模型規模，教師模型固定未探討不同教師效果；自主代理的技能設計泛化性、計算成本與更廣泛任務的表現仍待驗證。
