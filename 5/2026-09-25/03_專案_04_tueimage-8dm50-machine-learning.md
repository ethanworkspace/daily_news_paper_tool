# GitHub 專案 04：tueimage/8dm50-machine-learning

- 日期：2026-09-25
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
本專案為 Eindhovens 工業大學 8DM50《醫學影像與生物機器學習》課程的教學資源庫，主要面向修讀該課程的研究生與高年級本科生。課程目標是讓學生理解機器學習基本概念，掌握常見算法（如線性模型、支撐向量機、隨機森林、深度學習與 Transformer），並能在醫學影像與計算生物學領域設計實驗、執行模型訓練與評估。透過講義、實作筆記與課堂討論，幫助學生將理論知識應用於真實醫學數據問題。

## 技術
資料庫主要使用 TeX 編寫說明文件與講義，課程實作採用 Python 進行，以 Jupyter Notebook 形式提供練習題，其中一次作業在 Google Colab 環境完成。環境設定說明位於 software.md，建議使用 Git 管理程式碼與版本。課程資訊與作業提交則透過 TU/e 的 Canvas 平台進行，學生可在 Canvas 討論區提問。此外，參考書籍採用線上免費 PDF 形式，如《Deep Learning》與《Elements of Statistical Learning》。

## 架構
課程結構分為講義、實作與評量三部分。講義以 PDF 形式放在 lectures/ 目錄，對應每週主題；實作練習則放在 practicals/ 目錄，以 Jupyter Notebook (.ipynb) 形式呈現，學生在 guided self‑study 時段完成並可於 Canvas 上傳作業。課程資訊（時間表、指引、常見問題）存放於根目錄的 README 與各種 .md 檔案，Canvas 用於發布非公開連結、收作業及討論區。評量包括實作佔 25%、閱讀報告 10%、期末考 65%，成績由助教在 Canvas 中給出。若需推斷資料流，則為：教師上傳講義與筆記 → 學生下載 → 完成 Jupyter 練習 → 透過 Canvas 提交 → 助教批分。

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
