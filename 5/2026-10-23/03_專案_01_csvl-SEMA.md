# GitHub 專案 01：csvl/SEMA

- 日期：2026-10-23
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals]

## 在做什麼
SEMA 是一個基於 angr 的符號執行工具鏈，用於從二進位檔案中提取系統呼叫並構建系統呼叫依賴圖（SCDG），進而利用圖礦石與 SVM（含 INRIA 或 Weisfeiler-Lehman 圖核）進行惡意軟體家族的特徵提取與分類，目標使用者為惡意軟體研究者、逆向工程師與安全分析師，解決手動特徵工程耗時且難以捕捉行為關聯的問題。

## 技術
專案主要使用 Python 實作，核心依賴 angr 框架進行符號執行以追蹤系統呼叫及其參數；透過自訂啟發式優化符號執行，將多條執行追蹤合併為 System Call Dependency Graph（SCDG），節點為系統呼叫，邊代表共享參數；接著使用 gspan 進行常見子圖探索，或利用 SVM 與 INRIA 圖核／Weisfeiler-Lehman 圖核進行分類；此外提供 SemaWebApp 網頁介面來管理實驗與視覺化，並透過 pre‑commit、Makefile 確保程式碼品質與建置流程。

## 架構
架構由四個主要階段組成：(1) 資料準備：收集標註好的惡意軟體二進位檔案作為輸入；(2) 符號執行與圖建構：使用 angr 對每個二進位檔案進行符號執行，記錄所有系統呼叫及其參數，依據啟發式規則將追蹤合併為節點為系統呼叫、邊為共享參數的 SCDG；(3) 特徵與簽名生成：對同家族的多個 SCDG 執行 gspan 常見子圖探索或圖核方法，提取代表性圖樣作為族群簽名；(4) 分類與偵測：對待測試樣本重複產生 SCDG，計算其與已知簽名的相似度（子圖覆蓋率）或透過 SVM＋圖核進行分類，最終輸出家族標籤或惡意/良性判斷。整個流程可透過 SemaWebApp 網頁介面啟動 SemaSCDG（圖萃取）與 SemaClassifier（分類）兩個子實驗，README 中已說明模組與資料流，至於具體啟發式細則與停止條件則需參考原始碼推斷。

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
