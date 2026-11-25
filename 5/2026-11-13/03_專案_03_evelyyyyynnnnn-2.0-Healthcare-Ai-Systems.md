# GitHub 專案 03：evelyyyyynnnnn/2.0-Healthcare-Ai-Systems

- 日期：2026-11-13
- URL：https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems
- 描述：Machine learning and decision intelligence models designed to improve healthcare safety through clinical risk prediction and medical interaction analysis.
- Stars：225  |  Forks：38  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-10T00:23:36+00:00
- 配對論文：https://doi.org/10.5281/zenodo.24094763
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
此專案構建四個臨床決策支援子系統，針對醫療安全的關鍵問題：提前預測 ICU 低氧血症與低血壓、評估主群劃分對模型效能的洩漏成本、驗證光電容積波形心率估計的準確度、以及以理論為基礎的同理心詞彙量測真實醫師‑病人對話。目標使用者為臨床研究員、醫療資料科學家與系統安全工作者，旨在提供可量化、可重現的風險預測與互動分析工具，降低誤決策帶來的系統性後果。

## 技術
主要採用 Python 3，搭配 scikit‑learn 實作 logistic regression 與 gradient boosting 模型；利用 PyHealth/RHealth Extension 提供的 icuflow 套件進行主群劃分、校準與警報比較；透過 pandas、numpy 處理時序生理訊號；使用 Librosa 或自訂濾波器從 PPG 提取心率；建立詞彙加權的同理心分數計算；提供可安裝的 CLI 工具與完整的單元測試（pytest），所有程式碼放在各子專案的 src/ 目錄下，依循統一的 README‑driven 結果紀錄規範。

## 架構
每個子專案遵守相同的目錄結構：src/ 放置模型實作與特徵工程腳本；data/ 包含真實第三方資料（MIMIC‑IV、BIDMC、MTS‑Dialog）與標註樣本；results/ 儲存每次實驗的最新指標（latest‑real.json）以及對應的 README.md，所有數字必須有對應的運行日誌；tests/ 包含驗證資料切分、校準誤差與警報比較的單元測試；website/ 用於展示專案說明。執行流程為：載入真實資料 → 預處理／特徵抽取 → 按照 subject‑grouped 或隨機劃分訓練／測試集 → 訓練模型（logistic regression、GBDT 等） → 計算校準誤差、AUROC、心率誤差或同理心分數 → 寫入 results/latest‑real.json 並更新 README.md，整個過程由 GitHub Actions 工作流程自動觸發測試與報告。

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
