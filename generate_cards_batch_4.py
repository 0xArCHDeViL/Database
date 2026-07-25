import csv

data = [
    {
        "kana": "なし",
        "kanji": "梨",
        "arti": "Pir",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "梨を食べます。",
        "id": "Makan buah pir.",
        "kanji_list": [
            {
                "char": "梨",
                "kun": "なし",
                "on": "リ",
                "makna": "Pir. Radikal 木 (pohon) dan 利 (tajam/lancar). Pohon yang buahnya manis dan melancarkan pencernaan."
            }
        ],
        "cocoklogi": "Makan buah dari pohon 木 yang rasanya manis, berair, dan bisa melancarkan 利 tenggorokan, itulah buah pir 梨."
    },
    {
        "kana": "くだもの",
        "kanji": "果物",
        "arti": "Buah-buahan",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "店で果物を買います。",
        "id": "Membeli buah-buahan di toko.",
        "kanji_list": [
            {
                "char": "果",
                "kun": "は.たす",
                "on": "カ",
                "makna": "Buah / Hasil. Radikal 木 (pohon) dan 田 (kotak/bentuk bulat). Buah bulat yang dihasilkan dari atas pohon."
            },
            {
                "char": "物",
                "kun": "もの",
                "on": "ブツ",
                "makna": "Benda / Barang."
            }
        ],
        "cocoklogi": "Benda 物 bulat yang tumbuh dan merupakan hasil panen utama dari ujung pohon 果, itulah yang kita sebut buah-buahan 果物."
    },
    {
        "kana": "うめ",
        "kanji": "梅",
        "arti": "Buah ume (Plum Jepang)",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "梅はおいしいです。",
        "id": "Buah ume itu enak.",
        "kanji_list": [
            {
                "char": "梅",
                "kun": "うめ",
                "on": "バイ",
                "makna": "Plum. Radikal 木 (pohon) dan 毎 (setiap/selalu). Pohon yang selalu berbunga setiap kali musim semi datang."
            }
        ],
        "cocoklogi": "Pohon 木 yang selalu dan setiap 毎 musim semi datang menjadi yang pertama mekar bunganya, itulah pohon plum/ume 梅."
    },
    {
        "kana": "えだまめ",
        "kanji": "枝豆",
        "arti": "Kacang edamame",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "枝豆を食べました。",
        "id": "Telah makan kacang edamame.",
        "kanji_list": [
            {
                "char": "枝",
                "kun": "えだ",
                "on": "シ",
                "makna": "Dahan / Ranting. Radikal 木 (pohon) dan 支 (mendukung/menopang)."
            },
            {
                "char": "豆",
                "kun": "まめ",
                "on": "トウ",
                "makna": "Kacang. Gambar wadah berleher tinggi bertutup yang mirip polong kacang."
            }
        ],
        "cocoklogi": "Kacang 豆 yang tumbuh dan menempel pada tangkai atau dahan 枝 tanaman secara merapat, jadilah ia kacang edamame 枝豆."
    },
    {
        "kana": "もも",
        "kanji": "桃",
        "arti": "Buah persik",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "桃はおいしいです。",
        "id": "Buah persik itu enak.",
        "kanji_list": [
            {
                "char": "桃",
                "kun": "もも",
                "on": "トウ",
                "makna": "Persik. Radikal 木 (pohon) dan 兆 (tanda/miliar). Pohon yang buahnya sangat banyak dan jadi pertanda musim panas."
            }
        ],
        "cocoklogi": "Pohon 木 yang berbuah sangat banyak hingga menjadi pertanda 兆 datangnya musim panas, itulah si pohon buah persik 桃."
    },
    {
        "kana": "どんぐり",
        "kanji": "団栗",
        "arti": "Kacang donguri (Ek)",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "森で団栗を見ました。",
        "id": "Melihat kacang donguri di hutan.",
        "kanji_list": [
            {
                "char": "団",
                "kun": "–",
                "on": "ダン",
                "makna": "Kelompok / Bulat. Sesuatu yang bulat atau berkumpul jadi satu."
            },
            {
                "char": "栗",
                "kun": "くり",
                "on": "リツ",
                "makna": "Kastanya / Ek. Radikal 木 (pohon) dan 覀 (berduri/penutup). Kacang dari pohon yang cangkangnya berduri atau keras."
            }
        ],
        "cocoklogi": "Kacang ek 栗 yang bentuknya sangat bulat seperti bola kecil yang padat 団, ini adalah makanan favorit tupai alias kacang donguri 団栗."
    },
    {
        "kana": "みかん",
        "kanji": "蜜柑",
        "arti": "Jeruk",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "蜜柑を買います。",
        "id": "Membeli jeruk.",
        "kanji_list": [
            {
                "char": "蜜",
                "kun": "–",
                "on": "ミツ",
                "makna": "Madu / Manis. Radikal 虫 (serangga) dan 宓 (tersembunyi). Sesuatu manis (madu) yang disembunyikan lebah."
            },
            {
                "char": "柑",
                "kun": "–",
                "on": "カン",
                "makna": "Jeruk. Radikal 木 (pohon) dan 甘 (manis). Pohon yang berbuah manis."
            }
        ],
        "cocoklogi": "Pohon yang berbuah sangat manis 甘 seperti ada madu 蜜 di dalamnya, itulah buah jeruk mandarin 蜜柑."
    },
    {
        "kana": "スイカ",
        "kanji": "西瓜",
        "arti": "Semangka",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "夏に西瓜を食べます。",
        "id": "Makan semangka di musim panas.",
        "kanji_list": [
            {
                "char": "西",
                "kun": "にし",
                "on": "セイ",
                "makna": "Barat. Gambar sarang burung saat matahari terbenam (di barat)."
            },
            {
                "char": "瓜",
                "kun": "うり",
                "on": "カ",
                "makna": "Melon / Labu. Gambar tanaman merambat yang buahnya menggantung."
            }
        ],
        "cocoklogi": "Buah sejenis melon atau labu 瓜 yang pada zaman dulu bibitnya dibawa dari daerah barat 西 ke Tiongkok, itulah semangka 西瓜."
    },
    {
        "kana": "ピーナツ",
        "kanji": "",
        "arti": "Kacang",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "ピーナツを食べます。",
        "id": "Makan kacang.",
        "cocoklogi": "Piinatsu! (Berasal dari bahasa Inggris 'Peanuts'). Enak buat cemilan nonton TV."
    },
    {
        "kana": "バナナ",
        "kanji": "",
        "arti": "Pisang",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "バナナを買います。",
        "id": "Membeli pisang.",
        "cocoklogi": "Banana! (Berasal dari bahasa Inggris 'Banana'). Makanan favorit monyet dan orang yang mau diet."
    },
    {
        "kana": "パイナップル",
        "kanji": "",
        "arti": "Nanas",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "パイナップルはおいしいです。",
        "id": "Nanas itu enak.",
        "cocoklogi": "Painappuru! (Berasal dari bahasa Inggris 'Pineapple'). Apel berduri ala tropis."
    },
    {
        "kana": "メロン",
        "kanji": "",
        "arti": "Melon",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "メロンを食べました。",
        "id": "Telah makan melon.",
        "cocoklogi": "Meron! (Berasal dari bahasa Inggris 'Melon'). Buah sultan yang sering dibungkus mewah."
    },
    {
        "kana": "マンゴー",
        "kanji": "",
        "arti": "Mangga",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "マンゴーはおいしいです。",
        "id": "Mangga itu enak.",
        "cocoklogi": "Mangoo! (Berasal dari bahasa Inggris 'Mango'). Buah tropis andalan musim panas."
    },
    {
        "kana": "チェリー",
        "kanji": "",
        "arti": "Ceri",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "チェリーを買いました。",
        "id": "Telah membeli ceri.",
        "cocoklogi": "Cherii! (Berasal dari bahasa Inggris 'Cherry'). Buah kecil merah yang sering ada di atas kue."
    },
    {
        "kana": "ちゅうしょく",
        "kanji": "昼食",
        "arti": "Makan siang",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "十二時に昼食を食べます。",
        "id": "Makan siang jam 12.",
        "kanji_list": [
            {
                "char": "昼",
                "kun": "ひる",
                "on": "チュウ",
                "makna": "Siang. Radikal 日 (matahari), 尺 (mengukur), dan 一 (cakrawala). Saat matahari berada tinggi dan bisa diukur."
            },
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan / Makanan."
            }
        ],
        "cocoklogi": "Mengisi perut dengan cara makan 食 di kala matahari sedang terik di waktu siang 昼, itulah makan siang 昼食."
    },
    {
        "kana": "ゆうしょく",
        "kanji": "夕食",
        "arti": "Makan malam",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "家族と夕食を食べます。",
        "id": "Makan malam bersama keluarga.",
        "kanji_list": [
            {
                "char": "夕",
                "kun": "ゆう",
                "on": "セキ",
                "makna": "Sore / Senja. Gambar bulan sabit yang baru mulai muncul di langit sore."
            },
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan / Makanan."
            }
        ],
        "cocoklogi": "Saat bulan sabit mulai terlihat di waktu senja/sore 夕, itulah saat yang tepat untuk menyantap makanan 食 malam 夕食."
    },
    {
        "kana": "ちょうしょく",
        "kanji": "朝食",
        "arti": "Makan pagi",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "朝食はおいしいです。",
        "id": "Makan pagi itu enak.",
        "kanji_list": [
            {
                "char": "朝",
                "kun": "あさ",
                "on": "チョウ",
                "makna": "Pagi. Radikal 月 (bulan) dan 日 (matahari/waktu). Waktu di mana bulan memudar dan matahari terbit."
            },
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan / Makanan."
            }
        ],
        "cocoklogi": "Memulai hari di saat matahari baru terbit di pagi 朝 hari dengan menyantap makanan 食 bergizi, alias makan pagi 朝食."
    },
    {
        "kana": "すしや",
        "kanji": "すし屋",
        "arti": "Kedai sushi",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "すし屋に行きます。",
        "id": "Pergi ke kedai sushi.",
        "kanji_list": [
            {
                "char": "屋",
                "kun": "や",
                "on": "オク",
                "makna": "Toko / Kedai. Radikal 尸 (atap) dan 至 (tiba)."
            }
        ],
        "cocoklogi": "Orang-orang berkumpul di bawah satu atap atau kedai 屋 khusus untuk menikmati hidangan 'sushi' yang segar."
    },
    {
        "kana": "パンや",
        "kanji": "パン屋",
        "arti": "Toko roti",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "パン屋でパンを買います。",
        "id": "Membeli roti di toko roti.",
        "kanji_list": [
            {
                "char": "屋",
                "kun": "や",
                "on": "オク",
                "makna": "Toko / Kedai."
            }
        ],
        "cocoklogi": "Sebuah bangunan atau kedai 屋 yang aroma panggangan rotinya (pan) tercium sampai ke jalan raya."
    },
    {
        "kana": "ラーメンや",
        "kanji": "ラーメン屋",
        "arti": "Kedai ramen",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "ラーメン屋で昼食を食べます。",
        "id": "Makan siang di kedai ramen.",
        "kanji_list": [
            {
                "char": "屋",
                "kun": "や",
                "on": "オク",
                "makna": "Toko / Kedai."
            }
        ],
        "cocoklogi": "Kedai 屋 yang khusus menyajikan semangkuk mi ramen panas yang kuahnya mengepul menggoda selera."
    },
    {
        "kana": "あさごはん",
        "kanji": "朝ごはん",
        "arti": "Sarapan",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "七時に朝ごはんを食べます。",
        "id": "Makan sarapan jam 7.",
        "kanji_list": [
            {
                "char": "朝",
                "kun": "あさ",
                "on": "チョウ",
                "makna": "Pagi. Waktu matahari terbit."
            }
        ],
        "cocoklogi": "Nasi (gohan) yang hangat dinikmati di waktu pagi 朝 untuk menambah energi memulai hari."
    },
    {
        "kana": "ひるごはん",
        "kanji": "昼ごはん",
        "arti": "Makan siang",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "十二時に昼ごはんを食べます。",
        "id": "Makan siang jam 12.",
        "kanji_list": [
            {
                "char": "昼",
                "kun": "ひる",
                "on": "チュウ",
                "makna": "Siang. Waktu matahari di atas kepala."
            }
        ],
        "cocoklogi": "Menyantap nasi (gohan) di kala cuaca siang 昼 bolong sedang terik-teriknya, ini adalah makan siang andalan."
    },
    {
        "kana": "ばんごはん",
        "kanji": "晩ごはん",
        "arti": "Makan malam",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "晩ごはんはおいしいです。",
        "id": "Makan malam itu enak.",
        "kanji_list": [
            {
                "char": "晩",
                "kun": "–",
                "on": "バン",
                "makna": "Malam. Radikal 日 (matahari) dan 免 (menghindar/lepas). Waktu di mana matahari sudah melepaskan sinarnya alias malam."
            }
        ],
        "cocoklogi": "Saat cahaya matahari 日 sudah benar-benar hilang dan lepas 免 berganti malam 晩, itulah waktunya menyantap nasi (gohan) malam."
    },
    {
        "kana": "ランチ",
        "kanji": "",
        "arti": "Makan siang",
        "grup": "MAKANAN (UMUM & OLAHAN)",
        "jp": "レストランでランチを食べます。",
        "id": "Makan siang di restoran.",
        "cocoklogi": "Ranchi! (Berasal dari bahasa Inggris 'Lunch'). Biasanya dipakai untuk menu paket makan siang khusus (Lunch Set)."
    },
    {
        "kana": "きっさてん",
        "kanji": "喫茶店",
        "arti": "Kedai teh",
        "grup": "MINUMAN",
        "jp": "喫茶店でお茶を飲みます。",
        "id": "Minum teh di kedai teh.",
        "kanji_list": [
            {
                "char": "喫",
                "kun": "–",
                "on": "キツ",
                "makna": "Menyesap / Merokok. Radikal 口 (mulut) dan 契 (perjanjian). Mulut yang mengisap sesuatu dengan nikmat."
            },
            {
                "char": "茶",
                "kun": "–",
                "on": "チャ",
                "makna": "Teh. Radikal 艹 (tanaman). Tanaman herbal untuk diseduh."
            },
            {
                "char": "店",
                "kun": "みせ",
                "on": "テン",
                "makna": "Toko / Kedai. Bangunan untuk berjualan."
            }
        ],
        "cocoklogi": "Sebuah toko 店 yang nyaman untuk menyesap 喫 nikmatnya secangkir teh 茶 panas sambil mengobrol santai."
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

        tag = "Makanan" if "MAKANAN" in item['grup'] else "Minuman"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Appended 25 cards to BAB_06/BAB_06.txt")
