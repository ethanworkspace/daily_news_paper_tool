# GitHub 專案 05：csvl/SEMA

- 日期：2026-11-17
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SEMA 是一個基於 angr 的符號執行工具鏈，用於從惡意程式二進位檔中提取系統呼叫及其參數，構建系統呼叫依賴圖（SCDG），然後利用圖挖掘（gspan）與圖核 SVM 進行惡意軟體家族的特徵提取與分類。目標使用者為惡意軟體分析師、安全研究員與 CTF 參賽者，核心在於自動化從二進位檔產生可辨識的圖結構特徵，以解決傳統靜態特徵難以捕捉行為變異的問題。

## 技術
專案主要使用 Python 實作，核心依賴 angr 框架進行符號執行以提取 API 呼叫與參數；透過自發 heuristics 優化符號執行，將多條執行追蹤合併為系統呼叫依賴圖（SCDG）；接著使用 gspan 演算法提取最大公共子圖，並以圖相似度評分或 SVM 搭配 INRIA 圖核、Weisfeiler-Lehman 延伸圖核進行分類；此外提供 SemaWebApp 網頁介面管理實驗，並透過 pre‑commit 與 Makefile 確保程式碼品質與重建流程。

## 架構
架構方面，SEMA 的工具鏈分為四個主要階段：首先，將標註好的惡意程式二進位檔送入 angr 進行符號執行，在執行過程中記錄所有系統呼叫及其參數；其次，依據預設的停止條件（如路徑數量或時間）將收到的追蹤透過圖啟發式合併，以系統呼叫為節點、參數共享為邊構建 SCDG；第三階段，對同家族的多個 SCDG 執行 gspan 圖挖掘提取最大公共子圖，或直接計算圖相似度，亦可將圖轉為核心特徵送入 SVM（使用 INRIA 圖核或 Weisfeiler-Lehman 延伸圖核）進行分類；最後，透過 SemaWebApp 網頁應用提供實驗啟動、結果視覺化與模型管理，整個流程可由 Makefile 一鍵執行。若需更細緻的模組間資料流（如特徵向量產製）則需參考原始碼，此處僅根據 README 推斷。

## README 摘錄（節選）
```text
# :skull_and_crossbones: SEMA :skull_and_crossbones:
## ToolChain using Symbolic Execution for Malware Analysis.
[code block omitted]
(https://gendocs.readthedocs.io/en/latest/)
(https://github.com/csvl/SEMA-ToolChain/actions/workflows/.pre-commit-config.yaml)
(https://github.com/csvl/SEMA-ToolChain/actions/workflows/github-code-scanning/codeql)
(https://github.com/csvl/SEMA-ToolChain/actions/workflows/pr-generate-docs.yaml)
(https://github.com/csvl/SEMA-ToolChain/actions/workflows/pages/pages-build-deployment)
(https://github.com/csvl/SEMA-ToolChain/actions/workflows/python-app.yml)
### Toolchain architecture
Our toolchain is represented in the following figure and works as follows:
- A collection of labelled binaries from different malware families is collected and used as the input of the toolchain.
- **Angr**, a framework for symbolic execution, is used to execute binaries symbolically and extract execution traces. For this purpose, different heuristics have been developed to optimize symbolic execution.
- Several execution traces (i.e., API calls used and their arguments) corresponding to one binary are extracted with Angr and gathered together using several graph heuristics to construct a SCDG.
- These resulting SCDGs are then used as input to graph mining to extract common graphs between SCDGs of the same family and create a signature.
- Finally, when a new sample has to be classified, its SCDG is built and compared with SCDGs of known families using a simple similarity metric.
This repository contains a first version of a SCDG extractor. During the symbolic analysis of a binary, all system calls and their arguments found are recorded. After some stop conditions for symbolic analysis, a graph is built as follows: Nodes are system calls recorded, edges show that some arguments are shared between calls.
When a new sample has to be evaluated, its SCDG is first built as described previously. Then, `gspan` is applied to extract the biggest common subgraph and a similarity score is evaluated to decide if the graph is considered as part of the family or not. The similarity score `S` between graph `G'` and `G''` is computed as follows:
Since `G''` is a subgraph of `G'`, this is calculating how much `G'` appears in `G''`.
Another classifier we use is the Support Vector Machine (`SVM`) with INRIA graph kernel or the Weisfeiler-Lehman extension graph kernel.
A web application is available and is called SemaWebApp. It allows to manage the launch of experiments on SemaSCDG and/or SemaClassifier.
### Pre-commit
This repository uses pre-commit to ensure that the code is formatted correctly and that the code is clean. To install pre-commit, run the following command:
[code block omitted]
### Documentation
* Complete README of the entire toolchain :
* SCDG README :
* Classifier README :
* Web app README :
* A Makefile is provided to ease the usage of the toolchain, run
[code block omitted]
for more information about the available commands
### Credentials
Main authors of the projects:
* **Charles-Henry Bertrand Van Ouytsel** (UCLouvain)
* **Christophe Crochet** (UCLouvain)
* **Khanh Huu The Dam** (UCLouvain)
* **Oreins Manon** (UCLouvain)
Under the supervision and with the support of **Fabrizio Biondi** (Avast)
Under the supervision and with the support of our professor **Axel Legay** (UCLouvain) (:heart:)
### Linked papers
* Analysis and classification of malware based on symbolic execution and machine learning (https://dial.uclouvain.be/pr/boreal/object/boreal:285757)
* Tool Paper - SEMA: Symbolic Execution Toolchain for Malware Analysis (https://doi.org/10.1007/978-3-031-31108-6\_5)
* On Exploiting Symbolic Execution to Improve the Analysis of RAT Samples with angr (https://dial.uclouvain.be/pr/boreal/object/boreal%3A280744/datastream/PDF_01/view)
```
