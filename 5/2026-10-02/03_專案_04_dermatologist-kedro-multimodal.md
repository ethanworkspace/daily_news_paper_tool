# GitHub 專案 04：dermatologist/kedro-multimodal

- 日期：2026-10-02
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
此專案提供一個基於 Kedro 框架的醫療多模態機器學習範本，使資料科學家與醫學研究者能够將病歷報告、結構化表格資料與醫療影像透過早期融合、晚期融合等方法結合，解決異質醫療數據整合與模型訓練的挑戰，並可直接部署至 Kubeflow 或 Vertex AI 進行訓練與服務。

## 技術
該範本使用 Python 3 與 Kedro 0.18.4 構建資料工程管線，透過 kedro-tf-image、kedro-tf-text、kedro-tf-utils 處理影像、文字與表格資料，支援早期融合與晚期融合（以及圖形資料 WIP），可選擇使用 kedro-dicom 處理 DICOM、kedro-graph 建立 DGL 圖與 fhiry 扁平化 FHIR 資源，模型訓練基於 TensorFlow/Keras，參數與資料目錄分別定義在 conf/base/parameters 與 conf/base/catalog，支援 JupyterLab/Notebook 互動開發與 kedro-viz 視覺化管線，最終可匯出含有 base64 影像簽名的 TensorFlow Serving 模型，並可部署至 Kubeflow 或 Vertex AI。

## 架構
專案遵循 Kedro 典型目錄結構：原始多模態資料放置於 data/01_raw，透過 conf/base/catalog.yml 定義為 image_*、text_*、tabular_* 或 bert_* 前綴的資料集；conf/base/parameters/train.yml 提供可調參數如 NCLASSES、融合方式等；src/kedro_tf_multimodal/pipelines 中的 train pipeline 依序執行各模態前處理節點（由 kedro-tf-image、kedro-tf-text、kedro-tf-utils 提供）與特徵擷取節點，接著進行早期或晚期融合節點產出融合特徵，最後送入 TensorFlow/Keras 模型訓練節點生成 SavedModel；訓練完成後可透過 serving.py 與 serving.sh 將模型匯出為 TensorFlow Serving 格式並啟動服務；整個流程可由 kedro run 或 kedro-viz 視覺化管線觀察。若需圖形或 FHIR 處理，則可選擇加入 kedro-graph 或 fhiry 節點。

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
