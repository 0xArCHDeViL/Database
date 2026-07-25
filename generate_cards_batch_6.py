import csv

data = [
    {
        "kana": "なんじ？",
        "kanji": "何時？",
        "arti": "Jam berapa?",
        "grup": "ALAT ELEKTRONIK & MESIN",
        "jp": "今は何時ですか。",
        "id": "Sekarang jam berapa?",
        "kanji_list": [
            {
                "char": "何",
                "kun": "なに",
                "on": "カ",
                "makna": "Apa. Radikal 亻 (orang) dan 可 (bisa). Seseorang yang bertanya 'Apa yang bisa saya lakukan?'"
            },
            {
                "char": "時",
                "kun": "とき",
                "on": "ジ",
                "makna": "Waktu / Jam."
            }
        ],
        "cocoklogi": "Bertanya apa 何 waktu 時に saat ini, atau dengan kata lain, jam berapa sekarang?"
    },
    {
        "kana": "ボックス",
        "kanji": "",
        "arti": "Kotak",
        "grup": "FURNITUR & PERALATAN RUMAH",
        "jp": "ボックスに本を入れます。",
        "id": "Memasukkan buku ke dalam kotak.",
        "cocoklogi": "Bokkusu! (Berasal dari bahasa Inggris 'Box'). Kotak buat nyimpen barang biar rapi."
    },
    {
        "kana": "キャビネット",
        "kanji": "",
        "arti": "Lemari kabinet",
        "grup": "FURNITUR & PERALATAN RUMAH",
        "jp": "キャビネットに服をしまいます。",
        "id": "Menyimpan baju di lemari kabinet.",
        "cocoklogi": "Kyabinetto! (Berasal dari bahasa Inggris 'Cabinet'). Lemari tempat naruh dokumen atau baju."
    },
    {
        "kana": "ダンボール",
        "kanji": "段ボール",
        "arti": "Kardus",
        "grup": "FURNITUR & PERALATAN RUMAH",
        "jp": "ダンボールに荷物を入れます。",
        "id": "Memasukkan barang ke dalam kardus.",
        "kanji_list": [
            {
                "char": "段",
                "kun": "–",
                "on": "ダン",
                "makna": "Tingkat / Tangga. Radikal 殳 (tombak/memukul) dan 叚 (meminjam/langkah). Memukul dan melangkah naik."
            }
        ],
        "cocoklogi": "Kardus itu permukaannya kalau dilihat dari samping bentuknya bergelombang dan bertingkat-tingkat 段 seperti tangga kecil."
    },
    {
        "kana": "ひこうき",
        "kanji": "飛行機",
        "arti": "Pesawat",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "飛行機で国へ帰ります。",
        "id": "Pulang ke negara asal dengan pesawat.",
        "kanji_list": [
            {
                "char": "飛",
                "kun": "と.ぶ",
                "on": "ヒ",
                "makna": "Terbang. Gambar burung yang mengepakkan sayapnya ke atas."
            },
            {
                "char": "行",
                "kun": "い.く",
                "on": "コウ",
                "makna": "Pergi / Melakukan."
            },
            {
                "char": "機",
                "kun": "はた",
                "on": "キ",
                "makna": "Mesin. Radikal 木 (kayu) dan 幾 (berapa/kecil). Mesin tenun kayu yang kompleks dari zaman dulu."
            }
        ],
        "cocoklogi": "Sebuah mesin 機 besar bersayap yang bisa terbang 飛 untuk pergi 行 membelah awan melintasi benua, alias pesawat terbang 飛行機."
    },
    {
        "kana": "でんしゃ",
        "kanji": "電車",
        "arti": "Kereta",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "電車で学校へ行きます。",
        "id": "Pergi ke sekolah dengan kereta.",
        "kanji_list": [
            {
                "char": "電",
                "kun": "–",
                "on": "デン",
                "makna": "Listrik. Radikal 雨 (hujan) dan 申 (petir). Kilatan cahaya petir saat hujan."
            },
            {
                "char": "車",
                "kun": "くるま",
                "on": "シャ",
                "makna": "Mobil / Kendaraan beroda. Gambar gerobak beroda dua dilihat dari atas."
            }
        ],
        "cocoklogi": "Kendaraan panjang beroda 車 yang bergerak mengandalkan energi listrik 電 dan berjalan di atas rel, itulah kereta listrik 電車."
    },
    {
        "kana": "しんかんせん",
        "kanji": "新幹線",
        "arti": "Kereta cepat",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "新幹線は速いです。",
        "id": "Kereta cepat itu cepat.",
        "kanji_list": [
            {
                "char": "新",
                "kun": "あたら.しい",
                "on": "シン",
                "makna": "Baru. Radikal 斤 (kapak), 立 (berdiri), dan 木 (pohon). Memotong kayu pohon untuk membuat sesuatu yang baru."
            },
            {
                "char": "幹",
                "kun": "みき",
                "on": "カン",
                "makna": "Batang utama. Radikal 十 (sepuluh/pusat) dan 旱 (kering). Bagian utama atau pusat yang kuat."
            },
            {
                "char": "線",
                "kun": "–",
                "on": "セン",
                "makna": "Garis / Jalur. Radikal 糸 (benang) dan 泉 (mata air). Jalur panjang seperti aliran benang air."
            }
        ],
        "cocoklogi": "Jalur 線 utama 幹 yang dibangun dengan teknologi baru 新, yang menghubungkan kota-kota besar di Jepang super cepat, yaitu Shinkansen 新幹線."
    },
    {
        "kana": "バス",
        "kanji": "",
        "arti": "Bus",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "バスで会社へ行きます。",
        "id": "Pergi ke kantor dengan bus.",
        "cocoklogi": "Basu! Kendaraan umum panjang yang sering penuh di pagi hari."
    },
    {
        "kana": "モノレール",
        "kanji": "",
        "arti": "Monorel",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "モノレールで空港へ行きます。",
        "id": "Pergi ke bandara dengan monorel.",
        "cocoklogi": "Monoreeru! Kereta yang jalurnya cuma satu rel di atas, kayak di taman hiburan."
    },
    {
        "kana": "タクシー",
        "kanji": "",
        "arti": "Taksi",
        "grup": "KENDARAAN & TRANSPORTASI",
        "jp": "タクシーで帰ります。",
        "id": "Pulang dengan taksi.",
        "cocoklogi": "Takushii! Kendaraan sewaan yang pintunya suka kebuka otomatis di Jepang."
    },
    {
        "kana": "コンサート",
        "kanji": "",
        "arti": "Konser",
        "grup": "HIBURAN, HOBI & OLAHRAGA",
        "jp": "明日、コンサートに行きます。",
        "id": "Besok, pergi ke konser.",
        "cocoklogi": "Konsaato! Ajang teriak-teriak sambil bawa lighstick dukung idola."
    },
    {
        "kana": "かんげいかい",
        "kanji": "歓迎会",
        "arti": "Acara penyambutan",
        "grup": "ACARA & PERAYAAN",
        "jp": "今日、歓迎会があります。",
        "id": "Hari ini, ada acara penyambutan.",
        "kanji_list": [
            {
                "char": "歓",
                "kun": "よろこ.ぶ",
                "on": "カン",
                "makna": "Gembira. Radikal 欠 (menguap/membuka mulut) dan 雚 (burung bangau/banyak). Orang-orang yang bersorak gembira."
            },
            {
                "char": "迎",
                "kun": "むか.える",
                "on": "ゲイ",
                "makna": "Menyambut. Radikal 辶 (jalan) dan 卬 (menengadah). Berjalan keluar untuk menjemput tamu."
            },
            {
                "char": "会",
                "kun": "あ.う",
                "on": "カイ",
                "makna": "Berkumpul / Bertemu."
            }
        ],
        "cocoklogi": "Pesta perkumpulan 会 di mana kita menyambut 迎 anggota baru dengan penuh rasa gembira 歓, alias acara penyambutan 歓迎会!"
    },
    {
        "kana": "そうべつかい",
        "kanji": "送別会",
        "arti": "Acara perpisahan",
        "grup": "ACARA & PERAYAAN",
        "jp": "明日、送別会に行きます。",
        "id": "Besok, pergi ke acara perpisahan.",
        "kanji_list": [
            {
                "char": "送",
                "kun": "おく.る",
                "on": "ソウ",
                "makna": "Mengirim. Radikal 辶 (jalan) dan 关 (tangan). Mengantar atau mengirimkan sesuatu di jalan."
            },
            {
                "char": "別",
                "kun": "わか.れる",
                "on": "ベツ",
                "makna": "Berpisah / Membagi. Radikal 刂 (pisau/pedang) dan 另 (tulang). Memotong dan memisahkan tulang."
            },
            {
                "char": "会",
                "kun": "あ.う",
                "on": "カイ",
                "makna": "Berkumpul / Bertemu."
            }
        ],
        "cocoklogi": "Acara kumpul-kumpul 会 untuk mengantar 送 atau mengirim seseorang yang akan berpisah 別 jauh, yaitu pesta perpisahan 送別会."
    },
    {
        "kana": "ぼうねんかい",
        "kanji": "忘年会",
        "arti": "Acara akhir tahun",
        "grup": "ACARA & PERAYAAN",
        "jp": "来週、忘年会があります。",
        "id": "Minggu depan, ada acara akhir tahun.",
        "kanji_list": [
            {
                "char": "忘",
                "kun": "わす.れる",
                "on": "ボウ",
                "makna": "Melupakan. Radikal 心 (hati/pikiran) dan 亡 (hilang/mati). Sesuatu yang hilang dari pikiran."
            },
            {
                "char": "年",
                "kun": "とし",
                "on": "ネン",
                "makna": "Tahun."
            },
            {
                "char": "会",
                "kun": "あ.う",
                "on": "カイ",
                "makna": "Berkumpul / Bertemu."
            }
        ],
        "cocoklogi": "Pesta perkumpulan 会 untuk bersenang-senang dan melupakan 忘 semua kesedihan serta penat selama satu tahun 年 ke belakang (Bounenkai)."
    },
    {
        "kana": "はなみ",
        "kanji": "花見",
        "arti": "Hanami (melihat bunga sakura)",
        "grup": "ACARA & PERAYAAN",
        "jp": "春に花見に行きます。",
        "id": "Di musim semi pergi melihat bunga sakura.",
        "kanji_list": [
            {
                "char": "花",
                "kun": "はな",
                "on": "カ",
                "makna": "Bunga. Radikal 艹 (rumput) dan 化 (berubah)."
            },
            {
                "char": "見",
                "kun": "み.る",
                "on": "ケン",
                "makna": "Melihat. Gambar mata yang besar di atas kaki."
            }
        ],
        "cocoklogi": "Acara kumpul-kumpul di bawah pohon pada musim semi khusus untuk sekadar melihat-lihat 見 indahnya bunga 花 sakura yang berguguran."
    },
    {
        "kana": "いっぷん",
        "kanji": "１分",
        "arti": "1 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "１分で終わります。",
        "id": "Selesai dalam 1 menit.",
        "kanji_list": [
            {
                "char": "１",
                "kun": "–",
                "on": "いち",
                "makna": "Satu."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi. Radikal 刀 (pisau) dan 八 (membelah dua). Memotong jam menjadi bagian-bagian menit."
            }
        ],
        "cocoklogi": "Satu bagian pecahan kecil dari jam adalah satu menit １分. (Hati-hati bacanya ippun, bukan ichifun)."
    },
    {
        "kana": "にふん",
        "kanji": "２分",
        "arti": "2 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "２分、待ちます。",
        "id": "Menunggu 2 menit.",
        "kanji_list": [
            {
                "char": "２",
                "kun": "–",
                "on": "に",
                "makna": "Dua."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Angka dua yang dipasangkan dengan kanji menit, dibaca normal jadi ni-fun ２分."
    },
    {
        "kana": "さんぷん",
        "kanji": "３分",
        "arti": "3 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "３分でラーメンができます。",
        "id": "Ramennya selesai dalam 3 menit.",
        "kanji_list": [
            {
                "char": "３",
                "kun": "–",
                "on": "さん",
                "makna": "Tiga."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Waktu emas buat seduh cup ramen, tiga menit ３分. (Bacanya berubah jadi san-pun)."
    },
    {
        "kana": "よんぷん",
        "kanji": "４分",
        "arti": "4 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "あと４分です。",
        "id": "Tinggal 4 menit lagi.",
        "kanji_list": [
            {
                "char": "４",
                "kun": "–",
                "on": "よん",
                "makna": "Empat."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Angka empat untuk hitungan menit, bacanya yon-pun ４分 ya, bukan shi-fun."
    },
    {
        "kana": "ごふん",
        "kanji": "５分",
        "arti": "5 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "５分、休みます。",
        "id": "Istirahat 5 menit.",
        "kanji_list": [
            {
                "char": "５",
                "kun": "–",
                "on": "ご",
                "makna": "Lima."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Angka ganjil lima ketemu menit, suaranya tetap ringan, go-fun ５分."
    },
    {
        "kana": "ろっぷん",
        "kanji": "６分",
        "arti": "6 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "６分、かかります。",
        "id": "Makan waktu 6 menit.",
        "kanji_list": [
            {
                "char": "６",
                "kun": "–",
                "on": "ろく",
                "makna": "Enam."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Angka genap enam, bacaannya jadi kenceng bertekanan, roppun ６分."
    },
    {
        "kana": "ななふん",
        "kanji": "７分",
        "arti": "7 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "７分で着きます。",
        "id": "Tiba dalam 7 menit.",
        "kanji_list": [
            {
                "char": "７",
                "kun": "–",
                "on": "なな",
                "makna": "Tujuh."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Tujuh dipasangkan sama menit, dibaca pelan dan santai nana-fun ７分."
    },
    {
        "kana": "はっぷん",
        "kanji": "８分",
        "arti": "8 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "８分、待ちました。",
        "id": "Telah menunggu 8 menit.",
        "kanji_list": [
            {
                "char": "８",
                "kun": "–",
                "on": "はち",
                "makna": "Delapan."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Delapan itu angkanya memantul, bacaannya juga kencang jadi happun ８分."
    },
    {
        "kana": "きゅうふん",
        "kanji": "９分",
        "arti": "9 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "あと９分です。",
        "id": "Tinggal 9 menit lagi.",
        "kanji_list": [
            {
                "char": "９",
                "kun": "–",
                "on": "きゅう",
                "makna": "Sembilan."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Sembilan ketemu menit, suaranya tetap biasa, kyuu-fun ９分."
    },
    {
        "kana": "じゅっぷん",
        "kanji": "１０分",
        "arti": "10 menit",
        "grup": "WAKTU (JAM, MENIT, DETIK)",
        "jp": "１０分、休みましょう。",
        "id": "Mari istirahat 10 menit.",
        "kanji_list": [
            {
                "char": "１０",
                "kun": "–",
                "on": "じゅう",
                "makna": "Sepuluh."
            },
            {
                "char": "分",
                "kun": "わ.ける",
                "on": "フン / プン",
                "makna": "Menit / Membagi."
            }
        ],
        "cocoklogi": "Sepuluh adalah angka pas dan padat, bacanya jadi kenceng juppun １０分 atau jippun."
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

        tag = "Waktu" if "WAKTU" in item['grup'] else "Kendaraan" if "KENDARAAN" in item['grup'] else "Lainnya"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Appended 25 cards to BAB_06/BAB_06.txt")
