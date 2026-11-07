import json
import os
import re
import asyncio
import hashlib
from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import edge_tts

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
NOTES_PATH = os.path.join(PROJECT_DIR, "data", "ncku_1107_notes.md")
AUDIO_CACHE_DIR = os.path.join(PROJECT_DIR, "audio_summary", "cache")

os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

# 讀取知識庫
with open(NOTES_PATH, "r", encoding="utf-8") as f:
    KNOWLEDGE_BASE = f.read()

# 支援的微軟高品質真人神經網路語音
VOICES = {
    "yunjhe": "zh-TW-YunJheNeural",     # 台灣專業男助教（極推，沉穩自然）
    "hsiaochen": "zh-TW-HsiaoChenNeural", # 台灣親切女助教（溫暖親和）
    "hsiaoyu": "zh-TW-HsiaoYuNeural",     # 台灣溫柔女助教（知性婉轉）
    "yunyang": "zh-CN-YunyangNeural"      # 專業財經播報員（權威清晰）
}

async def generate_speech_file(text: str, voice_key: str = "yunjhe", rate: str = "+0%"):
    voice = VOICES.get(voice_key, "zh-TW-YunJheNeural")
    # 用 hash 命名快取，避免重複生成耗時
    text_hash = hashlib.md5((text + voice + rate).encode("utf-8")).hexdigest()
    filename = f"tts_{text_hash}.mp3"
    filepath = os.path.join(AUDIO_CACHE_DIR, filename)
    
    if not os.path.exists(filepath):
        # 移除 markdown 格式符號以優化發音
        clean_text = re.sub(r'[*_#`~]', '', text)
        clean_text = clean_text.replace("M1B", "M 1 B").replace("M2", "M 2").replace("CPI", "C P I").replace("GDP", "G D P").replace("ADR", "A D R").replace("FED", "聯準會")
        communicate = edge_tts.Communicate(clean_text, voice, rate=rate)
        await communicate.save(filepath)
    
    return f"/audio_summary/cache/{filename}"

