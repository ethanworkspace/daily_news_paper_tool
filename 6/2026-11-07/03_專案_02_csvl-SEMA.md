# GitHub 專案 02：csvl/SEMA

- 日期：2026-11-07
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
SEMA 是一個基於 angr 符號執行引擎的惡意程式分析工具鏈，目標使用者為惡意程式研究者、逆向工程師與安全分析師。它自動從標記好的二進位檔案中提取系統呼叫及其參數，構建系統呼叫依賴圖（SCDG），並利用圖形挖掘與機器學習（SVM 與圖核）產生代表性簽名，以實現惡意程式家族的分類與偵測。

## 技術
技術實現主要使用 Python 程式語言，依賴 angr 框架進行二進位檔案的符號執行以擷取系統呼叫及其參數；接著透過圖論啟發式方法將提取的追蹤組合成系統呼叫依賴圖（SCDG），節點為系統呼叫，邊代表共享參數。然後使用 gspan 演算法進行頻繁子圖挖掘，尋找同家族 SCDG 間的最大公共子圖；最後採用支援向量機（SVM）搭配 INRIA 圖核或 Weisfeiler‑Lehman 圖核進行分類，並提供 SemaWebApp 網頁介面來管理實驗的啟動與結果檢視。

## 架構
工具鏈流程如下：首先將已標記的惡意程式二進位檔案送入 Angr 進行符號執行，產生系統呼叫追蹤（包括呼叫名稱與參數）；根據預設的停止條件將追蹤轉換為 SCDG，其中每個節點對應一次系統呼叫，當兩個呼叫共享至少一個參數時在它們之間加入有向或無向邊；接著對所有同家族的 SCDG 使用 gspan 挖掘頻繁子圖，提取代表該家族的簽圖；對於待判樣本，重複上述步驟產生其 SCDG，然後計算該圖與已知簽圖之間的相似度（例如 gspan 最大公共子圖佔比或 SVM 圖核得分），依據預設閾值決定是否屬於某個惡意程式家族。此外，專案附帶 SemaWebApp 網頁應用，使用者可透過它上傳樣本、觸發符號執行與圖形挖掘任務，並檢視分類結果與中間產生的圖形。README 未詳細說明網頁應用的具體框架或資料儲存方式，因此上述架構描述僅基於文件中可見的模組與資料流程進行推斷。

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
