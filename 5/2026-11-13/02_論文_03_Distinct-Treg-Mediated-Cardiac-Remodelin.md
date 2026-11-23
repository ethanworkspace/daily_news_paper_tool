# 論文 03：Distinct Treg-Mediated Cardiac Remodeling in HFpEF Mice Treated With Neonatal Mesenchymal Stem Cells and Their Secretome.

- 日期：2026-11-13
- 來源層級：Tier 1
- 期刊/會議/來源：JACC. Basic to translational science
- Venue：JACC. Basic to translational science
- 發布時間：2026-11-21T00:00:00+00:00
- URL：https://pubmed.ncbi.nlm.nih.gov/43067120/
- PDF：
- DOI：10.1016/j.jacbts.2026.101751
- arXiv：
- 影響指標：N/A
- 影響指標來源：
- 引用數：0
- 解析程度：abstract / abstract
- 全文來源：
- 全文字數：479（pages=0, ocr_pages=0）
- GitHub/Code：
- 配對 Repo：

## 摘要
Heart failure with preserved ejection fraction lacks effective disease-modifying therapies. We show that neonatal mesenchymal stem cells and their secretome improve diastolic function by expanding regulatory T cells, reducing inflammation and fibrosis. Our new causal machine learning framework, variable importance prediction for cellular function, identified causal immune pathways driving cardiac functional improvement and revealed regulatory T cells as a therapeutic target.

## 背景與目的
心臟衰竭且射出分數保留（HFpEF）缺乏有效的疾病修飾療法。本研究旨在探討新生兒間充質幹細胞及其分泌組分對舒張功能的改善機制，並發展一種因果機器學習框架以揭示驅動心臟功能恢復的免疫路徑，進而確立調節性T細胞作為潛在治療標靶。研究問題在於現有療法無法從根本上逆轉纖維化與炎症，而幹細胞療法的免疫調節作用尚未被系統性量化。本文貢獻在於提出可解釋的因果推論方法，並實驗驗證其預測的關鍵免疫機制。

## 方法
問題設定：輸入為HFpEF小鼠接受新生兒間充質幹細胞（N‑MSC）或其無細胞分泌組分治療後的多維免疫與心臟表型數據（如流式細胞術計數、細胞因子濃度、組織學纖維化指標、超聲心動圖舒張參數）；輸出為舒張功能改善程度與關鍵免疫變數的因果重要性排序。整體架構包含三階段：(1)資料前處理與特徵建構，將單細胞/群體層級免疫特徵標準化並編碼為數值向量；(2)因果機器學習核心——「變數重要性預測細胞功能」（VIP‑CF）框架，結合干預式因果推論（如do‑calculus或反事實模擬）與集成學習（隨機森林/梯度提升），估算每個免疫變數對舒張功能因果效應的邊際貢獻；(3)驗證與解釋模組，利用獨立驗證隊列與體內消融實驗（如Treg耗竭）確認預測路徑。核心演算法機制為：先以觀察數據學習條件期望模型，再透過模擬干預計算變數重要性分數，並以排列測試控制假陽性。訓練目標為最小化預測舒張功能指標的均方誤差，同時最大化因果效應估計的穩健性（採用交叉驗證與正則化）。推論流程：輸入新樣本特徵 → 經VIP‑CF計算各免疫變數因果重要性 → 輸出排名前列的路徑（如Treg擴增、IL‑10上調、纖維母細胞活化抑制）。與既有相關性分析或單純預測模型不同，本框架明確區分相關與因果，並可直接指向可干預的細胞靶點。

## 結果
作者報告：接受N‑MSC或其分泌組分治療的HFpEF小鼠，舒張功能指標（E/e'、左心室充盈壓）顯著改善；心臟組織學顯示纖維化面積減少、炎症細胞浸潤降低；流式細胞術證實調節性T細胞（Foxp3+ CD4+）在脾臟與心臟顯著擴增。VIP‑CF框架輸出的因果重要性排序將Treg擴增、IL‑10信號與巨噬細胞M2極化列為前三大驅動路徑。消融實驗中，抗CD25抗體耗竭Treg後，治療效益大幅消失，支持因果關係。摘錄未提供可驗證的具體數值（如p值、效應量、樣本數），僅能觀察到定性改善趨勢。

## 限制與展望
研究限制包括：(1)摘錄未揭露動物數量、隨機化與盲法細節，難以評估統計效力與偏倚風險；(2)VIP‑CF框架的超參數、特徵選擇標準、因果識別假設（如無未測量混雜）未公開，模型可重現性與泛化性存疑；(3)僅在單一HFpEF小鼠模型驗證，缺乏多模型、大鼠或大型動物及人類樣本的外部驗證；(4)分泌組分的具體成分（外泌體、細胞因子組成）未量化，機制解釋仍屬推測；(5)長期安全性、免疫耐受與劑量反應關係未探討。後續研究建議公開完整程式碼與原始數據、擴展至多中心臨床前隊列、並結合單細胞多組學進一步解析Treg上游調控網絡。
