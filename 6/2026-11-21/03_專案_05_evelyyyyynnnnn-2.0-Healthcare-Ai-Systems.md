# GitHub 專案 05：evelyyyyynnnnn/2.0-Healthcare-Ai-Systems

- 日期：2026-11-21
- URL：https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems
- 描述：Machine learning and decision intelligence models designed to improve healthcare safety through clinical risk prediction and medical interaction analysis.
- Stars：225  |  Forks：38  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-10T00:23:36+00:00
- 配對論文：https://doi.org/10.5281/zenodo.24094763
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
本專案提供醫療安全決策支援系統，透過臨床風險預測與醫療互動分析，協助醫護人員降低錯誤決策帶來的系統性後果。目標使用者為醫院重症監護室、臨床研究者與醫療AI開發者，核心問題在於校正警報、避免主題洩漏、生理波形品質評估與同理心量測的缺失。該系統透過可量化的校準指標與真實第三方資料驗證，確保所報告的效能具備可重現性與臨床可用性。

## 技術
專案主要以 Python 實作，使用 scikit-learn 的邏輯斯蒂迴歸與梯度提升樹（Gradient Boosting）進行風險預測，並自行開發 PyHealth/RHealth Extension 套件（icuflow 0.1.0）提供主題分組切分、校準評估及警報比對功能。資料來源包括 PhysioNet MIMIC‑IV、BIDMC 以及 MTS‑Dialog 真實臨床 transcript，處理流程倚賴 pandas、numpy 與自訂腳本進行特徵工程與模型訓練。

## 架構
每個子專案遵循統一目錄結構：src/ 放置模型與處理腳本，data/ 存放真實或樣本資料，results/ 保存最新實驗指標（latest-real.json）與對應的 README.md，tests/ 包含單元與整合測試，website/ 用於文件展示。執行流程為：先從 data/ 讀取真實資料（如 MIMIC‑IV stays、BIDMC PPG、MTS‑Dialog transcript），進行前處理與特徵抽象，接著在 src/ 中訓練邏輯斯蒂迴歸或梯度提升模型，使用 PyHealth/RHealth Extension 進行主題分組切分與校準誤差計算，最後將評估結果寫入 results/ 並更新 README.md，所有數字必須對應可追蹤的運行日誌。

## README 摘錄（節選）
```text
# 2.0 — Healthcare AI Systems
(https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems/actions/workflows/tests.yml)
(https://doi.org/10.5281/zenodo.24094763)
Clinical decision-support and patient-safety systems. This repository carries the Healthcare Safety pillar of the endeavor.
Part of a five-repository portfolio on one theme: **optimization-driven,
system-level decision frameworks** —
integrating operations research, mathematical optimization and applied AI — for
domains where a wrong decision carries systemic consequences. The three pillars
are financial stability, healthcare safety and secure digital infrastructure.
| | |
|---|---|
| Projects with measured results | **4 of 4** |
| Tests across the four suites | **126** |
| Running on real third-party data | **4 of 4** |
| Most recent reportable run | 2026-09-06 |
> "Measured" means: original work, a stated method, real data at a stated
> scale, a measured result, and a README a reviewer can follow. Counts exclude
> duplicates, forks of third-party work, retired projects, and asset-only
> folders.
## Projects
| Folder | Project | Pillar | What it measures |
|---|---|---|---|
| `2-icu-early-warning/` (2-icu-early-warning/) | ICU Early-Warning Models | Healthcare Safety | Calibration of a deployed-style alarm |
| `4-pyhealth-rhealth-extension/` (4-pyhealth-rhealth-extension/) | PyHealth / RHealth Extension | Healthcare Safety | What subject leakage costs, measured |
| `3-physiological-waveform-pipeline/` (3-physiological-waveform-pipeline/) | Physiological Waveform Pipeline | Healthcare Safety | PPG heart rate against a bedside monitor |
| `1-clinical-empathy-analysis/` (1-clinical-empathy-analysis/) | Clinical Empathy Analysis | Healthcare Safety | A lexical empathy measure, on real transcripts |
## What each one is
### 1. ICU Early-Warning Models — `2-icu-early-warning/` (2-icu-early-warning/)
Hypoxemia and hypotension four hours ahead on the PhysioNet MIMIC-IV open-access
demo — 134 stays, 24,304 observations, 31 features — compared at a matched
sensitivity of 80% against the single-threshold alarm a ward actually runs.
** The finding is calibration, not discrimination.** The ward-style alarm has an
expected calibration error of **0.276** on hypoxemia and
** 0.416** on hypotension; plain logistic regression reaches
** 0.030** and **0.045**. At matched sensitivity that is worth
** 77.2 → 62.3** and **31.8 → 22.9** false alerts per 100 observations.
Gradient boosting does not beat logistic regression here, and that is reported.
### 2. PyHealth / RHealth Extension — `4-pyhealth-rhealth-extension/` (4-pyhealth-rhealth-extension/)
`icuflow` 0.1.0, an installable package with 14 exports and a working CLI,
covering the three things easiest to get wrong in a clinical pipeline:
subject-grouped splits, calibration, and alarm comparison at matched sensitivity.
** It measures what one of those mistakes costs.** On the same cohort, features
and model, a random row-level split reports **AUROC 0.9058**; a subject-grouped
split reports **0.4989** — chance. That is **81.57%** inflation, from
97 subjects and 22,512 rows.
The package is **not** published to PyPI. It has no downloads and no users, and
neither is claimed.
### 3. Physiological Waveform Pipeline — `3-physiological-waveform-pipeline/` (3-physiological-waveform-pipeline/)
Heart rate derived from the photoplethysmogram on the PhysioNet BIDMC dataset —
10 records at 125 Hz — checked against the bedside monitor's own
reported rate.
Agreement is close: median difference **0.084 bpm**, worst case
6.372 bpm, **9 of 10 records within 5 bpm**. The more useful number is
the one usually left out: the artifact gate accepts between **2.1% and 100%**
of windows depending on the record, so the quality gate — not the beat detector —
is where the variance lives.
Artifact precision and recall are **not** reported: BIDMC does not annotate
artifact locations, so there is no answer key.
### 4. Clinical Empathy Analysis — `1-clinical-empathy-ana
```
