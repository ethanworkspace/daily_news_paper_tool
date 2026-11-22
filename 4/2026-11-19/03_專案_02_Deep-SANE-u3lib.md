# GitHub 專案 02：Deep-SANE/u3lib

- 日期：2026-11-19
- URL：https://github.com/Deep-SANE/u3lib
- 描述：An AI-ready library for U(3) symmetry algebra, Wigner coupling & Racah recoupling coefficients
- Stars：0  |  Forks：0  |  Language：C++
- License：MIT
- Topics：clebsch-gordan, elliott-symmetry, gelfand-tsetlin-patterns, lie-algebra, nuclear-physics, nuclear-shell-model, nuclear-structure, racah-coefficients, su3-symmetry, symmetry-group, u3-symmetry, wigner-coefficients
- 更新時間：2026-11-09T16:48:58+00:00
- 配對論文：http://arxiv.org/abs/2611.26558v1
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
u3lib 是一個面向 AI 的計算框架，專門實現 U(3)/SU(3) 對稱代數的不可約表示、不變量、正則與物理基底、生成元矩陣元、基底變換、克羅內克積分解以及 Wigner 耦合與 Racah 重耦合係數，提供 C++ API、Python 綁定及代理人驅動的技能層，服務於從事核殼模型、對稱性適配結構計算的理論物理研究者，解決對稱代數量的自動化計算需求。

## 技術
技術重點：採用 C++20 標準並啟用 OpenMP 進行多執行緒運算，依賴 Eigen3 進行線性代數、Boost 通用庫、fmt 格式化輸出、libwignernj 處理 Wigner 3j 符號以及 KraNS 零空間求解器；透過 pybind11 提供 Python 擴充模組，使用 CMake 與 Makefile 進行自動偵測、下載與編譯相依項目；agents/ 目錄內含代理人技能檔案（AGENTS.md、install/SKILL.md），使 AI 助理能透過自然語言指令完成建置、測試與計算任務。

## 架構
架構方面，u3lib 採用 header‑only 設計，核心程式碼位於 include/，提供 U(3) 不可約表示、Gelfand–Tsetlin 與 SO(3) 約簡基底、生成元矩陣元、基底變換、克羅內克積分解以及 Wigner 與 Racah 係數的函式介面；src/ 中的範例驅動程式示範如何呼叫這些介面並編譯至 bin/；python/ 透過 pybind11 建立 python/u3lib.so，使得 Jupyter Notebook 可直接互動；test/ 含回歸測試與參考表，驗證維數、交錯、分支規則及係數的正交性；doc/ 保存 LaTeX 手冊並自動產布 PDF；agents/ 存放代理人技能文件（AGENTS.md、install/SKILL.md），讓 AI 助理依照自然語言提示執行 make config、make、make test 等步驟，從而完成從設定、編譯、測試到計算的完整流程。

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
