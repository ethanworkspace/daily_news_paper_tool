# GitHub 專案 04：evelyyyyynnnnn/2.0-Healthcare-Ai-Systems

- 日期：2026-11-17
- URL：https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems
- 描述：Machine learning and decision intelligence models designed to improve healthcare safety through clinical risk prediction and medical interaction analysis.
- Stars：225  |  Forks：38  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-10T00:23:36+00:00
- 配對論文：https://doi.org/10.5281/zenodo.24094763
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
此專案構建四個互補的醫療安全模型，目標是透過臨床風險預測與醫療互動分析降低醫療決策失誤。主要服務於醫院重症監護團隊、臨床研究者與醫療AI開發者，提供ICU早期警示、生理波形品質評估、臨床同理心量測以及資料分割與校準工具，以解決資訊洩漏、警報不準、模型校準差距與同理心評估缺失等核心問題。

## 技術
專案以 Python 為主要實作語言，使用 logistic regression 與 gradient boosting 進行風險預測；提供 PyHealth/RHealth Extension（icuflow）套件，處理受試者分組切分、校準及警報比對；包含生理波形管線，從 PPG 訊號提取心率並與床旁監測器比較；臨床同理心分析則採用理論驅動的加權同理心詞彙結合對話結構特徵。評估指標涉及 AUROC、校準誤差、中位數誤差等，資料來源為 PhysioNet MIMIC‑IV、BIDMC 與 MTS‑Dialog 真實臨床資料集。

## 架構
倉庫採用統一的專案骨架：每個子專案（ICU Early‑Warning Models、PyHealth/RHealth Extension、Physiological Waveform Pipeline、Clinical Empathy Analysis）皆含 src/、data/、results/、tests/ 與 website/ 目錄。資料流程始於從對應的真實資料集讀取樣本，進入 src/ 進行前處理、特徵工程與模型訓練（如 logistic regression、gradient boosting 或波形峰值檢測），接著在同目錄下執行評估（校準、AUROC、誤差分析、同理心得分），最後將量化結果寫入 results/latest-real.json 並於 results/README.md 中標註運行日期。四個子專案彼此獨立，均遵守「無數字無運行紀錄」與「不使用模擬資料作實際主張」的規則；整體架構可視為模組化的決策支援集合，但倉庫未提供中央協調器或統一執行流程，此部份的描述僅基於目錄結構與 README 中所述的個別流程推斷。

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
