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
論文指出任務成功並不代表教師軌跡中的行為都值得強化，成功軌跡可能包含無根據假設、無效重複或表面驗證。因此提出 Skill-FT 利用自然語言技能引導教師行為，並構建 AutoMaster 自主後訓練系統，透過技能設計、軌跡分析與學生模型評估回饋，使固定教師模型成為更有效的教師。

## 方法
AutoMaster 採雙層迴圈：內層由 LLM 代理分析任務與初始軌跡，設計自然語言技能附加於系統提示，進行試驗性教師推演並篩選優質軌跡；外層以固定教師、任務池、訓練集大小與 SFT 配方，在保留技能指令的情況下對學生模型（Qwen3.5-4B/9B）進行監督微調，評估時不提供技能。代理根據學生評分與軌跡決定下一輪技能修訂與資料選擇。

## 結果
在 Terminal、Search、軟體工程三領域、兩種模型尺寸共六組實驗中，AutoMaster 相較 Vanilla SFT 平均提升 1.42–8.99 個百分點（±1 SD，三次評估）。消融實驗顯示保留技能指令訓練優於移除，且教師與學生模型固定時，行為塑形能釋放額外後訓練空間。摘錄未提供可驗證的具體數據集規模或訓練步數。

## 限制與展望
為 arXiv 預印本，未經同行審查；實驗僅涵蓋三類任務與兩種模型，教師模型未揭露；自主代理的技能設計泛化能力未驗證；評估僅三次運行，統計功效有限；未討論計算成本、擴展性及與其他自主後訓練方法的比較。
