# GitHub 專案 03：evelyyyyynnnnn/2.0-Healthcare-Ai-Systems

- 日期：2026-11-14
- URL：https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems
- 描述：Machine learning and decision intelligence models designed to improve healthcare safety through clinical risk prediction and medical interaction analysis.
- Stars：225  |  Forks：38  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-10T00:23:36+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.5281/zenodo.24094763
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
此專案屬於「Healthcare Safety」支柱，透過機器學習與決策智慧模型，針對臨床風險預測與醫療互動分析，降低錯誤決策帶來的系統性後果。目標使用者為醫院臨床團隊、醫療資訊研究者及政策制定者，核心問題在於現有警報模型校準不足導致過多誤警報或漏報，需提供可驗證、以真實資料為基礎的校準與決策框架。

## 技術
主要使用 Python 實作，包含 logistic regression 與 gradient boosting 模型，利用 PhysioNet MIMIC‑IV 與 BIDMC 數據集進行 hypoxemia/hypotension 預測與 PPG 心率估算。透過自行開發的 PyHealth/RHealth Extension（可安裝套件，提供 CLI）實施 subject‑grouped 分割、校準誤差計算及警報比對。臨床共情分析則結合加權同理心詞彙與對話結構特徵。所有實驗結果必須對應結果目錄中的 run log，且僅使用真實資料，未使用模擬數據。

## 架構
儲存庫採用多子專案結構，每個子專案（ICU Early‑Warning Models、PyHealth/RHealth Extension、Physiological Waveform Pipeline、Clinical Empathy Analysis）均含 README、src、data、results、tests、website。資料流程：原始 PhysioNet/MTS‑Dialog 數據放入 data/，經 src/ 中的前處理與特徵工程產生模型輸入；在 src/ 內訓練 logistic regression 或 gradient boosting 模型，或執行波形Pipeline 的 artefact gate 與心率估算；透過 PyHealth/RHealth Extension 進行 subject‑grouped 分割、校準（ECE）與警報比對；最終評估指標寫入 results/（如 latest‑real.json）並於 results/README.md 中標註運行日期。tests/ 提供單元與整合測試，website/ 用於展示說明。此結構確保每項數字皆有對應的運行紀錄，符合「No number without a run log」的規則。

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
