# GitHub 專案 04：abhisheksaxena1998/Malicious-Urlv5

- 日期：2026-10-12
- URL：https://github.com/abhisheksaxena1998/Malicious-Urlv5
- 描述：A multi-layered and multi-tiered Machine Learning security solution, it supports always on detection system, Django REST framework used, equipped with a web-browser extension that uses a REST API call.
- Stars：46  |  Forks：20  |  Language：Python
- License：
- Topics：api, chrome-extension, cybersecurity, data-science, database, deep-learning, django, django-rest-framework, hacktoberfest, heroku, html5, javascript, json, machine-learning, phishing, phishing-attacks, phishing-detection, phishing-websites, python, sqlite3
- 更新時間：2026-04-08T16:47:29+00:00
- 論文層級：未對應論文
- 配對論文：
- 品質分數：7/10 [implementation_signals, stale_backfill]

## 在做什麼
此專案提供多層次、多階段的機器學習惡意網址偵測系統，目標使用者為一般網民、企業安全人員與開發者，旨在即時辨識釣魚、惡意下載及詐騙網站，透過 Django REST 框架提供 API，搭配瀏覽器擴充套件與 Android App，讓使用者在瀏覽或點擊網址時獲得即時風險評估，降低網路詐騙與資料外洩風險。

## 技術
專案主要使用 Python 3，後端採用 Django 與 Django REST Framework 建構 RESTful API，資料儲存採用 SQLite3；機器學習模型採用深度學習與傳統特徵工程（URL 字元頻率、域名特徵、HTML/JavaScript 特徵等），模型訓練與推論分別在離線環境完成，推論結果透過 API 回傳 JSON；前端提供 Chrome 擴充套件（HTML5、JavaScript）透過 AJAX 呼叫後端 API；同時提供 Android 應用程式（Java/Kotlin）使用同一 API 進行偵測。

## 架構
系統架構分為三層：(1) 資料與模型層，負責收集 URL 特徵、訓練與更新 ML 模型，模型儲存為檔案或資料表；(2) API 服務層，由 Django REST Framework 暴露 /predict/ 端點，接受 URL 輸入，呼叫模型進行推論並回傳判斷結果與信心分數；(3) 用戶端層，包括瀏覽器擴充套件與 Android App，兩者在使用者輸入或偵測到網址時，透過 HTTPS 請求呼叫 API，顯示結果（惡意/合法）並可選擇封鎖或警告。資料流程為：使用者輸入 URL → 用戶端送請求至 API → API 讀取模型特徵 → 模型推論 → 回傳 JSON → 用戶端顯示。若 README 未詳細說明模型更新機制或擴充套件實作細節，則此部分為基於可見檔案結構與描述的合理推斷。

## README 摘錄（節選）
```text
## Malicious URL Detector
** Malicious URL Detector**
** CONCEPT VIDEO 👇**
(https://www.youtube.com/watch?v=-6fd996HWrQ)
#### Updated Application at: https://mudvfinalradar.eu-gb.cf.appdomain.cloud/
This application is live at https://malicious-url-detectorv5.herokuapp.com/
Android application repository URL : https://github.com/abhisheksaxena1998/Android-Application-Malicious-URL-Detector
APK URL : https://github.com/abhisheksaxena1998/Android-Application-Malicious-URL-Detector/blob/master/Malicious%20URL%20Detector.apk
Life is dependent mainly on internet in todays life for moving business online, or making online transactions. Resulting in cyber-thefts and cyber-frauds increasing exponentially day by day, leading to compromised security and infiltration of hackers or third parties while transacting online.
## Test Data
Test URL | Result (Target)
------------ | -------------
https://home-paypal-jp.moonkahonda.com/panel_JP/-/jp/xppl/ | Malicious
https://galsterberg.panomax.com/ | Legitimate
https://oberstdorf.panomax.com/schrattenwang | Legitimate
https://addons.mozilla.org/de/firefox/addon/mynthos-tv/?src=search | Legitimate
http://ord-amazsn.com | Malicious
http://ww17.login-appleid.apple.com.alert-wode.com/ | Malicious
http://support.facebook.com-uuynqiyacp.tekhencorp.com/ | Malicious
https://galsterberg.panomax.com/ | Legitimate
https://www.google.com/ | Legitimate
https://wallpapersite.com/abstract/ | Legitimate
https://www.freepik.com/free-vector | Legitimate
## Installation Guide.
1. Extract Malicious-Urlv5 zip file.
2. Inside Malicious-Urlv5 there is a file requirements.txt
3. Open command prompt in Malicious-Urlv5 folder
4. Type following command in cmd
5. Dependencies will start installing.
6. To run the code, write following command in terminal.
python manage.py runserver
7. Type http://127.0.0.1:8000/ in URL bar of browser and press Enter. Machine Learning powered Web Application will start.
8. Type a valid URL for example to fetch analysis:
https://www.mi.com
This is an example of Legitimate URL.
9. Another example of Legitimate URL
https://technoutsav.techgig.com/
10. Another Legitimate URL
https://www2.deloitte.com/in/en.html
11. Example of Malicious Website
http://www.dhilloncraneservice.com/.well-known/bankofamerica.com/
12. Another Malicious URL
https://home-paypal-jp.moonkahonda.com/panel_JP/-/jp/xppl/
```
