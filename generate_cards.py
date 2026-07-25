import csv

data = [
    {
        "kana": "かいます",
        "kanji": "買います",
        "arti": "Membeli",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "明日、デパートでカメラを買います。",
        "id": "Besok, saya membeli kamera di pasar raya.",
        "kanji_list": [
            {
                "char": "買",
                "kun": "か.う",
                "on": "バイ",
                "makna": "Membeli. Radikal 罒 (jaring/mata) dan 貝 (kerang/uang). Mengawasi dengan teliti kerang (uang) atau barang saat melakukan pertukaran alias membeli."
            }
        ],
        "cocoklogi": "Punya kerang 貝 (uang di zaman dulu), lalu memakai jaring 罒 untuk mengambil barang yang diinginkan, proses itulah yang disebut kegiatan membeli 買."
    },
    {
        "kana": "あらいます",
        "kanji": "洗います",
        "arti": "Mencuci",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "朝、シャツを洗います。",
        "id": "Pagi hari, saya mencuci kemeja.",
        "kanji_list": [
            {
                "char": "洗",
                "kun": "あら.う",
                "on": "セン",
                "makna": "Mencuci. Radikal 氵 (air) dan 先 (duluan/sebelumnya). Saat bersiap-siap, hal yang dilakukan duluan adalah menyiram air ke tubuh untuk membersihkan diri alias mencuci."
            }
        ],
        "cocoklogi": "Mencuci kotoran menggunakan air 氵 sebagai hal pertama 先 yang dilakukan agar bersih sebelum melakukan aktivitas."
    },
    {
        "kana": "いきます",
        "kanji": "行きます",
        "arti": "Pergi",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "毎日、電車で学校に行きます。",
        "id": "Setiap hari, saya pergi ke sekolah dengan kereta.",
        "kanji_list": [
            {
                "char": "行",
                "kun": "い.く / ゆ.く / おこな.う",
                "on": "コウ / ギョウ",
                "makna": "Pergi/berjalan. Gambar persimpangan jalan besar melambangkan pergerakan dan aktivitas."
            }
        ],
        "cocoklogi": "Seperti melihat jalan raya yang bersilangan, ini adalah tempat orang berlalu lalang dan pergi ke berbagai tujuan."
    },
    {
        "kana": "はたらきます",
        "kanji": "働きます",
        "arti": "Bekerja",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "兄は会社で働きます。",
        "id": "Kakak laki-laki saya bekerja di perusahaan.",
        "kanji_list": [
            {
                "char": "働",
                "kun": "はたら.く",
                "on": "ドウ",
                "makna": "Bekerja. Radikal 亻 (orang) dan 動 (bergerak). Seseorang yang aktif bergerak secara fisik maupun pikiran untuk menghasilkan sesuatu."
            }
        ],
        "cocoklogi": "Kalau manusia 亻 sudah mulai bergerak 動 dengan giat dari pagi sampai sore, berarti dia sedang bekerja 働 keras!"
    },
    {
        "kana": "シャワーをあびます",
        "kanji": "シャワーを浴びます",
        "arti": "Mandi",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "夜、シャワーを浴びます。",
        "id": "Malam hari, saya mandi.",
        "kanji_list": [
            {
                "char": "浴",
                "kun": "あ.びる",
                "on": "ヨク",
                "makna": "Mandi / bermandikan. Radikal 氵 (air) dan 谷 (lembah). Seperti air yang mengalir deras di lembah, menyiramkan air ke sekujur tubuh."
            }
        ],
        "cocoklogi": "Merasakan guyuran air 氵 yang deras mengalir seperti sungai di lembah 谷 saat kita mandi 浴 membasahi sekujur tubuh."
    },
    {
        "kana": "やすみます",
        "kanji": "休みます",
        "arti": "Libur / Istirahat",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "日曜日は休みます。",
        "id": "Hari Minggu saya libur.",
        "kanji_list": [
            {
                "char": "休",
                "kun": "やす.む",
                "on": "キュウ",
                "makna": "Istirahat / Libur. Radikal 亻 (orang) dan 木 (pohon). Seseorang yang bersandar di pohon untuk menghilangkan lelah."
            }
        ],
        "cocoklogi": "Kalau sudah capek bekerja, seorang manusia 亻 akan mencari pohon rindang 木 dan bersandar di sana untuk istirahat 休 sejenak."
    },
    {
        "kana": "よみます",
        "kanji": "読みます",
        "arti": "Membaca",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "図書館で本を読みます。",
        "id": "Saya membaca buku di perpustakaan.",
        "kanji_list": [
            {
                "char": "読",
                "kun": "よ.む",
                "on": "ドク",
                "makna": "Membaca. Radikal 言 (kata/berbicara) dan 売 (menjual). Dulu orang membacakan/berbicara tentang barang dagangannya dengan lantang agar laku terjual."
            }
        ],
        "cocoklogi": "Mengeluarkan kata-kata 言 secara nyaring seperti orang yang sedang berjualan 売 menjajakan barangnya, itulah kegiatan membaca 読 bersuara di zaman dulu!"
    },
    {
        "kana": "うります",
        "kanji": "売ります",
        "arti": "Menjual",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "店で果物を売ります。",
        "id": "Saya menjual buah-buahan di toko.",
        "kanji_list": [
            {
                "char": "売",
                "kun": "う.る",
                "on": "バイ",
                "makna": "Menjual. Radikal 士 (prajurit/sarjana), 冖 (penutup), dan 儿 (kaki orang). Orang yang menggelar barang dagangannya untuk menawarkannya."
            }
        ],
        "cocoklogi": "Seorang pria (awalnya 士) membawa dan menggelar barang dagangannya (ada penutup 冖) dengan kaki 儿 melangkah ke pasar untuk menjual 売 dagangannya."
    },
    {
        "kana": "かえります",
        "kanji": "帰ります",
        "arti": "Pulang",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "五時に家へ帰ります。",
        "id": "Saya pulang ke rumah pada jam 5.",
        "kanji_list": [
            {
                "char": "帰",
                "kun": "かえ.る",
                "on": "キ",
                "makna": "Pulang. Mengandung unsur 刂 (pedang/pisau) dan 帚 (sapu). Kembali ke rumah setelah bepergian jauh."
            }
        ],
        "cocoklogi": "Setelah lelah bepergian dan bertahan menggunakan pedang 刂, akhirnya bisa pulang 帰 ke rumah yang sudah bersih karena rutin memakai sapu 帚."
    },
    {
        "kana": "もどります",
        "kanji": "戻ります",
        "arti": "Kembali",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "昼休みに会社へ戻ります。",
        "id": "Saya kembali ke perusahaan pada saat istirahat siang.",
        "kanji_list": [
            {
                "char": "戻",
                "kun": "もど.る",
                "on": "レイ",
                "makna": "Kembali. Radikal 戸 (pintu) dan 犬 (anjing). Anjing yang kembali ke pintu rumahnya."
            }
        ],
        "cocoklogi": "Bayangkan seekor anjing peliharaan 犬 yang habis jalan-jalan, pada akhirnya dia pasti akan kembali 戻 ke pintu 戸 rumah pemiliknya."
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

with open('BAB_06/BAB_06.txt', 'w', encoding='utf-8') as f:
    f.write("#separator:tab\n")
    f.write("#html:true\n")
    f.write("#notetype column:1\n")
    f.write("#deck column:2\n")
    f.write("#tags column:5\n")

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

        back_html = f'''{CSS_ONELINE}<div class="jpcard"><div class="label">Yomikata</div><div class="yomi">{item['kana']}</div><div class="arti">{item['arti']}</div><div class="kalimat"><div class="label">Contoh Kalimat</div><div class="jp">{item['jp']}</div><div class="id">{item['id']}</div></div>{analisis_box_html}{cocoklogi_html}</div>'''

        # Remove any newlines just in case
        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        tag = "KataKerja"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Generated BAB_06/BAB_06.txt")
