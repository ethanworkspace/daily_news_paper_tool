# 論文 02：Wireless, optoelectronic, multimodal skin sensor for simultaneous monitoring of mechanical stress and vascular responses.

- 日期：2026-10-18
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
長期機械負載導致血管缺血，進而引發嚴重壓力傷害。現有診斷工具受限於剛性結構、單一參數檢測與主觀視覺評估，難以同步監測多軸力學與紅斑生理指標。本研究旨在開發無線、免電池的光電子多模態感測平台，整合姿態相關的力學負載與局部紅斑監測，為壓力傷害風險的數據驅動預防提供技術基礎。

## 方法
本平台採用柔性、貼膚的封裝結構，內部建立隔離光學腔，利用幾何光調變機制將正向壓力與雙軸剪力轉換為光強度變化。為解耦三軸力（Fx、Fy、Fz），研究者訓練一個深度神經網路回歸模型，輸入為多通道光訊號，輸出為三向力分量。同步地，雙波長光學反射機制在兩個特定波長下量測血紅素吸收差異，以量化皮膚紅斑程度。不透明彈性體封裝層屏蔽環境光與皮膚狀態變化，確保光學讀取穩定。系統層面透過近場通訊（NFC）實現無電池、無線供電與多感測器網路的多工讀取。推論流程為：NFC 接收能量與指令 → 光學腔採集多波長反射訊號 → 類比前端放大與類比數位轉換 → 神經網路解碼三軸力 → 雙波長比值計算紅斑指數 → 無線回傳至讀取器。關鍵差異在於單一柔性裝置同時實現力學解耦與血氧光學量測，並以 NFC 實現全無線多點部署。

## 結果
於模擬臨床床邊場景的穿戴測試中，平台能即時繪製姿態依賴的生物力學負載分佈與局部血管反應，證明其可同步捕捉三軸力變化與紅斑動態。摘錄未提供可驗證數字，僅呈現定性結論：系統在不同體位下穩定輸出力學與光學讀值，支持後續壓力傷害風險的數據驅動研究。

## 限制與展望
目前驗證僅限於模擬床邊環境，缺乏真實病患長期臨床數據；神經網路架構、訓練資料集規模與泛化能力未揭露；雙波長紅斑量測未與金標準（如分光光度法）比對；NFC 通訊距離與多點干擾在大面積部署下的穩定性未評估；封裝材料長期生物相容性與機械疲勞亦待驗證。後續研究需擴大臨床樣本、公開模型細節、進行長期穩定性與干擾測試。
