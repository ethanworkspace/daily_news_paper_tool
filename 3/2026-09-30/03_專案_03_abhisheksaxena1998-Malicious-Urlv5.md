# GitHub 專案 03：abhisheksaxena1998/Malicious-Urlv5

- 日期：2026-09-30
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
此專案提供多層次、多階層的機器學習惡意網址偵測方案，包含基於 Django REST Framework 的網頁應用、Chrome 擴充套件與 Android App，透過即時 API 呼叫判斷輸入網址是否為釣魚或惡意站點，目標使用者為一般上網者、資安人員與開發者，解決線上交易與瀏覽時遭受網路詐騙的問題。

## 技術
主要使用 Python 3、Django 與 Django REST Framework 建置後端 API，資料庫採用 SQLite3，機器學習模型以 scikit-learn 或深度學習框架（依專案 Topics 中的 deep-learning、machine-learning）訓練，前端以 HTML5、JavaScript 實現，Chrome 擴充套件透過 AJAX 呼叫 REST API，Android 端亦以同樣方式取得偵測結果，部署曾於 Heroku 與 IBM Cloud 示範。

## 架構
系統架構分為四層：(1) 使用者介面層，包含 Django 渲染的網頁、Chrome 擴充套件與 Android App；(2) API 服務層，由 Django REST Framework 提供的 /predict/ 端點接收 URL 參數；(3) 模型推論層，後端載入預訓練的惡意網址分類模型，提取 URL 特徵（如字元頻率、域名特徵等）進行二元分類；(4) 資料儲存層，使用 SQLite3 記錄查詢紀錄與模型元資料。使用者輸入網址後，前端經由非同步請求送至 API，API 呼叫模型得到惡意/合法標籤並回傳 JSON，前端依結果顯示警示或安全提示。若 README 未明確說明模型特徵與訓練流程，則此部分為基於專案 Topics 的合理推斷。

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
