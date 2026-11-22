# GitHub 專案 04：NVIDIA-NeMo/Speech

- 日期：2026-11-21
- URL：https://github.com/NVIDIA-NeMo/Speech
- 描述：A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)
- Stars：18775  |  Forks：3698  |  Language：Python
- License：Apache-2.0
- Topics：asr, deeplearning, generative-ai, machine-translation, neural-networks, speaker-diariazation, speaker-recognition, speech-synthesis, speech-translation, tts
- 更新時間：2026-11-22T01:40:08+00:00
- 配對論文：
- 品質分數：9/10 [implementation_signals]

## 在做什麼
A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)
A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)

主要語言：Python；Topics：asr, deeplearning, generative-ai, machine-translation, neural-networks, speaker-diariazation, speaker-recognition, speech-synthesis；Stars：18775；License：Apache-2.0

## 技術
實作語言以 Python 為主。
從 topics 可見技術方向：asr, deeplearning, generative-ai, machine-translation, neural-networks, speaker-diariazation, speaker-recognition, speech-synthesis。
專案描述：A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)

## 架構
README 未明確提供架構章節；依描述推斷此專案聚焦於：A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)

## README 摘錄（節選）
```text
(http://www.repostatus.org/#active)
(https://github.com/NVIDIA-NeMo/Speech/actions/workflows/codeql.yml)
(https://github.com/NVIDIA-NeMo/Speech/blob/main/LICENSE)
(https://badge.fury.io/py/nemo-toolkit)
(https://badge.fury.io/py/nemo-toolkit)
(https://pepy.tech/project/nemo-toolkit)
(https://github.com/psf/black)
# **NVIDIA NeMo Speech**
Checkout our HuggingFace🤗 collection (https://huggingface.co/collections/nvidia/nemotron-speech) for the latest open
weight checkpoints and demos!
## Updates
> NeMo Speech 3.0 is now available as release v3.0.0 (https://github.com/NVIDIA-NeMo/Speech/releases/tag/v3.0.0)
> and in the 26.07.00 NeMo Speech NGC container (https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo-speech?version=26.07.00).
> The final NeMo release before the repository split was
> v2.7.3 (https://github.com/NVIDIA-NeMo/Speech/releases/tag/v2.7.3), available in the
> 26.04 NeMo NGC container (https://catalog.ngc.nvidia.com/orgs/nvidia/containers/nemo?version=26.04).
- 2026-10: Nemotron 3.5 Transcribe (https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B)
is now available: an open-weight, offline speech LLM for 40 languages and recordings up to one hour.
Control transcription with instructions and vocabulary context, request speaker-attributed transcripts with
word timestamps, translate speech, and ask questions about audio. Start with the
NeMo Speech quickstart (https://docs.nvidia.com/nemo/speech/nightly/speechlm2/nemotron_transcribe.html)
or try the demo (https://huggingface.co/spaces/nvidia/nemotron-transcribe).
- 2026-07: MagpieTTS v2607 (https://huggingface.co/nvidia/magpie_tts_multilingual_357m) has been released with support
for 3 new languages (Ar, Ko, Pt) + 9 existing languages (En, Es, De, Fr, Vi, It, Zh, Hi, Ja). Try out
the demo (https://huggingface.co/spaces/nvidia/magpie_tts_multilingual_demo)!
- 2026-06: Nemotron-3.5-ASR-Streaming-0.6B (https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) has been released with 40 languages supported, controllable latency 80ms-1s, and 240-2400 1xH100 concurrent streams. Built on cache-aware Fastconformer architecture.
- 2026-04: Parakeet-unified-en-0.6b (https://huggingface.co/nvidia/parakeet-unified-en-0.6b) has been released with high-quality offline and streaming (with a minimum latency of 160ms) inference in one model for English language with punctuation and capitalization support.
- 2026-03: Nemotron 3 VoiceChat (https://build.nvidia.com/nvidia/nemotron-voicechat/modelcard) is now released in Early Access. Built on the Nemotron Nano v2 LLM backbone with Nemotron speech and TTS decoder, VoiceChat delivers full-duplex, natural, interruptible conversations with low latency. Try out the demo (https://build.nvidia.com/nvidia/nemotron-voicechat) and apply for early access (https://developer.nvidia.com/nemotron-voicechat-early-access).
- 2026-03: Nemotron-Speech-Streaming v2603 (https://huggingface.co/nvidia/nemotron-speech-streaming-en-0.6b) has been
updated. It has been trained on a larger and more diverse corpus, resulting in lower WER across all latency modes.
Try out the demo (https://huggingface.co/spaces/nvidia/nemotron-speech-streaming-en-0.6b) and check out
the NIM (https://build.nvidia.com/nvidia/nemotron-asr-streaming).
- 2026-03: MagpieTTS v2602 (https://huggingface.co/nvidia/magpie_tts_multilingual_357m/tree/v2602) has been released with support
for 9 languages (En, Es, De, Fr, Vi, It, Zh, Hi, Ja).
- 2026-01: Nemotron-Speech-Streaming was released: One checkpoint that enables users to pick their optimal point
on the latency-accuracy Pareto curve!
- 2026-01: MagpieTTS v2512 (https://huggingface.co/nvidia/magpie_tts_multilingual_357m/tree/v2512) was released.
- 2026: This repo has pivoted to focus on audio, speech, and multimodal LLMs. For the final pre-split NeMo release with
support for additional modalities, see v2.7.3 (https://github.com/NVIDIA-NeMo/Speech/releases/tag/v2.7.3).
- 2025-08: Parakeet V3 (https://huggingface.co/nvid
```
