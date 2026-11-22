# GitHub 專案 01：RUCAIBox/AutoMaster

- 日期：2026-11-20
- URL：https://github.com/RUCAIBox/AutoMaster
- 描述：
- Stars：26  |  Forks：2  |  Language：Python
- License：MIT
- Topics：
- 更新時間：2026-11-22T12:31:46+00:00
- 配對論文：http://arxiv.org/abs/2611.26510v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
AutoMaster 是一個自主後訓練框架，透過讓同一個模型同時扮演 Teacher 與 Student 的角色，自行設計技能（Skill）並選擇示範軌跡，以提升模型在終端任務、網頁搜尋與文件到倉庫三個領域的教學品質。目標使用者為希望在不增大模型規模的情況下改善模型教學能力的研究者與開發者，核心問題在於僅看任務成功率無法判斷示範的教學價值，導致訓練時可能強化不良習慣。

## 技術
AutoMaster 以 Python 3.11+ 為主要實作語言，基礎模型採用 Qwen3.5，透過 SGLang 提供 OpenAI‑相容的推論端點。框架整合 AweAgent 實現 agentic rollout，技能以獨立資料夾的 SKILL.md 形式存在，內容包括行為規則與適用條件。內部流程包含 Inner Loop（軌跡分析、技能設計與測試、示範選擇）與 Outer Loop（利用技能導引的 Teacher rollout 生成示範資料，對 Student 進行監督微調（SFT），根據 Student 分數與執行追蹤回饋以迭代優化技能）。資料流經過 trajectory → skill design/demo selection → demonstration dataset → SFT → student evaluation → skill refinement。

## 架構
系統主要由四個模組組成：1) Skill Library（存放所有技能的 SKILL.md 與說明文件）；2) Inner Loop（負責分析 Teacher 的執行軌跡、設計/測試新技能、根據當前技能選擇最具訓練價值的示範）；3) Outer Loop（使用 Inner Loop 產出的技能導引 Teacher 產生示範資料，對 Student 進行監督微調，評估 Student 表現並將分數與追蹤資料回饋給 Inner Loop 以進行下一輪技能優化）；4) 推論與評估環境（SGLang 伺服器載入 Qwen3.5 權重，提供評估腳本 recipes/inference 來跑 terminal.yaml、browsecomp.yaml、doc2repo.yaml 三個基準）。資料流程為：Teacher rollout 產生 trajectory → Inner Loop 產出技能與篩選的示範 → Skill‑FT 生成監督微調資料集 → Outer Loop 對 Student 進行 SFT → 評估 Student 得分與追蹤 → 回饋至 Inner Loop 進行下一輪技能設計。README 未提供更細緻的類別圖或同步機制細節，以上架構說明僅基於可見的模組與流程描述。

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
