# GitHub 專案 05：DEEPX-AI/dx-runtime

- 日期：2026-11-17
- URL：https://github.com/DEEPX-AI/dx-runtime
- 描述：DEEPX NPU runtime and Linux driver for edge AI inference: DX-RT, firmware, DX-APP C++/Python examples and DX-Stream GStreamer plugins. Runs .dxnn models on DX-M1 M.2 accelerators.
- Stars：25  |  Forks：5  |  Language：Shell
- License：NOASSERTION
- Topics：ai-accelerator, arm64, computer-vision, deepx, dx-m1, dxnn, edge-ai, embedded-systems, gstreamer, inference, inference-engine, linux-driver, npu, on-device-ai, runtime, video-analytics
- 更新時間：2026-11-17T04:56:56+00:00
- 配對論文：
- 品質分數：7/10 [implementation_signals]

## 在做什麼
DEEPX NPU runtime and Linux driver for edge AI inference: DX-RT, firmware, DX-APP C++/Python examples and DX-Stream GStreamer plugins. Runs .dxnn models on DX-M1 M.2 accelerators.
DEEPX NPU runtime and Linux driver for edge AI inference: DX-RT, firmware, DX-APP C++/Python examples and DX-Stream GStreamer plugins. Runs .dxnn models on DX-M1 M.2 accelerators.

主要語言：Shell；Topics：ai-accelerator, arm64, computer-vision, deepx, dx-m1, dxnn, edge-ai, embedded-systems；Stars：25；License：NOASSERTION

## 技術
實作語言以 Shell 為主。
從 topics 可見技術方向：ai-accelerator, arm64, computer-vision, deepx, dx-m1, dxnn, edge-ai, embedded-systems。
專案描述：DEEPX NPU runtime and Linux driver for edge AI inference: DX-RT, firmware, DX-APP C++/Python examples and DX-Stream GStreamer plugins. Runs .dxnn models on DX-M1 M.2 accelerators.

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：DEEPX NPU runtime and Linux driver for edge AI inference: DX-RT, firmware, DX-APP C++/Python examples and DX-Stream GStreamer plugins. Runs .dxnn models on DX-M1 M.2 accelerators.

## README 摘錄（節選）
```text
# DEEPX DX-Runtime
## DXNN® - DEEPX NPU SDK (DX-AS: DEEPX All-Suite)
** DX-AS (DEEPX All-Suite)** is an integrated environment of frameworks and tools that enables inference and compilation of AI models using DEEPX devices. Users can build the integrated environment by installing individual tools, but DX-AS maintains optimal compatibility by aligning the versions of the individual tools.
--- 
### AI Model Runtime Environment (https://github.com/DEEPX-AI/dx-runtime) (Deployment Platform)
** Purpose**
- Must be installed on the Target system where the DEEPX M1 M.2 module is attached and the DEEPX AI model (.dxnn) will be executed.
** Core Components**
- DX-RT & DX-FW & NPU Driver: Foundational software for NPU control
- DX-APP: C++ and Python examples to jump-start your projects
- DX-Stream: GStreamer integration for seamless multimedia pipelines
** Flexibility & Support**
- OS: Compatible with Debian-based Linux (Ubuntu 26.04/24.04/22.04/20.04(LTS), Debian 13/12)
- Architecture: Supports both x86_64 and arm64
** Easy Installation**
- Our script automates the entire process
- One-time reboot is required after installation to finalize the NPU Driver setup
** You can install dx-runtime by following the instructions at this LINK (https://github.com/DEEPX-AI/dx-all-suite/blob/main/docs/source/02_Setting_Up_Environment.md#dx-runtime-installation-rt-driver-fw-app-stream).**
--- 
## Quick Guide (Install and Run)
DX-Runtime includes source code for each module. The repositories are managed as Git submodules(`dx_rt_npu_linux_driver`, `dx_fw`, `dx_rt`, `dx_app`, and `dx_stream`) under `./dx-runtime`.
### Local Installation
DX-Runtime supports installation in local environments.
You can install DX-Runtime by following the instructions at this Link (https://github.com/DEEPX-AI/dx-all-suite/blob/main/docs/source/02_Setting_Up_Environment.md#dx-runtime-installation-rt-driver-fw-app-stream)
### APT Repository Installation
The NPU driver and DX-RT are also published as Debian packages in the DEEPX APT repository (Ubuntu / Debian, `amd64` / `arm64`), so you can install and upgrade them with `apt`.
Verify the signing key before trusting it: `gpg --show-keys` must print the fingerprint `3A20CC853C64AE328D0F58CFD816AAC6689DBDEA`. If it does not match, stop — do not install the key.
[code block omitted]
- The `dx_engine` Python wheels matching the installed `libdxrt-bin` are staged in `/usr/share/libdxrt-bin/python`; install the one for your Python version into your virtualenv.
- Firmware is not part of these packages; update it by running `./install.sh --target=dx_fw` from the dx-runtime root. A reboot after installing the driver is recommended.
- `dx_app` and `dx_stream` are not covered by this route; use the Local Installation guide for them.
See the APT Repository Install (https://github.com/DEEPX-AI/dx-all-suite/blob/main/docs/source/02_Setting_Up_Environment.md#apt-repository-install-dx-runtime) section for details.
### Docker Installation
DX-Runtime supports installation in docker environments.
You can install DX-Runtime by following the instructions at this Link (https://github.com/DEEPX-AI/dx-all-suite/blob/main/docs/source/02_Setting_Up_Environment.md#docker-installation)
### One-Line Installation (Runtime-Only)
For a quick setup of just the NPU driver, DX-RT, and DX-FW — without cloning this repository — run:
[code block omitted]
This installs `dx_rt_npu_linux_driver`, `dx_rt`, and `dx_fw` from the prebuilt binaries on each component's `main` branch, so it always tracks the newest published build. It does **not** cover `dx_app` or `dx_stream` — for those, use the Local or Docker Installation above.
Pin a component instead of tracking `main` with `DX_RT_VERSION`, `DX_DRIVER_VERSION`, or
`DX_FW_VERSION`, e.g. `curl -fsSL ... | DX_RT_VERSION=3.5.0 sh`. `DX_FW_VERSION` covers M1,
M1M and H1 together — the three are released as one firmware set, and H1 ships inside the
M1 version directory. Because the versions are
resolved at run time, the ar
```
