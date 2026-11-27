# GitHub 專案 04：tueimage/8dm50-machine-learning

- 日期：2026-09-21
- URL：https://github.com/tueimage/8dm50-machine-learning
- 描述：TU/e 8DM50 Machine Learning in Medical Imaging and Biology course materials.
- Stars：42  |  Forks：101  |  Language：TeX
- License：MIT
- Topics：
- 更新時間：2026-09-15T08:53:50+00:00
- 論文層級：未對應論文
- 配對論文：
- 品質分數：5/10 

## 在做什麼
本專案提供荷蘭埃因霍芬理工大學 8DM50 課程《Medical Imaging and Biology 中的機器學習》的教學資源，包括講義投影片、Jupyter 筆記本實作練習、環境設置指南及 Python 自我評估測驗，目標對象為修讀該課程的研究生以及對醫學影像與計算生物學應用機器學習感興趣的學習者，旨在幫助學生理解機器學習基本概念、實作常見模型並學會設計實驗與批判性評估結果。

## 技術
課程主要使用 Python 程式語言進行實作，實作練習以 Jupyter Notebook 形式提供，其中一項作業在 Google Colab 上完成；講義投影片採用 LaTeX（TeX）編輯產出 PDF；環境設置說明於 software.md 中，包含建議的套件與版本控管（Git）使用方式；課程資訊與作業提交透過 Canvas 平台進行，學生可在其討論區提出問題。

## 架構
資料結構分為講義（lectures/ 目錄下的 PDF 投影片）、實作練習（practicals/ 目錄下的 Jupyter Notebook）、環境與工具指南（software.md、how_to_ask_questions.md）、評量材料（exam.pdf、Python quiz）等模組。學生先依照 software.md 設定 Python 虛擬環境與必要套件，接著依課程進度下載對應週次的筆記本進行實作，完成後將答案或報告上傳至 Canvas 的 Assignments 區；若使用 ChatGPT 等大型語言模型，需另繳交一頁使用心得報告。整體流程為：取得資源 → 環境設置 → 觀看講義 → 完成實作 → 提交作業 → 參與討論 → 期末考試。由於 README 未詳細說明底層推論框架或自動化測流程，以上架構說明僅基於可見的目錄與說明文件推斷。

## README 摘錄（節選）
```text
# Machine Learning in Medical Imaging and Biology (8DM50)
The course covers a number of machine learning methods and concepts, including state-of-the-art deep learning methods, with example applications in the medical imaging and computational biology domains.
## Use of Canvas
This GitHub page contains all the general information about the course and the study materials. The Canvas page of the course (https://canvas.tue.nl/courses/31358) will be used only for sharing of course information that cannot be made public (e.g. Microsoft Teams links), submission of the practical work and posting questions to the instructors and teaching assistants (in the Discussion section). The students are highly encouraged to use the Discussion section in Canvas. All general questions (e.g. issues with setting up the programming environment, error messages etc., general methodology questions) should be posted in the Discussion section. **Such questions asked by email will not be answered.**
** TLDR**: GitHub is for content, Canvas for communication and submission of assignments. Do not ask questions by email unless absolutely necessary.
## Schedule
The course schedule is as follows:
* **Lectures**, *time*: Wednesdays 08:45 - 10:45, *location*: Neuron -1.354 (always check your timetable for changes).
* **Guided self-study**, *time*: Wednesdays 10.45 - 12.45, *location*: Atlas 4.215 (always check your timetable for changes).
## Practical work
The practical work will be done in groups. The groups will be formed in Canvas and you will also submit all your work there (check the Assignments section for the deadlines). Your are expected to do this work independently with the help of the teaching assistants during the guided self-study sessions (*begeleide zelfstudie*). You can also post your questions in the Discussion section in Canvas at any time (i.e. not just during the practical sessions).
** IMPORTANT: Please read this guide (how_to_ask_questions.md) on effectively asking questions during the practical sessions.**
### Use of ChatGPT and other large language models
The use of ChatGPT and other large language models for the practical work is allowed, provided that:
1) You use ChatGPT and other large language models only as aid in your work and **NOT** as primary sources of information (e.g. to do literature search), and primary mode of writing and coding (e.g. asking for answers to entire assignment questions is not allowed, however, improving the writing or coding of answers to questions is allowed).
2) You write a one-page reflection report on the use of such tools answering the following questions:
* What were the up- and down-sides of using ChatGPT (or similar tools) in your work?
* In your view, are such tools helpful or harmful when used in education?
* Did it make you more or less productive?
* How did you specifically use these tools (give examples)?
* Were these tools accurate in their answers?
Note that the report is **mandatory** if you used ChatGPT (or similar tools) in any way for the course and it does NOT have any negative consequence (e.g. lead to lower grades). If you do not submit the report we will assume that you did not use such tools but if this is detected during the grading it will be considered cheating.
# Materials
## Books
The lectures are mainly based on the selected chapters from the following two books that are freely available online:
* Deep Learning (https://www.deeplearningbook.org/), Ian Goodfellow and Yoshua Bengio and Aaron Courville
* Elements of Statistical Learning (https://web.stanford.edu/~hastie/ElemStatLearn/), Trevor Hastie, Robert Tibshirani, Jerome Friedman
The follwing book is optional but highly recommended:
* Probabilistic Machine Learning: An Introduction (https://probml.github.io/pml-book/book1.html), Kevin Patrick Murphy.
Additional reading materials such as journal articles are listed within the lecture slides.
## Software
** IMPORTANT: It is essential that you correctly set up the Python working
```
