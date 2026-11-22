# GitHub 專案 02：Deep-SANE/u3lib

- 日期：2026-11-20
- URL：https://github.com/Deep-SANE/u3lib
- 描述：An AI-ready library for U(3) symmetry algebra, Wigner coupling & Racah recoupling coefficients
- Stars：0  |  Forks：0  |  Language：C++
- License：MIT
- Topics：clebsch-gordan, elliott-symmetry, gelfand-tsetlin-patterns, lie-algebra, nuclear-physics, nuclear-shell-model, nuclear-structure, racah-coefficients, su3-symmetry, symmetry-group, u3-symmetry, wigner-coefficients
- 更新時間：2026-11-09T16:48:58+00:00
- 配對論文：http://arxiv.org/abs/2611.26558v1
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
u3lib 是一個專門為核物理與對稱性研究設計的 C++ 計算框架，提供 U(3)/SU(3) 群論的完整表示論工具，包括不可約表示、不變量、正則與物理基底、生成元矩陣元、基底變換、克羅內克積分解以及 Wigner 耦合與 Racah 重耦合係數。透過 C++ API、Python 綁定以及代理驅動的技能層，使得核殼模型計算、對稱適配結構分析以及 AI 代理自動化工作流程能夠直接調用這些代數運算。目標使用者為理論核物理研究者、計算物理學家以及需要進行對稱性代數運算的 AI 開發者，核心問題在於傳統實作繁瑣且缺乏統一、可擴充且 AI 友好的介面。

## 技術
u3lib 使用現代 C++20 標準並依賴 OpenMP 進行多執行緒加速，核心數學運算依賴 Eigen3 進行線性代數、Boost 提供通用容器與演算法、fmt 用於格式化輸出、libwignernj 提供 Wigner 3j 符號計算，並透過子儲存庫 KraNS 進行零空間求解。Python 綁定透過 pybind11 建置，提供 python/u3lib.so 模組，並附帶 Jupyter 教學 notebook。建置流程透過 Makefile 的 config、make、make test 與 make python 完成，依賴項可自動偵測、指定路徑或透過 git、cmake、curl/wget 下載編譯。此外，agents/ 目錄提供 AI 代理技能檔案，使得代理能透過自然語言驅動安裝、編譯與測試。

## 架構
u3lib 的原始碼分為數個主要目錄：include/ 放置標頭檔案，提供 u3lib.h 傘型標頭以及 irreps、bases、generators、coupling、recoupling 等子模組的宣告；src/ 包含示範驅動程式，經編譯後產生執行檔放於 bin/；python/ 存放 pybind11 綁定原始碼與建置腳本，產生 python/u3lib.so 供 Python 呼叫；test/ 放置回歸測試與參考資料；doc/ 保存 LaTeX 手冊來源，會自動編譯為 PDF 發布於 GitHub Pages；agents/ 則收錄 AI 代理技能說明與安裝腳本。使用者透過 C++ API 或 Python 綁定呼叫庫函式，內部依序進行不可約表示標籤計算、基底建構（正則 Gelfand–Tsetlin 與物理 SO(3) 減少基底）、生成元矩陣元求值、基底變換、克羅內克積分解以及 Wigner 與 Racah 係數的計算，最後將結果回傳給呼叫端。由於 README 未詳細說明內部執行緒調度或記憶體管理的具體實作，此部份僅根據可見的模組結構進行推斷。

## README 摘錄（節選）
```text
# u3lib
** u3lib** is an **AI-ready computational framework for U(3)/SU(3) algebra**:
irreps and their invariants, canonical and physical bases, generators and their
matrix elements, basis transformations, tensor-product decompositions, and the
** Wigner coupling** and **Racah recoupling** coefficients — exposed through a
C++ API, Python bindings, and an agent-driven skill layer over all of it.
- **Paper:** Eur. Phys. J. Plus **139**, 704 (2024) (https://doi.org/10.1140/epjp/s13360-024-05501-8)
- **Manual:** Manual (PDF) (https://deep-sane.github.io/u3lib/Manual.pdf), built automatically from the LaTeX source in `doc/Manual.tex`.
> **Note for AI Agents:** Do not parse this human documentation. Refer directly to agents/AGENTS.md (agents/AGENTS.md) for repository guidance, first-time build/installation, runtime lifecycle, and task-specific skills.
--- 
## Scope
The framework covers the complete U(3) representation theory needed for symmetry-adapted structure calculations:
- **Irreps & invariants** — SU(3) $(\lambda,\mu)$ and U(3) $[n_{13},n_{23},n_{33}]$ labels, dimension, Casimir invariants $C_1, C_2, C_3$, and conjugation.
- **Bases** — canonical Gelfand–Tsetlin basis and physical SO(3)-reduced basis $(\kappa,L)$, with inner and outer multiplicities.
- **Generators** — canonical $E_{ij}$ matrix elements on Gelfand states, and SO(3)-reduced matrix elements of physical $\mathbf{L}$ and $\mathbf{Q}$.
- **Transformations** — physical $|(\lambda\mu)\kappa LM\rangle \leftrightarrow$ canonical Gelfand expansion.
- **Decomposition** — full Kronecker product series $A \otimes B$ with outer multiplicities.
- **Coupling & recoupling** — $\mathrm{U(3)}\supset\mathrm{U(2)}$ canonical and SO(3)-reduced Wigner coefficients, and $U$-, $Z$-, and $9$-$(\lambda\mu)$ Racah recoupling.
--- 
## Build & Test
u3lib is self-contained and needs no environment variables. Configure once, then build:
[code block omitted]
`make config` detects each dependency and lets you accept the detected default, point to your own install, or fetch and build it. The **KraNS** null-space solver is used as a sibling repository next to u3lib (`../krans`), built in place if not already installed; `make config` clones it from Deep-SANE automatically if it is missing. Configuration is interactive by default; for scripted use pass flags through, e.g. `make config CONFIG_ARGS="--yes"`.
** Installing with an AI agent.** Point a code-executing assistant at this repository and prompt, for example:
> Install u3lib in this repository: follow `agents/install/SKILL.md` — run `make config` (download and build any missing dependencies), then `make` and `make test` — and report the test result.
The agent resolves the steps through the repository-local install skill (agents/install/SKILL.md).
- **Regression Tests (`make test`):** Tests dimensions, basis interlacing, branching rules, coupling orthonormality, and documented analytic values. Checks remain enabled in release builds (`-UNDEBUG`).
- **Python Extension (`make python`):** Builds `python/u3lib.so`. The interpreter is auto-detected — one that has `pybind11` and, for the tutorial, `ipykernel` — and can be overridden with `make python PYTHON=/path/to/python`. See `python/tutorial.ipynb` for interactive usage.
- **Dependencies:** a C++20 compiler and OpenMP are required on the system; the library dependencies — Eigen3, Boost, fmt, libwignernj, and KraNS — are each either **detected**, **taken from a path** you give, or **fetched and built by `make config`**. Fetching needs `git`, `cmake`, and `curl` or `wget`. Linux and macOS are both supported. Full configuration options are in the Manual (PDF) (https://deep-sane.github.io/u3lib/Manual.pdf).
--- 
## Repository Layout
- `include/` — header-only C++ library (`u3lib.h` umbrella; irreps, bases, generators, coupling, recoupling, containers).
- `src/` — C++ example driver programs; compiled into `bin/`.
- `python/` — pybind11 bindings (`pyu3lib.cpp`), build script, tutorial notebook (`tut
```
