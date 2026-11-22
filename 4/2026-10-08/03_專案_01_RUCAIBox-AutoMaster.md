# GitHub 專案 01：RUCAIBox/AutoMaster

- 日期：2026-10-08
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：24  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T08:04:09+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
▶ Watch the overview

主要語言：Python；Stars：24；License：MIT

## 技術
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

## 架構
[code block omitted]

相關論文/文件：https://arxiv.org/abs/2611.26510

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