def generate_assistant_response(user_msg: str):
    msg = user_msg.lower()
    
    if any(k in msg for k in ["m1b", "m2", "貨幣", "黃金交叉", "死亡交叉"]):
        explanation = (
            "老師下午特別強調資金面，因為『有量才有價』！\n"
            "你可以把 M1B 想成是我們一般散戶隨時可以拿去買股票的『熱錢口袋』；而 M2 則是包含定存和外幣的『國家總資金池』。\n\n"
            "所謂的『黃金交叉』，就是大家發現定存利息太低、股市好賺，紛紛解約定存把錢移到活存衝進股市（M1B 年增率大於 M2 年增率）。這時市場活水氾濫，大盤就算遇到利空也容易『該回不回』直線上漲！\n"
            "反過來，如果資金都收攤跑回銀行存定存（M2 大於 M1B 死亡交叉），股市沒有熱錢推動，動能就會受阻陷入盤整。"
        )
        quiz = "那我考考你：如果下個月公布的央行數據顯示 M1B 向上突破 M2 形成黃金交叉，但是大盤卻因為美國政治消息連續急跌兩天，這時候依照主力思維，我們應該跟著做空，還是分批找買點？為什麼？"
        return explanation, quiz

    elif any(k in msg for k in ["台積電", "adr", "外資", "借券", "代工"]):
        explanation = (
            "課堂上老師特別剖析了台積電的籌碼大戰！\n"
            "外資常常趁美股大跌時，把台積電當成『提款機』大舉借券賣出、打壓股價；但是國內的投信和本土主力資金，知道台積電具備不可替代的 AI 護城河，會在低檔持續承接。\n\n"
            "主力操盤的心法是：當外資發現股價『怎麼打都打不下去』，而且每個月公布的『月營收』持續爆發成長時，外資放空的成本太高，最終被迫回頭『借券回補並轉為大買超』，直接帶動股價飆破新高！所以散戶千萬不要一次性買滿（All-in），要分成 3 到 5 次分批建倉。"
        )
        quiz = "換我考考你：當外資在借券賣出台積電，但你發現台積電的『融資餘額已經洗盤近乎歸零』，而且守在關鍵的季線之上，這時通常代表什麼訊號？"
        return explanation, quiz

    elif any(k in msg for k in ["指標", "pmi", "領先指標", "轉折", "採購經理人"]):
        explanation = (
            "判斷大盤轉折，老師教了絕配雙指標：景氣領先指標 ＋ PMI！\n"
            "領先指標口訣是：『領先預判未來看轉折，連續 3 個月同向即成勢』。\n"
            "而 PMI（製造業採購經理人指數）以 50 為榮枯線，高於 50 擴張、低於 50 緊縮。因為工廠採購主管最先知道有沒有訂單，所以最靈敏！\n\n"
            "實戰精髓在於：當台灣 PMI 維持在 60 以上熱絡區間，且領先指標持續向上，代表『基本面極其健康』！如果這時候大盤指數突然急跌跌破均線，這絕對不是基本面惡化，而是主力在藉由政治變數洗盤，反而是最好的分批承接時機！"
        )
        quiz = "助教考考你：如果領先指標已經連續三個月往下掉，而且美國 ISM 製造業指數跌破多少數值時，老師提醒大家代表經濟進入嚴重衰退？"
        return explanation, quiz

    elif any(k in msg for k in ["停利", "出場", "均線", "三天", "警訊", "保命", "cpi", "gdp"]):
        explanation = (
            "老師常說：『指上富貴不如落袋為安』！懂得買是徒弟，懂得賣才是師父。課堂特別交代了三大保命與出場訊號：\n"
            "1. 技術面警訊：股價跌破月線或半年線，『連續三天無法站回』，代表趨勢轉弱，果斷停利落袋。\n"
            "2. 通膨爆表警訊：月度 CPI 突然飆破 4% 以上，代表通膨失控、聯準會將重啟暴力升息，主力會藉機打壓股市，必須果斷停利。\n"
            "3. 終極逃命點：美國 GDP 只要出現『單季負成長』，這代表硬著陸來臨，老師說此時要『跑得比飛的還快』，全面清倉！"
        )
        quiz = "那考考你：如果你的持股目前獲利 30%，但今天突然跌破半年線，明天小漲、後天又跌，連續三天都站不回半年線，這時候你應該心存僥倖繼續抱著等反彈，還是執行紀律？"
        return explanation, quiz

    elif any(k in msg for k in ["三高", "高股息", "選股", "營收", "月營收"]):
        explanation = (
            "面對現在『高利率、高通膨、高不確定性』的三高環境，選股千萬不要去碰沒有獲利支撐的本夢比投機股！\n"
            "老師傳授的選股兩大支柱：\n"
            "第一是看『月營收逐月增加』：因為 GDP 和企業財報都是每季才公布一次（落後指標），只有每月 10 號前公布的月營收，是散戶能抓到獲利爆發的最即時指標！\n"
            "第二是鎖定『6% 到 7% 以上高股息』：在高利率時代，高配息能帶來極佳的『利差保護』，就算大盤震盪洗盤，高殖利率也能提供穩定的現金流防禦！"
        )
        quiz = "助教考考你：為什麼老師一再強調『月營收』比每季公布的『企業財報獲利』對散戶更有實戰價值？關鍵原因是什麼？"
        return explanation, quiz

    elif any(k in msg for k in ["做多", "買點", "分批", "主力", "承接", "及時", "護城河", "季線", "42", "紀律", "停利", "賣"]):
        explanation = (
            "回答得太棒了！完全切中老師課堂的思維！\n"
            "你的觀念非常清晰：不被市場上的恐慌消息洗出場，懂得看籌碼沉澱（融資洗乾淨）與基本面保護，這就是標準的『主力操盤順向思維』！"
        )
        quiz = "你掌握得很好！你還想深入了解哪一個部分？例如：FED 美聯準會的三大關鍵指標（非農就業、CPI、失業率4.5%軟著陸），還是想聽聽各國國債的風險分析？"
        return explanation, quiz

    else:
        explanation = (
            f"收到你的提問！關於「{user_msg}」在今天的成大課堂中：\n"
            "老師的核心邏輯在於『個股漲跌受大盤限制，大盤受總體經濟牽引』。在操作時，我們必須同時搭配『領先指標看趨勢、M1B/M2看資金動能、均線與融資看籌碼洗盤』，並且嚴格執行『分批 3 到 5 次進場』與『三天不站回均線停利』。"
        )
        quiz = "那助教考考你：老師今天說的『科技產業的爸爸是誰』？為什麼我們看台股大盤，眼睛一定要盯著美國的總經數據？"
        return explanation, quiz

class AssistantServer(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parsed = urllib.parse.urlparse(path).path
        if parsed.startswith("/audio_summary/"):
            rel = parsed[len("/audio_summary/"):].lstrip("/")
            return os.path.join(PROJECT_DIR, "audio_summary", rel)
        elif parsed == "/" or parsed == "/index.html":
            return os.path.join(BASE_DIR, "index.html")
        else:
            return os.path.join(BASE_DIR, parsed.lstrip("/"))

    def do_POST(self):
        if self.path == "/api/chat":
            content_length = int(self.headers.get("Content-Length", 0))
            raw_data = self.rfile.read(content_length).decode("utf-8", errors="ignore")
            user_msg = ""
            voice_choice = "yunjhe"
            
            try:
                data = json.loads(raw_data)
                user_msg = data.get("message", "")
                voice_choice = data.get("voice", "yunjhe")
            except Exception:
                m = re.search(r'"message"\s*:\s*"([^"]+)"', raw_data)
                if m:
                    user_msg = m.group(1)
                else:
                    user_msg = raw_data
            
            explanation, quiz = generate_assistant_response(user_msg)
            
            # 使用微軟 Edge 高階神經網路真人語音生成 MP3
            full_speech_text = f"{explanation}。那助教換我考考你：{quiz}"
            audio_url = asyncio.run(generate_speech_file(full_speech_text, voice_choice))
            
            res_payload = {
                "explanation": explanation,
                "quiz": quiz,
                "audio_url": audio_url
            }
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(res_payload, ensure_ascii=False).encode("utf-8"))
        else:
            self.send_error(404, "Not Found")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

def run():
    print(f"成大 1107 課堂專屬語音助教正在啟動: http://localhost:{PORT}")
    httpd = HTTPServer(("127.0.0.1", PORT), AssistantServer)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
