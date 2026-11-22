# GitHub 專案 03：Genesis-Embodied-AI/genesis-world

- 日期：2026-11-21
- URL：https://github.com/Genesis-Embodied-AI/genesis-world
- 描述：Simulation platform for general-purpose robotics & embodied AI learning.
- Stars：30284  |  Forks：2929  |  Language：Python
- License：Apache-2.0
- Topics：
- 更新時間：2026-11-21T23:20:26+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
Simulation platform for general-purpose robotics & embodied AI learning.
Simulation platform for general-purpose robotics & embodied AI learning.

主要語言：Python；Stars：30284；License：Apache-2.0

## 技術
實作語言以 Python 為主。
專案描述：Simulation platform for general-purpose robotics & embodied AI learning.

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：Simulation platform for general-purpose robotics & embodied AI learning.

## README 摘錄（節選）
```text
# Genesis World
(https://pypi.org/project/genesis-world/)
(https://pepy.tech/projects/genesis-world)
(https://genesis-world.readthedocs.io/en/latest/)
(https://github.com/Genesis-Embodied-AI/genesis-world/issues)
(https://github.com/Genesis-Embodied-AI/genesis-world/discussions)
** Genesis World** is a simulation platform for physical AI developments. It combines a unified multi-physics engine, a photo-realistic renderer (Nyx (https://github.com/Genesis-Embodied-AI/genesis-nyx)), and a cross-platform compiler (Quadrants (https://github.com/Genesis-Embodied-AI/quadrants)) behind a Pythonic simulation interface. Genesis World is designed to scale from a single laptop kernel to datacenter-grade GPUs, while remaining easy to read, extend, and embed in research code.
It was previously named **Genesis** and started as an academic project since Dec 2024, and its development is now officially supported by Genesis AI (https://www.genesis.ai/).
For more technical details, refer to our blog post (https://genesis.ai/blog/the-role-of-simulation-in-scalable-robotics-genesis-world-10-and-the-path-forward).
## Table of Contents
1. What is Genesis World? (#what-is-genesis-world)
2. Catalogue (#catalogue)
3. Quick Installation (#quick-installation)
4. Contribution (#contributing-to-genesis)
5. Support (#support)
6. License and Acknowledgments (#license-and-acknowledgments)
7. Citation (#citation)
## What is Genesis World?
Genesis World occupies the four layers inside the dashed box. Above sits whatever you build (robotics environments, ML pipelines, data generation, agentic simulation); below sits whatever compute backend you have.
- **Simulation Interface** — the user-facing API: asset parsing (URDF, MJCF, OBJ, GLB, USD, …), entity accessors, controllers, sensors, parallel and heterogeneous environments, and a built-in GUI.
- **Physics** — a unified multi-physics engine integrating Rigid, FEM, MPM, Particle (PBD / SPH), uipc (https://github.com/spiriMirror/libuipc), an explicit coupler, and SAP, all sharing one scene and one state.
- **Render** — three rendering paths plug in as camera sensors: **Nyx (https://github.com/Genesis-Embodied-AI/genesis-nyx)** (our in-house renderer designed for robotics), Luisa (DSL ray tracer), and Pyrender (rasterizer).
- **Compiler** — **Quadrants (https://github.com/Genesis-Embodied-AI/quadrants)** lowers Python kernel code to CUDA, AMD ROCm, Apple Metal, Vulkan, x86, and ARM64. It carries Genesis's autodiff, GPU graphs, and fastcache machinery.
** Eden (https://github.com/embodied-ai-nexus/Eden)** is one example of the application layer: a robot-learning framework built on Genesis World.
### Documentation
- Genesis World (https://genesis-world.readthedocs.io/en/latest/)
- Quadrants (https://genesis-embodied-ai.github.io/quadrants/index.html)
- Nyx (https://genesis-embodied-ai.github.io/genesis-nyx/latest/)
## Catalogue
Three sections, mirroring the Genesis layers that ship runnable demos: **Physics** (solvers and multi-solver coupling), **Rendering** (in-repo camera setups plus the Nyx walkthroughs hosted in genesis-nyx (https://github.com/Genesis-Embodied-AI/genesis-nyx)), and **Simulation Interface** (sensors, GUI, controllers, parallel/heterogeneous envs, and tutorials). Most scripts run end-to-end after `pip install -e ".[dev]"`; demos that depend on optional backends (e.g. the IPC and Nyx examples) need the extras listed in Optional extras (#optional-extras).
### Physics
| | | |
|---|---|---|
| Rigid: franka cube (./examples/rigid/franka_cube.py) | Rigid: collision tower (./examples/collision/tower.py) | Rigid: contype (./examples/collision/contype.py) |
| | | |
| FEM: hard & soft constraint (./examples/deformable/fem_hard_and_soft_constraint.py) | MPM: tutorial (./examples/tutorials/mpm.py) | MPM: sand wheel (./examples/coupling/sand_wheel.py) |
| | | |
| SPH: rigid (./examples/coupling/sph_rigid.py) | SPH: + MPM (./examples/coupling/sph_mpm.py) | PBD: liquid (./examples/deformable/pbd_liquid.py) |
| | |
```
