# 論文 03：Wireless, optoelectronic, multimodal skin sensor for simultaneous monitoring of mechanical stress and vascular responses.

- 日期：2026-10-13
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
長期機械載荷導致血管缺血，進而引發嚴重壓力傷害。有效預防不可逆組織損傷需同步監測多軸機械力與生理性紅斑，但傳統診斷工具受限於剛性結構、單一參數檢測與主觀視覺評估。本研究旨在開發一種無線、免電池的光電多模態感測平台，整合姿態相關的機械載荷與局部紅斑追蹤，為壓力傷害風險的數據驅動監測提供技術基礎。

## 方法
本平台採用柔性、貼膚裝置，核心包含三大模組：(1) 幾何光調變機制，於隔離光學腔內利用光路變化量測正向壓力與雙軸剪應力；(2) 深度神經網路回歸模型，輸入光學腔的多通道光強訊號，輸出皮膚介面的三軸力 Fx、Fy、Fz，實現同步解耦；(3) 雙波長光學反射機制，透過兩組波長捕捉血紅素吸收細微變化，量化紅斑程度。裝置內部光學元件由不透明彈性體封裝，抑制環境光與膚況干擾。系統層面透過近場通訊（NFC）實現無線供電與多感測器網路多工操作，支援即時數據傳輸。推論流程為：感測器採集光強 → 預處理（去噪、歸一化） → DNN 回歸解碼三軸力 → 雙波長反射比計算紅斑指數 → NFC 封包回傳。與既有方法差異在於單一柔性平台同步實現三軸力解耦與紅斑光學量化，且免電池、無線操作。摘錄未提供 DNN 架構細節、損失函數、訓練資料集、最佳化策略等具體訓練設定。

## 結果
本研究提出無線、無電池、光電多模態皮膚感測器，整合幾何光調變與雙波長反射機制，並以深度神經網路解耦三軸力（Fx、Fy、Fz）與紅斑指數。實驗顯示：感測器能於模擬臨床床榻環境即時繪製姿態相關之生物力學載荷與局部血管反應；不透明彈性封裝有效屏蔽環境光干擾，確保光學讀數穩定；近場通訊實現多感測器無線網路運作。與傳統剛性、單參數、主觀視覺評估工具相比，本平台具備多軸力與紅斑同步監測優勢。摘錄未提供可驗證數字。文中未提供消融實驗或定量誤差分析數據。系統展示多感測器同步讀取與無線供電可行性。整體結果支持未來以數據驅動方式評估壓力傷害風險。

## 限制與展望
目前僅在模擬床榻場景驗證，缺乏大規模臨床病患數據與長期穩定性評估；DNN 模型架構、訓練樣本數、泛化能力未揭露，難以判斷對不同體位、膚色、溫濕度的魯棒性；NFC 通訊距離與多感測器同步延遲未量化；封裝材料長期生物相容性與機械疲勞未測試。後續研究需擴大臨床隊列、公開模型細節、評估功耗與封裝耐久性，並探討即時預警演算法整合。
