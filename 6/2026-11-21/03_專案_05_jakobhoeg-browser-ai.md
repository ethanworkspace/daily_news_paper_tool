# GitHub 專案 05：jakobhoeg/browser-ai

- 日期：2026-11-21
- URL：https://github.com/jakobhoeg/browser-ai
- 描述：In-browser AI model providers for the Vercel AI SDK, built to make client-side AI integration simpler and more consistent across vendors.
- Stars：208  |  Forks：27  |  Language：TypeScript
- License：NOASSERTION
- Topics：ai, ai-sdk, browser, browser-ai, built-in-ai, chrome-ai, edge, inference, llm, transformer-models, transformers, transformers-js, vercel, webllm
- 更新時間：2026-11-16T05:50:25+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
Browser AI model providers for the Vercel AI SDK enable developers to run language models directly in the browser (via Chrome/Edge AI, WebLLM, Transformers.js, or wllama) while automatically falling back to server‑side models when client‑side execution is unavailable. The target users are web developers building AI‑powered applications who want a consistent, vendor‑agnostic API without writing custom hooks, UI components, or complex fallback logic.

## 技術
The libraries are written in TypeScript and expose ES‑module packages (@browser-ai/core, @browser-ai/web-llm, @browser-ai/transformers-js, @browser-ai/wllama). They integrate with the Vercel AI SDK and wrap browser‑specific inference backends: the Chrome/Edge Prompt API, WebLLM (WebGPU‑based), Transformers.js (running transformer models via WebAssembly), and wllama (llama.cpp compiled to WebAssembly). No external build steps are required; the packages work in modern browsers that support the respective APIs.

## 架構
@browser-ai/core defines a common provider interface used by the Vercel AI SDK. Each provider package implements this interface for a specific in‑browser runtime (Chrome/Edge AI, WebLLM, Transformers.js, wllama). When the SDK requests a generation, core selects the first available provider, executes the model in the browser, and streams the result back. If the selected provider fails or is unsupported, core automatically falls back to the server‑side model configured in the Vercel AI SDK. The flow is: user call → SDK → core provider selection → browser inference → result → (fallback if needed) → SDK returns output to the application.

## README 摘錄（節選）
```text
# Browser AI model providers for Vercel AI SDK
(https://www.npmjs.com/package/@browser-ai/core)
(https://www.npmjs.com/package/@browser-ai/web-llm)
(https://www.npmjs.com/package/@browser-ai/transformers-js)
(https://www.npmjs.com/package/@browser-ai/wllama)
TypeScript libraries that provide access to in-browser AI model providers with seamless fallback to using server-side models.
## Documentation
For detailed documentation, browser requirements and advanced usage, refer to the official documentation site (https://browser-ai.dev/docs).
### Package Versions
| Package | AI SDK v5 | AI SDK v6 | AI SDK v7 |
| ----------------------------- | :-------: | :-------: | :---------: |
| `@browser-ai/core` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/transformers-js` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/web-llm` | ✓ `1.0.0` | ✓ `2.x` | ✓ `≥ 3.0.0` |
| `@browser-ai/wllama` | - | - | ✓ `≥ 3.0.0` |
[code block omitted]
### Basic Usage with Chrome/Edge AI
[code block omitted]
### Basic Usage with WebLLM
[code block omitted]
### Basic Usage with Transformers.js
[code block omitted]
### Basic Usage with wllama (llama.cpp)
[code block omitted]
## Resources
### Articles & guides
- Chrome for Developers: Use the Prompt API with the Vercel AI SDK (https://developer.chrome.com/blog/prompt-api-with-vercel-ai?hl=en)
- Chrome for Developers: Use the Vercel AI SDK UI and AI Elements with the Prompt API (https://developer.chrome.com/blog/prompt-ui-ai-elements-with-vercel-ai?hl=en)
- Hugging Face: Building a Next.js application with the AI SDK (https://huggingface.co/docs/transformers.js/tutorials/next-ai-sdk)
- Hugging Face: Transformers.js × Vercel AI SDK integration (https://huggingface.co/docs/transformers.js/integrations/vercel-ai-sdk)
### Example applications
- Huggingface Transformers.js AI SDK v5: next-vercel-ai-sdk-v5-transformers-js-example (https://github.com/huggingface/transformers.js-examples/tree/main/next-vercel-ai-sdk-v5)
- Huggingface Transformers.js AI SDK v6: next-vercel-ai-sdk-v6-transformers-js-example (https://github.com/huggingface/transformers.js-examples/blob/main/next-vercel-ai-sdk-v6-tool-calling)
## Sponsors
This project is part of the Vercel OSS Program (https://vercel.com/open-source-program), and was previously sponsored by Chrome for Developers (https://developer.chrome.com/).
## Contributing
Contributions are more than welcome! However, please make sure to check out the contribution guidelines (https://github.com/jakobhoeg/browser-ai/blob/main/CONTRIBUTING.md) before contributing.
## Why?
If you've ever built apps with local language models, you're likely familiar with the challenges: creating custom hooks, UI components and state management (lots of it), while also building complex integration layers to fall back to server-side models when compatibility is an issue.
Read more about this here (https://www.browser-ai.dev/docs/ai-sdk-v7).
## Author
2025 © Jakob Hoeg Mørk
```
