# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '違う', 'y': 'ちがう', 'a': 'Salah / Berbeda', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'それは違います。', 'ei': 'Itu salah / berbeda.',
        'ch': [('違', 'ちが(う)', 'イ', 'Berbeda/Menyimpang. 辶 (jalan) + 韋 (kulit hewan yang saling bertolak belakang). Dua orang berjalan ke arah yang berlawanan.')],
        'co': 'Bayangkan dua orang yang <b>berjalan</b> (辶) namun kepalanya saling berpaling ke arah <b>berlawanan</b> (韋). Pendapat mereka tidak sama, makanya <b>berbeda</b> atau <b>salah</b>.'
    },
    {
        'w': '来る', 'y': 'くる', 'a': 'Datang', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '日本へ来ました。', 'ei': 'Telah datang ke Jepang.',
        'ch': [('来', 'く(る) / き(ます)', 'ライ', 'Datang. Piktogram gandum (pohon dengan bulir menggantung) yang diyakini "datang" dari surga. / Datangnya musim panen.')],
        'co': 'Bentuk gandum yang tumbuh subur menjuntai diartikan sebagai berkah yang <b>datang</b> dari langit. Ini adalah kata kerja ireguler (Gol 3) paling penting, pasangannya 行く (pergi).'
    },
    {
        'w': '住む', 'y': 'すむ', 'a': 'Tinggal / Bermukim', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'ジャカルタに住んでいます。', 'ei': 'Saya tinggal di Jakarta.',
        'ch': [('住', 'す(む)', 'ジュウ', 'Tinggal. 亻 (orang) + 主 (tuan/utama). Orang yang menjadi tuan/menetap di suatu tempat.')],
        'co': 'Orang (亻) yang menjadi penguasa atau tuan (主) di suatu tanah. Menandakan ia tidak lagi berpindah-pindah nomaden, melainkan <b>menetap</b> dan <b>tinggal</b> di sana.'
    },
    {
        'w': '食べる', 'y': 'たべる', 'a': 'Makan', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'ご飯を食べます。', 'ei': 'Makan nasi.',
        'ch': [('食', 'た(べる) / く(う)', 'ショク', 'Makan. 亼 (mengumpulkan/mulut) + 皀 (butiran nasi wangi/wadah makanan). Mengumpulkan makanan ke dalam mulut.')],
        'co': 'Kamu melihat wadah makanan (皀) dan sebuah tutup/mulut (亼) di atasnya. Kegiatan memasukkan nutrisi dari wadah ke tubuh: <b>Makan</b>. Karena Gol 2, konjugasinya sangat gampang (tinggal hapus る).'
    },
    {
        'w': '飲む', 'y': 'のむ', 'a': 'Minum', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '水を飲みます。', 'ei': 'Minum air.',
        'ch': [('飲', 'の(む)', 'イン', 'Minum. 食 (makan/makanan) + 欠 (orang menguap/membuka mulut lebar-lebar).')],
        'co': 'Setelah makan (食), kamu membuka mulut (欠) karena haus, lalu meneguk cairan. <b>Minum</b> air atau bahkan "minum obat" (薬を飲む).'
    },
    {
        'w': '有る', 'y': 'ある', 'a': 'Ada (Benda Mati/Tanaman)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '机の上に本が有ります。', 'ei': 'Ada buku di atas meja.',
        'ch': [('有', 'あ(る)', 'ユウ', 'Ada/Memiliki. ナ (tangan) + 月 (daging). Tangan yang memegang sepotong daging = memiliki kekayaan.')],
        'co': 'Di zaman dulu, orang yang memegang sepotong <b>daging</b> (月) di tangannya (ナ) berarti dia <b>memiliki sesuatu</b> atau "ada" makanan. Kata dasar untuk eksistensi benda mati.'
    },
    {
        'w': '居る', 'y': 'いる', 'a': 'Ada (Makhluk Hidup)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'あそこに犬が居ます。', 'ei': 'Ada anjing di sana.',
        'ch': [('居', 'い(る)', 'キョ', 'Berada. 尸 (tubuh/pantat) + 古 (tua/tetap). Orang yang duduk menetap diam di suatu tempat.')],
        'co': 'Orang (尸) yang berjongkok atau duduk mantap (古). Menandakan eksistensi atau keberadaan fisik yang bernyawa. Hanya untuk benda yang bisa bernapas / berpindah sendiri (manusia, hewan).'
    },
    {
        'w': '為る', 'y': 'する', 'a': 'Melakukan', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '宿題をします。', 'ei': 'Melakukan/mengerjakan PR.',
        'ch': [('為', 'ため / す(る)', 'イ', 'Melakukan / Demi. (Kanji ini jarang dipakai untuk kata "suru", biasanya ditulis hiragana saja). Piktogram tangan menuntun gajah untuk melakukan pekerjaan berat.')],
        'co': 'Kata kerja paling ajaib (Gol 3). Biasanya ditulis <b>する</b> saja tanpa Kanji. Bisa menempel di belakang kata benda (Noun) dan mengubahnya jadi kata kerja. (Contoh: 勉強 + する = Belajar).'
    },
    {
        'w': '頂く', 'y': 'いただく', 'a': 'Menerima (Humble/Sopan)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '先生から本を頂きました。', 'ei': 'Saya menerima buku dari guru (bahasa sopan).',
        'ch': [('頂', 'いただ(く) / いただき', 'チョウ', 'Puncak / Menerima. 丁 (paku/tegas) + 頁 (kepala). Puncak kepala. Saat menerima dari atasan, kita menundukkan kepala.')],
        'co': '<b>Menerima</b> sesuatu sambil menundukkan puncak kepala (頂) sebagai rasa hormat (merendahkan diri). Sering didengar saat mau makan: いただきます (Saya menerima hidangan ini).'
    },
    {
        'w': '呼ぶ', 'y': 'よぶ', 'a': 'Memanggil', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': 'タクシーを呼びます。', 'ei': 'Memanggil taksi.',
        'ch': [('呼', 'よ(ぶ)', 'コ', 'Memanggil / Menghembuskan napas. 口 (mulut) + 乎 (huruf seru/teriakan). Mulut yang mengeluarkan suara keras.')],
        'co': 'Menggunakan mulut (口) untuk berteriak atau <b>memanggil</b> orang dari kejauhan. Kata ini sering dipakai juga untuk "memanggil/mengundang taksi".'
    },
    {
        'w': '申す', 'y': 'もうす', 'a': 'Bernama / Berkata (Humble/Sopan)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '山田と申します。', 'ei': 'Saya bernama Yamada / Saya disebut Yamada.',
        'ch': [('申', 'もう(す)', 'シン', 'Berkata / Monyet. Piktogram petir yang memanjang (melapor kepada Dewa).')],
        'co': 'Kanji bentuk petir yang menyambar. Dulu bermakna melapor kepada dewa dengan rasa segan. Sekarang dipakai sebagai bahasa sangat sopan (Kenjougo) pengganti 言う (berkata/disebut). "Tono <b>to moushimasu</b>" = Hamba bernama Tono.'
    },
    {
        'w': '働く', 'y': 'はたらく', 'a': 'Bekerja', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '工場で働きます。', 'ei': 'Bekerja di pabrik.',
        'ch': [('働', 'はたら(く)', 'ドウ', 'Bekerja. 亻 (orang) + 動 (bergerak). Kokuji (kanji buatan Jepang). Orang yang badannya terus bergerak aktif.')],
        'co': 'Ini adalah kanji asli ciptaan Jepang (Kokuji). Terdiri dari <b>Orang</b> (亻) yang <b>Bergerak/Beraktivitas</b> (動). Tentu saja itu artinya orang yang sedang <b>bekerja membanting tulang</b>!'
    },
    {
        'w': '買う', 'y': 'かう', 'a': 'Membeli', 'g': 1, 'subdeck': 'KK::Rumah_Tangga',
        'ej': 'りんごを買います。', 'ei': 'Membeli apel.',
        'ch': [('買', 'か(う)', 'バイ', 'Membeli. 罒 (jaring/mata) + 貝 (kerang/uang). Melihat uang kerang untuk dibarter dengan barang.')],
        'co': 'Di zaman kuno, 貝 (kerang) adalah mata uang. Menyerahkan jaring/kerang (uang) untuk mendapatkan sesuatu. <b>Membeli</b>.'
    },
    {
        'w': '売る', 'y': 'うる', 'a': 'Menjual', 'g': 1, 'subdeck': 'KK::Rumah_Tangga',
        'ej': '車を売ります。', 'ei': 'Menjual mobil.',
        'ch': [('売', 'う(る)', 'バイ', 'Menjual. 士 (prajurit/orang terhormat) + 罒 (tutup) + 儿 (kaki). (Aslinya 賣 = 出 keluar + 買 uang). Mengeluarkan barang untuk ditukar uang.')],
        'co': 'Mengeluarkan stok barangmu lalu memamerkannya supaya ditukar dengan kerang/uang. <b>Menjual</b> barang demi cuan.'
    },
    {
        'w': '植える', 'y': 'うえる', 'a': 'Menanam', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '木を植えます。', 'ei': 'Menanam pohon.',
        'ch': [('植', 'う(える)', 'ショク', 'Menanam. 木 (pohon) + 直 (lurus). Menancapkan batang kayu agar berdiri lurus.')],
        'co': 'Mengambil bibit pohon/kayu (木) lalu menancapkannya secara <b>tegak lurus</b> (直) ke dalam tanah. <b>Menanam</b> tanaman, bukan sekadar melempar biji.'
    },
    {
        'w': '洗う', 'y': 'あらう', 'a': 'Mencuci', 'g': 1, 'subdeck': 'KK::Rumah_Tangga',
        'ej': '手を洗います。', 'ei': 'Mencuci tangan.',
        'ch': [('洗', 'あら(う)', 'セン', 'Mencuci. 氵 (air) + 先 (sebelum/lebih dulu). Membasuh telapak kaki/tangan dengan air sebelum melakukan hal lain.')],
        'co': 'Selalu gunakan air (氵) <b>lebih dulu</b> (先) sebelum melakukan kegiatan suci atau makan. Itulah fungsi <b>Mencuci</b> (tangan, baju, piring).'
    },
    {
        'w': '読む', 'y': 'よむ', 'a': 'Membaca', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '新聞を読みます。', 'ei': 'Membaca koran.',
        'ch': [('読', 'よ(む)', 'ドク', 'Membaca. 言 (kata-kata) + 売 (menjual/bersuara keras). Mengucapkan kata-kata teks dengan keras.')],
        'co': 'Zaman dulu belum ada "membaca dalam hati", semua gulungan buku dilantunkan (言) dengan suara nyaring seperti orang berjualan (売). <b>Membaca</b> teks tertulis.'
    },
    {
        'w': '食事する', 'y': 'しょくじする', 'a': 'Makan (Formal)', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '家族と食事します。', 'ei': 'Makan bersama keluarga.',
        'ch': [
            ('食', 'た(べる)', 'ショク', 'Makan.'),
            ('事', 'こと', 'ジ', 'Hal / Urusan.')
        ],
        'co': '食 (Makan) + 事 (Urusan) + する (melakukan). Bedanya dengan 食べる, ini bernuansa lebih rapi dan menjurus ke "kegiatan bersantap/dining", bukan sekadar aksi memamah makanan.'
    },
    {
        'w': '勉強する', 'y': 'べんきょうする', 'a': 'Belajar', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '日本語を勉強します。', 'ei': 'Belajar bahasa Jepang.',
        'ch': [
            ('勉', 'つと(める)', 'ベン', 'Berusaha keras / Memaksa. 兔 (kelinci yang menghindar) + 力 (tenaga). Memaksa tenaga.'),
            ('強', 'つよ(い)', 'キョウ', 'Kuat / Memaksa.')
        ],
        'co': 'Secara harfiah kanjinya agak menakutkan: "Memaksa (勉) sesuatu secara Kuat/Keras (強)". Belajar memang butuh memaksakan diri melawan kemalasan. Makanya orang Jepang sangat menghargai kerja keras akademis.'
    },
    {
        'w': '仕事する', 'y': 'しごとする', 'a': 'Bekerja / Melakukan pekerjaan', 'g': 3, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '会社で仕事します。', 'ei': 'Bekerja di perusahaan.',
        'ch': [
            ('仕', 'つか(える)', 'シ', 'Melayani. 亻 (orang) + 士 (prajurit/pejabat). Orang yang melayani atasannya.'),
            ('事', 'こと', 'ゴト', 'Pekerjaan / Hal.')
        ],
        'co': 'Urusan/Hal (事) yang berkaitan dengan Melayani orang lain (仕). "Bekerja" untuk bos, klien, atau perusahaan. Kata kerjanya tinggal tambah する (melakukan).'
    },
    {
        'w': '買い物する', 'y': 'かいものする', 'a': 'Berbelanja', 'g': 3, 'subdeck': 'KK::Rumah_Tangga',
        'ej': 'デパートで買い物します。', 'ei': 'Berbelanja di toserba.',
        'ch': [
            ('買', 'か(う)', 'バイ', 'Membeli.'),
            ('物', 'もの', 'ブツ', 'Barang. 牜 (sapi) + 勿 (bendera/percikan darah). Hewan kurban, lalu meluas jadi semua objek.')
        ],
        'co': 'Gabungan Membeli (買い) + Barang (物) + Melakukan (する). Jadi bukan spesifik beli apel atau mobil, tapi aksi keliling mal untuk <b>Belanja-belanja</b> secara umum.'
    },
    {
        'w': '運動する', 'y': 'うんどうする', 'a': 'Berolahraga', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '毎日運動します。', 'ei': 'Setiap hari berolahraga.',
        'ch': [
            ('運', 'はこ(ぶ)', 'ウン', 'Membawa / Nasib / Menggerakkan.'),
            ('動', 'うご(く)', 'ドウ', 'Bergerak. 重 (berat) + 力 (tenaga). Menggunakan tenaga untuk memindah barang berat.')
        ],
        'co': 'Menggerakkan (動) dan membawa/menjalankan (運) seluruh anggota badanmu agar keluar keringat dan otot bekerja. <b>Berolahraga</b> secara fisik.'
    },
    {
        'w': '案内する', 'y': 'あんないする', 'a': 'Memandu / Menunjukkan jalan', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '京都を案内します。', 'ei': 'Memandu keliling Kyoto.',
        'ch': [
            ('案', 'あん', 'アン', 'Rencana/Meja. 木 (kayu) + 安 (tenang/aman). Meja kayu untuk membuat draf rencana dengan tenang.'),
            ('内', 'うち', 'ナイ', 'Dalam. 冂 (batas) + 人 (orang). Masuk ke dalam suatu area.')
        ],
        'co': 'Rencana/petunjuk (案) untuk membimbing seseorang masuk ke Dalam (内) suatu area asing. Kamu memandu turis karena mereka belum tahu jalan. <b>Memandu / Mengantar masuk</b>.'
    },
    {
        'w': '洗濯する', 'y': 'せんたくする', 'a': 'Mencuci baju', 'g': 3, 'subdeck': 'KK::Rumah_Tangga',
        'ej': '服を洗濯します。', 'ei': 'Mencuci baju.',
        'ch': [
            ('洗', 'あら(う)', 'セン', 'Mencuci (dengan air 氵).'),
            ('濯', 'すす(ぐ)', 'タク', 'Membilas/Mencuci bersih. 氵 (air) + 翟 (bulu burung berkilau). Air yang membersihkan sampai berkilau.')
        ],
        'co': 'Duet maut 氵(air) ganda. Mencuci (洗) dan Membilas (濯) hingga kotoran hilang dan kain kembali berkilau bersih layaknya bulu burung merak. Khusus untuk <b>Mencuci Pakaian</b>.'
    },
    {
        'w': 'ジョギングする', 'y': 'ジョギングする', 'a': 'Jogging', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '公園でジョギングします。', 'ei': 'Jogging di taman.',
        'ch': [],
        'co': 'Kata serapan dari bahasa Inggris "Jogging". Tidak punya Kanji. Tambahkan する untuk mengubahnya jadi kata kerja. <b>Berlari kecil / Jogging</b>.'
    },
    {
        'w': '釣る', 'y': 'つる', 'a': 'Memancing', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '海で魚を釣ります。', 'ei': 'Memancing ikan di laut.',
        'ch': [('釣', 'つ(る)', 'チョウ', 'Memancing. 釒 (emas/logam) + 勺 (sendok/mengikat/melengkung). Mata kail dari logam yang melengkung.')],
        'co': 'Logam (釒) kecil yang ujungnya dibengkokkan seperti kaitan/sendok (勺). Dilempar ke laut untuk menggaet ikan. Tentu saja: <b>Memancing</b>.'
    },
    {
        'w': '起きる', 'y': 'おきる', 'a': 'Bangun (tidur) / Terjadi', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '朝６時に起きます。', 'ei': 'Saya bangun jam 6 pagi.',
        'ch': [('起', 'お(きる) / お(こす)', 'キ', 'Bangun/Bangkit. 走 (berlari/kaki) + 己 (berlutut/diri). Mengangkat badan dari tanah untuk bangkit dan bergerak.')],
        'co': 'Badan yang tadinya merebah (tidur), lalu bangkit bertumpu di atas kaki (走). <b>Bangun tidur</b> atau <b>bangkit berdiri</b>. Beda Kanji dengan 置く (Meletakkan).'
    },
    {
        'w': '寝る', 'y': 'ねる', 'a': 'Tidur', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '夜１０時に寝ます。', 'ei': 'Saya tidur jam 10 malam.',
        'ch': [('寝', 'ね(る)', 'シン', 'Tidur. 宀 (atap) + 爿 (tempat tidur) + 帚 (sapu/tangan) + 浸(sebagian) = Berbaring masuk ke tempat tidur.')],
        'co': 'Berlindung di bawah atap (宀), merebahkan tubuh lelah ke atas dipan/tempat tidur. Mengistirahatkan badan. <b>Tidur / Berbaring</b>.'
    },
    {
        'w': '浴びる', 'y': 'あびる', 'a': 'Mandi (Shower) / Mengguyur', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'シャワーを浴びます。', 'ei': 'Mandi shower.',
        'ch': [('浴', 'あ(びる)', 'ヨク', 'Mandi/Bermandi. 氵 (air) + 谷 (lembah). Seperti berada di dasar lembah yang diguyur air terjun dari atas.')],
        'co': 'Bayangkan kamu berdiri di sebuah lembah (谷) dan air (氵) mengalir deras mengguyur kepalamu (seperti air terjun mini). Itulah esensi <b>Mandi shower (mengguyur tubuh)</b>.'
    },
    {
        'w': '料理する', 'y': 'りょうりする', 'a': 'Memasak', 'g': 3, 'subdeck': 'KK::Rumah_Tangga',
        'ej': '晩ご飯を料理します。', 'ei': 'Memasak makan malam.',
        'ch': [
            ('料', '–', 'リョウ', 'Bahan/Biaya. 米 (beras) + 斗 (sukatan beras). Menakar bahan baku utama.'),
            ('理', 'ことわり', 'リ', 'Alasan/Logika/Mengatur. 王 (giok) + 里 (kampung). Memoles/mengatur giok dengan rapi.')
        ],
        'co': 'Mempersiapkan bahan-bahan pangan (料) lalu meracik dan mengaturnya (理) dengan logika/resep sedemikian rupa sehingga menjadi sajian nikmat. <b>Memasak</b>.'
    },
    {
        'w': '散歩する', 'y': 'さんぽする', 'a': 'Jalan-jalan (Santai)', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '犬と散歩します。', 'ei': 'Jalan-jalan bersama anjing.',
        'ch': [
            ('散', 'ち(る)', 'サン', 'Tersebar/Terpencar. 艹 (tanaman) + 月 (daging) + 攵 (memukul).'),
            ('歩', 'ある(く)', 'ホ', 'Berjalan. 止 (jejak kaki) bolak-balik.')
        ],
        'co': 'Berjalan kaki (歩) secara santai tak tentu arah, membiarkan pikiran tersebar bebas (散) tanpa tujuan terburu-buru. <b>Jalan-jalan sore / Strolling</b>.'
    },
    {
        'w': '掃除する', 'y': 'そうじする', 'a': 'Bersih-bersih', 'g': 3, 'subdeck': 'KK::Rumah_Tangga',
        'ej': '部屋を掃除します。', 'ei': 'Membersihkan kamar.',
        'ch': [
            ('掃', 'は(く)', 'ソウ', 'Menyapu. 扌 (tangan) + 帚 (sapu). Tangan memegang sapu.'),
            ('除', 'のぞ(く)', 'ジョ', 'Menyingkirkan/Menghapus. 阝 (bukit) + 余 (sisa). Membuang rintangan.')
        ],
        'co': 'Menggunakan sapu di tangan (掃) untuk menyingkirkan atau membuang debu dan kotoran (除) dari lantaimu. Benar-benar deskripsi harfiah untuk <b>Bersih-bersih</b>.'
    },
    {
        'w': '終わる', 'y': 'おわる', 'a': 'Selesai / Berakhir', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '仕事が終わりました。', 'ei': 'Pekerjaan sudah selesai.',
        'ch': [('終', 'お(わる)', 'シュウ', 'Berakhir/Akhir. 糸 (benang) + 冬 (musim dingin/akhir tahun). Benang yang ujungnya telah habis dipintal, digambarkan seperti musim dingin yang menjadi akhir tahun.')],
        'co': 'Musim dingin (冬) menandakan siklus tahunan bumi yang telah <b>usai/berakhir</b>. Sama seperti seutas benang (糸) yang ujungnya sudah terputus. <b>Selesai</b>.'
    },
    {
        'w': '始まる', 'y': 'はじまる', 'a': 'Mulai / Dimulai (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '映画が始まります。', 'ei': 'Filmnya (akan) dimulai.',
        'ch': [('始', 'はじ(まる) / はじ(める)', 'シ', 'Mulai. 女 (perempuan) + 台 (panggung/janin). Rahim seorang ibu tempat sebuah kehidupan baru "dimulai".')],
        'co': 'Kehidupan manusia berawal (Mulai) dari seorang Perempuan/Ibu (女). Segala sesuatu pasti punya titik nol, dan 始 adalah garis <b>Start / Dimulai</b>.'
    },
    {
        'w': '休む', 'y': 'やすむ', 'a': 'Beristirahat / Libur / Absen', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': '学校を休みます。', 'ei': 'Libur / Absen dari sekolah.',
        'ch': [('休', 'やす(む)', 'キュウ', 'Istirahat. 亻 (orang) + 木 (pohon). Orang yang bersandar di bawah rindangnya pohon.')],
        'co': 'Coba bayangkan hari yang sangat panas, kamu lelah bekerja, lalu duduk menyandarkan diri (亻) ke sebatang pohon (木). Sangat damai. <b>Istirahat / Cuti</b>.'
    },
    {
        'w': '営業する', 'y': 'えいぎょうする', 'a': 'Beroperasi / Buka (Toko/Bisnis)', 'g': 3, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'この店は２４時間営業します。', 'ei': 'Toko ini beroperasi 24 jam.',
        'ch': [
            ('営', 'いとな(む)', 'エイ', 'Mengelola/Mengurus. 呂 (dua tulang punggung menyambung) + api unggun. Melakukan kegiatan tanpa putus.'),
            ('業', 'わざ', 'ギョウ', 'Pekerjaan / Bisnis / Karma. Instrumen kayu bergigi.')
        ],
        'co': 'Pernah lihat papan "OPEN" di depan toko Jepang? Sering ditulis 営業中 (Sedang Beroperasi). Artinya toko sedang <b>menjalankan (営) roda bisnis/pekerjaannya (業)</b>.'
    },
    {
        'w': '遊ぶ', 'y': 'あそぶ', 'a': 'Bermain', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '公園で友達と遊びます。', 'ei': 'Bermain dengan teman di taman.',
        'ch': [('遊', 'あそ(ぶ)', 'ユウ', 'Bermain / Berkelana. 辶 (jalan) + 斿 (bendera/anak-anak yang mengembara bahagia). Bergerak bebas ke sana kemari.')],
        'co': 'Berjalan-jalan lari ke sana kemari tanpa ikatan beban atau tujuan serius (辶). Fokus pada kesenangan semata. <b>Bermain atau Nongkrong santai</b>.'
    },
    {
        'w': '言う', 'y': 'いう', 'a': 'Berkata / Mengatakan', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '「ありがとう」と言います。', 'ei': 'Berkata "Terima kasih".',
        'ch': [('言', 'い(う)', 'ゲン / ゴン', 'Kata/Berbicara. 辛 (jarum/alat ukir) + 口 (mulut). Dulu melambangkan sumpah yang keluar dari mulut dan mengikat.')],
        'co': 'Mulut (口) yang mengeluarkan garis-garis ucapan (huruf atas). Tindakan paling mendasar dari komunikasi vokal. <b>Berkata / Ngomong</b>.'
    },
    {
        'w': '置く', 'y': 'おく', 'a': 'Meletakkan / Menaruh', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'かばんを机の上に置きます。', 'ei': 'Meletakkan tas di atas meja.',
        'ch': [('置', 'お(く)', 'チ', 'Meletakkan. 罒 (jaring/tutup) + 直 (lurus/tegak). Mengatur atau menaruh sesuatu agar berdiri/terletak lurus dengan benar di posisinya.')],
        'co': 'Hati-hati! Cara bacanya sama persis dengan 起きる (Oki-), tapi ini adalah Gol 1 (Okimasu, Oite, Okanai) yang artinya <b>Meletakkan / Memposisikan barang</b>.'
    },
    {
        'w': '泳ぐ', 'y': 'およぐ', 'a': 'Berenang', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'プールで泳ぎます。', 'ei': 'Berenang di kolam renang.',
        'ch': [('泳', 'およ(ぐ)', 'エイ', 'Berenang. 氵 (air) + 永 (panjang/abadi, piktogram orang berenang di arus sungai).')],
        'co': 'Banyak unsur air (氵) di sini. Badan manusia menyelam ke dalam air, terus memanjang dan meluncur menembus arus (永). <b>Berenang</b>.'
    },
    {
        'w': '書く', 'y': 'かく', 'a': 'Menulis', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '手紙を書きます。', 'ei': 'Menulis surat.',
        'ch': [('書', 'か(く)', 'ショ', 'Menulis/Buku. 聿 (kuas tangan) + 曰 (berkata/menyatakan). Tangan memegang kuas untuk memindahkan kata-kata yang diucapkan ke atas bambu/kertas.')],
        'co': 'Sebuah tangan menggenggam kuas (聿), menggoreskan tinta. Aksi memindahkan pikiran abstrak menjadi simbol fisik yang bisa dibaca. <b>Menulis (tulisan)</b>. Beda dengan 描く (menggambar).'
    },
    {
        'w': '貸す', 'y': 'かす', 'a': 'Meminjamkan', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '友達にペンを貸します。', 'ei': 'Saya meminjamkan pulpen kepada teman.',
        'ch': [('貸', 'か(す)', 'タイ', 'Meminjamkan. 代 (menggantikan) + 貝 (uang/harta). Harta/Uang diserahkan sementara (menggantikan kepemilikan) kepada pihak lain.')],
        'co': 'Menyerahkan uang (貝) atau barang milikmu kepada orang lain sebagai pengganti (代) sementara. Jangan terbalik! 貸す (Kasu) = <b>Kasih pinjam</b>. 借りる (Kariru) = Kamu yang pinjam.'
    },
    {
        'w': '聞く', 'y': 'きく', 'a': 'Mendengar / Bertanya', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '音楽を聞きます。 / 先生に聞きます。', 'ei': 'Mendengarkan musik. / Bertanya kepada guru.',
        'ch': [('聞', 'き(く) / き(こえる)', 'ブン', 'Mendengar. 門 (gerbang) + 耳 (telinga). Menempelkan telinga di celah gerbang untuk menguping suara dari luar/dalam.')],
        'co': 'Daun telinga (耳) yang ditempelkan ke daun pintu gerbang (門) untuk <b>Menyimak/Mendengar</b> desas-desus. Punya arti kedua: <b>Bertanya</b> (karena bertanya untuk mendengar jawaban).'
    },
    {
        'w': '切る', 'y': 'きる', 'a': 'Memotong / Memutuskan', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'はさみで紙を切ります。', 'ei': 'Memotong kertas dengan gunting.',
        'ch': [('切', 'き(る)', 'セツ', 'Memotong. 七 (tujuh, aslinya gambar potongan silang) + 刀 (pisau/pedang). Pisau yang diiris tegak lurus menembus barang.')],
        'co': 'Menghujamkan pisau (刀) dengan tegas. Awas, walau akhirannya ~iru (kiru), ini adalah <b>Golongan 1 (Godan)</b>. Konjugasinya: kitte (bukan kite), kiranai (bukan kinai). <b>Memotong</b>.'
    },
    {
        'w': '探す', 'y': 'さがす', 'a': 'Mencari (Barang hilang / Hal baru)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '無くした鍵を探します。', 'ei': 'Mencari kunci yang hilang.',
        'ch': [('探', 'さが(す)', 'タン', 'Mencari/Meraba. 扌 (tangan) + 罙 (mencari ke dalam, lubang yang jauh). Tangan yang merogoh ke dalam mencari-cari sesuatu.')],
        'co': 'Tangan (扌) yang dikerahkan untuk menjelajahi area yang dalam (罙) demi menemukan sesuatu. <b>Mencari benda</b> yang terselip, atau "mencari jodoh".'
    },
    {
        'w': '死ぬ', 'y': 'しぬ', 'a': 'Mati / Meninggal', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '交通事故で死にました。', 'ei': 'Meninggal karena kecelakaan lalu lintas.',
        'ch': [('死', 'し(ぬ)', 'シ', 'Mati. 歹 (tulang belulang yang tersisa) + 匕 (orang yang terbalik/jatuh pingsan). Orang yang badannya hancur/tumbang tinggal tulang.')],
        'co': 'Kanji yang cukup mengerikan (Tulang belulang 歹). Satu-satunya kata kerja bahasa Jepang dalam bentuk kamus yang berakhiran N (ぬ/nu) di level N5/N4. Konjugasi Te-nya = 死んで (Shinde).'
    },
    {
        'w': '使う', 'y': 'つかう', 'a': 'Menggunakan / Memakai', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'パソコンを使います。', 'ei': 'Menggunakan komputer pribadi.',
        'ch': [('使', 'つか(う)', 'シ', 'Menggunakan/Utusan. 亻 (orang) + 吏 (petugas/utusan). Menyuruh/memanfaatkan orang atau benda untuk suatu tugas.')],
        'co': 'Awalnya bermakna mengutus (menggunakan tenaga orang). Sekarang bermakna mengoperasikan benda (uang, komputer, alat) demi mempermudah tujuan. <b>Menggunakan</b>.'
    },
    {
        'w': '作る', 'y': 'つくる', 'a': 'Membuat / Memproduksi', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'ケーキを作ります。', 'ei': 'Membuat kue.',
        'ch': [('作', 'つく(る)', 'サク / サ', 'Membuat. 亻 (orang) + 乍 (pisau berukir / kerah baju). Seseorang menggunakan alat untuk membentuk sesuatu yang baru.')],
        'co': 'Seseorang (亻) mengerahkan keterampilannya untuk memotong, memahat, atau merangkai material menjadi sesuatu (kue, meja, PR). <b>Membuat dari nol</b>. Golongan 1 (tsukutte, tsukuranai).'
    },
    {
        'w': '手伝う', 'y': 'てつだう', 'a': 'Membantu (Tenaga)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '母の料理を手伝います。', 'ei': 'Membantu ibu memasak.',
        'ch': [
            ('手', 'て', 'シュ', 'Tangan.'),
            ('伝', 'つた(える) / てつだ(う)', 'デン', 'Menyampaikan/Meneruskan. 亻 (orang) + 云 (berputar/kata).')
        ],
        'co': 'Secara harfiah: "Menyampaikan/meminjamkan Tangan (手)". Kamu mengulurkan tangan tenaga fisikmu untuk meringankan beban pekerjaan orang lain. <b>Bantu-bantu / Menolong (tugas)</b>.'
    },
    {
        'w': '取る', 'y': 'とる', 'a': 'Mengambil', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'そこの塩を取ってください。', 'ei': 'Tolong ambilkan garam di situ.',
        'ch': [('取', 'と(る)', 'シュ', 'Mengambil/Merampas. 耳 (telinga) + 又 (tangan). Di medan perang kuno, tangan mengambil telinga musuh yang tumbang sebagai bukti kemenangan.')],
        'co': 'Etimologinya kelam (mengambil telinga rampasan). Tapi sekarang murni dipakai untuk gerakan <b>memungut / meraup / mengambil</b> objek yang ada di depan mata. Golongan 1.'
    }
]
