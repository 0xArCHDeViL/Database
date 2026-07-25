import csv

data = [
    {
        "kana": "はじまります",
        "kanji": "始まります",
        "arti": "Mulai",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "九時にクラスが始まります。",
        "id": "Kelas mulai pada jam sembilan.",
        "kanji_list": [
            {
                "char": "始",
                "kun": "はじ.まる",
                "on": "シ",
                "makna": "Mulai. Radikal 女 (perempuan) dan 台 (panggung/podium). Perempuan yang naik ke atas panggung untuk memulai sebuah pertunjukan."
            }
        ],
        "cocoklogi": "Bayangkan seorang perempuan 女 yang naik ke atas panggung 台, itu adalah tanda bahwa pertunjukan atau acara akan segera dimulai 始."
    },
    {
        "kana": "おわります",
        "kanji": "終ります",
        "arti": "Selesai",
        "grup": "KATA KERJA GOL. 1 (GODAN)",
        "jp": "十五時にクラスが終ります。",
        "id": "Kelas selesai pada jam 15.",
        "kanji_list": [
            {
                "char": "終",
                "kun": "お.わる",
                "on": "シュウ",
                "makna": "Selesai. Radikal 糸 (benang) dan 冬 (musim dingin). Seperti benang yang habis atau dipotong saat musim dingin yang merupakan akhir dari tahun."
            }
        ],
        "cocoklogi": "Sama seperti musim dingin 冬 yang menjadi penanda akhir tahun, sebuah gulungan benang 糸 yang habis berarti pekerjaannya sudah selesai 終."
    },
    {
        "kana": "うえます",
        "kanji": "植えます",
        "arti": "Menanam",
        "grup": "KATA KERJA GOL. 2 (ICHIDAN)",
        "jp": "庭で木を植えます。",
        "id": "Menanam pohon di halaman.",
        "kanji_list": [
            {
                "char": "植",
                "kun": "う.える",
                "on": "ショク",
                "makna": "Menanam. Radikal 木 (pohon) dan 直 (lurus/langsung). Menanam pohon agar tumbuh tegak lurus."
            }
        ],
        "cocoklogi": "Kegiatan menanam 植 adalah proses membesarkan pohon 木 dan memastikan batangnya tumbuh lurus 直 ke atas."
    },
    {
        "kana": "おきます",
        "kanji": "起きます",
        "arti": "Bangun tidur",
        "grup": "KATA KERJA GOL. 2 (ICHIDAN)",
        "jp": "毎朝、六時に起きます。",
        "id": "Setiap pagi, bangun jam 6.",
        "kanji_list": [
            {
                "char": "起",
                "kun": "お.きる",
                "on": "キ",
                "makna": "Bangun. Radikal 走 (berlari) dan 己 (diri sendiri). Mengangkat diri sendiri untuk berdiri atau berlari dari posisi berbaring."
            }
        ],
        "cocoklogi": "Memaksa diri sendiri 己 untuk segera berlari 走 dari tempat tidur, itulah perjuangan untuk bangun 起 di pagi hari!"
    },
    {
        "kana": "でかけます",
        "kanji": "出かけます",
        "arti": "Pergi keluar",
        "grup": "KATA KERJA GOL. 2 (ICHIDAN)",
        "jp": "明日、彼女と出かけます。",
        "id": "Besok, pergi keluar dengan pacar.",
        "kanji_list": [
            {
                "char": "出",
                "kun": "で.る",
                "on": "シュツ",
                "makna": "Keluar. Gambar tunas tanaman yang tumbuh keluar dari tanah."
            }
        ],
        "cocoklogi": "Seperti tunas tanaman yang akhirnya menembus dan keluar 出 dari dalam tanah untuk melihat dunia luar."
    },
    {
        "kana": "ねます",
        "kanji": "寝ます",
        "arti": "Tidur",
        "grup": "KATA KERJA GOL. 2 (ICHIDAN)",
        "jp": "夜、十時ごろ寝ます。",
        "id": "Malam hari, tidur sekitar jam 10.",
        "kanji_list": [
            {
                "char": "寝",
                "kun": "ね.る",
                "on": "シン",
                "makna": "Tidur. Radikal 宀 (atap), 爿 (tempat tidur), dan 浸 (menyapu/tenggelam). Berada di bawah atap dan tenggelam di tempat tidur."
            }
        ],
        "cocoklogi": "Berada di bawah atap 宀 rumah yang nyaman, lalu merebahkan diri di tempat tidur 爿, bersiap untuk tenggelam dalam lelapnya tidur 寝."
    },
    {
        "kana": "きます",
        "kanji": "来ます",
        "arti": "Datang",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "兄は明日、来ます。",
        "id": "Kakak laki-laki besok datang.",
        "kanji_list": [
            {
                "char": "来",
                "kun": "く.る",
                "on": "ライ",
                "makna": "Datang. Gambar tanaman gandum (麦). Gandum datang/dibawa dari luar ke Tiongkok pada zaman dulu."
            }
        ],
        "cocoklogi": "Bentuknya mirip tanaman gandum yang dulu didatangkan 来 atau dibawa dari negeri jauh ke tempat kita."
    },
    {
        "kana": "あんないします",
        "kanji": "案内します",
        "arti": "Memandu",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "学校を案内します。",
        "id": "Saya memandu (berkeliling) sekolah.",
        "kanji_list": [
            {
                "char": "案",
                "kun": "–",
                "on": "アン",
                "makna": "Rencana / Ide. Radikal 木 (pohon/meja) dan 安 (aman). Rencana atau ide yang didiskusikan di atas meja agar aman/lancar."
            },
            {
                "char": "内",
                "kun": "うち",
                "on": "ナイ",
                "makna": "Dalam. Radikal 冂 (batas) dan 人 (orang). Seseorang yang berada di dalam suatu batas atau area."
            }
        ],
        "cocoklogi": "Membuat rencana 案 yang matang untuk membawa seseorang masuk ke dalam 内 suatu tempat, itulah tugas utama saat memandu 案内 seseorang!"
    },
    {
        "kana": "うんどうします",
        "kanji": "運動します",
        "arti": "Olah raga",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "公園で運動します。",
        "id": "Berolah raga di taman.",
        "kanji_list": [
            {
                "char": "運",
                "kun": "はこ.ぶ",
                "on": "ウン",
                "makna": "Membawa / Bergerak. Radikal 辶 (jalan) dan 軍 (tentara). Pasukan tentara yang berbaris/bergerak maju di jalan."
            },
            {
                "char": "動",
                "kun": "うご.く",
                "on": "ドウ",
                "makna": "Bergerak. Radikal 重 (berat) dan 力 (tenaga/kekuatan). Menggunakan kekuatan untuk memindahkan benda berat."
            }
        ],
        "cocoklogi": "Membawa 運 diri sendiri untuk terus bergerak 動 dan menggunakan tenaga, itulah hakikat dari olahraga 運動!"
    },
    {
        "kana": "ねぼうします",
        "kanji": "寝坊します",
        "arti": "Bangun siang",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "今日、寝坊しました。",
        "id": "Hari ini, saya bangun siang.",
        "kanji_list": [
            {
                "char": "寝",
                "kun": "ね.る",
                "on": "シン",
                "makna": "Tidur. Radikal 宀 (atap), 爿 (tempat tidur). Berbaring di tempat tidur di bawah atap."
            },
            {
                "char": "坊",
                "kun": "–",
                "on": "ボウ",
                "makna": "Anak laki-laki / Biksu. Radikal 土 (tanah) dan 方 (arah). Tempat/area tempat tinggal biksu atau sebutan untuk anak."
            }
        ],
        "cocoklogi": "Tidur 寝 terus-menerus seperti anak kecil 坊 yang belum punya banyak tanggung jawab, akhirnya jadi bangun kesiangan 寝坊."
    },
    {
        "kana": "べんきょうします",
        "kanji": "勉強します",
        "arti": "Belajar",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "図書館で日本語を勉強します。",
        "id": "Belajar bahasa Jepang di perpustakaan.",
        "kanji_list": [
            {
                "char": "勉",
                "kun": "つと.める",
                "on": "ベン",
                "makna": "Berusaha keras. Radikal 免 (menghindar) dan 力 (kekuatan). Menggunakan kekuatan keras untuk menghindari kegagalan."
            },
            {
                "char": "強",
                "kun": "つよ.い",
                "on": "キョウ",
                "makna": "Kuat. Radikal 弓 (busur) dan 虫 (serangga). Busur yang ditarik dengan kuat."
            }
        ],
        "cocoklogi": "Belajar adalah proses berusaha keras 勉 dengan seluruh tenaga agar otak kita menjadi kuat 強 dalam memahami ilmu pengetahuan 勉強."
    },
    {
        "kana": "えいぎょうします",
        "kanji": "営業します",
        "arti": "Beroperasi (bisnis)",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "あの店は九時から営業します。",
        "id": "Toko itu beroperasi dari jam 9.",
        "kanji_list": [
            {
                "char": "営",
                "kun": "いとな.む",
                "on": "エイ",
                "makna": "Mengelola / Membangun. Radikal ツ (atap) dan 呂 (tulang punggung/banyak ruangan). Membangun dan mengelola bangunan besar atau bisnis."
            },
            {
                "char": "業",
                "kun": "わざ",
                "on": "ギョウ",
                "makna": "Pekerjaan / Bisnis. Menggambarkan papan kayu atau instrumen musik yang menunjukkan keterampilan/pekerjaan."
            }
        ],
        "cocoklogi": "Mengelola 営 suatu bisnis atau pekerjaan 業 secara profesional agar terus berjalan, itulah kegiatan operasional bisnis 営業."
    },
    {
        "kana": "さぎょうします",
        "kanji": "作業します",
        "arti": "Bekerja (Tugas fisik / praktis)",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "工場で作業します。",
        "id": "Mengerjakan tugas di pabrik.",
        "kanji_list": [
            {
                "char": "作",
                "kun": "つく.る",
                "on": "サク",
                "makna": "Membuat / Pekerjaan. Radikal 亻 (orang) dan 乍 (membuat). Orang yang sedang membuat atau memproduksi sesuatu."
            },
            {
                "char": "業",
                "kun": "わざ",
                "on": "ギョウ",
                "makna": "Pekerjaan / Bisnis. Keterampilan atau usaha yang dilakukan."
            }
        ],
        "cocoklogi": "Membuat 作 atau memproduksi sesuatu sebagai bagian dari tugas dan pekerjaan 業, itulah yang dinamakan melakukan kerja fisik 作業."
    },
    {
        "kana": "ざんぎょうします",
        "kanji": "残業します",
        "arti": "Lembur",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "今日、会社で残業します。",
        "id": "Hari ini, lembur di perusahaan.",
        "kanji_list": [
            {
                "char": "残",
                "kun": "のこ.る",
                "on": "ザン",
                "makna": "Sisa / Tertinggal. Radikal 歹 (tulang/kematian) dan 戔 (tombak). Sisa tulang setelah pertempuran atau sisa-sisa sesuatu yang belum selesai."
            },
            {
                "char": "業",
                "kun": "わざ",
                "on": "ギョウ",
                "makna": "Pekerjaan / Bisnis. Tugas yang harus diselesaikan."
            }
        ],
        "cocoklogi": "Masih ada sisa 残 pekerjaan 業 yang belum selesai hari ini, makanya harus rela tertinggal di kantor untuk lembur 残業."
    },
    {
        "kana": "せんたくします",
        "kanji": "洗濯します",
        "arti": "Mencuci baju",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "朝、洗濯しました。",
        "id": "Pagi hari, saya mencuci baju.",
        "kanji_list": [
            {
                "char": "洗",
                "kun": "あら.う",
                "on": "セン",
                "makna": "Mencuci. Radikal 氵 (air) dan 先 (duluan)."
            },
            {
                "char": "濯",
                "kun": "すす.ぐ",
                "on": "タク",
                "makna": "Membilas. Radikal 氵 (air) dan 翟 (bulu burung). Membilas dan mengibas sayap/pakaian di air untuk membersihkannya."
            }
        ],
        "cocoklogi": "Mencuci 洗 menggunakan sabun dan air, lalu membilasnya 濯 berkali-kali sampai bersih mengkilat, itulah kegiatan mencuci baju 洗濯."
    },
    {
        "kana": "そうじします",
        "kanji": "掃除します",
        "arti": "Bersih-bersih",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "日曜日、部屋を掃除します。",
        "id": "Hari Minggu, saya membersihkan kamar.",
        "kanji_list": [
            {
                "char": "掃",
                "kun": "は.く",
                "on": "ソウ",
                "makna": "Menyapu. Radikal 扌 (tangan) dan 帚 (sapu). Tangan yang sedang memegang sapu untuk membersihkan debu."
            },
            {
                "char": "除",
                "kun": "のぞ.く",
                "on": "ジョ",
                "makna": "Menyingkirkan / Menghapus. Radikal 阝 (bukit/undakan) dan 余 (sisa/berlebih). Menyingkirkan kotoran atau sesuatu yang berlebih."
            }
        ],
        "cocoklogi": "Menyapu 掃 dengan sapu di tangan untuk menyingkirkan 除 semua kotoran dan debu, proses bersih-bersih 掃除 pun selesai dengan sempurna."
    },
    {
        "kana": "しょくじします",
        "kanji": "食事します",
        "arti": "Makan (sebagai kegiatan)",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "レストランで食事します。",
        "id": "Makan di restoran.",
        "kanji_list": [
            {
                "char": "食",
                "kun": "た.べる",
                "on": "ショク",
                "makna": "Makan / Makanan. Menggambarkan wadah makanan tertutup."
            },
            {
                "char": "事",
                "kun": "こと",
                "on": "ジ",
                "makna": "Hal / Urusan. Pekerjaan atau aktivitas yang dilakukan."
            }
        ],
        "cocoklogi": "Ini bukan sekadar mengunyah makanan 食, tapi makan adalah sebuah urusan 事 penting dan kegiatan sehari-hari yang dinamakan acara makan 食事."
    },
    {
        "kana": "しごとします",
        "kanji": "仕事します",
        "arti": "Bekerja",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "毎日、仕事をします。",
        "id": "Setiap hari, bekerja.",
        "kanji_list": [
            {
                "char": "仕",
                "kun": "つか.える",
                "on": "シ",
                "makna": "Melayani / Bekerja. Radikal 亻 (orang) dan 士 (sarjana/prajurit). Seseorang yang melayani atau bekerja secara profesional."
            },
            {
                "char": "事",
                "kun": "こと",
                "on": "ゴト",
                "makna": "Hal / Urusan. Pekerjaan atau aktivitas."
            }
        ],
        "cocoklogi": "Melayani 仕 dengan tenaga dan pikiran untuk menyelesaikan suatu urusan 事 penting, itulah definisi dari sebuah pekerjaan 仕事."
    },
    {
        "kana": "かいものします",
        "kanji": "買い物します",
        "arti": "Belanja",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "デパートで買い物をします。",
        "id": "Berbelanja di pasar raya.",
        "kanji_list": [
            {
                "char": "買",
                "kun": "か.う",
                "on": "バイ",
                "makna": "Membeli. Radikal 罒 (jaring/mengawasi) dan 貝 (kerang/uang)."
            },
            {
                "char": "物",
                "kun": "もの",
                "on": "ブツ",
                "makna": "Barang / Benda. Radikal 牛 (sapi) dan 勿 (bendera). Sapi atau benda berharga pada zaman dahulu."
            }
        ],
        "cocoklogi": "Pergi keluar untuk membeli 買 berbagai macam barang dan benda 物, aktivitas ini kita kenal dengan istilah berbelanja 買い物."
    },
    {
        "kana": "さんぽします",
        "kanji": "散歩します",
        "arti": "Jalan-jalan",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "朝、公園を散歩します。",
        "id": "Pagi hari, jalan-jalan di taman.",
        "kanji_list": [
            {
                "char": "散",
                "kun": "ち.る",
                "on": "サン",
                "makna": "Menyebar. Bertebaran atau berjalan-jalan santai tanpa arah yang pasti."
            },
            {
                "char": "歩",
                "kun": "ある.く",
                "on": "ポ",
                "makna": "Berjalan kaki. Radikal 止 (berhenti/jejak kaki). Menggambarkan jejak kaki yang melangkah bergantian."
            }
        ],
        "cocoklogi": "Melangkahkan kaki berjalan 歩 secara santai dan menyebar 散 ke berbagai tempat untuk menikmati udara segar, itulah esensi jalan-jalan 散歩."
    },
    {
        "kana": "りょうりします",
        "kanji": "料理します",
        "arti": "Memasak",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "母は台所で料理します。",
        "id": "Ibu memasak di dapur.",
        "kanji_list": [
            {
                "char": "料",
                "kun": "–",
                "on": "リョウ",
                "makna": "Bahan / Biaya. Radikal 米 (beras) dan 斗 (takar). Menakar beras sebagai bahan masakan."
            },
            {
                "char": "理",
                "kun": "–",
                "on": "リ",
                "makna": "Logika / Mengatur. Radikal 王 (permata) dan 里 (desa). Memotong permata sesuai alurnya secara logis."
            }
        ],
        "cocoklogi": "Mengambil bahan 料 makanan lalu mengatur 理 dan mengolahnya dengan logika rasa yang pas, jadilah kegiatan memasak 料理 yang lezat!"
    },
    {
        "kana": "ゆっくりします",
        "kanji": "",
        "arti": "Bersantai",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "休日は家でゆっくりします。",
        "id": "Hari libur saya bersantai di rumah.",
        "cocoklogi": "Yuk, Kuri! (Berasal dari bunyi yukkuri) Mari kita rebahan santai sambil menikmati hari tanpa beban!"
    },
    {
        "kana": "おいのりします",
        "kanji": "お祈りします",
        "arti": "Berdoa",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "夜、お祈りします。",
        "id": "Malam hari, berdoa.",
        "kanji_list": [
            {
                "char": "祈",
                "kun": "いの.る",
                "on": "キ",
                "makna": "Berdoa. Radikal 示 (altar/spiritual) dan 斤 (kapak/berat). Meminta perlindungan di altar."
            }
        ],
        "cocoklogi": "Berlutut di depan altar 示 untuk memanjatkan harapan suci dan berdoa 祈 agar hal buruk disingkirkan."
    },
    {
        "kana": "ごろごろします",
        "kanji": "",
        "arti": "Bermalas-malasan",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "日曜日、家でごろごろします。",
        "id": "Hari Minggu, bermalas-malasan di rumah.",
        "cocoklogi": "Bunyinya seperti suara roda besar bergulir lambat... Goro... goro... Mirip banget sama orang yang cuma guling-guling malas di kasur."
    },
    {
        "kana": "つりをします",
        "kanji": "釣りをします",
        "arti": "Memancing",
        "grup": "KATA KERJA GOL. 3 (FUKISOKU)",
        "jp": "海で釣りをします。",
        "id": "Memancing di laut.",
        "kanji_list": [
            {
                "char": "釣",
                "kun": "つ.る",
                "on": "チョウ",
                "makna": "Memancing. Radikal 金 (logam) dan 勺 (sendok/kait). Menggunakan kail logam untuk menangkap ikan."
            }
        ],
        "cocoklogi": "Menggunakan kail yang terbuat dari logam 金 lalu dilemparkan untuk memancing 釣 ikan di air yang jernih."
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

        back_html = f'''{CSS_ONELINE}<div class="jpcard"><div class="label">Yomikata</div><div class="yomi">{item['kana']}</div><div class="arti">{item['arti']}</div><div class="kalimat"><div class="label">Contoh Kalimat</div><div class="jp">{item['jp']}</div><div class="id">{item['id']}</div></div>{analisis_box_html}{cocoklogi_html}</div>'''

        # Remove any newlines just in case
        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        tag = "KataKerja"
        deck = f"Bab 6::{item['grup']}"

        line = f"Basic\t{deck}\t{front_html}\t{back_html}\t{tag}\n"
        f.write(line)

print("Appended 25 cards to BAB_06/BAB_06.txt")
