# GitHub 專案 02：Deep-SANE/u3lib

- 日期：2026-11-16
- URL：https://github.com/Deep-SANE/u3lib
- 描述：An AI-ready library for U(3) symmetry algebra, Wigner coupling & Racah recoupling coefficients
- Stars：0  |  Forks：0  |  Language：C++
- License：MIT
- Topics：clebsch-gordan, elliott-symmetry, gelfand-tsetlin-patterns, lie-algebra, nuclear-physics, nuclear-shell-model, nuclear-structure, racah-coefficients, su3-symmetry, symmetry-group, u3-symmetry, wigner-coefficients
- 更新時間：2026-11-09T16:48:58+00:00
- 配對論文：http://arxiv.org/abs/2611.26558v1
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
u3lib 是一個專門為核物理對稱性研究設計的 C++ 函式庫，提供 U(3)/SU(3) 群論的完整表示論工具，包括不可約表示、不變量、正則與物理基底、生成子矩陣元、基底變換、克羅內克積分解以及 Wigner 耦合與 Racah 重耦合係數。透過 C++ API、Pybind11 Python 繫結以及內建的 AI‑agent 技能層，使理論物理學家、計算核物理研究者以及希望以自然語言驅動對稱性計算的自動化助理能夠快速進行對稱適配結構計算與符號推導。

## 技術
u3lib 以現代 C++20 為基礎，使用 OpenMP 進行多執行緒加速，依賴 Eigen3 進行線性代數運算、Boost 提供通用工具、fmt 用於格式化輸出、libwignernj 處理 Wigner 3j 符號，並透過本地 KraNS 空間求解器進行零空間計算。庫提供 header‑only 的核心介面（include/u3lib.h），並透過 pybind11 建立 Python 擴充套件（python/u3lib.so），支援互動式 Jupyter 教學。建置流程透過 make config 自動偵測或下載編譯相依項目，接著執行 make 編譯核心庫與範例程式，make test 進行回歸驗證，make python 產生 Python 繫結。此外，agents/ 目錄內含 AI‑agent 技能檔案，使代理能依自然語言指令執行安裝、編譯與測試等任務。

## 架構
專案結構採用模組化目錄：include/ 放置 header‑only 核心庫（u3lib.h 與子模組，涵蓋不可約表示、基底、生成子、耦合與重耦合等功能）；src/ 包含示範驅動程式，編譯後放入 bin/；test/ 存放回歸測試來源檔與參考表，透過 make test 執行；python/ 放置 pybind11 繫結原始碼、建置腳本與 Jupyter 教學 notebook；doc/ 保存 LaTeX 手冊來源，會自動編譯成 PDF 並發布於 GitHub Pages；agents/ 提供 AI‑agent 技能目錄，包括 AGENTS.md 與各任務技能檔（如 install/SKILL.md），使代理能遵循庫的建置、測試與使用流程。資料流程方面，使用者首先透過 make config 解決與建置依賴（Eigen3、Boost、fmt、libwignernj、KraNS），接著編譯核心庫與範例，最後可透過 C++ 匯入 header 或 Python 匯入 u3lib 進行對稱性計算，亦可呼叫 agents/ 中的技能讓 AI 助理自動完成安裝、編譯與測試步驟。

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
