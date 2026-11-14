import os
import subprocess

DATA_DIR = r"E:\Gemin bak\ncku_course_assistant\data"
HTML_PATH = os.path.join(DATA_DIR, "course_full_handbook.html")
PDF_PATH = os.path.join(DATA_DIR, "成大投資實戰全課程精華講義與手寫筆記全書_1107_1114.pdf")

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>成大投資實戰全課程精華講義與手寫筆記全書</title>
    <style>
        @page {
            size: A4;
            margin: 18mm 16mm 18mm 16mm;
            @bottom-right {
                content: counter(page);
                font-size: 9pt;
                color: #64748b;
            }
        }
        * {
            box-sizing: border-box;
            font-family: 'Noto Sans TC', 'Microsoft JhengHei', sans-serif;
            line-height: 1.6;
        }
        body {
            color: #1e293b;
            background: white;
            margin: 0;
            padding: 0;
            font-size: 10.5pt;
        }
        .cover-page {
            page-break-after: always;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            border: 4px double #1e3a8a;
            padding: 40px;
            margin: 10px;
        }
        .cover-title {
            font-size: 26pt;
            font-weight: 800;
            color: #1e3a8a;
            margin-bottom: 12px;
            letter-spacing: 1.5px;
        }
        .cover-subtitle {
            font-size: 14pt;
            color: #2563eb;
            margin-bottom: 30px;
            font-weight: 600;
        }
        .cover-badge {
            background: #dbeafe;
            color: #1e40af;
            padding: 8px 18px;
            border-radius: 20px;
            font-size: 11pt;
            font-weight: 700;
            margin-bottom: 40px;
            display: inline-block;
        }
        .cover-meta {
            margin-top: 50px;
            font-size: 11pt;
            color: #475569;
            line-height: 1.8;
            border-top: 1px solid #cbd5e1;
            padding-top: 20px;
            width: 80%;
        }
        h1 {
            color: #1e3a8a;
            font-size: 18pt;
            border-bottom: 2.5px solid #2563eb;
            padding-bottom: 6px;
            margin-top: 24px;
            margin-bottom: 14px;
            page-break-after: avoid;
        }
        h2 {
            color: #0f172a;
            font-size: 14pt;
            border-left: 5px solid #3b82f6;
            padding-left: 10px;
            margin-top: 18px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        h3 {
            color: #1e40af;
            font-size: 12pt;
            margin-top: 14px;
            margin-bottom: 8px;
            page-break-after: avoid;
        }
        p, li {
            text-align: justify;
            margin-bottom: 8px;
        }
        ul, ol {
            padding-left: 22px;
            margin-bottom: 12px;
        }
        .card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 14px;
            margin-bottom: 14px;
            page-break-inside: avoid;
        }
        .highlight-box {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 12px 14px;
            margin: 12px 0;
            border-radius: 0 6px 6px 0;
            page-break-inside: avoid;
        }
        .formula-box {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 6px;
            padding: 10px 14px;
            font-family: 'Consolas', monospace;
            font-size: 10pt;
            font-weight: 700;
            color: #1e40af;
            margin: 10px 0;
            text-align: center;
            page-break-inside: avoid;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0;
            font-size: 9.5pt;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #cbd5e1;
            padding: 8px 10px;
            text-align: left;
        }
        th {
            background: #f1f5f9;
            color: #1e3a8a;
            font-weight: 700;
        }
        tr:nth-child(even) {
            background: #f8fafc;
        }
        .note-img-container {
            text-align: center;
            margin: 16px 0;
            page-break-inside: avoid;
        }
        .note-img {
            max-width: 85%;
            height: auto;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .note-caption {
            font-size: 9pt;
            color: #64748b;
            margin-top: 6px;
            font-weight: 600;
        }
        .page-break {
            page-break-after: always;
        }
    </style>
</head>
<body>

    <!-- 封面 -->
    <div class="cover-page">
        <div class="cover-badge">成大高階財經投資實戰班 官方全套講義</div>
        <div class="cover-title">總體經濟大局、財務指標選股<br>與主力操盤實戰全書</div>
        <div class="cover-subtitle">完整收錄 1107 宏觀總經篇 ＋ 1114 股票風險管理與 AI 選股篇<br>獨家整合：課堂現場 3 大手寫筆記與川湖 9% 實戰手算算式</div>
        <div class="cover-meta">
            <strong>授課核心</strong>：景氣領先指標與 PMI、M1B/M2 熱錢動能、台積電 ADR 籌碼對作<br>
            <strong>選股模型</strong>：ROE 負債防禦、近一年毛利率 > 40%、資本支出率 30%～90% 良性擴張<br>
            <strong>獨家手寫還原</strong>：川湖 9% 資本支出手算、速動比率 > 1.5、XQ 全球贏家步步教學、切三旬金字塔<br>
            <strong>整理日期</strong>：2026 年 11 月 14 日 ｜ <strong>適用對象</strong>：波段投資人、長期成長價值投資者
        </div>
    </div>

    <!-- 目錄與導讀 -->
    <h1>📖 全書架構導讀</h1>
    <p>本書根據成大課堂連續兩週（11/07 與 11/14）共 18 段全天上課錄音、完整講義投影片與現場 3 張手寫筆記精心編撰。全書分為四大部：</p>
    <ul>
        <li><strong>第一部：1107 總體經濟大局與美台科技連動本質</strong>（牽連機制、爸爸是美國、日本國債與渡邊太太套利交易、三大核心指標、台積電籌碼大戰、三大保命出場警訊）。</li>
        <li><strong>第二部：1114 股票投資風險管理與核心投資思維</strong>（2027 AI 資本支出峰值年、市場震盪加劇、跌破 20% 超級送分題、大資產配置與定期定額切三旬分散法）。</li>
        <li><strong>第三部：課堂三大手寫筆記深度解密與手算演練</strong>（手寫筆記全彩還原、川湖 9% 資本支出手算公式、速動比率 > 1.5、XQ 全球贏家操作四步驟、台積電本益比評價三階梯）。</li>
        <li><strong>第四部：三大趨勢產業、個股實戰對照與避坑全手冊</strong>（ESG 公司治理 G 賺錢效應、AI 吃電怪獸、生技醫療熟齡經濟、地雷股 5 大特徵與散戶常見三大虧損盲點、專有名詞白話對照表）。</li>
    </ul>

    <div class="page-break"></div>

    <!-- 第一部 -->
    <h1>第一部：1107 總體經濟大局與美台科技連動本質</h1>
    
    <h2>一、個股漲跌受大盤限制，大盤受總經走勢牽引</h2>
    <p>散戶常沉迷於技術線型去挑飆股，但事實上<strong>「個股漲跌受大盤指數限制，大盤指數的漲跌與總體經濟強弱走向呈高度連動」</strong>。當總經指標沒有惡化、景氣不拖後腿時，大盤的急跌多半是短暫的政治消息或主力洗盤；但如果總經基本面真正陷入衰退，任何績優個股都難以逆勢對抗大盤下殺。</p>
    
    <div class="highlight-box">
        <strong>💡 主力思維 vs 散戶盲點：</strong><br>
        主力要賺錢必須在市場製造「波動」。當股價漲到高檔無法繼續推升時，主力會「兩手準備」：一手布空單獲利，一手藉由政治利空打壓現貨洗盤。散戶盲目做空容易被主力反手強拉洗出場。正確心法是：順著主力思維在低檔分批做多，拉升到高檔滯漲時波段停利、落袋為安。
    </div>

    <h2>二、台灣科技產業的「爸爸是美國」與美聯準會牽動機制</h2>
    <p>台灣科技製造廠本質是「代工模式」，缺乏終端品牌，最核心大客戶全在美國（輝達、微軟、蘋果、Google）。老師生動比喻：「台灣科技產業的爸爸是美國，爸爸給單，兒子才有飯吃；爸爸過不下去，怎麼可能照顧台灣？」</p>
    
    <div class="formula-box">
        公司價值估值公式： V = EBIT / K （息稅前利潤 / 必要折現率）
    </div>
    <p>當美聯準會（FED）升息，無風險利率飆升，折現率 $K$ 拉高，科技股高估值大幅縮水；降息時熱錢推升估值。同時台灣科技出口採美元報價，台幣升值會產生匯損；美元借款利率暴增更會提高擴建資本支出的財務成本。</p>

    <h2>三、三大核心總經指標深度判讀</h2>
    <div class="card">
        <h3>1. 景氣領先指標 與 PMI 雙指標搭配</h3>
        <ul>
            <li><strong>領先指標 7 大要素</strong>：外銷訂單動向指數、實質半導體設備進口值、實質貨幣總計數 M1B、股價指數、受僱員工淨進入率、建築物開工樓地板面積、製造業營業氣候測驗點。<strong>口訣：「領先預判未來看轉折，連續 3 個月同向即成勢」</strong>。</li>
            <li><strong>PMI 與 ISM</strong>：50 為榮枯線，高於 50 擴張、低於 50 萎縮。美國 ISM 跌破 42.0 代表陷入嚴重衰退。</li>
            <li><strong>抓非基本面洗盤買點</strong>：台灣 PMI 高掛 60 以上熱絡區間，領先指標向上，大盤因政治消息急跌破均線，非基本面惡化，純屬主力洗盤，為分批撿便宜良機。</li>
        </ul>
    </div>

    <div class="card">
        <h3>2. M1B 與 M2 貨幣供給量（資金面命脈）</h3>
        <ul>
            <li><strong>M1B</strong>：M1A 加上活期儲蓄存款（散戶隨時可用於買股的「熱錢口袋」）。</li>
            <li><strong>M2</strong>：M1B 加上定存與外幣（「國家總資金大水庫」）。</li>
            <li><strong>黃金交叉（M1B 年增率 > M2 年增率）</strong>：定存解約流進股市，活水充沛大盤漲。</li>
            <li><strong>死亡交叉（M2 年增率 > M1B 年增率）</strong>：熱錢撤回定存，大盤缺乏推升動能。</li>
            <li><strong>真理</strong>：「有量才有價」，熱錢充沛時，股市「該回不回、直線攀高」。</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- 第二部 -->
    <h1>第二部：1114 股票投資風險管理與核心投資思維</h1>

    <h2>一、2026～2027 宏觀定調：資本投資經濟＋股市震盪加劇</h2>
    <p>世界經濟論壇（WEF）最新發布的全球風險報告：短期兩年內，最大的風險就是「地緣經濟對抗（中美對抗、關稅）」與「假新聞假消息洗盤」；長期十年內則以氣候變遷與 AI 技術不良後果為主。</p>
    <div class="highlight-box">
        <strong>⚠️ 2027 年投資典範轉移——從「盲目普漲」走向「結構分化」：</strong><br>
        2027 年是全球四大雲端廠商（CSP）AI 資本支出的「峰值年」，總支出衝上 1.1 兆至 1.47 兆美元歷史新高，2028 年增速將急劇放緩！市場將從「風口上的豬都能飛」轉向嚴厲檢驗「AI 商業變現能力」。營收若未逐月創高，隨時會被主力大幅打壓，必須採取「不追高、相對低檔布局」的防禦思維。
    </div>

    <h2>二、現金保留的靈活性與資產配置大局觀</h2>
    <ul>
        <li><strong>跌破 20% 是超級送分題</strong>：大盤指數跌幅超過 10% 叫大跌，而跌幅超過 20% 是市場非理性恐慌送給你的「超級送分題」。平日絕不可把資金買滿，否則大跌 20% 時沒有子彈抄底。</li>
        <li><strong>核心 vs 衛星資金配置</strong>：
            <ul>
                <li><strong>核心部位（大資產）</strong>：放在穩健型/累積型基金、公用事業、短中天期投資等級債。</li>
                <li><strong>衛星部位（短線波段金）</strong>：僅動用約 70～80 萬元，打帶跑、短進短出，每個月設定獲利了結 3 萬元 cover 生活開銷。</li>
            </ul>
        </li>
        <li><strong>定期定額「拆單切三旬法」</strong>：每月 12,000 元不要單一天扣款，拆成三旬：1～10 號扣 4,000、11～20 號扣 4,000、21～30 號扣 4,000，平滑月內高低點。</li>
    </ul>

    <h2>三、三大關鍵財務指標深度剖析</h2>
    <div class="formula-box">
        1. ROE（股東權益報酬率） = (稅後淨利 / 股東權益) × 100% ［門檻：10%～15% 以上］<br>
        2. 毛利率 = [(營業收入 - 營業成本) / 營業收入] × 100% ［門檻：近一年 > 40%］<br>
        3. 資本支出率 = 近四季資本支出之和 / 近四季營運現金流量之和 ［標準：30%～90%］
    </div>
    <ul>
        <li><strong>ROE 負債陷阱防禦</strong>：資產 = 負債 + 股東權益。借大債會虛增帳面 ROE！防禦標準：負債比率近三年平均 < 30%，每股自由現金流連續 5 年 > 0 元。2027 不能只看 ROE（落後指標），應優先看高毛利率與強勁營運現金流。</li>
        <li><strong>毛利率與定價權</strong>：蘋果（高毛利抗通膨定價權）vs 鴻海（代工毛利薄靠衝量）。</li>
        <li><strong>資本支出率判定</strong>：30%～90% 良性擴張；< 30% 為成熟型或全球寡占 No.1（如川湖僅 9%）；> 120% 為盲目擴張地雷警訊（如星宇航空初期大買新機折舊重壓）。</li>
    </ul>

    <div class="page-break"></div>

    <!-- 第三部：手寫筆記全彩還原與手算演練 -->
    <h1>第三部：課堂三大手寫筆記深度解密與手算演練</h1>
    <p>以下為學員在 11/14 課堂現場所記錄的三頁手寫筆記，完整保留了老師在黑板上的實戰推演、個股評價門檻與軟體操作步驟：</p>

    <h2>手寫筆記一：台積電本益比區間、G公司治理與 XQ 查法</h2>
    <div class="note-img-container">
        <img class="note-img" src="./handwritten_note1.jpg" alt="手寫筆記一">
        <div class="note-caption">【圖一：課堂手寫筆記實錄——台積電本益比三階梯與 XQ 查找步驟】</div>
    </div>
    <div class="card">
        <h3>📝 筆記核心解密：</h3>
        <ul>
            <li><strong>台積電本益比三階梯評價</strong>：
                <ul>
                    <li><code>20 - 25 倍</code>：<strong>便宜（天上掉下來的禮物、超級送分題）</strong>。</li>
                    <li><code>25 - 30 倍</code>：<strong>合理估值區間</strong>。</li>
                    <li><code>30 - 35 倍</code>：<strong>貴、過熱（隨時引發劇烈震盪修正）</strong>。</li>
                </ul>
            </li>
            <li><strong>G 公司治理容易漲</strong>：實務統計公司治理表現優良企業最容易賺到錢，推薦研究 <strong>富邦公司治理（00692）</strong>。</li>
            <li><strong>HPC 台灣龍頭股票</strong>：高速運算必備高階交換器龍頭 <strong>智邦（2345）</strong>，在低檔整理久，一旦發動爆發力強。</li>
            <li><strong>XQ 全球贏家查「資本支出」步驟</strong>：
                <code>先找個股 ➔ 在個股上按右鍵 ➔ 按基本資料 ➔ 再找財務分析 ➔ 資本支出</code>。
            </li>
        </ul>
    </div>

    <div class="page-break"></div>

    <h2>手寫筆記二：川湖 9% 資本支出率現場手算實錄與速動比率</h2>
    <div class="note-img-container">
        <img class="note-img" src="./handwritten_note2.jpg" alt="手寫筆記二">
        <div class="note-caption">【圖二：課堂手寫筆記實錄——川湖資本支出率 9% 算式與速動比率】</div>
    </div>
    <div class="card">
        <h3>📝 筆記核心解密：</h3>
        <ul>
            <li><strong>速動比率標準 > 1.5</strong>：
                <div class="formula-box">速動比率 = (流動資產 - 存貨 - 預付款) / 流動負債 ［要求 > 1.5］</div>
                剔除變現慢的存貨與不能退的預付款，衡量最即時的償債安全墊。
            </li>
            <li><strong>川湖（2059）資本支出率現場計算（震撼全場案例）</strong>：
                <ul>
                    <li>分子（近四季資本支出之和）：$324.02 + 159.03 + 568.78 + 103.84 = \mathbf{1,155.67}$ 百萬元。</li>
                    <li>分母（來自營運之現金流量）：$26.79 + 3,076 + 4,246 + 2,782 = \mathbf{12,781}$ 百萬元（注意第 3 季營運現金流暴增）。</li>
                    <li>計算結果：$1,155.67 \div 12,781 = 0.09042 \approx \mathbf{9\%}$！</li>
                </ul>
                <strong>意義</strong>：比率僅 9%，遠低於 30%，並非公司不投資，而是本業營運現金流極度龐大！身為全球伺服器導軌第一龍頭，享有全球最多專利與定價護城河，產能早已足以吃下市場且坐收豐沛現金！
            </li>
            <li><strong>營收移動平均線（3平均線）</strong>：取 7、8、9 月與 8、9、10 月之平滑移動平均。</li>
        </ul>
    </div>

    <div class="page-break"></div>

    <h2>手寫筆記三：資產負債結構、金字塔配置與切三旬</h2>
    <div class="note-img-container">
        <img class="note-img" src="./handwritten_note3.jpg" alt="手寫筆記三">
        <div class="note-caption">【圖三：課堂手寫筆記實錄——資產負債 40/60 結構與切三旬金字塔】</div>
    </div>
    <div class="card">
        <h3>📝 筆記核心解密：</h3>
        <ul>
            <li><strong>基金指標</strong>：評估基金要看 <strong>Beta 值</strong>（國泰全球基建基金 Beta 僅 0.14 抗震避暴跌），搭配中短天期<strong>投資等級債券</strong>。</li>
            <li><strong>ROE 結構分析</strong>：淨利 / 股東權益。假設資產 100%，健康配置為<strong>負債 40%、股東權益 60%（淨值）</strong>。若負債拉高到 80%，ROE 雖然衝高但風險極大！</li>
            <li><strong>核心選股六字訣</strong>：
                <code>毛利率高的股票</code> ｜ <code>高殖利率股票（6%~7%利差保護）</code> ｜ <code>長期成長產業</code> ｜ <code>不追高 相對低檔布局</code> ｜ <code>營收月月高（比較不容易被打壓）</code>。
            </li>
            <li><strong>金字塔配置與切三旬</strong>：
                金字塔底部寬大（核心穩健資產）、頂部小（波段衛星金 70~80 萬）；定期定額切三旬（1 旬 10 號、2 旬 20 號、3 旬 30 號）。
            </li>
        </ul>
    </div>

    <div class="page-break"></div>

    <!-- 第四部 -->
    <h1>第四部：趨勢產業、個股實戰對照與避坑全手冊</h1>

    <h2>一、三大核心趨勢產業</h2>
    <ul>
        <li><strong>ESG 永續投資</strong>：全球逾 130 兆美元基金進場（日本 GPIF、CalPERS、挪威主權基金）。實務統計<strong>「公司治理（G）推升力最強」</strong>。標的：00692、00878、00923。</li>
        <li><strong>綠色基礎建設與能源轉型</strong>：AI 吃電怪獸（IEA 預測 AI 用電激增至 1,260 TWh）。供電三件套「足＋穩＋安全」。標的：國泰全球基建基金（Beta 0.14）、散熱奇鋐（3017）、交換器智邦（2345）。</li>
        <li><strong>生技醫療</strong>：熟齡經濟（未來十年 65 歲以上增 37%）。標的：國泰基因免疫生技（00678）。警示：生技多無息，缺乏獲利支撐的本夢比極度危險。</li>
    </ul>

    <h2>二、個股實戰對照表</h2>
    <table>
        <tr>
            <th>股票代號與名稱</th>
            <th>性質</th>
            <th>關鍵特徵與課堂原話</th>
        </tr>
        <tr>
            <td><strong>台積電 (2330)</strong></td>
            <td>護城河龍頭</td>
            <td>十年 CAGR 28%~33%，本益比 20~25 送分題、25~30 合理、30~35 貴。盤面見 888、999 為好買點。</td>
        </tr>
        <tr>
            <td><strong>川湖 (2059)</strong></td>
            <td>獨占龍頭</td>
            <td>全球伺服器導軌 No.1，專利一條龍，資本支出率僅 9%，本業現金流龐大，獲投信持續加碼。</td>
        </tr>
        <tr>
            <td><strong>聯電 (2303)</strong></td>
            <td>防禦對照</td>
            <td>2022 升息由 65 跌到 49，但殖利率 6.8% 提供強大利差保護，抗跌且能落袋為安。</td>
        </tr>
        <tr>
            <td><strong>矽力-KY (6415)</strong></td>
            <td>地雷反面</td>
            <td>前股王（5,025元），一拆四後逢升息暴跌至 365 元。殖利率僅 0.8% 缺乏保護遭資金踩踏。</td>
        </tr>
        <tr>
            <td><strong>基亞 (3176)</strong></td>
            <td>地雷反面</td>
            <td>常年虧損全憑解盲本夢比炒至千元，解盲失敗連吞 17 根跌停板打不開，股價剩不到百元。</td>
        </tr>
        <tr>
            <td><strong>宏達電 (2498)</strong></td>
            <td>指標警示</td>
            <td>營收移動平均線常常鈍化無交叉警訊；營收年增率同期比較完整對沖淡旺季，精準發出警訊。</td>
        </tr>
        <tr>
            <td><strong>星宇航空</strong></td>
            <td>折舊警訊</td>
            <td>創立初期大量買新機，資本支出龐大，按季提列沉重折舊，侵蝕損益表獲利。</td>
        </tr>
    </table>

    <h2>三、地雷股五大特徵與三大出場保命警訊</h2>
    <div class="card">
        <h3>🚨 地雷股五大特徵：</h3>
        <ol>
            <li>董監事與高階經營層異常大量拋售自家持股（最凶險逃命訊號）。</li>
            <li>連續 5 年每股自由現金流為負值（$< 0$），本業無法造血全靠借貸續命。</li>
            <li>資本支出率暴增超過 120%，過度擴張引發折舊重壓與資金斷鏈。</li>
            <li>營收年增率連續下滑死亡交叉。</li>
            <li>常年無獲利憑本夢比炒作，殖利率近乎零，升息必遭提款。</li>
        </ol>
        <h3>🛑 三大出場保命警訊：</h3>
        <ul>
            <li><strong>均線三天不站回</strong>：跌破月線或半年線連續 3 天無法站回，趨勢轉弱果斷停利。</li>
            <li><strong>月度 CPI 突破 4%</strong>：通膨失控 FED 將暴力升息，主力大舉打壓，必須果斷停利。</li>
            <li><strong>美國 GDP 單季負成長</strong>：硬著陸訊號，「跑得比飛的還快，能跑就全部跑，全面清倉獲利了結！」</li>
        </ul>
    </div>

</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML 講義模板已產生: {HTML_PATH}")

# 使用 Chrome 或 Edge headless 轉換成 PDF
browser_cmd = None
if os.path.exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe"):
    browser_cmd = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
elif os.path.exists(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"):
    browser_cmd = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

if browser_cmd:
    print(f"使用瀏覽器無頭模式轉換 PDF: {browser_cmd}")
    cmd = [
        browser_cmd,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_PATH}",
        HTML_PATH
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(PDF_PATH) and os.path.getsize(PDF_PATH) > 0:
        size_kb = os.path.getsize(PDF_PATH) / 1024
        print(f"🎉 成功生成高解析度 PDF 講義: {PDF_PATH} ({size_kb:.1f} KB)")
    else:
        print("PDF 生成失敗，錯誤輸出:", res.stderr)
else:
    print("找不到 Chrome 或 Edge 瀏覽器。")
