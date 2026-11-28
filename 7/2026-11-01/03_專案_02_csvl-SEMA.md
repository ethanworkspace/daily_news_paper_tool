# GitHub 專案 02：csvl/SEMA

- 日期：2026-11-01
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
SEMA 是一個基於 angr 符號執行引擎的惡意程式分析工具鏈，目標是從二進位檔案中提取系統呼叫及其參數，構建系統呼叫依賴圖（SCDG），並利用圖探勘與機器學習方法產生代表性簽名，以實現惡意軟體家族的分類與偵測。適用於安全研究人員、惡意程式分析師以及需要自動化特徵提取與分類的 CTF 參賽者。

## 技術
專案主要使用 Python 實作，核心依賴 angr 框架進行符號執行以提取 API 呼叫與參數。透過自訂啟發式規則最佳化符號執行，並將多條執行追蹤合併為系統呼叫依賴圖（SCDG），其中節點為系統呼叫，邊代表參數共享。接著使用 gspan 演算法提取最大公共子圖，並計算相似度分數；分類階段則採用支援向量機（SVM）搭配 INRIA 圖核或 Weisfeiler-Lehman 擴展圖核。此外，提供 SemaWebApp 網頁應用來管理實驗的啟動與結果檢視，並透過 pre-commit 保證程式碼格式與品質，Makefile 簡化工具鏈的使用流程。

## 架構
工具鏈流程如下：首先將標註好的惡意程式二進位檔案作為輸入；接著利用 angr 進行符號執行，在符號執行過程中記錄所有系統呼叫及其參數；在達到預設停止條件後，將這些呼叫與參數構造成 SCDG，節點為系統呼叫，邊表示兩個呼叫之間有共享的參數。接著對同一家族的多個 SCDG 進行圖探勘（使用 gspan）提取最大公共子圖，以此產生代表該家族的簽名。對於未知樣本，重複上述步驟建立其 SCDG，然後與已知家族的簽名圖計算相似度分數（基於子圖包含度），或直接送入 SVM 與圖核進行分類。整個流程可透過 SemaWebApp 網頁介面啟動實驗、檢視圖與分類結果，並由 Makefile 提供一鍵指令簡化操作。

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
