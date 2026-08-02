# -*- coding: utf-8 -*-
# Batch 8: Restored missing entries with premium quality (FINAL)
CARDS = [
    {
        'w': '下げる', 'y': 'さげる', 'a': 'Menurunkan / Menggantung', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '値段を下げます。', 'ei': 'Menurunkan harga.',
        'ch': [('下', 'さ.げる / した', 'カ / ゲ', '[Radikal: 一 (Garis dasar)] + [Komponen: 卜 (Tongkat ke bawah)]')],
        'co': 'Garis horizontal (tanah) dengan tanda menunjuk ke bawah. Kebalikan dari 上げる. <b>Menurunkan (harga/suhu/volume) / Menggantung benda</b>.'
    },
    {
        'w': '辞める', 'y': 'やめる', 'a': 'Berhenti / Mengundurkan diri', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '会社を辞めます。', 'ei': 'Mengundurkan diri dari perusahaan.',
        'ch': [('辞', 'や.める', 'ジ', '[Radikal: 辛 (Pedas/Menderita)] + [Komponen: 舌 (Lidah)]')],
        'co': 'Lidah (舌) mengucapkan kata-kata pedih (辛) berupa surat pengunduran diri. <b>Resign / Berhenti dari pekerjaan</b>. Beda dengan 止める (menghentikan aksi).'
    },
    {
        'w': '会う', 'y': 'あう', 'a': 'Bertemu', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '友達に会います。', 'ei': 'Bertemu teman.',
        'ch': [('会', 'あ.う', 'カイ', '[Radikal: 𠆢 (Penutup/Atap)] + [Komponen: 云 (Awan/Berkumpul)]')],
        'co': 'Sekelompok orang berkumpul (云) di bawah satu atap (𠆢) untuk saling berjumpa. <b>Bertemu seseorang (dengan sengaja/janjian)</b>. Pakai partikel に.'
    },
    {
        'w': '合う', 'y': 'あう', 'a': 'Cocok / Sesuai', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'この服が私に合います。', 'ei': 'Baju ini cocok untuk saya.',
        'ch': [('合', 'あ.う', 'ゴウ', '[Radikal: 合 (Menyatu)]')],
        'co': 'Penutup (𠆢) yang dipasangkan ke mulut wadah (口) menempel dengan sempurna tanpa celah. <b>Cocok / Sesuai / Pas</b>. Beda kanji dengan 会う (bertemu)!'
    },
    {
        'w': '付き合う', 'y': 'つきあう', 'a': 'Berpacaran / Bergaul', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '彼女と付き合っています。', 'ei': 'Sedang berpacaran dengannya.',
        'ch': [
            ('付', 'つ.く', 'フ', '[Radikal: 亻 (Orang)] + [Komponen: 寸 (Ukuran/Tangan)]'),
            ('合', 'あ.う', 'ゴウ', '[Radikal: 口 (Mulut)] + [Komponen: 亼 (Mengumpulkan)]')
        ],
        'co': 'Dua orang saling menempel (付) dan cocok (合) satu sama lain. <b>Berpacaran / Menjalin hubungan / Menemani bergaul</b>.'
    },
    {
        'w': '結婚する', 'y': 'けっこんする', 'a': 'Menikah', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '来年結婚します。', 'ei': 'Tahun depan menikah.',
        'ch': [
            ('結', 'むす.ぶ', 'ケツ', '[Radikal: 糸 (Benang)] + [Komponen: 吉 (Beruntung)]'),
            ('婚', 'コン', 'コン', '[Radikal: 女 (Perempuan)] + [Komponen: 昏 (Senja)]')
        ],
        'co': 'Mengikat benang takdir (結) pada saat upacara senja hari (婚) ketika wanita (女) resmi dipersunting. <b>Menikah / Pernikahan</b>.'
    },
    {
        'w': '婚約する', 'y': 'こんやくする', 'a': 'Bertunangan', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '先月婚約しました。', 'ei': 'Bulan lalu bertunangan.',
        'ch': [
            ('婚', 'コン', 'コン', '[Radikal: 女 (Perempuan)] + [Komponen: 昏 (Senja)]'),
            ('約', 'ヤク', 'ヤク', '[Radikal: 糸 (Benang)] + [Komponen: 勺 (Cendok)]')
        ],
        'co': 'Membuat perjanjian/kontrak (約) untuk pernikahan (婚) di masa depan. <b>Bertunangan / Engagement</b>.'
    },
    {
        'w': '回す', 'y': 'まわす', 'a': 'Memutar (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ハンドルを回します。', 'ei': 'Memutar stir.',
        'ch': [('回', 'まわ.す', 'カイ', '[Radikal: 囗 (Kotak)] + [Komponen: 口 (Mulut/Pusat)]')],
        'co': 'Ada sebuah pusat (口) yang dikelilingi oleh orbit lingkaran (囗). <b>Memutar benda (stir, sekrup, gagang) secara transitif</b>.'
    },
    {
        'w': '無くす', 'y': 'なくす', 'a': 'Menghilangkan / Kehilangan (Transitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '財布を無くしました。', 'ei': 'Kehilangan dompet.',
        'ch': [('無', 'な.い', 'ム / ブ', '[Radikal: 灬 (Api)] + [Komponen: 舞 (Menari)]')],
        'co': 'Api yang menari (舞 + 灬) membakar segalanya sampai tidak bersisa. Kamu yang menyebabkan sesuatu <b>Hilang/Lenyap (Transitif)</b>. "Gue ngilangin kunci!"'
    },
    {
        'w': '思い出す', 'y': 'おもいだす', 'a': 'Teringat / Mengingat kembali', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '昔のことを思い出しました。', 'ei': 'Teringat kejadian masa lalu.',
        'ch': [
            ('思', 'おも.う', 'シ', '[Radikal: 心 (Hati)] + [Komponen: 田 (Sawah/Otak)]'),
            ('出', 'だ.す', 'シュツ', '[Radikal: 凵 (Wadah terbuka)] + [Komponen: 山 (Gunung)]')
        ],
        'co': 'Mengeluarkan (出す) kembali ingatan lama dari dalam pikiran (思い). Memori yang tadinya tersimpan terkubur di dasar otak kini muncul ke permukaan. <b>Teringat mendadak / Recall</b>.'
    },
    {
        'w': '動く', 'y': 'うごく', 'a': 'Bergerak (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '電車が動きません。', 'ei': 'Kereta tidak bergerak.',
        'ch': [('動', 'うご.く', 'ドウ', '[Radikal: 力 (Tenaga)] + [Komponen: 重 (Berat)]')],
        'co': 'Mengerahkan tenaga (力) untuk menggeser beban berat (重) dari titik A ke B. <b>Bergerak / Beraksi (Intransitif)</b>. Benda itu yang bergerak sendiri.'
    },
    {
        'w': '吸う', 'y': 'すう', 'a': 'Menghisap / Menghirup', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'タバコを吸います。', 'ei': 'Menghisap rokok.',
        'ch': [('吸', 'す.う', 'キュウ', '[Radikal: 口 (Mulut)] + [Komponen: 及 (Mencapai/Menarik)]')],
        'co': 'Mulut (口) menarik (及) gas/cairan dari luar masuk ke dalam paru-paru. <b>Menghisap rokok / Menghirup udara segar</b>.'
    },
    {
        'w': '上手くなる', 'y': 'うまくなる', 'a': 'Menjadi mahir / Jadi pintar', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '日本語が上手くなりました。', 'ei': 'Jadi mahir bahasa Jepang.',
        'ch': [
            ('上', 'うえ', 'ジョウ', '[Radikal: 一 (Satu)] + [Komponen: 卜 (Ramalan)]'),
            ('手', 'て', 'シュ', '[Radikal: 手 (Tangan)]'),
        ],
        'co': 'Kemampuan tanganmu (手) naik ke level atas (上) sehingga kamu <b>Menjadi mahir / Jadi jago</b> dalam suatu skill.'
    },
    {
        'w': '剥く', 'y': 'むく', 'a': 'Mengupas (Kulit buah)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'りんごの皮を剥きます。', 'ei': 'Mengupas kulit apel.',
        'ch': [('剥', 'む.く', 'ハク', '[Radikal: 刂 (Pisau)] + [Komponen: 录 (Mencakar)]')],
        'co': 'Pisau (刂) yang mencakar (录) permukaan kulit buah dan menariknya lepas dari daging buah. <b>Mengupas kulit buah / Menguliti</b>.'
    },
    {
        'w': '渡る', 'y': 'わたる', 'a': 'Menyeberang', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '橋を渡ります。', 'ei': 'Menyeberangi jembatan.',
        'ch': [('渡', 'わた.る', 'ト', '[Radikal: 氵 (Air)] + [Komponen: 度 (Ukuran/Kali)]')],
        'co': 'Mengukur (度) lebar sungai (氵) lalu berjalan menembus arus dari tepi satu ke tepi lainnya. <b>Menyeberang jalan / Menyeberangi sungai</b>.'
    },
    {
        'w': '曲がる', 'y': 'まがる', 'a': 'Berbelok / Melengkung', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '次の角を右に曲がります。', 'ei': 'Berbelok ke kanan di tikungan berikutnya.',
        'ch': [('曲', 'ま.がる', 'キョク', '[Radikal: 曲 (Bengkok)]')],
        'co': 'Bentuk kanji ini sendiri sudah terlihat seperti garis-garis yang <b>melengkung bengkok</b>. <b>Berbelok di persimpangan / Bengkok (Intransitif)</b>.'
    },
    {
        'w': '止まる', 'y': 'とまる', 'a': 'Berhenti (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'バスが止まりました。', 'ei': 'Bus berhenti.',
        'ch': [('止', 'と.まる', 'シ', '[Radikal: 止 (Kaki berhenti)]')],
        'co': 'Jejak telapak kaki yang membeku di tempat dan tidak melanjutkan langkah. <b>Berhenti bergerak secara otomatis (Intransitif)</b>.'
    },
    {
        'w': '触る', 'y': 'さわる', 'a': 'Menyentuh', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '触らないでください。', 'ei': 'Tolong jangan disentuh.',
        'ch': [('触', 'さわ.る', 'ショク', '[Radikal: 角 (Tanduk)] + [Komponen: 虫 (Serangga)]')],
        'co': 'Serangga (虫) menggunakan tanduk/antenanya (角) untuk meraba dan menyentuh permukaan benda asing. <b>Menyentuh / Meraba</b>.'
    },
    {
        'w': '点ける', 'y': 'つける', 'a': 'Menyalakan (Lampu/Api)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '電気を点けてください。', 'ei': 'Tolong nyalakan lampunya.',
        'ch': [('点', 'つ.ける', 'テン', '[Radikal: 灬 (Api)] + [Komponen: 占 (Meramal/Titik)]')],
        'co': 'Menyalakan titik api kecil (占) hingga membara (灬). Kebalikan dari 消す (mematikan). <b>Menyalakan lampu / Menyulut api</b>.'
    },
    {
        'w': '掛ける', 'y': 'かける', 'a': 'Menggantung / Menelepon', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '壁に絵を掛けます。', 'ei': 'Menggantung lukisan di dinding.',
        'ch': [('掛', 'か.ける', 'カイ', '[Radikal: 扌 (Tangan)] + [Komponen: 卦 (Gantungan/Tanda)]')],
        'co': 'Tangan (扌) mengangkat benda lalu menggantungkannya (卦) di paku dinding. <b>Menggantung / Menelepon (電話を掛ける) / Memakai kacamata</b>.'
    },
    {
        'w': '変える', 'y': 'かえる', 'a': 'Mengubah (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '予定を変えます。', 'ei': 'Mengubah rencana.',
        'ch': [('変', 'か.える', 'ヘン', '[Radikal: 変 (Berubah)]')],
        'co': 'Versi transitif dari 変わる. KAMU yang secara sadar dan sengaja <b>Mengubah</b> rencana/situasi/desain. Subjek = pelaku perubahan.'
    },
    {
        'w': '降ろす', 'y': 'おろす', 'a': 'Menurunkan (Dari kendaraan/Uang ATM)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'お金を降ろします。', 'ei': 'Menurunkan (menarik) uang dari ATM.',
        'ch': [('降', 'お.ろす', 'コウ', '[Radikal: 阝 (Bukit)] + [Komponen: 夅 (Turun)]')],
        'co': 'Versi transitif dari 降りる. Kamu aktif <b>Menurunkan penumpang dari kendaraan / Menarik uang dari ATM (tabungan di atas diturunkan ke tangan)</b>.'
    },
    {
        'w': '返す', 'y': 'かえす', 'a': 'Mengembalikan (Barang pinjaman)', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '本を図書館に返します。', 'ei': 'Mengembalikan buku ke perpustakaan.',
        'ch': [('返', 'かえ.す', 'ヘン', '[Radikal: 辶 (Jalan)] + [Komponen: 反 (Membalik)]')],
        'co': 'Berjalan (辶) dan membalikkan (反) barang pinjaman ke tangan pemilik aslinya. <b>Mengembalikan buku / Membalas email</b>.'
    },
    {
        'w': '汚す', 'y': 'よごす', 'a': 'Mengotori (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '服を汚しました。', 'ei': 'Mengotori baju.',
        'ch': [('汚', 'よご.す', 'オ', '[Radikal: 氵 (Air)] + [Komponen: 亏 (Menyimpang/Rusak)]')],
        'co': 'Air murni (氵) yang tercampur kotoran hingga menyimpang (亏) dari kejernihan aslinya. Kamu yang menyebabkan: <b>Mengotori / Mencemari (Transitif)</b>.'
    },
    {
        'w': '汚れる', 'y': 'よごれる', 'a': 'Kotor / Ternoda (Intransitif)', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '白いシャツが汚れました。', 'ei': 'Kemeja putih jadi kotor.',
        'ch': [('汚', 'よご.れる', 'オ', '[Radikal: 汚 (Kotor)]')],
        'co': 'Versi intransitif. Kemeja putih itu <b>Kotor/Ternoda sendiri</b> tanpa siapapun yang sengaja mengotorinya.'
    },
    {
        'w': '無くなる', 'y': 'なくなる', 'a': 'Habis / Hilang (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'お金が無くなりました。', 'ei': 'Uang sudah habis.',
        'ch': [('無', 'な.い', 'ム', '[Radikal: 無 (Tidak ada)]')],
        'co': 'Versi intransitif dari 無くす. Barang itu <b>Hilang/Habis dengan sendirinya</b>. "Uangku habis!" (bukan "aku menghabiskan").'
    },
    {
        'w': '産む', 'y': 'うむ', 'a': 'Melahirkan', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '赤ちゃんを産みました。', 'ei': 'Melahirkan bayi.',
        'ch': [('産', 'う.む', 'サン', '[Radikal: 生 (Lahir)] + [Komponen: 彦 (Orang berdiri) + 亠 (Penutup)]')],
        'co': 'Kehidupan (生) yang baru muncul ke dunia dari rahim seorang ibu. <b>Melahirkan bayi / Menghasilkan produk</b>.'
    },
    {
        'w': '生まれる', 'y': 'うまれる', 'a': 'Dilahirkan / Terlahir', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '東京で生まれました。', 'ei': 'Dilahirkan di Tokyo.',
        'ch': [('生', 'う.まれる', 'セイ', '[Radikal: 生 (Kehidupan)]')],
        'co': 'Versi intransitif dari 産む. Bukan "ibu yang melahirkan", tapi <b>Bayi yang terlahir ke dunia</b>. "Aku lahir di Tokyo."'
    },
    {
        'w': '慣れる', 'y': 'なれる', 'a': 'Terbiasa', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '日本の生活に慣れました。', 'ei': 'Sudah terbiasa dengan kehidupan di Jepang.',
        'ch': [('慣', 'な.れる', 'カン', '[Radikal: 忄 (Hati)] + [Komponen: 貫 (Menembus)]')],
        'co': 'Hati (忄) yang ditusuk pengalaman berulang-ulang (貫) sampai akhirnya kebal dan tidak kaget lagi. <b>Terbiasa / Sudah familiar</b> dengan budaya/kebiasaan baru.'
    },
    {
        'w': '掛かる', 'y': 'かかる', 'a': 'Tergantung / Memakan (Waktu/Biaya)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '一時間掛かります。', 'ei': 'Memakan waktu satu jam.',
        'ch': [('掛', 'か.かる', 'カイ', '[Radikal: 扌 (Tangan)] + [Komponen: 卦 (Tanda gantung)]')],
        'co': 'Versi intransitif dari 掛ける. <b>Tergantung di paku / Memakan waktu / Butuh biaya segini</b>. "Berapa lama kakaru?"'
    },
    {
        'w': '込む', 'y': 'こむ', 'a': 'Padat / Penuh sesak', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '電車が込んでいます。', 'ei': 'Kereta sedang padat/penuh.',
        'ch': [('込', 'こ.む', 'コミ', '[Radikal: 辶 (Jalan)] + [Komponen: 入 (Masuk)]')],
        'co': 'Banyak orang berjalan (辶) dan masuk (入) ke satu tempat secara bersamaan. <b>Padat sesak / Crowded</b>. 混む juga dipakai.'
    },
    {
        'w': '間違える', 'y': 'まちがえる', 'a': 'Salah / Keliru (Transitif)', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '答えを間違えました。', 'ei': 'Salah menjawab.',
        'ch': [
            ('間', 'ま', 'カン', '[Radikal: 門 (Gerbang)] + [Komponen: 日 (Matahari)]'),
            ('違', 'ちが.う', 'イ', '[Radikal: 辶 (Jalan/Pergerakan)] + [Komponen: 韋 (Saling Membelakangi)]')
        ],
        'co': 'Jeda waktu (間) yang salah arah (違) sehingga jawabanmu meleset dari kebenaran. <b>Membuat kesalahan / Keliru (Transitif)</b>.'
    },
    {
        'w': '風邪を引く', 'y': 'かぜをひく', 'a': 'Masuk angin / Pilek', 'g': 1, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '風邪を引きました。', 'ei': 'Terkena masuk angin.',
        'ch': [
            ('風', 'かぜ', 'フウ', '[Radikal: 風 (Angin)]'),
            ('邪', 'よこし.ま', 'ジャ', '[Radikal: 阝 (Kota/Desa)] + [Komponen: 牙 (Taring)]'),
            ('引', 'ひ.く', 'イン', '[Radikal: 弓 (Busur)] + [Komponen: 丨 (Garis lurus)]')
        ],
        'co': 'Secara harfiah "menarik (引く) angin jahat (風邪)" ke dalam tubuhmu. Ungkapan tetap (idiom) yang harus dihafal utuh. <b>Terkena flu / Masuk angin</b>.'
    },
    {
        'w': '咳が出る', 'y': 'せきがでる', 'a': 'Batuk (Keluar batuk)', 'g': 2, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '咳が出ます。', 'ei': 'Batuk (keluar batuk).',
        'ch': [
            ('咳', 'せき', '-', '[Radikal: 口 (Mulut)] + [Komponen: 亥 (Babi Hutan)]'),
            ('出', 'で.る', 'シュツ', '[Radikal: 凵 (Wadah terbuka)] + [Komponen: 山 (Gunung)]')
        ],
        'co': 'Batuk (咳) yang "keluar" (出る) dari mulutmu. Pola ga deru ini khas gejala medis Jepang: <b>Gejala yang muncul secara otomatis</b>.'
    },
    {
        'w': '病気に罹る', 'y': 'びょうきにかかる', 'a': 'Terjangkit penyakit', 'g': 1, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': 'インフルエンザに罹りました。', 'ei': 'Terjangkit influenza.',
        'ch': [
            ('病', 'やまい', 'ビョウ', '[Radikal: 疒 (Sakit)] + [Komponen: 丙 (Ketiga)]'),
            ('気', 'き', 'キ', '[Radikal: 气 (Udara/Hawa)] + [Komponen: 乂 (Menyilang)]'),
            ('罹', 'かか.る', 'リ', '[Radikal: 网 (Jaring)] + [Komponen: 惟 (Burung)]')
        ],
        'co': 'Energi jahat penyakit (病気) menjerat (罹) tubuhmu layaknya jaring. <b>Terjangkit/Kena penyakit serius</b>.'
    },
    {
        'w': '頭痛がする', 'y': 'ずつうがする', 'a': 'Sakit kepala', 'g': 3, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '頭痛がします。', 'ei': 'Saya sakit kepala.',
        'ch': [
            ('頭', 'あたま', 'ズ', '[Radikal: 頁 (Kepala)] + [Komponen: 豆 (Kacang)]'),
            ('痛', 'いた.い', 'ツウ', '[Radikal: 疒 (Sakit)] + [Komponen: 甬 (Terowongan)]')
        ],
        'co': 'Kepala (頭) yang berdenyut nyeri (痛) seolah ditusuk-tusuk. Pola ～がする berarti gejala yang "terjadi/terasa". <b>Sakit kepala</b>.'
    },
    {
        'w': '挫く', 'y': 'くじく', 'a': 'Keseleo / Terkilir', 'g': 1, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '足首を挫きました。', 'ei': 'Pergelangan kaki keseleo.',
        'ch': [('挫', 'くじ.く', 'ザ', '[Radikal: 扌 (Tangan)] + [Komponen: 坐 (Duduk/Jatuh)]')],
        'co': 'Tangan atau kaki yang terjatuh (坐) terpelintir secara tidak wajar. <b>Keseleo / Terkilir pergelangan</b>.'
    }
]
