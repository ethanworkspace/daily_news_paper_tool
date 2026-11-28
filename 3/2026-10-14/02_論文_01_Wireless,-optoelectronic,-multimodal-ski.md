# 論文 01：Wireless, optoelectronic, multimodal skin sensor for simultaneous monitoring of mechanical stress and vascular responses.

- 日期：2026-10-14
- 來源層級：Tier 1（頂級期刊）
- 期刊/會議/來源：Nature communications
- Venue：Nature communications
- 發布時間：2026-10-13T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43009486/
- PDF：https://pmc.ncbi.nlm.nih.gov/articles/PMC13752271/
- DOI：10.1038/s41467-026-77832-2
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：1649（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Prolonged mechanical loading and subsequent vascular ischemia drive the development of severe pressure injuries. Effective prevention of irreversible tissue damage requires monitoring both multiaxial mechanical forces and physiological erythema. However, conventional diagnostic tools remain limited by rigid architectures, single parameter detection, and subjective visual assessments. Here, a wireless, battery free optoelectronic multimodal sensor platform provides an integrated framework for tracking posture dependent mechanical loading and localized erythema. The soft, skin conformable device uses geometric light modulation within an isolated optical cavity to quantify normal pressure and biaxial shear stresses. To resolve complex mechanical environments, a deep neural network regression model decouples simultaneous tri-axial forces, Fx, Fy, and Fz, at the skin interface. Concurrently, a dual wavelength optical reflectance mechanism quantifies skin erythema by capturing subtle variations in hemoglobin absorption. Opaque elastomeric encapsulation shields the internal optics, supporting stable optical measurements under varying ambient illumination and skin conditions. System level integration via near field communication enables untethered operation across a multiplexed sensor network. On-body evaluations in a simulated clinical bed setting demonstrate the ability of the platform to dynamically map posture-dependent biomechanical loading and localized vascular responses, providing a technological basis for future studies on data-driven monitoring of the mechanical and vascular factors associated with pressure-injury risk.

## 背景與目的
長期機械載荷導致血管缺血，進而引發嚴重壓力傷害。現有診斷工具受限於剛性結構、單一參數檢測與主觀視覺評估，難以同步量測多軸力學與紅斑生理指標。本研究提出無線、免電池的光電多模態感測平台，整合姿態相關的力學載荷與局部紅斑監測，旨在為壓力傷害風險的數據驅動監測提供技術基礎。

## 方法
系統以柔性、貼膚的封裝為基礎，內部構建隔離光學腔體，利用幾何光調變機制將正向壓力與雙軸剪力轉換為光強度變化。輸入為皮膚界面的三軸力（Fx、Fy、Fz）與雙波長反射光譜，輸出為解耦後的三向力向量與紅斑指數。核心模組包含：(1) 光學腔體結構，透過微結構改變光路長度以編碼法向與切向應力；(2) 深度神經網路回歸模型，接收多通道光訊號並輸出三軸力，實現同時解耦；(3) 雙波長反射檢測，選擇血紅素吸收峰與參考波長，計算吸光度差異以量化紅斑程度；(4) 不透明彈性體封裝，阻隔環境光與皮膚光學干擾，保證光學測量穩定；(5) 近場通訊（NFC）介面，提供無線供電與多感測節點的時分多工讀取，實現無線、免電池的網路化操作。推論流程為：感測節點採集光訊號 → NFC 傳輸至手持讀取器 → 端側執行 DNN 推理與雙波長紅斑計算 → 即時輸出力學與血管參數圖譜。與傳統單一參數、有線或剛性感測器相比，關鍵差異在於光學幾何調變實現多軸力解耦、雙波長光學紅斑量化、以及全無線多節點整合。

## 結果
作者在模擬臨床床鋪場景進行人體測試，展示平台能動態繪製姿態依賴的生物力學載荷分佈與局部血管反應，驗證多軸力解耦與紅斑量化功能。然而摘錄未提供可驗證數字（如誤差率、相關係數、採樣率等），僅能觀察到定性結論：系統可同步捕捉正向壓力、剪力與紅斑變化，並具備無線多節點操作能力。

## 限制與展望
目前僅在模擬床鋪環境進行短期人體驗證，缺乏長期穩定性、不同體位與膚質的系統性評估；未報告量化指標（誤差、延遲、功耗），難以判斷臨床可用性；NFC 通訊距離與多節點擴展性尚未詳細說明；封裝材料生物相容性與滅菌流程未討論。後續研究需擴大樣本、引入臨床終點、優化演算法泛化能力並進行長期穩定性測試。
