# GitHub 專案 03：FastCrest/tether

- 日期：2026-11-11
- URL：https://github.com/FastCrest/tether
- 描述：FastCrest Tether: the OSS edge-to-cloud AI deploy CLI. Optimize, verify, deploy across Jetson, RTX, Apple Silicon, AMD. Hybrid edge-cloud inference with parity certs.
- Stars：86  |  Forks：21  |  Language：Python
- License：NOASSERTION
- Topics：cli, deployment, edge-ai, edge-cloud, fastcrest, groot, inference, jetson, onnx, pi0, python, robot-learning, robotics, smolvla, tensorrt, tether, vision-language-action, vla
- 更新時間：2026-11-01T01:06:22+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
FastCrest Tether 是一個開源的邊緣到雲端 AI 部署命令列工具，專門針對視覺語言動作（VLA）機器人策略提供部署信心。它能在 Jetson、RTX、Apple Silicon、AMD 等平台上最佳化、驗證並部署模型，支援混合式邊緣‑雲端推理與 parity 證明，確保策略在真實硬體上安全前進。目標使用者為機器學習工程師、機器人系統開發者與邊緣設備運維人員，核心問題是如何在異質硬體上保證 VLA 模型的數值等價與推論可靠性。

## 技術
Tether 以 Python 3.10+ 為主要語言，提供 CLI 介面；核心功能包括將 PyTorch VLA 模型匯出為單一 ONNX（支援外部權重資料 >2GB），使用 ONNX Runtime 搭配 CUDA、TensorRT 或 CPU 執行提供者，可選擇 Triton fast kernels 以獲得額外加速；支援 safetensors 直接載入減少記憶體開銷，並提供 ZMQ 傳輸與 msgpack 圖像序列化以實現低延遲機器人通訊；內建 ROS2 適配器起始套件、transformers 5.x DynamicCache 相容性修復以及 DreamZero WAM、FluxVLA 等新 VLA 家族的支援。

## 架構
Tether 的架構圍繞模組化 CLI 指令與 BaseVLA 骨幹展開：安裝階段會偵測硬體與 Python 版本，自動選擇對應的安裝 extras（serve、gpu、onnx、monolithic、fast‑kernels 等）；匯出階段透過各 VLA 的匯出器（pi0、smolvla、gr00t）將模型轉換為 monolithic ONNX，必要時會分割為 .onnx + .onnx_data；服務階段載入 ONNX 模型，依據選擇的執行提供者（CUDAExecutionProvider、TensorrtExecutionProvider 或 CPU）建立推理 session，可透過 --transport zmq 使用 ZMQ 低延遲通道，並將錯誤導向 stderr 以保持 JSON 輸出乾淨；雲端或邊緣驗證則透過 tether connect 與 parity 證明機制，比對參考 PyTorch 政策的輸出以確保數值等價（cos = 1.0）。整體資料流為：使用者指令 → 安裝/匯出 → 本地或遠端推理服務 → 結果回傳給機器人控制迴路或驗證腳本。若 README 未明確說明某些內部細節，則標示為推斷依據不足。

## README 摘錄（節選）
```text
# Tether
> by FastCrest (https://fastcrest.com) — deployment infrastructure for vision-language-action models.
(https://pypi.org/project/fastcrest-tether/)
(https://pypi.org/project/fastcrest-tether/)
(https://github.com/FastCrest/tether/blob/main/LICENSE)
(https://pypi.org/project/fastcrest-tether/)
** Deployment confidence for VLA robot policies** — Tether answers one production question: can this policy safely move forward?
** Verified parity across ALL four major open VLAs.** Tether's monolithic ONNX export matches the reference PyTorch policy to **cos = +1.000000** end-to-end on SmolVLA, pi0, pi0.5 (canonical 10-step flow-matching unrolled) and GR00T N1.6 (canonical 4-step DDIM loop external to the ONNX). Per-model first-action max_abs: SmolVLA 5.96e-07, pi0 2.09e-07, pi0.5 2.38e-07, GR00T 8.34e-07 — all at machine precision, shared seeded inputs. Full claim ledger in reflex_context/measured_numbers.md (reflex_context/measured_numbers.md).
The public workflow is intentionally small:
[code block omitted]
Everything else in the CLI feeds evidence into that answer.
## Install
** Recommended** — runs hardware + Python checks first, picks the right install extras for your machine:
[code block omitted]
The bootstrap installer detects your platform (Mac / Jetson Orin / NVIDIA GPU / CPU) and chooses the right extras automatically. It also bails early with a useful message on unsupported hardware (e.g. original 4 GB Jetson Nano — Maxwell GPU + JetPack 4.6 / Python 3.6, too old for VLAs).
** Manual install** if you know what you want:
[code block omitted]
`serve` installs the HTTP stack; choose `onnx` or `gpu` for the inference
runtime. Keep model export in its own virtual environment with `[monolithic]`
when its PyTorch/CUDA requirements differ from serving. The default GPU extra
selects one bounded CUDA 12 dependency family. Jetson uses its JetPack vendor
stack through the installer instead of these x86 GPU wheels. A manually managed
CUDA 13 serving environment must provide matching ORT, TensorRT and CUDA
libraries; mixing CUDA families is not an automatic repair path.
Requires Python ≥ 3.10.
For a smaller existing monolithic export, use the opt-in
validated mixed-FP16 conversion (docs/precision-conversion.md). It preserves the
FP32 source and requires supplied parity inputs and explicit tolerances. Target
memory fit and TensorRT remain separate qualification checks.
The standalone RTSM SigLIP encoder export (docs/rtsm-siglip-export.md) records its
checkpoint, applied preprocessing and CPU parity; policy integration needs a
separate adapter contract.
### What's new in v0.11.2 (2026-05-29)
- **`tether connect` works on a clean install** — `requests` is now a core dependency, so `tether connect status` no longer raises `ModuleNotFoundError` on `pip install fastcrest-tether` without extras (it had been an undeclared import that only resolved transitively).
- **`--fast-kernels` cleared the formal N=100/task L3 LIBERO parity gate** — on Pi0.5 LIBERO-10 tasks 0-2 (600 episodes), Triton fast kernels scored 91.3% (274/300) vs native ORT 85.3% (256/300) — 6.0pp *ahead* of native, so kill-trigger 3 stays clear and the opt-in Triton runtime stays on.
- **Hardened monolithic serve/bench path, with external-data ONNX** — dedicated ORT provider-options + tokenizer-loading modules are extracted from the request hot path; ONNX models with external weight data (`.onnx` + `.onnx_data`, required once a graph exceeds the 2 GB protobuf limit) now load in both serve and the weight-fusion export pass.
- **Cleaner streams** — integration-command errors route to stderr, so `--json` consumers and shell pipelines get a clean stdout.
### What's new in v0.11.1 (2026-05-27)
- **Triton fast kernels** — 2.5x PyTorch, ~12x ORT on A100. Opt in with `tether serve --fast-kernels` (requires the `[fast-kernels]` extra). Falls back to ORT silently when Triton is unavailable.
- **ZMQ transport** — `tether serve --transport zmq` for low-latency robot communication. JPEG
```
