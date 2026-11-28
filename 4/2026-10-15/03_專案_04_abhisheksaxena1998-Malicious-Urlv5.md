# GitHub 專案 04：abhisheksaxena1998/Malicious-Urlv5

- 日期：2026-10-15
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
此專案提供一個多層次的惡偽 URL 偵測系統，透過機器學習模型判斷輸入網址是為合法站點或釣魚/惡意網站。目標使用者包括一般上網人士、企業員工及開發者，他們可透過網頁介面或 Chrome 擴充功能即時檢查連結，以降低遭受網路詐騙、惡意軟體下載或資料竊取的風險。核心在於解決日益增加的網路詐騙與惡意網站問題，提供即時、可擴充的偵測服務。

## 技術
專案主要使用 Python 開發，後端採用 Django 框架搭配 Django REST Framework 提供 RESTful API，資料儲存採 SQLite3。機器學習元件（未在 README 中詳細說明模型類型）負責從 URL 特徵中提取訊息並進行二元分類（惡意/合法）。前端以 HTML5、JavaScript 撰寫網頁介面，並開發了 Chrome 擴充功能，透過 AJAX 呼叫後端 API 取得偵測結果。部署方面曾在 Heroku 與 IBM Cloud（App Domain）上線示範。

## 架構
系統架構可分為三層：(1) 前端層 – 包含網頁 UI 與 Chrome 擴充功能，使用者在此輸入或偵測 URL；(2) API 層 – Django REST Framework 提供的端點（如 /api/detect/）接收前端請求，呼叫機器學習模型進行推論；(3) 模型與資料層 – 輸入的 URL 先經過特徵擷取（如域名長度、特殊字元、子域數等），再送入已訓練好的 ML 模型，模型輸出機率或標籤，結果透過 JSON 回傳給前端顯示。資料流為：使用者 → 前端擴充/網頁 → HTTP POST 至 Django API → 特徵處理 → ML 模型預測 → API 回傳結果 → 前端顯示。由於 README 未說明模型訓練流程或特徵工具細節，以上架構推斷主要基於所見的 Django、REST API、擴充功能與 ML 字樣。

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
