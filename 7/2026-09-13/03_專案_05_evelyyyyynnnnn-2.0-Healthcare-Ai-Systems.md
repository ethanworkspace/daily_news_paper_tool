# GitHub 專案 05：evelyyyyynnnnn/2.0-Healthcare-Ai-Systems

- 日期：2026-09-13
- URL：https://github.com/evelyyyyynnnnn/2.0-Healthcare-Ai-Systems
- 描述：Machine learning and decision intelligence models designed to improve healthcare safety through clinical risk prediction and medical interaction analysis.
- Stars：225  |  Forks：38  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-10T00:23:36+00:00
- 配對論文：https://doi.org/10.5281/zenodo.24094763
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
此專案由四個醫療安全導向的 AI 子專案組成，涵蓋 ICU 早期警報模型、PyHealth/RHealth 擴充套件、生理波形處理管線與臨床同理心分析。目標使用者為醫療研究者、臨床工程師與決策支援系統開發者，透過風險預測、警報校正與同理心量測，降低臨床決策失誤對病人安全的系統性影響。

## 技術
專案主要以 Python 實作，使用 logistic regression、gradient boosting 等模型，依賴 PhysioNet MIMIC‑IV 與 BIDMC 公開資料集進行實驗。ICU 早期警報透過校正誤差（EEC）評估，PyHealth/RHealth 提供可安裝套件與 CLI，強調 subject‑grouped 分割與警報比對於匹配靈敏度；生理波形管線從 PPG 導出心率並與床旁監測器比對；臨床同理心分析則結合加權同理心詞彙與結構特徵，於 MTS‑Dialog 轉錄上計分。所有實驗結果必須對應結果目錄中的 run log 與 latest‑real.json，確保可追溯性。

## 架構
每個子專案遵守統一目錄結構：README.md、src/（程式碼）、data/（原始與樣本資料）、results/（含 latest‑real.json 與 README.md）、tests/（單元測試）與 website/（說明頁面）。執行流程為：先在 data/ 中放置第三方資料（如 MIMIC‑IV、BIDMC），透過 src/ 內的腳本進行資料清洗、特徵工程、模型訓練與評估；評估指標（AUROC、校正誤差、警報率等）寫入 results/latest‑real.json，並自動更新對應的 results/README.md 以符合「無數字無 run log」的規則。測試套件驗證程式正確性，所有實驗均在真實第三方資料上進行，未使用模擬數據作為宣稱依據。若 README 未明確說明跨子專案的資料共享或部署管線，則此部份為基於所述結構的合理推斷。

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
