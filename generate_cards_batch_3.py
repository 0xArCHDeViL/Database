import csv

data = [
    {
        "kana": "ジョギングします",
        "kanji": "",
        "arti": "Jogging",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "朝、公園でジョギングします。",
        "id": "Pagi hari, jogging di taman.",
        "cocoklogi": "Jogingu! (Berasal dari kata serapan bahasa Inggris 'jogging')."
    },
    {
        "kana": "スポーツします",
        "kanji": "",
        "arti": "Berolahraga",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "日曜日、スポーツします。",
        "id": "Hari Minggu, berolahraga.",
        "cocoklogi": "Supootsu! (Berasal dari kata serapan bahasa Inggris 'sports')."
    },
    {
        "kana": "しょくじ",
        "kanji": "食事",
        "arti": "Makan",
        "grup": "KATA BENDA VERBAL (SURU-MEISHI)",
        "jp": "レストランで食事をしました。",
        "id": "Telah makan di restoran.",
        "kanji_list": [
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan. Menggambarkan wadah makanan tertutup."
            },
            {
                "char": "事",
                "kun": "こと",
                "on": "ジ",
                "makna": "Urusan. Pekerjaan atau aktivitas yang dilakukan."
            }
        ],
        "cocoklogi": "Urusan 事 mengisi perut dengan cara makan 食, inilah kegiatan makan 食事 yang mengenyangkan."
    },
    {
        "kana": "しょくどう",
        "kanji": "食堂",
        "arti": "Kantin",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "食堂で昼ごはんを食べます。",
        "id": "Makan siang di kantin.",
        "kanji_list": [
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan / Makanan."
            },
            {
                "char": "堂",
                "kun": "–",
                "on": "ドウ",
                "makna": "Aula / Ruang besar. Radikal 土 (tanah/lantai). Bangunan besar yang lantainya ditinggikan."
            }
        ],
        "cocoklogi": "Sebuah aula besar 堂 yang dipenuhi meja dan kursi khusus untuk makan 食 bersama, itulah ruang makan atau kantin 食堂."
    },
    {
        "kana": "はたけ",
        "kanji": "畑",
        "arti": "Sawah / ladang",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "父は畑で働きます。",
        "id": "Ayah bekerja di ladang.",
        "kanji_list": [
            {
                "char": "畑",
                "kun": "はたけ",
                "on": "–",
                "makna": "Ladang. Kokuji (kanji buatan Jepang). Radikal 火 (api) dan 田 (sawah/lahan). Membakar semak-semak untuk membuka lahan pertanian kering."
            }
        ],
        "cocoklogi": "Petani membakar rumput liar dengan api 火 di sebidang tanah 田 untuk menciptakan ladang 畑 tempat bercocok tanam yang subur."
    },
    {
        "kana": "みせ",
        "kanji": "店",
        "arti": "Toko",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "この店でかばんを買いました。",
        "id": "Membeli tas di toko ini.",
        "kanji_list": [
            {
                "char": "店",
                "kun": "みせ",
                "on": "テン",
                "makna": "Toko. Radikal 广 (bangunan terbuka/kanopi) dan 占 (meramal/menempati). Bangunan tempat memajang barang untuk memikat pengunjung."
            }
        ],
        "cocoklogi": "Menempati 占 sebuah bangunan berkanopi 广 untuk memajang dan menjual barang-barang, itulah wujud sebuah toko 店."
    },
    {
        "kana": "たんぼ",
        "kanji": "田んぼ",
        "arti": "Sawah",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "田んぼで米を植えます。",
        "id": "Menanam padi di sawah.",
        "kanji_list": [
            {
                "char": "田",
                "kun": "た",
                "on": "デン",
                "makna": "Sawah. Gambar petak-petak sawah yang dialiri air."
            }
        ],
        "cocoklogi": "Petak-petak tanah kotak yang berjejer rapi ini melambangkan sebidang sawah 田 tempat padi tumbuh merunduk."
    },
    {
        "kana": "〜や",
        "kanji": "〜屋",
        "arti": "Kedai~",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "パン屋でパンを買います。",
        "id": "Membeli roti di toko roti.",
        "kanji_list": [
            {
                "char": "屋",
                "kun": "や",
                "on": "オク",
                "makna": "Toko / Atap / Pekerjaan. Radikal 尸 (atap/badan) dan 至 (tiba). Tempat (di bawah atap) orang berkumpul/tiba untuk melakukan transaksi."
            }
        ],
        "cocoklogi": "Tempat orang-orang tiba 至 dan bernaung di bawah satu atap 尸 khusus untuk berbelanja, itulah sebuah kedai/toko 屋."
    },
    {
        "kana": "いざかや",
        "kanji": "居酒屋",
        "arti": "Bar",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "居酒屋でビールを飲みます。",
        "id": "Minum bir di bar.",
        "kanji_list": [
            {
                "char": "居",
                "kun": "い.る",
                "on": "キョ",
                "makna": "Berada / Tinggal. Radikal 尸 (tubuh/atap) dan 古 (lama). Tubuh yang berdiam lama di satu tempat."
            },
            {
                "char": "酒",
                "kun": "さけ",
                "on": "シュ",
                "makna": "Sake / Alkohol. Radikal 氵 (air) dan 酉 (guci arak)."
            },
            {
                "char": "屋",
                "kun": "や",
                "on": "オク",
                "makna": "Toko / Kedai."
            }
        ],
        "cocoklogi": "Sebuah kedai 屋 tempat orang-orang bisa betah berada 居 di sana berlama-lama sambil menikmati minuman keras 酒, itulah bar tradisional 居酒屋."
    },
    {
        "kana": "たいしかん",
        "kanji": "大使館",
        "arti": "Kantor kedutaan",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "明日、大使館へ行きます。",
        "id": "Besok, pergi ke kantor kedutaan.",
        "kanji_list": [
            {
                "char": "大",
                "kun": "おお.きい",
                "on": "タイ",
                "makna": "Besar. Gambar orang yang merentangkan tangan dan kakinya besar-besar."
            },
            {
                "char": "使",
                "kun": "つか.う",
                "on": "シ",
                "makna": "Utusan / Menggunakan. Radikal 亻 (orang) dan 吏 (pejabat)."
            },
            {
                "char": "館",
                "kun": "–",
                "on": "カン",
                "makna": "Gedung besar. Radikal 食 (makanan) dan 官 (pejabat). Gedung tempat pejabat diberi makan dan diinapkan."
            }
        ],
        "cocoklogi": "Sebuah gedung resmi 館 untuk tempat tinggal utusan 使 negara tingkat tinggi yang sangat besar 大 pangkatnya, alias Kedutaan Besar 大使館."
    },
    {
        "kana": "カフェ",
        "kanji": "",
        "arti": "Kafe",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "カフェでコーヒーを飲みます。",
        "id": "Minum kopi di kafe.",
        "cocoklogi": "Kafe! Tempat asyik buat nongkrong sambil minum kopi hangat."
    },
    {
        "kana": "デパート",
        "kanji": "",
        "arti": "Pasar raya",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "デパートで服を買います。",
        "id": "Membeli pakaian di pasar raya.",
        "cocoklogi": "Depaato! (Berasal dari Department Store). Tempat belanja besar dengan banyak departemen."
    },
    {
        "kana": "コンビニ",
        "kanji": "",
        "arti": "Minimarket",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "コンビニでおにぎりを買います。",
        "id": "Membeli onigiri di minimarket.",
        "cocoklogi": "Konbini! (Singkatan dari Convenience Store). Toko serba ada yang selalu buka dan gampang dicari."
    },
    {
        "kana": "レストラン",
        "kanji": "",
        "arti": "Restoran",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "レストランで夕食を食べます。",
        "id": "Makan malam di restoran.",
        "cocoklogi": "Resutoran! (Berasal dari kata Restaurant). Tempat makan enak yang ada pelayannya."
    },
    {
        "kana": "スーパー",
        "kanji": "",
        "arti": "Supermarket",
        "grup": "TEMPAT, BANGUNAN & FASILITAS",
        "jp": "スーパーで野菜を買います。",
        "id": "Membeli sayuran di supermarket.",
        "cocoklogi": "Suupaa! (Singkatan dari Supermarket). Tempat luas buat belanja kebutuhan dapur dan rumah tangga."
    },
    {
        "kana": "いか",
        "kanji": "烏賊",
        "arti": "Cumi-cumi",
        "grup": "MAKANAN (DAGING & SEAFOOD)",
        "jp": "いかのすしを食べます。",
        "id": "Makan sushi cumi-cumi.",
        "kanji_list": [
            {
                "char": "烏",
                "kun": "からす",
                "on": "ウ",
                "makna": "Burung gagak. Gambar burung gagak (hitam sehingga matanya tak terlihat, beda dengan 鳥)."
            },
            {
                "char": "賊",
                "kun": "–",
                "on": "ゾク",
                "makna": "Pencuri / Bandit. Radikal 貝 (harta) dan 戎 (senjata). Merampas harta dengan senjata."
            }
        ],
        "cocoklogi": "Dulu orang Cina melihat cumi-cumi menyemburkan tinta hitam seperti gagak 烏 dan suka menyerang diam-diam seperti bandit 賊 air."
    },
    {
        "kana": "うなぎ",
        "kanji": "鰻",
        "arti": "Belut",
        "grup": "MAKANAN (DAGING & SEAFOOD)",
        "jp": "うなぎはおいしいです。",
        "id": "Belut itu enak.",
        "kanji_list": [
            {
                "char": "鰻",
                "kun": "うなぎ",
                "on": "マン",
                "makna": "Belut. Radikal 魚 (ikan) dan 曼 (panjang). Ikan yang badannya panjang membentang."
            }
        ],
        "cocoklogi": "Seekor ikan 魚 yang badannya membentang sangat panjang 曼 menyerupai ular, itulah wujud dari belut 鰻."
    },
    {
        "kana": "たこ",
        "kanji": "蛸",
        "arti": "Gurita",
        "grup": "MAKANAN (DAGING & SEAFOOD)",
        "jp": "たこのすしを食べました。",
        "id": "Telah makan sushi gurita.",
        "kanji_list": [
            {
                "char": "蛸",
                "kun": "たこ",
                "on": "ショウ",
                "makna": "Gurita / Laba-laba. Radikal 虫 (serangga/hewan kecil) dan 肖 (menyerupai/kecil)."
            }
        ],
        "cocoklogi": "Hewan aneh mirip serangga 虫 yang melata dan menyerupai 肖 laba-laba karena kaki-kakinya yang banyak, itulah si gurita 蛸."
    },
    {
        "kana": "かに",
        "kanji": "蟹",
        "arti": "Kepiting",
        "grup": "MAKANAN (DAGING & SEAFOOD)",
        "jp": "蟹はおいしいです。",
        "id": "Kepiting itu enak.",
        "kanji_list": [
            {
                "char": "蟹",
                "kun": "かに",
                "on": "カイ",
                "makna": "Kepiting. Radikal 虫 (serangga/hewan bercangkang) dan 解 (mengurai/memotong). Hewan bercangkang dengan capit yang bisa memotong."
            }
        ],
        "cocoklogi": "Hewan bercangkang atau sebangsa serangga air 虫 yang punya capit tajam seperti pisau untuk memotong 解 mangsanya, itulah kepiting 蟹."
    },
    {
        "kana": "えび",
        "kanji": "蝦",
        "arti": "Udang",
        "grup": "MAKANAN (DAGING & SEAFOOD)",
        "jp": "えびを食べます。",
        "id": "Makan udang.",
        "kanji_list": [
            {
                "char": "蝦",
                "kun": "えび",
                "on": "カ",
                "makna": "Udang. Radikal 虫 (hewan) dan 叚 (kulit/lapisan). Hewan air yang dilapisi cangkang keras."
            }
        ],
        "cocoklogi": "Hewan air mirip serangga 虫 yang badannya dilapisi 叚 oleh cangkang pelindung, alias si udang 蝦."
    },
    {
        "kana": "らっかせい",
        "kanji": "落花生",
        "arti": "Kacang tanah",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "落花生を食べます。",
        "id": "Makan kacang tanah.",
        "kanji_list": [
            {
                "char": "落",
                "kun": "お.ちる",
                "on": "ラク",
                "makna": "Jatuh. Radikal 艹 (rumput) dan 洛 (jatuh air)."
            },
            {
                "char": "花",
                "kun": "はな",
                "on": "カ",
                "makna": "Bunga. Radikal 艹 (tanaman) dan 化 (berubah)."
            },
            {
                "char": "生",
                "kun": "い.きる",
                "on": "セイ",
                "makna": "Hidup / Tumbuh. Tunas yang tumbuh dari tanah."
            }
        ],
        "cocoklogi": "Bunga 花 kacang yang jatuh 落 ke dalam tanah dan tumbuh 生 menjadi biji di bawah permukaan bumi, itulah kacang tanah 落花生."
    },
    {
        "kana": "ぶどう",
        "kanji": "葡萄",
        "arti": "Anggur",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "葡萄はおいしいです。",
        "id": "Anggur itu enak.",
        "kanji_list": [
            {
                "char": "葡",
                "kun": "–",
                "on": "ブ",
                "makna": "Anggur. Radikal 艹 (tanaman) dan 匍 (merambat)."
            },
            {
                "char": "萄",
                "kun": "–",
                "on": "ドウ",
                "makna": "Anggur. Radikal 艹 (tanaman) dan 匋 (wadah)."
            }
        ],
        "cocoklogi": "Tanaman 艹 yang merambat 匍 di rambatan, menghasilkan buah bergerombol seperti isi wadah 匋, jadilah anggur 葡萄."
    },
    {
        "kana": "かき",
        "kanji": "柿",
        "arti": "Kesemek",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "柿を買います。",
        "id": "Membeli kesemek.",
        "kanji_list": [
            {
                "char": "柿",
                "kun": "かき",
                "on": "シ",
                "makna": "Kesemek. Radikal 木 (pohon) dan 市 (pasar). Pohon yang buahnya sering dijual di pasar sejak zaman dulu."
            }
        ],
        "cocoklogi": "Pohon 木 yang buah oren manisnya selalu laris manis dijual di pasar 市 tradisional, itulah pohon kesemek 柿."
    },
    {
        "kana": "いちご",
        "kanji": "苺",
        "arti": "Stroberi",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "苺はおいしいです。",
        "id": "Stroberi itu enak.",
        "kanji_list": [
            {
                "char": "苺",
                "kun": "いちご",
                "on": "バイ",
                "makna": "Stroberi. Radikal 艹 (tanaman) dan 母 (ibu). Tanaman yang beranak pinak dengan cepat seperti ibu yang melahirkan."
            }
        ],
        "cocoklogi": "Tanaman 艹 kecil merambat yang cepat berkembang biak layaknya seorang ibu 母 yang subur, menghasilkan stroberi 苺 yang manis."
    },
    {
        "kana": "りんご",
        "kanji": "林檎",
        "arti": "Apel",
        "grup": "MAKANAN (SAYURAN, BUMBU & BUAH)",
        "jp": "林檎を買います。",
        "id": "Membeli apel.",
        "kanji_list": [
            {
                "char": "林",
                "kun": "はやし",
                "on": "リン",
                "makna": "Hutan / Kebun. Dua pohon kayu yang berjejer."
            },
            {
                "char": "檎",
                "kun": "–",
                "on": "ゴ",
                "makna": "Apel liar. Radikal 木 (pohon) dan 禽 (burung). Pohon yang buahnya mengundang banyak burung."
            }
        ],
        "cocoklogi": "Di tengah kebun 林, ada pohon kayu manis yang buahnya selalu dipatuk burung 禽 karena saking lezatnya, dialah buah apel 林檎."
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

        # Omit Yomikata block if no kanji (kana-only word)
        yomikata_block = ""
        if item['kanji']:
            yomikata_block = f'''<div class="label">Yomikata</div><div class="yomi">{item['kana']}</div>'''

        back_html = f'''{CSS_ONELINE}<div class="jpcard">{yomikata_block}<div class="arti">{item['arti']}</div><div class="kalimat"><div class="label">Contoh Kalimat</div><div class="jp">{item['jp']}</div><div class="id">{item['id']}</div></div>{analisis_box_html}{cocoklogi_html}</div>'''

        # Remove any newlines just in case
        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        tag = "KataKerja" if "KATA KERJA" in item['grup'] else "Membeli" if "TEMPAT" in item['grup'] else "Makanan"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Appended 25 cards to BAB_06/BAB_06.txt")
