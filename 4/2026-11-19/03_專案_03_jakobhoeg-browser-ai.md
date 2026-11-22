# GitHub 專案 03：jakobhoeg/browser-ai

- 日期：2026-11-19
- URL：https://github.com/jakobhoeg/browser-ai
- 描述：In-browser AI model providers for the Vercel AI SDK, built to make client-side AI integration simpler and more consistent across vendors.
- Stars：208  |  Forks：27  |  Language：TypeScript
- License：NOASSERTION
- Topics：ai, ai-sdk, browser, browser-ai, built-in-ai, chrome-ai, edge, inference, llm, transformer-models, transformers, transformers-js, vercel, webllm
- 更新時間：2026-11-16T05:50:25+00:00
- 配對論文：
- 品質分數：8/10 [implementation_signals]

## 在做什麼
此專案提供適用於 Vercel AI SDK 的瀏覽器內 AI 模型提供者，讓開發者能在 Chrome/Edge、WebLLM、Transformers.js 或 wllama 等環境中直接執行大型語言模型，並自動在不支援時回退至伺服器端模型。目標使用者為希望簡化客戶端 AI 整合、減少自訂 Hook、UI 元件與狀態管理複雜度的前端與全棧開發者，核心問題在於瀏覽器推論的碎片化與備援機制的實作成本。

## 技術
專案以 TypeScript 編寫，透過四個 NPM 套件（@browser-ai/core、@browser-ai/web-llm、@browser-ai/transformers-js、@browser-ai/wllama）分別封裝 Chrome/Edge Prompt API、WebLLM、Transformers.js 與 wllama（llama.cpp）推論引擎。核心套件定義與 Vercel AI SDK 相容的提供者介面及自動備援邏輯，各引擎套件負載模型載入、WebGPU/WebAssembly 執行與結果回傳。全部為 ES 模組，可在現代瀏覽器中直接使用，無需額外伺服器。

## 架構
架構上，@browser-ai/core 作為統一入口，提供 createBrowserAIProvider 函式，依傳入的 provider 名稱（chrome、webllm、transformersjs、wllama）載入對應的實作套件。當應用透過 Vercel AI SDK 呼叫 generateText、streamText 等 API 時，SDK 會委派給 browser-ai 提供者，該提供者在主線程或 Web Worker 中初始化模型（若尚未載入），透過各自引擎進行推論，並將結果回傳給 SDK。若提供者因瀏覽器不支援或模型載入失敗，核心套件會自動切換至 AI SDK 的伺服器端模型作為備援。資料流程為：使用者輸入 → SDK → browser-ai 提供者 → 模型推論（在瀏覽器） → 輸出 → SDK 回傳給應用。由於 README 未詳細說明內部執行緒與快取機制，以上說明僅基於可見的套件結構與使用範例推斷。

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
