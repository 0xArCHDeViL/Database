import csv

data = [
    {
        "kana": "うさぎ",
        "kanji": "兎",
        "arti": "Kelinci",
        "grup": "HEWAN & BINATANG",
        "jp": "兎はかわいいです。",
        "id": "Kelinci itu lucu.",
        "kanji_list": [
            {
                "char": "兎",
                "kun": "うさぎ",
                "on": "ト",
                "makna": "Kelinci. Gambar binatang dengan telinga panjang di atasnya."
            }
        ],
        "cocoklogi": "Hewan bertelinga panjang yang melompat lincah ke sana kemari, itulah sosok kelinci 兎."
    },
    {
        "kana": "やぎ",
        "kanji": "山羊",
        "arti": "Kambing",
        "grup": "HEWAN & BINATANG",
        "jp": "山羊を見ました。",
        "id": "Telah melihat kambing.",
        "kanji_list": [
            {
                "char": "山",
                "kun": "やま",
                "on": "サン",
                "makna": "Gunung. Gambar puncak-puncak gunung."
            },
            {
                "char": "羊",
                "kun": "ひつじ",
                "on": "ヨウ",
                "makna": "Domba. Gambar kepala domba dengan tanduknya."
            }
        ],
        "cocoklogi": "Domba 羊 liar yang suka memanjat dan tinggal di tebing gunung 山 yang curam, itulah kambing gunung 山羊."
    },
    {
        "kana": "うし",
        "kanji": "牛",
        "arti": "Sapi",
        "grup": "HEWAN & BINATANG",
        "jp": "牛の肉はおいしいです。",
        "id": "Daging sapi itu enak.",
        "kanji_list": [
            {
                "char": "牛",
                "kun": "うし",
                "on": "ギュウ",
                "makna": "Sapi. Gambar kepala sapi dengan dua tanduk panjang."
            }
        ],
        "cocoklogi": "Kepala binatang yang memiliki sepasang tanduk melengkung tajam di kepalanya, dia adalah sapi 牛."
    },
    {
        "kana": "いのしし",
        "kanji": "猪",
        "arti": "Babi hutan",
        "grup": "HEWAN & BINATANG",
        "jp": "森で猪を見ました。",
        "id": "Melihat babi hutan di hutan.",
        "kanji_list": [
            {
                "char": "猪",
                "kun": "いのしし",
                "on": "チョ",
                "makna": "Babi hutan. Radikal 犭 (hewan) dan 者 (seseorang). Hewan liar yang mirip babi tapi ganas."
            }
        ],
        "cocoklogi": "Seekor binatang buas 犭 yang suka menyeruduk ke arah seseorang 者 di dalam hutan, itulah babi hutan 猪 yang ganas."
    },
    {
        "kana": "むし",
        "kanji": "虫",
        "arti": "Serangga",
        "grup": "HEWAN & BINATANG",
        "jp": "虫は小さいです。",
        "id": "Serangga itu kecil.",
        "kanji_list": [
            {
                "char": "虫",
                "kun": "むし",
                "on": "チュウ",
                "makna": "Serangga. Gambar bentuk awal ular berbisa/serangga yang melingkar."
            }
        ],
        "cocoklogi": "Makhluk kecil yang tubuhnya bisa melingkar dan melata di tanah atau terbang, dia adalah serangga 虫."
    },
    {
        "kana": "ぶた",
        "kanji": "豚",
        "arti": "Babi",
        "grup": "HEWAN & BINATANG",
        "jp": "豚の肉を食べます。",
        "id": "Makan daging babi.",
        "kanji_list": [
            {
                "char": "豚",
                "kun": "ぶた",
                "on": "トン",
                "makna": "Babi ternak. Radikal 月 (daging) dan 豕 (babi liar). Babi yang sengaja digemukkan untuk diambil dagingnya."
            }
        ],
        "cocoklogi": "Seekor hewan sebangsa babi hutan 豕 yang sengaja diternak untuk menghasilkan daging 月 yang lezat dan berlemak tebal 豚."
    },
    {
        "kana": "どうぶつ",
        "kanji": "動物",
        "arti": "Binatang",
        "grup": "HEWAN & BINATANG",
        "jp": "動物園にたくさんの動物がいます。",
        "id": "Di kebun binatang ada banyak binatang.",
        "kanji_list": [
            {
                "char": "動",
                "kun": "うご.く",
                "on": "ドウ",
                "makna": "Bergerak. Menggunakan kekuatan untuk berpindah."
            },
            {
                "char": "物",
                "kun": "もの",
                "on": "ブツ",
                "makna": "Benda / Makhluk."
            }
        ],
        "cocoklogi": "Makhluk atau benda bernyawa 物 yang bisa bergerak 動 bebas ke sana kemari menggunakan tenaganya sendiri, itulah binatang 動物."
    },
    {
        "kana": "へび",
        "kanji": "蛇",
        "arti": "Ular",
        "grup": "HEWAN & BINATANG",
        "jp": "蛇は長いです。",
        "id": "Ular itu panjang.",
        "kanji_list": [
            {
                "char": "蛇",
                "kun": "へび",
                "on": "ジャ",
                "makna": "Ular. Radikal 虫 (serangga/melata) dan 它 (ular berbisa)."
            }
        ],
        "cocoklogi": "Sebangsa hewan melata 虫 yang bentuk tubuhnya panjang tanpa kaki seperti ular berbisa 它 yang berbahaya, dialah ular 蛇."
    },
    {
        "kana": "うま",
        "kanji": "馬",
        "arti": "Kuda",
        "grup": "HEWAN & BINATANG",
        "jp": "馬は速いです。",
        "id": "Kuda itu cepat.",
        "kanji_list": [
            {
                "char": "馬",
                "kun": "うま",
                "on": "バ",
                "makna": "Kuda. Gambar kuda dengan surai, tubuh, dan kakinya."
            }
        ],
        "cocoklogi": "Melihat posturnya yang gagah dengan surai di leher dan empat kaki kuat untuk berlari kencang, dia adalah kuda 馬."
    },
    {
        "kana": "くま",
        "kanji": "熊",
        "arti": "Beruang",
        "grup": "HEWAN & BINATANG",
        "jp": "山で熊を見ました。",
        "id": "Melihat beruang di gunung.",
        "kanji_list": [
            {
                "char": "熊",
                "kun": "くま",
                "on": "ユウ",
                "makna": "Beruang. Radikal 灬 (api) dan 能 (kemampuan/tenaga). Binatang buas bertenaga besar yang berbahaya seperti api."
            }
        ],
        "cocoklogi": "Binatang buas yang kemampuan 能 tenaga dan marahnya bisa menghanguskan korbannya bagaikan dilalap api 灬, dialah beruang 熊."
    },
    {
        "kana": "あり",
        "kanji": "蟻",
        "arti": "Semut",
        "grup": "HEWAN & BINATANG",
        "jp": "蟻がたくさんいます。",
        "id": "Ada banyak semut.",
        "kanji_list": [
            {
                "char": "蟻",
                "kun": "あり",
                "on": "ギ",
                "makna": "Semut. Radikal 虫 (serangga) dan 義 (kebenaran/tugas mulia). Serangga yang selalu patuh bekerja sama."
            }
        ],
        "cocoklogi": "Serangga 虫 kecil yang hidup berkoloni dan selalu menjalankan tugas kebenaran 義 dengan patuh bekerja sama, itulah semut 蟻."
    },
    {
        "kana": "にわとり",
        "kanji": "鶏",
        "arti": "Ayam",
        "grup": "HEWAN & BINATANG",
        "jp": "鶏の肉を食べます。",
        "id": "Makan daging ayam.",
        "kanji_list": [
            {
                "char": "鶏",
                "kun": "にわとり",
                "on": "ケイ",
                "makna": "Ayam. Radikal 鳥 (burung) dan 奚 (hamba/pelayan). Burung peliharaan yang hidup di pekarangan rumah."
            }
        ],
        "cocoklogi": "Sejenis burung 鳥 yang dipelihara di pekarangan layaknya hamba 奚 untuk dimanfaatkan telur dan dagingnya, dialah ayam 鶏."
    },
    {
        "kana": "かえる",
        "kanji": "蛙",
        "arti": "Katak",
        "grup": "HEWAN & BINATANG",
        "jp": "蛙が鳴きます。",
        "id": "Katak berbunyi.",
        "kanji_list": [
            {
                "char": "蛙",
                "kun": "かえる",
                "on": "ア",
                "makna": "Katak. Radikal 虫 (serangga/hewan kecil) dan 圭 (permata/dua gundukan tanah). Hewan kecil yang hidup di lumpur."
            }
        ],
        "cocoklogi": "Hewan kecil 虫 yang suka melompat-lompat dan tinggal di atas tumpukan tanah berlumpur 圭 di dekat air, dia adalah katak 蛙."
    },
    {
        "kana": "いちじ",
        "kanji": "１時",
        "arti": "Jam 1",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "今は１時です。",
        "id": "Sekarang jam 1.",
        "kanji_list": [
            {
                "char": "１",
                "kun": "–",
                "on": "いち",
                "makna": "Angka Satu."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam. Radikal 日 (matahari) dan 寺 (kuil). Waktu yang ditandai oleh pergerakan matahari."
            }
        ],
        "cocoklogi": "Saat matahari bergerak satu langkah, jarum jam menunjuk ke angka 1, menandakan waktu tepat jam satu １時."
    },
    {
        "kana": "にじ",
        "kanji": "２時",
        "arti": "Jam 2",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "２時に帰ります。",
        "id": "Pulang jam 2.",
        "kanji_list": [
            {
                "char": "２",
                "kun": "–",
                "on": "に",
                "makna": "Angka Dua."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Angka dua ditambah penanda waktu, menjadi jam dua ２時 yang tepat."
    },
    {
        "kana": "さんじ",
        "kanji": "３時",
        "arti": "Jam 3",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "３時にお茶を飲みます。",
        "id": "Minum teh jam 3.",
        "kanji_list": [
            {
                "char": "３",
                "kun": "–",
                "on": "さん",
                "makna": "Angka Tiga."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Ketika jarum jam berada di angka tiga, inilah waktunya istirahat sore jam tiga ３時."
    },
    {
        "kana": "よじ",
        "kanji": "４時",
        "arti": "Jam 4",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "４時に終わります。",
        "id": "Selesai jam 4.",
        "kanji_list": [
            {
                "char": "４",
                "kun": "–",
                "on": "よ",
                "makna": "Angka Empat."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Perhatikan bacaannya, bukan yon-ji tapi yo-ji. Waktu menunjukkan pukul empat sore ４時."
    },
    {
        "kana": "ごじ",
        "kanji": "５時",
        "arti": "Jam 5",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "５時に出かけます。",
        "id": "Pergi keluar jam 5.",
        "kanji_list": [
            {
                "char": "５",
                "kun": "–",
                "on": "ご",
                "makna": "Angka Lima."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Matahari mulai turun dan waktu sudah menunjukkan pukul lima ５時, saatnya bersiap pulang kerja."
    },
    {
        "kana": "ろくじ",
        "kanji": "６時",
        "arti": "Jam 6",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "朝、６時に起きます。",
        "id": "Pagi hari, bangun jam 6.",
        "kanji_list": [
            {
                "char": "６",
                "kun": "–",
                "on": "ろく",
                "makna": "Angka Enam."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Angka enam yang dipadukan dengan kanji waktu, pas banget untuk bangun pagi di jam enam ６時."
    },
    {
        "kana": "しちじ",
        "kanji": "７時",
        "arti": "Jam 7",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "７時に朝ごはんを食べます。",
        "id": "Makan sarapan jam 7.",
        "kanji_list": [
            {
                "char": "７",
                "kun": "–",
                "on": "しち",
                "makna": "Angka Tujuh."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Ingat bacaannya shichi-ji bukan nana-ji. Waktu yang pas untuk sarapan tepat pukul tujuh ７時."
    },
    {
        "kana": "はちじ",
        "kanji": "８時",
        "arti": "Jam 8",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "８時に仕事が始まります。",
        "id": "Pekerjaan dimulai jam 8.",
        "kanji_list": [
            {
                "char": "８",
                "kun": "–",
                "on": "はち",
                "makna": "Angka Delapan."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Delapan disandingkan dengan jam, menandakan pukul delapan ８時 pas saat kantor mulai beroperasi."
    },
    {
        "kana": "くじ",
        "kanji": "９時",
        "arti": "Jam 9",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "夜、９時に寝ます。",
        "id": "Malam hari, tidur jam 9.",
        "kanji_list": [
            {
                "char": "９",
                "kun": "–",
                "on": "く",
                "makna": "Angka Sembilan."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Hati-hati bacaannya, ku-ji bukan kyuu-ji. Waktu yang enak buat masuk selimut di pukul sembilan ９時 malam."
    },
    {
        "kana": "じゅうじ",
        "kanji": "１０時",
        "arti": "Jam 10",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "１０時に休みます。",
        "id": "Istirahat jam 10.",
        "kanji_list": [
            {
                "char": "１０",
                "kun": "–",
                "on": "じゅう",
                "makna": "Angka Sepuluh."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Angka sepuluh bertemu penanda waktu, jadilah jam sepuluh １０時 yang bulat."
    },
    {
        "kana": "じゅういちじ",
        "kanji": "１１時",
        "arti": "Jam 11",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "１１時にテレビを見ます。",
        "id": "Menonton TV jam 11.",
        "kanji_list": [
            {
                "char": "１１",
                "kun": "–",
                "on": "じゅういち",
                "makna": "Angka Sebelas."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Jam menunjukkan pukul sebelas １１時 siang atau malam."
    },
    {
        "kana": "じゅうにじ",
        "kanji": "１２時",
        "arti": "Jam 12",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "１２時に昼ごはんを食べます。",
        "id": "Makan siang jam 12.",
        "kanji_list": [
            {
                "char": "１２",
                "kun": "–",
                "on": "じゅうに",
                "makna": "Angka Dua belas."
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Puncak hari telah tiba, jarum jam saling menindih di pukul dua belas １２時 siang."
    }
]

CSS = """<style>
.frontcard{font-family:'Hiragino Sans','Yu Gothic',sans-serif;
  background:#ffffff !important;color:#1a1a1a !important;
  padding:30px 20px;border-radius:14px;text-align:center;
  border:2px solid #e5e7eb}
.front-main{font-size:56px;font-weight:bold;color:#1a1a1a !important;
  line-height:1.3;letter-spacing:1px}
.front-hint{margin-top:14px;font-size:12px;text-transform:uppercase;
  letter-spacing:2px;color:#9ca3af !important;font-weight:600}
.jpcard{font-family:'Hiragino Sans','Yu Gothic',sans-serif;line-height:1.7;
  background:#ffffff !important;color:#1a1a1a !important;padding:16px;border-radius:10px}
.yomi{font-size:22px;color:#2b6cb0 !important;font-weight:bold;margin-bottom:4px}
.arti{font-size:20px;color:#1a1a1a !important;font-weight:bold;background:#fef3c7 !important;
  padding:4px 10px;border-radius:6px;display:inline-block;margin:6px 0}
.kalimat{margin:10px 0;padding:10px 14px;background:#eafaf1 !important;border-left:4px solid #22c55e;
  border-radius:4px;color:#14532d !important}
.kalimat .jp{font-size:17px;color:#166534 !important}
.kalimat .id{font-size:14px;color:#3f6212 !important;font-style:italic;margin-top:2px}
.label{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:#78716c !important;
  font-weight:bold;margin-bottom:6px}
.analisis-box{margin:12px 0;padding:12px;background:#eef2ff !important;
  border-radius:10px;border:1px solid #c7d2fe}
.analisis-title{font-size:11px;text-transform:uppercase;letter-spacing:1px;
  color:#78716c !important;font-weight:bold;margin-bottom:10px}
.kanji-strip{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:8px}
.kanji-mini{flex:1;min-width:130px;background:#ffffff !important;
  border-radius:8px;padding:12px 10px;text-align:center;border:1px solid #ddd6fe}
.kanji-mini-char{font-size:38px;font-weight:bold;color:#1a1a1a !important;line-height:1.2}
.yomi-badges{display:flex;justify-content:center;gap:6px;margin:8px 0}
.badge-kun{background:#dbeafe !important;color:#1e40af !important;
  font-size:12px;font-weight:600;padding:3px 8px;border-radius:6px}
.badge-on{background:#fce7f3 !important;color:#9d174d !important;
  font-size:12px;font-weight:600;padding:3px 8px;border-radius:6px}
.kanji-mini-makna{font-size:12.5px;color:#374151 !important;text-align:left;
  margin-top:8px;line-height:1.5;border-top:1px dashed #ddd6fe;padding-top:8px}
.cocoklogi-box{margin:12px 0;padding:12px 14px;background:#fdeef6 !important;
  border-left:4px solid #ec4899;border-radius:8px;font-size:14px;
  color:#831843 !important;line-height:1.7}
.cocoklogi-box b{color:#be185d !important}
</style>"""

CSS_ONELINE = CSS.replace('\n', '')

with open('BAB_06/BAB_06.txt', 'a', encoding='utf-8') as f:
    for item in data:
        front_word = item['kanji'] if item['kanji'] else item['kana']
        hint = "Kanji &middot; Ingat cara bacanya?" if item['kanji'] else "Kana &middot; Ingat artinya?"

        front_html = f'''{CSS_ONELINE}<div class="frontcard"><div class="front-main">{front_word}</div><div class="front-hint">{hint}</div></div>'''

        kanji_strip_html = ""
        if 'kanji_list' in item and len(item['kanji_list']) > 0:
            for k in item['kanji_list']:
                kanji_strip_html += f'''<div class="kanji-mini"><div class="kanji-mini-char">{k['char']}</div><div class="yomi-badges"><span class="badge-kun">Kun: {k['kun']}</span><span class="badge-on">On: {k['on']}</span></div><div class="kanji-mini-makna">{k['makna']}</div></div>'''

        analisis_box_html = ""
        if kanji_strip_html:
            analisis_box_html = f'''<div class="analisis-box"><div class="analisis-title">Analisis</div><div class="kanji-strip">{kanji_strip_html}</div></div>'''

        cocoklogi_html = f'''<div class="cocoklogi-box"><b>Cocoklogi:</b> {item['cocoklogi']}</div>'''

        yomikata_block = ""
        if item['kanji']:
            yomikata_block = f'''<div class="label">Yomikata</div><div class="yomi">{item['kana']}</div>'''

        back_html = f'''{CSS_ONELINE}<div class="jpcard">{yomikata_block}<div class="arti">{item['arti']}</div><div class="kalimat"><div class="label">Contoh Kalimat</div><div class="jp">{item['jp']}</div><div class="id">{item['id']}</div></div>{analisis_box_html}{cocoklogi_html}</div>'''

        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        tag = "Hewan" if "HEWAN" in item['grup'] else "Waktu"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Appended 25 cards to BAB_06/BAB_06.txt")
