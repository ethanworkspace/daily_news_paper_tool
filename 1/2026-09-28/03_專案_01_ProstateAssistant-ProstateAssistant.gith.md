# GitHub 專案 01：ProstateAssistant/ProstateAssistant.github.io

- 日期：2026-09-28
- URL：https://github.com/ProstateAssistant/ProstateAssistant.github.io
- 描述：
- Stars：0  |  Forks：0  |  Language：HTML
- License：
- Topics：
- 更新時間：2026-09-27T17:51:52+00:00
- 論文層級：Tier 4（一般期刊）（海事）
- 配對論文：https://doi.org/10.1007/s00330-026-12937-2
- 品質分數：7/10 [paper_paired]

## 在做什麼
Prostate Assistant 提供一個線上計算工具，根據德國 SHIP 社區隊列的 1,037 名健康男性數據，給出隨年齡、BMI 和身高調整的 PSA、PSA 密度與 MRI 前列腺體積的參考百分位數（第 5、50、95 百分位），幫助研究者與臨床醫師評估 PSA 前列腺體積比值是否處於正常範圍。

## 技術
技術實現為靜態網頁，採用 HTML5、CSS3 與純 JavaScript（Vanilla JS）建構互動式計算器；所有參考百分位數表格預先以 JSON 或 CSV 形式儲存於 `data/` 目錄，前端讀取這些表格並根據使用者輸入的年齡、BMI、身高進行線性插值或查表，即時顯示對應的 PSA、PSA 密度與前列腺體積百分位數。無需後端服務或資料庫。

## 架構
架構採用前端單頁應用模式：頁面由 index.html 提供結構與樣式，main.js 負責處理表單事件、讀取 data/ 中的 percentile 資料檔（JSON/CSV），依據使用者輸入的年齡、BMI、身高執行查表或線性插值運算，得到對應的 PSA、PSA 密度與前列腺體積百分位數，最後將結果渲染至結果區塊。資料流完全在瀏覽器端進行，無伺服器端處理或 API 呼叫。由於 README 未詳細說明程式碼細節，以上描述為基於靜態網頁特性與資料夾結構的合理推斷。

## README 摘錄（節選）
```text
# Prostate Reference Percentiles
(https://prostateassistant.github.io/)
(https://doi.org/10.1007/s00330-026-12937-2)
Age-, BMI- and height-adjusted reference values for **PSA**, **PSA density** and **MRI prostate volume**. They come from 1,037 men in the population-based SHIP cohort (Germany) who stayed free of prostate cancer, BPH and LUTS over about 10 years of follow-up. Prostate volume was measured by deep-learning MRI segmentation, and the percentiles were modelled with GAMLSS.
> Lindholz M, et al. **Reference values for PSA, PSA density, and MRI prostate volume in healthy German men.** *Eur Radiol* (2026). https://doi.org/10.1007/s00330-026-12937-2
| | Median | 95th percentile |
|---|---:|---:|
| Prostate volume | 31.3 mL | 51.4 mL |
| PSA | 0.81 ng/mL | 2.79 ng/mL |
| PSA density | 0.025 ng/mL² | 0.071 ng/mL² |
- **Prostate volume** and **PSA** increased progressively with age, with widening upper percentiles in older men.
- **PSA density** showed greater age-stability than PSA; the age-adjusted 95th percentile did not exceed 0.11 ng/mL².
- **BMI** was positively associated with prostate volume and inversely associated with PSA density.
The percentile tables are in `data/` (data/). The calculator is a research tool, not a diagnostic device.
```
