# GitHub 專案 03：abhisheksaxena1998/Malicious-Urlv5

- 日期：2026-10-05
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
此專案提供惡偽 URL 偵測系統，結合網頁應用、Chrome 擴充套件與 Android App，使用 Django 後端與 Django REST Framework 暴露 REST API，讓使用者輸入任意網址即可即時取得惡意或合法的判斷目標。核心問題在於即時偵測釣魚與惡意網站，降低一般使用者、企業與安全分析師遭受網路詐騙的風險。

## 技術
後端以 Python 3、Django 與 Django REST Framework 建構，資料儲存使用 SQLite3；機器學習模型（深度學習或傳統 ML）訓練後封裝為可呼叫的函式，負責從 URL 特徵（字串、域名、路徑等）進行二元分類。前端採用 HTML5、JavaScript 與 Chrome 擴充套件，透過 AJAX 呼叫後端 API；Android 端亦透過同一 REST API 取得結果。部署方面曾在 Heroku 與 IBM Cloud 上提供線上 Demo。

## 架構
使用者經由網頁、瀏覽器擴充或 Android App 輸入 URL，請求透過 HTTP 送至 Django REST API endpoint；API 先檢查 SQLite 快取是否有先前結果，若無則將 URL 傳入特徵擷取模組產生向量，接著呼載事先訓練好的 ML 模型進行推論，得到惡意/合法標籤並寫回快取；最後以 JSON 格式回傳結果給前端顯示。整個流程為無狀態的請求/回應模式，模型與資料庫皆位於後端伺服器內。

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
