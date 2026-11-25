# GitHub 專案 04：csvl/SEMA

- 日期：2026-11-12
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SEMA 是一個基於 angr 符號執行引擎的惡意程式分析工具鏈，目標使用者為惡意程式研究者、安全工程師與 CTF 參賽者。它從標記好的惡意程式二進位檔案中提取系統呼叫及其參數，透過圖啟發式構建系統呼叫依賴圖（SCDG），再利用圖礦工具（gspan）與圖核心 SVM 分類器產出代表性簽章，以進行惡意程式家族的偵測與分類。

## 技術
SEMA 使用 Python 實作，核心依賴 angr 進行符號執行以擷取 API 呼叫與參數；透過自訂啟發式優化符號執行，產出多條執行追蹤，再以圖啟發式將系統呼叫及共享參數轉為有向圖（SCDG）。接著利用 gspan 挖掘最大公共子圖，計算相似度分數；亦可選用 SVM 搭配 INRIA 圖核或 Weisfeiler‑Lehman 延伸圖核進行分類。專案透過 pre‑commit 保證程式碼品質，提供 Makefile 簡化指令，並附帶 SemaWebApp 網頁應用來管理實驗與視覺化結果。支援 Linux 與 Windows 二進位檔案的靜態與動態分析流程。

## 架構
架構方面，SEMA 的資料流程大致如下：首先，收集具標籤的惡意程式二進位檔案作為輸入；接著，使用 angr 對每個二進位檔案進行符號執行，在符號執行過程中記錄所有系統呼叫及其參數；根據預設的停止條件，將記錄的系統呼叫當作節點，若兩個呼叫共享參數則在它們之間加入有向邊，從而構建系統呼叫依賴圖（SCDG）；接著，對同一家族的多個 SCDG 運用圖礦工具（gspan）提取最大公共子圖，或利用圖核心 SVM 學習族內特徵，產出代表性簽章；當有新樣本需判斷時，重複上述符號執行與 SCDG 建構步驟，然後將其 SCDG 與已知族的簽章透過相似度計算（子圖佔比）或 SVM 分類器進行比較，得到惡意程式家族的預測結果。整個流程可透過 Makefile 指令或 SemaWebApp 網頁介面觸發，方便實驗的批次執行與結果檢視。由於 README 未提供詳細的類別圖或元件圖，以上說明僅根據文本敘述推斷而得。

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
