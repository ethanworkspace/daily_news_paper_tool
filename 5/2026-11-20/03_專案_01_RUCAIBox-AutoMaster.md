# GitHub 專案 01：RUCAIBox/AutoMaster

- 日期：2026-11-20
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：24  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T08:04:09+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AutoMaster 是一種自主後訓練框架，讓同一個大型語言模型同時扮演 Teacher 與 Student 的角色，透過設計與選擇技能（Skill）來改進 Teacher 的示範行為，從而產出更具教學價值的訓練資料，提升 Student 在終端任務、網頁搜尋與文件到倉庫三個領域的表現。目標使用者為希望在不增加模型規模或外部資料的前提下，提升已有模型教學能力的研究者與工程師；核心問題在於僅靠任務成功率無法保證示範品質，導致訓練時可能強化不良探索或假設。

## 技術
AutoMaster 以 Python 3.11+ 為主要實作語言，依賴 AweAgent 作為智能體框架，並以 Qwen3.5 為基礎模型（可透過 SGLang 或 OpenAI‑compatible 端點進行推論）。其工作流程包括：技能設計（Skill‑FT）產出 Teacher 行為規則、使用這些規則產生示範軌跡、選擇高價值示範作為訓練資料、對 Student 進行監督微調（SFT），最後根據 Student 的分數與執行追蹤回饋來迭代優化技能。資料流經過技能庫（skills/）、推論配方（recipes/inference/）與評估腳本（recipes/inference/README.md）等模組。

## 架構
AutoMaster 的架構分為內圈與外圈兩個迴圈。內圈負責『塑造示範』：讀取當前技能集合，分析 Teacher 的執行軌跡、設計或測試新技能、選擇適合當前任務子集的示範資料。外圈負責『從 Student 學習』：使用內圈產出的示範對 Student 進行 SFT，評估其在三個基準（Terminal‑Bench 2.1、BrowseComp、Doc2Repo）上的分數與執行追蹤，將這些回饋作為下一輪技能設計的依據。每個技能為獨立資料夾，包含 SKILL.md 入口與相關實作腳本；推論環境透過 SGLang 啟動模型檢查點，評估腳本讀取任務配置（terminal.yaml、browsecomp.yaml、doc2repo.yaml）並執行指定數量的 rollout。由於 README 未提供詳細的類別圖或元件接口說明，以下架構描述僅基於文本中所述的迴圈與模組結構進行推斷。

## README 摘錄（節選）
```text
## Autonomous Post-Training by Making the Same Model a Better Teacher
* Beyond task success: **autonomously shaping teacher behavior to improve what students learn**.*
Video (#how-automaster-works) · Inside AutoMaster (#inside-automaster) · Results (#results-across-three-domains) · Insights (#key-insights) · Skills (skills/README.md) · Quick start (#quick-start) · Models & data (https://huggingface.co/collections/RUC-AIBOX/automaster) · Citation (#citation)
(https://arxiv.org/pdf/2611.26510)
(https://aweai-team.github.io/AutoMaster/)
(https://huggingface.co/collections/RUC-AIBOX/automaster)
(skills/README.md)
(LICENSE)
* If you find AutoMaster useful, give us a star ⭐ to support the project.*
** AutoMaster** autonomously studies trajectories, designs skills, and selects demonstrations to make the same model a better teacher. **Skill-FT** guides Teacher rollouts with these skills and fine-tunes the Student on the resulting demonstrations. The Student is evaluated without generated skills.
This release includes nine selected skills (skills/README.md) and inference recipes (recipes/inference/README.md) for three domains, powered by AweAgent (https://github.com/AweAI-Team/AweAgent).
## How AutoMaster works
▶ Watch the overview
## Inside AutoMaster
** Inner loop · Shape the demonstrations.** Analyze behaviors, design and test skills, and select training examples. Skills can apply to overlapping task subsets, with different combinations for different tasks.
** Outer loop · Learn from the Student.** Train and evaluate the Student, then use its scores and execution traces to refine the next round of skill design and data selection.
Explore the method and behavioral examples → (docs/method.md)
## Results across three domains
## Key insights
- **Task success alone does not tell us what a demonstration teaches.** Even successful trajectories can contain unsupported assumptions, unproductive exploration, or superficial verification. Training on them can reinforce these habits alongside useful behaviors.
- **Better teaching without a stronger teacher.** Shaping how a fixed Teacher executes tasks can improve its demonstrations. AutoMaster improves mean Student performance by **1.42–8.99 percentage points** over Vanilla SFT, with the Teacher, task pool, training set size, and SFT recipe held fixed.
- **Generation and selection are complementary.** Skills shape the behaviors demonstrated; selection identifies valuable training examples. Removing either component lowers mean performance in all six evaluated settings, supporting their joint optimization.
- **Skill context helps behavioral internalization.** Keeping skill instructions during SFT improves mean performance by **2.15–4.01 percentage points** over removing them, with identical trajectories and supervised outputs—and no generated skills at evaluation. Explicit behavioral rules and their conditions of application offer a possible explanation.
- **Autonomous post-training benefits from exploration.** Rollout evidence and Student evaluation guide further skill design and data selection. Continued experimentation can uncover better candidates after limited progress; individual rounds need not improve monotonically.
## Skills in practice
Each skill is a self-contained folder with a `SKILL.md` entrypoint.
| Terminal tasks | Web search | Repository construction |
|---|---|---|
| Test a numerical claim (skills/tb2.1/execute-numeric-decision/SKILL.md) | Break out of a stalled search (skills/bc/recover-search-anchor/SKILL.md) | Exercise the public API (skills/doc2repo/run-observed-public-call/SKILL.md) |
| Compare against an independent reference and test the required bound. | Drop unsupported assumptions and follow a new identifying clue. | Call the real entry point and observe its external effects. |
Explore all nine skills and teacher instructions (skills/README.md#what-the-teacher-reads) · See how skills change a rollout (docs/method.md#behavioral-shaping-in-practice)
## Quick start
### 1.
```
