# 論文 01：Wireless, optoelectronic, multimodal skin sensor for simultaneous monitoring of mechanical stress and vascular responses.

- 日期：2026-10-19
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
長期機械載荷導致血管缺血，進而引發嚴重壓力傷害。現有診斷工具受限於剛性結構、單一參數檢測與主觀視覺評估，無法同步監測多軸力學與紅斑生理指標。本研究旨在開發無線、免電池的光電多模態感測平台，整合姿態相關的力學載荷與局部紅斑監測，解決傳統剛性感測器無法貼合皮膚、單一模態無法解耦三軸力與血氧變化的缺口，為壓力傷害風險的數據驅動預防提供技術基礎。

## 方法
本研究針對長期機械載荷導致的血管缺血與壓力傷害，提出一種無線、無電池的光電子多模態感測平台，同步監測皮膚介面的三軸力（Fx、Fy、Fz）與紅斑程度。問題設定為：輸入為感測器內部光學腔體的幾何光調變訊號與雙波長反射光強度，輸出為解耦後的法向壓力、雙軸剪力以及血紅素吸收變化指標。整體架構包含柔性皮膚貼合封裝、隔離光學腔、雙波長 LED/光電偵測器、近場通訊（NFC）供電與資料傳輸模組。核心演算法為深度神經網路回歸模型，接收多通道光強度序列，經由全連結層與非線性激活函數解耦三軸力；紅斑量化則利用雙波長反射率比值，依據血紅素吸收光譜差異計算紅斑指數。資料處理上，原始光訊號先經去噪、歸一化，再送入網路訓練；訓練目標為最小化三軸力預測的均方誤差與紅斑指數的平均絕對誤差，採用 Adam 最佳化器。推論流程：NFC 啟動感測器 → 即時讀取多通道光強度 → 神經網路前向傳播輸出三軸力 → 雙波長比值計算紅斑 → 無線回傳至手機/雲端。關鍵設計理由：幾何光調變提供高靈敏度力學轉換；不透明彈性體封裝消除環境光干擾；NFC 實現無電池、多點佈署；深度學習解耦多軸力，提升臨床姿態依賴載荷的精準度。

## 結果
本研究呈現一無線、免電池、光電多模態皮膚感測平台，能同步量測三軸力（Fx、Fy、Fz）與紅斑指數。利用隔離光腔內的幾何光調變解耦常壓與雙軸剪力，再以深度神經網路回歸模型分離三向力；雙波長反射機制捕捉血紅素吸收變化以量化紅斑。不透明彈性體封裝使光學讀取在環境光與膚況變化下保持穩定，近場通訊實現多感測器無線網路。床邊模擬臨床測試顯示系統可動態繪製姿勢依賴的生物力學負荷與局部血管反應，為壓力傷害風險的數據驅動監測奠基。摘錄未提供可驗證數字。

## 限制與展望
目前僅在模擬床榻場景進行短期人體驗證，缺乏長期穩定性、不同體位與患者群體的系統性評估；未提供與臨床金標準（如壓力映射床墊、組織氧合監測）的定量比較；封裝材料生物相容性、NFC 通訊距離與多節點干擾在真實病房環境中的表現仍待驗證；深度學習模型的泛化能力與訓練資料多樣性未詳細說明。後續研究需擴大樣本、引入長期監測與標準化基線比較。
