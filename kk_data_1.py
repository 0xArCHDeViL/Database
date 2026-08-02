# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '違う', 'y': 'ちがう', 'a': 'Salah / Berbeda', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'それは違います。', 'ei': 'Itu salah / berbeda.',
        'ch': [('違', 'ちが.う / ちが.い', 'イ', '[Radikal: 辶 (Jalan/Pergerakan)] + [Komponen: 韋 (Saling Membelakangi)]')],
        'co': 'Bayangkan lu lagi <b>jalan bareng</b> (辶), tapi satu orang milih <b>balik badan</b> (韋) dan jalan berlawanan arah. Langkah yang saling menjauh ini melambangkan <b>Perbedaan / Salah Jalan</b>. (Cing Cong! Chigau = Beda!)'
    },
    {
        'w': '来る', 'y': 'くる', 'a': 'Datang', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '日本へ来ました。', 'ei': 'Telah datang ke Jepang.',
        'ch': [('来', 'く.る / き.ます / こ.ない', 'ライ', '[Radikal: 木 (Pohon/Kayu)] + [Komponen: 丷 (Gandum yang turun dari langit)]')],
        'co': 'Bentuk gandum yang tumbuh subur menjuntai diartikan sebagai berkah yang <b>datang</b> dari langit. Ini adalah kata kerja ireguler (Gol 3) paling penting, pasangannya 行く (pergi). Perhatikan 3 cara bacanya: <b>Kuru</b> (Kamus), <b>Kimasu</b> (Masu), <b>Konai</b> (Negatif)!'
    },
    {
        'w': '住む', 'y': 'すむ', 'a': 'Tinggal / Bermukim', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'ジャカルタに住んでいます。', 'ei': 'Saya tinggal di Jakarta.',
        'ch': [('住', 'す.む / す.まう', 'ジュウ', '[Radikal: 亻 (Orang)] + [Komponen: 主 (Tuan/Utama)]')],
        'co': 'Orang (亻) yang mendeklarasikan dirinya sebagai penguasa atau tuan (主) di suatu tanah. Menandakan ia tidak lagi hidup nomaden, melainkan <b>menetap</b> dan <b>tinggal</b> di sana secara permanen.'
    },
    {
        'w': '食べる', 'y': 'たべる', 'a': 'Makan', 'g': 2, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'ご飯を食べます。', 'ei': 'Makan nasi.',
        'ch': [('食', 'た.べる / く.う', 'ショク / ジキ', '[Radikal: 飠(Makan/Makanan)]')],
        'co': 'Bayangkan sebuah wadah makanan (皀) yang mengepul, lalu ada tutup/mulut (亼) di atasnya yang siap menelan. Kegiatan memasukkan nutrisi dari wadah ke tubuh: <b>Makan</b>. Golongan 2 (Ichidan) -> konjugasi super gampang, tinggal hapus る (Tabemasu, Tabenai).'
    },
    {
        'w': '飲む', 'y': 'のむ', 'a': 'Minum', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '水を飲みます。', 'ei': 'Minum air.',
        'ch': [('飲', 'の.む', 'イン', '[Radikal: 飠(Makanan)] + [Komponen: 欠 (Kekurangan/Menguap/Buka Mulut)]')],
        'co': 'Setelah makan (飠), tenggorokan terasa kering (欠 - kekurangan cairan/membuka mulut lebar-lebar). Otomatis lu bakal meneguk cairan. <b>Minum</b> air. Orang Jepang juga pakai kata ini untuk "minum obat" (薬を飲む) loh!'
    },
    {
        'w': '有る', 'y': 'ある', 'a': 'Ada (Benda Mati/Tanaman)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '机の上に本が有ります。', 'ei': 'Ada buku di atas meja.',
        'ch': [('有', 'あ.る', 'ユウ / ウ', '[Radikal: 月 (Daging/Bulan)] + [Komponen: 𠂇 (Tangan Kanan)]')],
        'co': 'Zaman purba dulu, orang yang memegang sepotong <b>daging</b> (月) di tangan kanannya (𠂇) berarti dia orang kaya yang <b>memiliki sesuatu</b> atau "punya" stok makanan. Kata dasar untuk eksistensi benda mati.'
    },
    {
        'w': '居る', 'y': 'いる', 'a': 'Ada (Makhluk Hidup)', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'あそこに犬が居ます。', 'ei': 'Ada anjing di sana.',
        'ch': [('居', 'い.る', 'キョ', '[Radikal: 尸 (Tubuh jongkok/Pantat)] + [Komponen: 古 (Tua/Dulu/Tetap)]')],
        'co': 'Orang (尸) yang berjongkok atau duduk mantap dalam waktu lama (古). Menandakan eksistensi atau keberadaan fisik yang bernyawa. <b>Hanya untuk benda yang bernapas / bisa berpindah sendiri (manusia, hewan).</b>'
    },
    {
        'w': '為る', 'y': 'する', 'a': 'Melakukan', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '宿題をします。', 'ei': 'Melakukan/mengerjakan PR.',
        'ch': [('為', 'ため / す.る', 'イ', '[Radikal: 灬 (Api)]')],
        'co': 'Kata kerja terkuat se-Jepang (Gol 3). Biasanya ditulis <b>する</b> saja pakai Hiragana. Keajaibannya? Dia bisa nempel di belakang Kata Benda (Noun) dan langsung ngubah noun itu jadi kata kerja. (Contoh: 勉強 + する = Belajar).'
    },
    {
        'w': '働く', 'y': 'はたらく', 'a': 'Bekerja', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '会社で働いています。', 'ei': 'Sedang bekerja di perusahaan.',
        'ch': [('働', 'はたら.く', 'ドウ', '[Radikal: 亻 (Orang)] + [Komponen: 動 (Bergerak)]')],
        'co': 'Gampang banget tebakannya! Ada <b>Orang</b> (亻) yang badannya <b>Terus Bergerak</b> (動). Ngapain tuh orang mondar-mandir? Tentu saja lagi <b>Bekerja</b> banting tulang nyari duit! Ini Kanji asli Jepang (Kokuji) lho.'
    },
    {
        'w': '買う', 'y': 'かう', 'a': 'Membeli', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': 'スーパーでパンを買いました。', 'ei': 'Telah membeli roti di supermarket.',
        'ch': [('買', 'か.う', 'バイ', '[Radikal: 貝 (Kerang/Uang kuno)] + [Komponen: 罒 (Jaring)]')],
        'co': 'Di zaman dulu, kerang (貝) dipakai sebagai uang logam. Kamu bawa jaring (罒) penuh dengan uang kerang untuk menukar barang dagangan. Aktivitas <b>Membeli</b>. Golongan 1 akhiran "u" (Bentuk te: Katte).'
    },
    {
        'w': '売る', 'y': 'うる', 'a': 'Menjual', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '古い車を売ります。', 'ei': 'Menjual mobil lama.',
        'ch': [('売', 'う.る / う.れる', 'バイ', '[Radikal: 士 (Prajurit/Pria)] + [Komponen: 冖 (Tutup) + 儿(Kaki)]')],
        'co': 'Seorang pria (士) berdiri tegak mengeluarkan barang dari bawah meja dagangan (冖) dengan kakinya (儿) bersiap. Ia menawarkan barangnya ke pelanggan. <b>Menjual</b> (Bentuk te: Utte).'
    },
    {
        'w': '洗う', 'y': 'あらう', 'a': 'Mencuci', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '手を洗ってください。', 'ei': 'Tolong cuci tangan.',
        'ch': [('洗', 'あら.う', 'セン', '[Radikal: 氵 (Air)] + [Komponen: 先 (Duluan/Ujung)]')],
        'co': 'Ada cipratan <b>air</b> (氵) yang kamu basuhkan ke <b>ujung</b> kaki/tangan (先) sehabis dari luar ruangan (duluan cuci tangan sebelum masuk rumah). <b>Mencuci / Membersihkan dengan air</b>.'
    },
    {
        'w': '読む', 'y': 'よむ', 'a': 'Membaca', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '毎日新聞を読みます。', 'ei': 'Membaca koran setiap hari.',
        'ch': [('読', 'よ.む', 'ドク / トク', '[Radikal: 言 (Berkata/Kata-kata)] + [Komponen: 売 (Menjual/Menyebarkan)]')],
        'co': 'Kamu melihat rentetan <b>kata-kata</b> tulisan (言) dan otakmu berusaha menyerapnya. Atau zaman dulu, orang membacakan gulungan teks dengan suara lantang layaknya <b>menjual/menyebarkan</b> (売) informasi. <b>Membaca</b>.'
    },
    {
        'w': '遊ぶ', 'y': 'あそぶ', 'a': 'Bermain / Nongkrong', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '公園で友達と遊びます。', 'ei': 'Bermain dengan teman di taman.',
        'ch': [('遊', 'あそ.ぶ', 'ユウ', '[Radikal: 辶 (Jalan)] + [Komponen: 斿 (Benderan terbang/Melayang bebas)]')],
        'co': 'Langkah kakimu (辶) ngikutin bendera yang terbang kesana-kemari (斿). Tanpa beban pikiran, cuma cari kesenangan semata. Di Jepang, <b>Asobu</b> bukan cuma "main bongkar pasang", tapi juga bisa diartikan <b>Nongkrong/Hangout bareng teman</b> di kafe lho!'
    },
    {
        'w': '泳ぐ', 'y': 'およぐ', 'a': 'Berenang', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'プールで泳ぎます。', 'ei': 'Berenang di kolam renang.',
        'ch': [('泳', 'およ.ぐ', 'エイ', '[Radikal: 氵 (Air)] + [Komponen: 永 (Abadi/Lama)]')],
        'co': 'Terdapat cipratan <b>air</b> sungai (氵). Kamu masuk ke dalamnya, dan karena airnya sangat deras, gerakan renangmu terasa sangat <b>lama / memanjang</b> (永). Hati-hati, konjugasinya pakai "ide": 泳いで (Oyoide).'
    },
    {
        'w': '行く', 'y': 'いく', 'a': 'Pergi', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '明日、学校へ行きます。', 'ei': 'Besok akan pergi ke sekolah.',
        'ch': [('行', 'い.く / ゆ.く / おこな.う', 'コウ / ギョウ', '[Radikal: 行 (Jalan bersimpangan)]')],
        'co': 'Kanji ini adalah gambar denah <b>Persimpangan Jalan</b> lho! Makanya berhubungan dengan pergerakan lalu lintas. Kata <b>Pergi</b> (行く) ini agak nyeleneh dikit di konjugasi Te: bukan iite, tapi <b>行って (Itte)</b>!'
    },
    {
        'w': '帰る', 'y': 'かえる', 'a': 'Pulang', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '６時に家へ帰ります。', 'ei': 'Pulang ke rumah pada jam 6.',
        'ch': [('帰', 'かえ.る / かえ.す', 'キ', '[Radikal: ⺕ (Tangan babi/Menyapu)] + [Komponen: 止 (Berhenti)]')],
        'co': 'Setelah lelah seharian berjalan/bekerja, langkah kakimu akhirnya <b>berhenti</b> (止) dan menemukan tempat bernaung (冖). Artinya lu udah <b>Pulang</b> ke rumah! Ingat: Golongan 1, Te formnya <b>Kaette</b> (bukan kaete)!'
    },
    {
        'w': '書く', 'y': 'かく', 'a': 'Menulis', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '手紙を書きました。', 'ei': 'Telah menulis surat.',
        'ch': [('書', 'か.く', 'ショ', '[Radikal: 曰 (Berkata/Mengucapkan)] + [Komponen: 聿 (Kuas)]')],
        'co': 'Tanganmu menggenggam kuat sebuah <b>Kuas Tulis</b> (聿), dan kamu menorehkan isi pikiran / ucapanmu (曰) ke atas secarik kertas. Memindahkan alam abstrak ke simbol fisik: <b>Menulis tulisan</b>.'
    },
    {
        'w': '貸す', 'y': 'かす', 'a': 'Meminjamkan', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '友達にペンを貸します。', 'ei': 'Meminjamkan pulpen kepada teman.',
        'ch': [('貸', 'か.す', 'タイ', '[Radikal: 貝 (Kerang/Uang)] + [Komponen: 代 (Pengganti/Sementara)]')],
        'co': 'Menyerahkan harta atau uang (貝) milikmu kepada orang lain sebagai pengganti (代) sementara. Jangan sampai kebalik ya bang! 貸す (Kasu) = <b>Kasih pinjam</b>. Lawannya 借りる (Kariru) = Pinjam dari orang.'
    },
    {
        'w': '借りる', 'y': 'かりる', 'a': 'Meminjam', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '図書館で本を借りました。', 'ei': 'Telah meminjam buku di perpustakaan.',
        'ch': [('借', 'か.りる', 'シャク', '[Radikal: 亻 (Orang)] + [Komponen: 昔 (Zaman dulu)]')],
        'co': 'Ada <b>Orang</b> (亻) yang mengambil barang/janji yang dibuat pada waktu <b>Kemarin/Dulu</b> (昔). Sederhananya, lu ngambil barang yang bukan hak lu saat ini (barang pinjeman). Golongan 2 (Karite, Karinai).'
    },
    {
        'w': '聞く', 'y': 'きく', 'a': 'Mendengar / Bertanya', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '音楽を聞きます。 / 先生に聞きます。', 'ei': 'Mendengarkan musik. / Bertanya kepada guru.',
        'ch': [('聞', 'き.く / き.こえる', 'ブン / モン', '[Radikal: 耳 (Telinga)] + [Komponen: 門 (Gerbang)]')],
        'co': 'Daun telinga (耳) yang ditempelkan rapat-rapat ke daun pintu gerbang kayu (門) demi <b>menguping / mendengar</b> rahasia atau desas-desus dari luar ruangan. Punya dua fungsi: <b>Mendengar</b> atau <b>Bertanya</b>.'
    },
    {
        'w': '切る', 'y': 'きる', 'a': 'Memotong / Memutuskan', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'はさみで紙を切ります。', 'ei': 'Memotong kertas dengan gunting.',
        'ch': [('切', 'き.る', 'セツ / サイ', '[Radikal: 刀 (Pisau/Pedang)] + [Komponen: 七 (Angka 7 / Silang)]')],
        'co': 'Menghujamkan sebilah pisau (刀) dengan tegas ke sebuah objek membentuk luka sayat (七). Awas terkecoh! Meski akhirannya ~iru, Kiru ini adalah <b>Golongan 1 (Godan)</b>. Konjugasinya kitte, bukan kite!'
    },
    {
        'w': '探す', 'y': 'さがす', 'a': 'Mencari', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '鍵を探しています。', 'ei': 'Sedang mencari kunci.',
        'ch': [('探', 'さが.す', 'タン', '[Radikal: 扌 (Tangan)] + [Komponen: 罙 (Ke dalam/Gua)]')],
        'co': 'Bayangkan tanganmu (扌) sedang merogoh-rogoh lubang (罙) yang dalam untuk menemukan kunci yang hilang. Mengaduk-aduk tempat yang sulit dijangkau demi menemukan sesuatu: <b>Mencari</b>.'
    },
    {
        'w': '死ぬ', 'y': 'しぬ', 'a': 'Mati / Meninggal', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '交通事故で死にました。', 'ei': 'Meninggal karena kecelakaan lalu lintas.',
        'ch': [('死', 'し.ぬ', 'シ', '[Radikal: 歹 (Tulang belulang)] + [Komponen: 匕 (Orang rebahan)]')],
        'co': 'Kanji yang cukup mengerikan. Ada tulang belulang berserakan (歹) milik seseorang yang terkapar kaku tak bernyawa (匕). Satu-satunya kata kerja N5 berakhiran "nu". Te form: 死んで (Shinde).'
    },
    {
        'w': '使う', 'y': 'つかう', 'a': 'Menggunakan / Memakai', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'パソコンを使います。', 'ei': 'Menggunakan komputer.',
        'ch': [('使', 'つか.う', 'シ', '[Radikal: 亻 (Orang)] + [Komponen: 吏 (Petugas pemerintah)]')],
        'co': 'Pada masa feodal, bermakna <b>mengutus orang</b> (memakai tenaga manusia untuk menjalankan perintah). Sekarang berevolusi jadi bermakna mengoperasikan benda mati demi mencapai suatu tujuan. <b>Menggunakan / Memakai</b>.'
    },
    {
        'w': '作る', 'y': 'つくる', 'a': 'Membuat / Memproduksi', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ケーキを作ります。', 'ei': 'Membuat kue.',
        'ch': [('作', 'つく.る', 'サク / サ', '[Radikal: 亻 (Orang)] + [Komponen: 乍 (Kerah baju yang sedang dipotong pisau)]')],
        'co': 'Seseorang (亻) mengerahkan keterampilannya untuk memotong, memahat, atau merangkai material menggunakan perkakas (乍) menjadi sesuatu yang baru. <b>Membuat dari nol</b>. Golongan 1 (Tsukutte, Tsukuranai).'
    },
    {
        'w': '手伝う', 'y': 'てつだう', 'a': 'Membantu (Tenaga)', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '母の料理を手伝います。', 'ei': 'Membantu ibu memasak.',
        'ch': [
            ('手', 'て', 'シュ', '[Radikal: 手 (Tangan)]'),
            ('伝', 'つた.わる / つた.う', 'デン', '[Radikal: 亻 (Orang)] + [Komponen: 云 (Awan/Kata-kata)]')
        ],
        'co': 'Secara harfiah: "Meneruskan/menyampaikan Tangan". Kamu mengulurkan bantuan fisik (Tenaga Tanganmu) kepada orang lain untuk meringankan pekerjaannya. <b>Bantu-bantu / Menolong orang</b>.'
    },
    {
        'w': '取る', 'y': 'とる', 'a': 'Mengambil', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'そこの塩を取ってください。', 'ei': 'Tolong ambilkan garam di situ.',
        'ch': [('取', 'と.る', 'シュ', '[Radikal: 耳 (Telinga)] + [Komponen: 又 (Tangan Kanan)]')],
        'co': 'Etimologinya kelam! Di medan perang kuno, tangan kanan (又) mengambil telinga musuh (耳) yang terpenggal sebagai bukti kemenangan. Kini sekadar <b>Mengambil benda</b> dengan tangan.'
    },
    {
        'w': '習う', 'y': 'ならう', 'a': 'Belajar (Dengari bimbingan)', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': 'ピアノを習っています。', 'ei': 'Sedang belajar piano.',
        'ch': [('習', 'なら.う', 'シュウ', '[Radikal: 羽 (Sayap/Bulu)] + [Komponen: 白 (Putih/Sinar matahari)]')],
        'co': 'Burung kecil yang sayapnya (羽) mengembang berlatih mengepak di bawah cerahnya matahari (白). Bermakna <b>Belajar keterampilan / Berlatih dengan tekun</b> secara kontinu dari seorang guru.'
    },
    {
        'w': '乗る', 'y': 'のる', 'a': 'Naik (Kendaraan)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '電車に乗ります。', 'ei': 'Naik kereta api.',
        'ch': [('乗', 'の.る', 'ジョウ', '[Radikal: 禾 (Pohon)] + [Komponen: 北 (Bertentangan/Utara)]')],
        'co': 'Visualisasikan seseorang yang kakinya dinaikkan ke atas untuk menaiki sebuah kendaraan (kereta, kuda, mobil). Harus pakai partikel "Ni". <b>Menaiki sesuatu yang membawamu pergi.</b>'
    }
]
