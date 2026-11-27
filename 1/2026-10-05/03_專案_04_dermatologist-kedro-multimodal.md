# GitHub 專案 04：dermatologist/kedro-multimodal

- 日期：2026-10-05
- URL：https://github.com/dermatologist/kedro-multimodal
- 描述：Template for multi-modal machine learning in healthcare using Kedro. Combine reports, tabular data and images using various fusion methods.
- Stars：24  |  Forks：3  |  Language：Python
- License：Apache-2.0
- Topics：healthcare, jupyter, kedro, kubeflow, machine-learning, medical, multi-modal, pipeline, vertex-ai
- 更新時間：2026-01-30T08:02:12+00:00
- 論文層級：未對應論文
- 配對論文：
- 品質分數：7/10 [implementation_signals, stale_backfill]

## 在做什麼
此專案提供一個基於 Kedro 框架的多模態醫療機器學習範本，使使用者能够將病歷報表（文字）、結構化表格資料與醫學影像結合，透過早期融合、晚期融合等多種融合方法訓練統一模型。目標使用者為醫療資料科學家、機器學習工程師與研究人員，核心在解決異質醫療資料整合與特徵融合的挑戰，以提升診斷或預測任務的效果。該範本亦支援 Kubeflow 與 Vertex AI 部署，方便在雲端或混合環境中進行實驗與生產。

## 技術
專案主要使用 Python 3.x，以 Kedro 0.18.4 為工作流 orchestration 框架，搭配 TensorFlow 進行模型訓練與推論。資料處理方面提供 kedro-tf-image、kedro-tf-text、kedro-tf-utils 等 Kedro 插件，可分別載入與預處理影像、文字（包括 BERT）與通用表格資料；可選擇使用 kedro-dicom 處理 DICOM 影像、kedro-graph 建構 DGL 圖資料，以及 fhiry 扁平化 FHIR 資源。特徵融合採用早期融合（將不同模態特徵在輸入層連接）或晚期融合（分別訓練單模態模型後在決策層合併），並支援自訂融合方式。實驗追蹤與管線視覺化透過 kedro-viz 實現，部署則可利用 Kubeflow Pipelines 或 Vertex AI 進行訓練作業與模型服務，並提供 serving.py 與 serving.sh 範例來啟動 TensorFlow Serving Docker 容器。

## 架構
架構遵循 Kedro 約定：資料來源經 conf/base/catalog.yml 定義，原始資料放於 data/01_raw/，透過對應的節點（node）讀取並進行清理、標準化與特徵抽取（影像節點使用 kedro-tf-image，文字節點使用 kedro-tf-text，表格節點使用 kedro-tf-utils）。特徵抽取後進入融合節點，依參數 conf/base/parameters/train.yml 中的 fusion_type 選擇早期或晚期融合，產生融合特徵向量送入 TensorFlow 模型進行訓練，訓練管線位於 src/kedro_tf_multimodal/pipelines/train/pipeline.py。訓練完成後，模型會被導出並可透過 serving.py 建立 TensorFlow Serving REST API，或使用 serving.sh 啟動 Docker 容器；若啟用 Vertex AI 或 Kubeflow，則可將同一管線提交至雲端作業。資料流程大致為：原始多模態資料 → 目錄登錄 → 預處理節點 → 特徵抽取節點 → 融合節點 → 模型訓練節點 → 模型導出 → 服務節點。由於 README 未提供完整的圖節點或圖資料處理細節，架構描述僅基於可見的目錄與檔案說明。

## README 摘錄（節選）
```text
# Kedro TF Multimodal :hammer: [Template]
(https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/multimodal.drawio.svg)
This is a *template* for **multi-modal machine learning in healthcare** using the Kedro (https://kedro.org/) framework. You can combine reports, tabular data and images using various fusion methods (Early & Late fusion. Few other fusion methods and graph data are WIP). This project works with Kubeflow (https://www.kubeflow.org) and Vertex AI (https://cloud.google.com/vertex-ai).
## Usage
* If you are not familiar with the Kedro (https://kedro.org/) platform, please read the overview (#overview) :point_down:
* This is a template repository. Generate a new repository with the same directory structure by clicking the **Use this template** button :point_up: and use it as a Kedro project. (https://kedro.readthedocs.io/en/stable/get_started/new_project.html)
* Install dependenties
[code block omitted]
* Refer default pipeline (src/kedro_tf_multimodal/pipelines/train/pipeline.py) for usage examples.
* Refer sample data (/data/01_raw/) for data format. Prefix model datasets with appropriate model type from image_ , text_ , tabular_ , and bert_. (text_ is for CNN text models)
* Refer catalogue (conf/base/catalog.yml) for inputs and outputs
* See parameters (conf/base/parameters/train.yml) that can be tweaked.
The required pipelines are in requirements.txt (src/requirements.txt). More details on the components are in their respective repositories :point_down: (PR welcome. Read CONTRIBUTING.md in the repositories)
* kedro-tf-image (https://github.com/dermatologist/kedro-tf-image)
* kedro-tf-text (https://github.com/dermatologist/kedro-tf-text)
* kedro-tf-utils (https://github.com/dermatologist/kedro-tf-utils)
* kedro-dicom (https://github.com/dermatologist/kedro-dicom) (*optional*) for processing DICOM images
* kedro-graph (https://github.com/dermatologist/kedro-graph) (*optional*) for creating DGL (https://www.dgl.ai/) graph from multimodal data.
* fhiry (https://github.com/dermatologist/fhiry) (*optional*) for flattening FHIR resources (https://www.hl7.org/fhir/overview.html).
## Features
* Use any number/combination of data types.
* Export trained fusion model for TF serving with an additional signatureDef for receiving image as b64 string. Use SERVING: path/to/save/model in parameters (conf/base/parameters/train.yml). Also see serving.py (serving.py) (example serving REST client) and serving.sh (serving.sh) (start TF serving docker container with the model).
* Experimental support for **BERT** models with some caveats. (#troubleshoot)
## You can visualize pipelines using kedro-viz (https://github.com/kedro-org/kedro-viz). See the default pipeline below.
* Please note that you can build any multi-modal architecture!
(https://github.com/dermatologist/kedro-multimodal/blob/develop/notes/kedro-viz.png)
## Give us a star ⭐️
If you find this project useful, give us a star. It helps others discover the project.
## Troubleshoot
* Downloaded BERT models will not copy vocab.txt in assets folder to the newly created fusion model. This has to be manually copied.
* The class_num in TfModelWeights must be equal to to NCLASSES during training. Otherwise it throws an error: Tensorflow estimator ValueError: logits and labels must have the same shape ((?, 1) vs (?,))
* *import tensorflow_text as text* is required in pipeline_registry to avoid this error: Op type not registered 'CaseFoldUTF8' in binary running on xxxx
* Inconsistent NCLASSES leads to **ValueError: `logits` and `labels` must have the same shape, received ((None, 3) vs (None, 1)).**
## Contributors
* Bell Eapen (https://nuchange.ca) | (https://twitter.com/beapen)
## Overview
This is your new Kedro project, which was generated using `Kedro 0.18.4`.
Take a look at the Kedro documentation (https://kedro.readthedocs.io) to get started.
## Rules and guidelines
In order to get the best out of the template:
* Don't remove any lines from the `.gitignore` file we
```
