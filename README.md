# TutorAssist Bot 家教助理機器人
**TutorAssist Bot 不依賴按鍵或關鍵字來理解語言，使用者可以透過日常對話語句來與 Bot 溝通。** TutorAssist Bot 透過日常對話語句，辨識特定意圖及抽取資訊，並反覆予以回應確認，能隨時代為處理家教課程安排上的異動並將消息轉達給家教老師。

---
### TutorAssist Bot 的主要業務範圍
---
**TutorAssist Bot 並不是家教老師的分身，為保障師生雙方的個人隱私，未被授予課程及學生的相關資訊**，在這樣的前提之下，Bot 將不會回答上課時間地點及學生的個人資訊，僅負責處理學生課程異動事宜。

* **課程請假事宜**
* **課程時間調整**
* **改採線上授課**
* **恢復實體授課**
* **回應善意祝福**



---
### 檔案總攬
---
```
|
|
+---Discord
|   |   Discord_Jonathan_Boty.py ----------------- # Discord 主程式：處理 Bot 在 Discord 上的運作
|   |   Tutor_Assist_Bot.py----------------------- # Loki NLU 主程式：處理語言
|   |   
|   \---intent------------------------------------ # intent：utterance及語句意圖處理抽取                   
|       |   Loki_agree_adv.py
|       |   Loki_class_arrangement.py
|       |   Loki_day_off.py
|       |   Loki_disagree_adv.py
|       |   Loki_infrom_time.py
|       |   Loki_online_course.py
|       |   Loki_physical_course.py
|       |   Loki_warm_blessing.py
|       |   Updater.py
|       |   USER_DEFINED.json
|       |   
|               
\---ref------------------------------------------- # ref：可供 Loki 讀取的 ref
        |   agree_adv.ref
        |   class_arrangement.ref
        |   day_off.ref
        |   disagree_adv.ref
        |   infrom_time.ref
        |   online_course.ref
        |   physical_course.ref
        |   warm_blessing.ref
```
---

### 環境設定

---

* **Python 3+**
* **ArticutAPI：** 
  ```pip3 install ArticutAPI```
* [**註冊成為 Droidtown 會員**](https://api.droidtown.co/login/)


---
### 啟用 Loki 服務

---

1. 登入 **[Droidtown](https://api.droidtown.co/login/)** 前往**```服務資訊```**
2. 選擇**```Loki```**並**```開始使用```**
3. 輸入專案名稱並**```建立專案```**
4. 前往**```專案```**並**```選擇檔案```**
5. 選擇**```ref```**中的所有.py檔案
6. 開啟並**```讀取意圖```**
7. 點選左上房子圖示回到[**```Loki控制台```**](https://api.droidtown.co/loki/)
8. **```複製專案金鑰```**並填入 **```accout.info```** 中 **```loki-key```**欄位

---

### 建立 Discord Bot

1. 

---

### 聯絡資訊

---

**Jonathan Chen:** chenjonathan901210@gmail.com
若您有任何疑問，歡迎來信討論，感謝您。
