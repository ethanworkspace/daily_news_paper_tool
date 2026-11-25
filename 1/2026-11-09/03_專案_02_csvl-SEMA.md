# GitHub 專案 02：csvl/SEMA

- 日期：2026-11-09
- URL：https://github.com/csvl/SEMA
- 描述：SEMA is based on angr, a symbolic execution engine  used to extract API calls. Especially, we extend ANGR with strategies to create representative signatures based on System Call Dependency graph (SCDG). Those SCDGs can be exploited in machine learning modules to do classification/detection.
- Stars：124  |  Forks：25  |  Language：Python
- License：BSD-2-Clause
- Topics：angr, binary-analysis, classification, concolic-execution, ctf, cybersecurity, detection, linux, malware, malware-analysis, malware-detection, malware-research, python, reverse, reverse-engineering, sema, static-analysis, symbolic, symbolic-execution, windows
- 更新時間：2026-10-08T12:54:10+00:00
- 配對論文：https://doi.org/10.1007/978-3-031-31108-6
- 品質分數：9/10 [paper_paired, implementation_signals, stale_seed]

## 在做什麼
SEMA 是一個基於 angr 符號執行引擎的惡意程式分析工具鏈，其目標是從標記好的二進位檔案中自動提取系統呼叫依賴圖（SCDG），並利用圖礦業（gspan）與 SVM 加上圖核心（INRIA 或 Weisfeiler‑Lehman）進行惡意軟體家族的特徵建構與分類。主要使用者為惡意程式研究者、安全工程師與 CTF 參賽者，他們需要一種能夠將符號執行產生的 API 呼叫轉換為可用於機器學習的圖形特徵，以解決傳統靜態特徵難以捕捉行為變異的問題。

## 技術
SEMA 使用 Python 實作，核心依賴 angr 進行符號執行與半符號（concolic）分析，以提取系統呼叫及其參數；透過自訂啟發式規則最佳化符號執行路徑，將多條執行追蹤合併為系統呼叫依賴圖（SCDG），其中節點為系統呼叫，邊代表參數共享；接著利用 gspan 演算法挖掘最大公共子圖，產生族群特徵簽名；最後採用支援向量機（SVM）搭配 INRIA 圖核心或 Weisfeiler‑Lehman 延伸圖核心進行分類；專案同時提供 Makefile 與 pre‑commit 鉤子以統一建置與程式碼品質，並附帶 SemaWebApp 網頁介面來啟動實驗。

## 架構
工具鏈流程如下：首先將已標記之惡意程式二進位檔送入 angr 進行符號執行，記錄所有系統呼叫及其引數；依據預設停機條件（如路徑數上限或時間），將收到的追蹤經由圖啟發式規則組合成 SCDG，其中節點為系統呼叫，邊表示兩個呼叫共享至少一個引數；對每個惡意軟體家族的 SCDG 集合執行 gspan 圖礦業，提取最常見的子圖作為該家族的簽名；對於未知樣本，重複上述步驟產生其 SCDG，然後計算其與已知族群簽名之相似度（例如子圖佔比）或直接送入 SVM‑圖核心分類器，得到家族標籤；整個流程可透過 Makefile 指令或 SemaWebApp 網頁介面觸發，使研究者能夠一鍵執行特徵萃取、簽名建立與分類實驗。

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
