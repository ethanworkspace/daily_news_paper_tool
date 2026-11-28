# GitHub 專案 03：csvl/SEMA

- 日期：2026-11-10
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 論文層級：未對應論文
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals, stale_backfill]

## 在做什麼
SEMA 是一個基於 angr 符號執行引擎的惡意程式分析工具鏈，目標是從二進位檔案中提取系統呼叫依賴圖（SCDG），並利用圖探勘與機器學習方法建構代表惡意家族的簽名，以實現自動化的惡意程式分類與偵測。主要使用者為惡意程式研究者、安全分析師以及需要進行二進位行為特徵提取的開發者，核心問題在於如何從有限的執行痕跡中獲得具區別性的圖結構特徵，以克服傳統靜態或動態特徵易於混淆的限制。

## 技術
SEMA 以 Python 為主要開發語言，核心依賴 angr 框架進行符號執行以提取 API 呼叫及其參數。為提升符號執行效率，專案開發了多種啟發式規則。提取的執行痕跡經圖啟發式處理構建系統呼叫依賴圖（SCDG），之後使用 gspan 演算法尋找最大公共子圖來計算相似度。分類方面，除了基於子圖相似度的簡單度量外，亦支援使用 SVM 搭配 INRIA 圖核或 Weisfeiler-Lehman 擴展圖核進行學習。工具鏈還提供 SemaWebApp 網頁應用，方便管理實驗的啟動與結果檢視，並透過 pre-commit、Makefile 與完整文件保證程式碼品質與使用便利性。

## 架構
SEMA 的工具鏈流程如下：首先，收集具標籤的惡意程式二進位檔案作為輸入；接著，使用 angr 進行符號執行，在執行過程中記錄所有系統呼叫及其參數，並透過先前開發的啟發式規則最佳化符號執行；將同一二進位檔案的多個執行痕跡（API 呼叫與參數）圖啟發式地合併，生成系統呼叫依賴圖（SCDG）；對同家族的多個 SCDG 進行圖探勘（gspan）以提取最大公共子圖，形成該家族的簽名；當需分類新樣本時，先為其構建 SCDG，然後利用子圖相似度度量或 SVM（配合 INRIA 圖核或 Weisfeiler-Lehman 擴展圖核）與已知家族的簽名進行比較，得到分類結果。整個流程可透過 SemaWebApp 網頁介面啟動與監控，並由 Makefile 提供一鍵指令，pre-commit 確保程式碼格式與品質。

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
