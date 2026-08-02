# -*- coding: utf-8 -*-
# Batch 5: Restored missing entries with premium quality
CARDS = [
    {
        'w': '頂く', 'y': 'いただく', 'a': 'Menerima (Sopan) / Makan (Sopan)', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': 'お土産を頂きました。', 'ei': 'Menerima oleh-oleh (sopan).',
        'ch': [('頂', 'いただ.く', 'チョウ', '[Radikal: 頁 (Kepala)] + [Komponen: 丁 (Paku/Ujung)] = Ujung paling atas kepala.')],
        'co': 'Menerima sesuatu dengan kedua tangan diangkat setinggi puncak kepala (頂) sebagai tanda penghormatan tertinggi. Versi ultra-sopan dari もらう. <b>Menerima / いただきます (sebelum makan)</b>.'
    },
    {
        'w': '申す', 'y': 'もうす', 'a': 'Berkata (Sangat Sopan / Kenjougo)', 'g': 1, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '田中と申します。', 'ei': 'Nama saya Tanaka (sangat sopan).',
        'ch': [('申', 'もう.す', 'シン', '[Radikal: 田 (Sawah)] + [Komponen: | (Garis vertikal menembus)] = Petir menembus sawah / Menyampaikan ke Dewa.')],
        'co': 'Secara kuno, ini simbol petir (kilat vertikal) menembus sawah. Manusia <b>menyampaikan kata-kata hina diri</b> ke orang yang lebih tinggi / Dewa. Kenjougo (merendahkan diri sendiri) dari 言う.'
    },
    {
        'w': '植える', 'y': 'うえる', 'a': 'Menanam', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '庭に花を植えます。', 'ei': 'Menanam bunga di halaman.',
        'ch': [('植', 'う.える', 'ショク', '[Radikal: 木 (Pohon)] + [Komponen: 直 (Lurus)] = Pohon yang ditanam tegak lurus.')],
        'co': 'Kamu menancapkan bibit pohon (木) ke dalam tanah secara tegak lurus (直). Memastikan batangnya tumbuh ke atas dengan benar. <b>Menanam tanaman/pohon</b>.'
    },
    {
        'w': '食事する', 'y': 'しょくじする', 'a': 'Makan (Formal)', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '家族と食事します。', 'ei': 'Makan bersama keluarga.',
        'ch': [
            ('食', 'た.べる', 'ショク', 'Makan (Orang duduk di depan nasi).'),
            ('事', 'こと', 'ジ', 'Hal/Urusan.')
        ],
        'co': 'Urusan (事) yang berhubungan dengan Makan (食). Lebih formal daripada 食べる yang kasual. <b>Santap / Makan formal</b> (contoh: di restoran mewah, jamuan resmi).'
    },
    {
        'w': '勉強する', 'y': 'べんきょうする', 'a': 'Belajar', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '毎日日本語を勉強します。', 'ei': 'Setiap hari belajar bahasa Jepang.',
        'ch': [
            ('勉', 'ベン', 'ベン', 'Berusaha keras (Melahirkan 免 + Tenaga 力).'),
            ('強', 'つよ.い', 'キョウ', 'Kuat (Serangga 虫 yang kuat bertahan hidup).')
        ],
        'co': 'Memaksakan diri dengan tenaga kuat (強) untuk berusaha keras (勉) memahami materi. <b>Belajar dengan tekun</b>. Kata paling fundamental di Jepang untuk aktivitas akademik.'
    },
    {
        'w': '仕事する', 'y': 'しごとする', 'a': 'Bekerja (Formal)', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '月曜日から金曜日まで仕事します。', 'ei': 'Bekerja dari Senin sampai Jumat.',
        'ch': [
            ('仕', 'つか.える', 'シ', 'Melayani (Orang 亻 + Samurai 士).'),
            ('事', 'こと', 'ジ', 'Hal/Urusan.')
        ],
        'co': 'Orang (亻) yang mengabdikan dirinya (仕) pada suatu Urusan (事). Lebih formal daripada 働く yang menekankan kerja fisik. <b>Bekerja (Nuansa kantoran/profesional)</b>.'
    },
    {
        'w': '買い物する', 'y': 'かいものする', 'a': 'Berbelanja', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'デパートで買い物します。', 'ei': 'Berbelanja di department store.',
        'ch': [
            ('買', 'か.う', 'バイ', 'Membeli (Jaring 罒 menangkap harta 貝).'),
            ('物', 'もの', 'ブツ', 'Benda/Barang.')
        ],
        'co': 'Membeli (買) Barang-barang (物) secara aktif. Bukan sekadar beli satu barang, tapi aktivitas jalan-jalan dan <b>Shopping / Berbelanja</b>.'
    },
    {
        'w': '運動する', 'y': 'うんどうする', 'a': 'Berolahraga', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '毎朝運動します。', 'ei': 'Berolahraga setiap pagi.',
        'ch': [
            ('運', 'はこ.ぶ', 'ウン', 'Mengangkut/Nasib (Kendaraan 車 bergerak di jalan 辶).'),
            ('動', 'うご.く', 'ドウ', 'Bergerak (Tenaga 力 yang berat 重).')
        ],
        'co': 'Menggerakkan (動) tubuh secara berulang dan teratur (運). <b>Olahraga / Exercise</b>.'
    },
    {
        'w': '案内する', 'y': 'あんないする', 'a': 'Memandu / Mengantar', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '観光客を案内します。', 'ei': 'Memandu turis.',
        'ch': [
            ('案', 'アン', 'アン', 'Rencana/Ide (Tangan di atas meja 木 memikirkan 安).'),
            ('内', 'うち', 'ナイ', 'Dalam/Interior.')
        ],
        'co': 'Merancang rute (案) lalu mengantar orang ke dalam (内) suatu tempat. <b>Memandu / Guide tour</b>.'
    },
    {
        'w': '洗濯する', 'y': 'せんたくする', 'a': 'Mencuci (Pakaian)', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '毎週末洗濯します。', 'ei': 'Mencuci pakaian setiap akhir pekan.',
        'ch': [
            ('洗', 'あら.う', 'セン', 'Mencuci (Air 氵 + Kaki 先 = cuci kaki).'),
            ('濯', 'すす.ぐ', 'タク', 'Membilas (Air 氵 berulang-ulang).')
        ],
        'co': 'Mencuci (洗) lalu membilas (濯) pakaian dengan air berkali-kali hingga bersih dari kotoran. <b>Mencuci baju / Laundry</b>.'
    },
    {
        'w': 'ジョギングする', 'y': 'じょぎんぐする', 'a': 'Jogging', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '公園でジョギングします。', 'ei': 'Jogging di taman.',
        'ch': [],
        'co': 'Kata serapan dari bahasa Inggris "Jogging". Berlari pelan-pelan santai untuk kesehatan, bukan lomba sprint. <b>Jogging / Lari santai</b>.'
    },
    {
        'w': '釣る', 'y': 'つる', 'a': 'Memancing', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '川で魚を釣ります。', 'ei': 'Memancing ikan di sungai.',
        'ch': [('釣', 'つ.る', 'チョウ', '[Radikal: 金 (Logam)] + [Komponen: 勺 (Sendok/Kail)] = Kail logam untuk menangkap ikan.')],
        'co': 'Menggunakan kait logam kecil (金 + 勺) yang dicelupkan ke air untuk menjebak ikan yang lapar. <b>Memancing ikan</b>.'
    },
    {
        'w': '浴びる', 'y': 'あびる', 'a': 'Mandi (Shower) / Berjemur', 'g': 2, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'シャワーを浴びます。', 'ei': 'Mandi shower.',
        'ch': [('浴', 'あ.びる', 'ヨク', '[Radikal: 氵 (Air)] + [Komponen: 谷 (Lembah)] = Air yang mengguyur dari atas lembah.')],
        'co': 'Air (氵) mengalir deras dari puncak lembah (谷) mengguyur tubuhmu dari kepala sampai kaki. <b>Mandi shower / Diguyur air / Berjemur sinar matahari</b>.'
    },
    {
        'w': '料理する', 'y': 'りょうりする', 'a': 'Memasak', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '夕飯を料理します。', 'ei': 'Memasak makan malam.',
        'ch': [
            ('料', 'リョウ', 'リョウ', 'Bahan/Takaran (Beras 米 + Sendok takar 斗).'),
            ('理', 'リ', 'リ', 'Logika/Mengatur (Raja 王 dari giok yang terukir rapi 里).')
        ],
        'co': 'Menakar bahan (料) lalu mengolahnya secara logis dan teratur (理) menjadi sajian lezat. <b>Memasak / Cooking</b>.'
    },
    {
        'w': '散歩する', 'y': 'さんぽする', 'a': 'Jalan-jalan / Berjalan santai', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '犬と散歩します。', 'ei': 'Jalan-jalan bersama anjing.',
        'ch': [
            ('散', 'ち.る', 'サン', 'Berhamburan/Menyebar (Daging 月 dipukul 攵 hingga pecah).'),
            ('歩', 'ある.く', 'ホ', 'Berjalan.')
        ],
        'co': 'Berjalan (歩) tanpa tujuan pasti, menyebar (散) ke mana-mana dengan santai. <b>Jalan-jalan santai / Stroll</b>.'
    },
    {
        'w': '掃除する', 'y': 'そうじする', 'a': 'Membersihkan / Bersih-bersih', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '部屋を掃除します。', 'ei': 'Membersihkan kamar.',
        'ch': [
            ('掃', 'は.く', 'ソウ', 'Menyapu (Tangan 扌 + Sapu 帚).'),
            ('除', 'のぞ.く', 'ジョ', 'Menghilangkan (Bukit 阝 + Langkah 余 = menyingkirkan rintangan).')
        ],
        'co': 'Menyapu (掃) debu dan kotoran lalu menyingkirkannya (除) supaya ruangan jadi bersih. <b>Bersih-bersih / Cleaning</b>.'
    },
    {
        'w': '休む', 'y': 'やすむ', 'a': 'Istirahat / Absen', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '少し休みましょう。', 'ei': 'Mari istirahat sebentar.',
        'ch': [('休', 'やす.む', 'キュウ', '[Radikal: 亻 (Orang)] + [Komponen: 木 (Pohon)] = Orang bersandar di pohon.')],
        'co': 'Piktogram paling ikonik! Seorang manusia (亻) yang kelelahan lalu menyandarkan punggungnya ke batang pohon rindang (木) untuk <b>Istirahat / Rehat / Absen kerja</b>.'
    },
    {
        'w': '営業する', 'y': 'えいぎょうする', 'a': 'Buka usaha / Marketing', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'この店は９時から営業します。', 'ei': 'Toko ini buka dari jam 9.',
        'ch': [
            ('営', 'いとな.む', 'エイ', 'Mengelola (Api 火火 di atas rumah 宮 = Menjaga api bisnis).'),
            ('業', 'わざ', 'ギョウ', 'Usaha/Tugas.')
        ],
        'co': 'Mengelola (営) usaha/bisnis (業) secara aktif. <b>Buka toko / Operasional bisnis / Sales marketing</b>.'
    },
    {
        'w': '言う', 'y': 'いう', 'a': 'Berkata / Mengatakan', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '「おはよう」と言います。', 'ei': 'Mengatakan "Selamat pagi".',
        'ch': [('言', 'い.う', 'ゲン / ゴン', '[Radikal: 言 (Kata-kata)] = Mulut yang mengeluarkan gelombang suara (garis horizontal bertumpuk).')],
        'co': 'Kanji paling dasar untuk komunikasi. Mulut (口) di bawah dengan gelombang suara (garis-garis) yang memancar ke atas. <b>Berkata / Mengatakan sesuatu secara verbal</b>.'
    },
    {
        'w': '置く', 'y': 'おく', 'a': 'Meletakkan / Menaruh', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'テーブルの上に本を置きます。', 'ei': 'Menaruh buku di atas meja.',
        'ch': [('置', 'お.く', 'チ', '[Radikal: 罒 (Jaring/Jala)] + [Komponen: 直 (Lurus/Tepat)] = Meletakkan barang di posisi yang tepat.')],
        'co': 'Menempatkan barang secara rapi dan lurus (直) di tempatnya yang benar, seolah terjaring (罒) di posisi tetap. <b>Meletakkan / Menaruh benda</b>.'
    },
    {
        'w': '話す', 'y': 'はなす', 'a': 'Berbicara / Bercerita', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '友達と電話で話します。', 'ei': 'Berbicara dengan teman lewat telepon.',
        'ch': [('話', 'はな.す', 'ワ', '[Radikal: 言 (Kata)] + [Komponen: 舌 (Lidah)] = Lidah yang aktif mengolah kata-kata.')],
        'co': 'Lidah (舌) mengolah kata-kata (言) menjadi suara yang bermakna. Beda dengan 言う (satu arah), 話す lebih interaktif: <b>Berbicara / Bercakap-cakap / Bercerita</b>.'
    },
    {
        'w': '持って行く', 'y': 'もっていく', 'a': 'Membawa pergi', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '弁当を持って行きます。', 'ei': 'Membawa bekal pergi.',
        'ch': [
            ('持', 'も.つ', 'ジ', 'Memegang (Tangan 扌 + Kuil 寺).'),
            ('行', 'い.く', 'コウ', 'Pergi.')
        ],
        'co': 'Memegang (持) suatu barang lalu membawanya pergi (行く) menjauhi lokasi saat ini. <b>Membawa pergi (Take away)</b>.'
    },
    {
        'w': '片付ける', 'y': 'かたづける', 'a': 'Merapikan / Membereskan', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '部屋を片付けてください。', 'ei': 'Tolong rapikan kamarnya.',
        'ch': [
            ('片', 'かた', 'ヘン', 'Sebelah/Potongan (Setengah papan kayu 爿).'),
            ('付', 'つ.ける', 'フ', 'Menempelkan.')
        ],
        'co': 'Mengambil potongan-potongan (片) barang yang berserakan lalu menempelkannya (付) kembali ke tempatnya masing-masing. <b>Merapikan / Membereskan ruangan</b>.'
    },
    {
        'w': '着替える', 'y': 'きがえる', 'a': 'Berganti pakaian', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '仕事の服に着替えます。', 'ei': 'Berganti pakaian kerja.',
        'ch': [
            ('着', 'き.る', 'チャク', 'Memakai baju (Bulu domba 羊 + Mata 目).'),
            ('替', 'か.える', 'タイ', 'Mengganti (Dua orang 夫夫 + Matahari 日 = shift/ganti giliran).')
        ],
        'co': 'Menanggalkan pakaian (着) yang sedang dipakai lalu menggantinya (替) dengan baju yang berbeda. <b>Berganti baju / Ganti kostum</b>.'
    },
    {
        'w': '捨てる', 'y': 'すてる', 'a': 'Membuang / Melempar', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ゴミを捨ててください。', 'ei': 'Tolong buang sampahnya.',
        'ch': [('捨', 'す.てる', 'シャ', '[Radikal: 扌 (Tangan)] + [Komponen: 舎 (Pondok/Tempat tinggal)] = Tangan melepaskan barang dari pondok.')],
        'co': 'Tangan (扌) mengambil barang dari dalam pondok (舎) lalu melemparkannya keluar. Merelakan barang pergi selamanya. <b>Membuang sampah / Meninggalkan sesuatu</b>.'
    },
    {
        'w': '並べる', 'y': 'ならべる', 'a': 'Menyusun / Menjajarkan', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '本棚に本を並べます。', 'ei': 'Menyusun buku di rak.',
        'ch': [('並', 'なら.べる', 'ヘイ', '[Radikal: 並 (Berjajar)] = Piktogram dua orang berdiri bersisian sejajar.')],
        'co': 'Dua sosok manusia berdiri berdampingan dengan jarak sama rata. <b>Menyusun / Menjajarkan benda secara rapi berderet</b>.'
    },
    {
        'w': '見せる', 'y': 'みせる', 'a': 'Memperlihatkan / Menunjukkan', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '写真を見せてください。', 'ei': 'Tolong perlihatkan fotonya.',
        'ch': [('見', 'み.せる / み.る', 'ケン', '[Radikal: 見 (Melihat)] = Mata besar 目 di atas kaki 儿 yang berjalan mengamati.')],
        'co': 'Versi transitif kausal dari 見る (melihat). Bukan kamu yang lihat, tapi kamu <b>Membuat orang lain melihat</b> sesuatu. <b>Memperlihatkan / Pamer</b>.'
    },
    {
        'w': '見る', 'y': 'みる', 'a': 'Melihat / Menonton', 'g': 2, 'subdeck': 'KK::Sensori Emosi',
        'ej': 'テレビを見ます。', 'ei': 'Menonton TV.',
        'ch': [('見', 'み.る', 'ケン', '[Radikal: 見 (Melihat)] = Mata besar 目 di atas kaki 儿.')],
        'co': 'Mata (目) yang dibuka lebar-lebar dan berjalan (儿) mendekati objek untuk mengamatinya lebih jelas. <b>Melihat / Menonton / Mengamati</b>. Gol 2 (Mite, Minai).'
    }
]
