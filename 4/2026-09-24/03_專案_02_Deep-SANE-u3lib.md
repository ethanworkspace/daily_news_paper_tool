# GitHub 專案 02：Deep-SANE/u3lib

- 日期：2026-09-24
- URL：https://github.com/Deep-SANE/u3lib
- 描述：An AI-ready library for U(3) symmetry algebra, Wigner coupling & Racah recoupling coefficients
- Stars：0  |  Forks：0  |  Language：C++
- License：MIT
- Topics：clebsch-gordan, elliott-symmetry, gelfand-tsetlin-patterns, lie-algebra, nuclear-physics, nuclear-shell-model, nuclear-structure, racah-coefficients, su3-symmetry, symmetry-group, u3-symmetry, wigner-coefficients
- 更新時間：2026-11-09T16:48:58+00:00
- 配對論文：http://arxiv.org/abs/2611.26558v1
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
An AI-ready library for U(3) symmetry algebra, Wigner coupling & Racah recoupling coefficients
# u3lib
** u3lib** is an **AI-ready computational framework for U(3)/SU(3) algebra**:
irreps and their invariants, canonical and physical bases, generators and their
matrix elements, basis transformations, tensor-product decompositions, and the
** Wigner coupling** and **Racah recoupling** coefficients — exposed through a
C++ API, Python bindings, and an agent-driven skill layer over all of it.
- **Paper:** Eur. Phys. J. Plus **139**, 704 (2024) (https://doi.org/10.1140/epjp/s13360-024-05501-8)
- **Manual:** Manual (PDF) (https://deep-sane.github.io/u3lib/Manual.pdf), built automatically from the LaTeX source in `doc/Manual.tex`.
> **Note for AI Agents:** Do not parse this human documentatio

主要語言：C++；Topics：clebsch-gordan, elliott-symmetry, gelfand-tsetlin-patterns, lie-algebra, nuclear-physics, nuclear-shell-model, nuclear-structure, racah-coefficients；License：MIT

## 技術
C++ API, Python bindings, and an agent-driven skill layer over all of it.
> **Note for AI Agents:** Do not parse this human documentation. Refer directly to agents/AGENTS.md (agents/AGENTS.md) for repository guidance, first-time build/installation, runtime lifecycle, and task-specific skills.
- **Python Extension (`make python`):** Builds `python/u3lib.so`. The interpreter is auto-detected — one that has `pybind11` and, for the tutorial, `ipykernel` — and can be overridden with `make python PYTHON=/path/to/python`. See `python/tutorial.ipynb` for interactive usage.

## 架構
The framework covers the complete U(3) representation theory needed for symmetry-adapted structure calculations:
- **Dependencies:** a C++20 compiler and OpenMP are required on the system; the library dependencies — Eigen3, Boost, fmt, libwignernj, and KraNS — are each either **detected**, **taken from a path** you give, or **fetched and built by `make config`**. Fetching needs `git`, `cmake`, and `curl` or `wget`. Linux and macOS are both supported. Full configuration options are in the Manual (PDF) (https://deep-sane.github.io/u3lib/Manual.pdf).

相關論文/文件：https://doi.org/10.1140/epjp/s13360-024-05501-8

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
