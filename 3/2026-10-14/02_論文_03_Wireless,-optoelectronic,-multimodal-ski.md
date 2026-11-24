# 論文 03：Wireless, optoelectronic, multimodal skin sensor for simultaneous monitoring of mechanical stress and vascular responses.

- 日期：2026-10-14
- 來源層級：Tier 1
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
長期機械載荷導致血管缺血，進而引發嚴重壓力傷害。現有診斷工具受限於剛性結構、單一參數檢測與主觀視覺評估，難以同步監測多軸力學與紅斑生理指標。本研究提出無線、免電池的光電多模態感測平台，整合姿態相關的力學載荷與局部紅斑監測，旨在為壓力傷害風險的數據驅動監測提供技術基礎。

## 方法
問題設定：輸入為貼附於皮膚的柔性感測單元接收到的三軸力（Fx、Fy、Fz）與雙波長反射光信號；輸出為解耦後的正向壓力、雙軸剪力以及紅斑指數。系統架構：採用幾何光調變的隔離光學腔，將機械變形轉換為光強度變化；光學腔內嵌雙波長 LED 與光電偵測器，透過不透明彈性體封裝屏蔽環境光。核心模組：(1) 光學力學轉換層，利用腔體幾何變形實現正壓與雙軸剪力的光強調變；(2) 深度神經網路回歸模型，接收多通道光訊號並輸出三軸力向量，訓練目標為最小化預測力與地面真值的均方誤差（具體損失函數、網路深度、資料增強策略於摘錄未提及）；(3) 雙波長反射機制，依血紅素在兩波長吸收差異計算紅斑指數。資料前處理：原始光訊號經去噪、歸一化後輸入網路；推論流程為即時讀取多通道光強、經網路解耦力向量、並同步計算紅斑指數，經 NFC 以無電池方式傳輸至外部讀取器。關鍵差異：將力學與血氧光學整合於單一柔性晶片，並以幾何光調變與深度學習解耦三軸力，實現免電池、多點同步監測。

## 結果
作者在模擬臨床床榻環境進行人體測試，證實平台能動態繪製姿態相關的生物力學載荷分布與局部血管反應，展示多軸力解耦與紅斑量測的同步可行性。摘錄未提供可驗證數字（如誤差範圍、相關係數、感測器數量、採樣率等），僅能觀察到定性結論：系統在真實皮膚條件下仍能穩定運作，並具備無線多點同步能力。

## 限制與展望
限制包括：(1) 摘錄未揭露訓練資料集規模、網路架構細節、損失函數與優化超參數，難以評估模型泛化能力；(2) 實驗僅在模擬床榻單一姿態場景驗證，缺乏長時程、多體位、不同膚色與濕度條件的系統性評估；(3) 封裝材料長期生物相容性、光學腔老化對校準漂移的影響未討論；(4) NFC 供電距離與多點串擾在臨床大規模部署時的可靠性仍待驗證。後續研究可擴大受試者群體、引入長期監測協定、優化模型輕量化以利邊緣運算。
