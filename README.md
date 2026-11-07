# 🎓 成大課堂專屬語音學習助教 (NCKU Course Voice Assistant)

本專案專為成大 11/07「總體經濟走勢、核心指標與主力操盤實戰」課程量身打造，完整涵蓋 9 個課堂錄音檔與講義知識庫。

---

## 🌐 雲端專屬公開網址（手機在家或出外隨點隨用）

👉 **[https://chiululu8-sudo.github.io/ncku-1107-course-assistant/](https://chiululu8-sudo.github.io/ncku-1107-course-assistant/)**

- **外出聽重點**：戴上耳機，點擊網頁上的 3 首 MP3，隨開隨聽！
- **對話討論**：內建「先說後考」互動機制，手機螢幕可按麥克風語音對答或點擊主題提問。
- **手機通話模式**：網頁上一鍵複製「隨身助教指令」，在手機 Gemini App 開啟藍牙通話討論。

---

## 🌟 兩大核心模式介紹

### 🎧 模式一：外出隨身聽（精華音訊 MP3）
出門、通勤或散步時，可戴上耳機隨時聆聽，音檔存放在 `audio_summary/` 目錄：
1. **`EP01_Main_Force_and_Stock_Selection.mp3`**（主力操盤邏輯與三高環境選股哲學）
2. **`EP02_Three_Indicators_and_Liquidity.mp3`**（看懂大盤轉折與 M1B 熱錢動能）
3. **`EP03_TSMC_Strategy_and_Exit_Rules.mp3`**（台積電 ADR 實戰與三大保命出場警訊）

> 💡 **使用小撇步**：您可以直接將這三個 MP3 傳到手機或 LINE 自己的 Keep，隨時隨地像聽 Podcast 一樣複習課堂精華！

---

### 💻 模式二：在家深度討論（網頁版「先說後考」語音助教）
回到家後，打開電腦與專屬助教進行雙向對話：
- **開啟方式**：雙擊根目錄下的 **`啟動成大語音助教.bat`**，系統會自動在瀏覽器開啟助教網頁（`http://localhost:8080`）。
- **「先說後考」互動模式**：
  1. **按住紅色麥克風**直接開口提問（例如：「*助教，老師下午講的 M1B 跟 M2 黃金交叉到底是什麼意思？*」）。
  2. **先說**：助教會用最生活化的白話比喻解說觀念。
  3. **後考**：講完後助教會出一道實戰考題（例如：「*那如果下個月 M1B 向上衝破 M2，大盤卻因政治消息急跌，你該做多還是做空？*」）。
  4. 您可以直接再開麥克風回答，助教會給您即時回饋並加深印象！
  5. 支援**隨時打斷**：助教講話時，隨時點擊「停止朗讀」或再次開口即可打斷。

---

## 📁 檔案與目錄結構

```text
E:\Gemin bak\ncku_course_assistant\
├── README.md                      # 專案說明手冊（本檔案）
├── 啟動成大語音助教.bat           # 雙擊一鍵啟動網頁助教與瀏覽器
├── data/
│   └── ncku_1107_notes.md         # 匯總整理之成大1107全課程核心知識庫
├── audio_summary/
│   ├── EP01_Main_Force_and_Stock_Selection.mp3 # 精華音訊 EP01
│   ├── EP02_Three_Indicators_and_Liquidity.mp3 # 精華音訊 EP02
│   ├── EP03_TSMC_Strategy_and_Exit_Rules.mp3   # 精華音訊 EP03
│   └── generate_audio_v2.py       # 音訊生成程式
└── app/
    ├── index.html                 # 語音互動介面（支援 Web Speech 雙向語音）
    └── server.py                  # 本機助教後端與對話邏輯服務
```
