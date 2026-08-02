# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '起きる', 'y': 'おきる', 'a': 'Bangun / Terjadi', 'g': 2, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '毎朝６時に起きます。', 'ei': 'Setiap pagi bangun jam 6.',
        'ch': [('起', 'お.きる / お.こす', 'キ', '[Radikal: 走 (Berlari/Berjalan)] + [Komponen: 己 (Diri sendiri/Ular)]')],
        'co': 'Orang yang tadinya rebahan tidur, kini perlahan bangkit lalu tubuhnya (己) mulai berjalan/beraktivitas (走). <b>Bangun tidur</b> atau <b>terjadinya suatu insiden</b>.'
    },
    {
        'w': '寝る', 'y': 'ねる', 'a': 'Tidur / Rebahan', 'g': 2, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '昨夜、遅く寝ました。', 'ei': 'Tadi malam tidur larut.',
        'ch': [('寝', 'ね.る', 'シン', '[Radikal: 宀 (Atap rumah)] + [Komponen: 爿 (Ranjang) + 帚 (Sapu/Tangan rebahan)]')],
        'co': 'Berada di dalam rumah di bawah atap (宀), kamu membaringkan diri di atas ranjang (爿) untuk beristirahat. <b>Tidur / Membaringkan diri</b>. (Beda dengan 眠る/nemuru yang spesifik "memejamkan mata/terlelap").'
    },
    {
        'w': '立つ', 'y': 'たつ', 'a': 'Berdiri', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '立ってください。', 'ei': 'Tolong berdiri.',
        'ch': [('立', 'た.つ', 'リツ', '[Radikal: 立 (Berdiri)]')],
        'co': 'Bentuk Kanji ini sangat ikonik. Ada sebuah garis horizontal yang melambangkan tanah, dan ada tubuh beserta kaki yang <b>berdiri lurus / tegak</b> di atasnya. <b>Berdiri</b>.'
    },
    {
        'w': '座る', 'y': 'すわる', 'a': 'Duduk', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '椅子に座ります。', 'ei': 'Duduk di kursi.',
        'ch': [('座', 'すわ.る', 'ザ', '[Radikal: 广 (Rumah/Tebing)] + [Komponen: 坐 (Dua orang duduk di atas tanah)]')],
        'co': 'Ada dua orang (人人) yang pantatnya saling menempel ke tanah (土) di bawah sebuah atap/tebing (广) peneduh. Menandakan aktivitas <b>Duduk santai</b> atau tempat duduk (Za).'
    },
    {
        'w': '開ける', 'y': 'あける', 'a': 'Membuka (Pintu/Jendela)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ドアを開けます。', 'ei': 'Membuka pintu.',
        'ch': [('開', 'あ.ける / ひら.く', 'カイ', '[Radikal: 門 (Gerbang)] + [Komponen: 幵 (Dua palang kayu terbuka sejajar)]')],
        'co': 'Dua daun pintu gerbang (門) yang palang kuncinya telah dilepas (幵) sehingga gerbang bisa didorong <b>terbuka</b>. Membuka sesuatu secara fisik. Transitive verb (butuh objek).'
    },
    {
        'w': '閉める', 'y': 'しめる', 'a': 'Menutup (Pintu/Jendela)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '窓を閉めてください。', 'ei': 'Tolong tutup jendela.',
        'ch': [('閉', 'し.める / と.じる', 'ヘイ', '[Radikal: 門 (Gerbang)] + [Komponen: 才 (Kayu penyangga/Bakat)]')],
        'co': 'Kamu mengambil sebuah balok kayu (才) lalu menyelipkannya ke tengah-tengah pintu gerbang (門) untuk menguncinya rapat-rapat. <b>Menutup rapat</b> benda fisik (pintu, laci, botol).'
    },
    {
        'w': '始まる', 'y': 'はじまる', 'a': 'Mulai / Dimulai', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '映画が始まります。', 'ei': 'Film akan dimulai.',
        'ch': [('始', 'はじ.まる / はじ.める', 'シ', '[Radikal: 女 (Wanita)] + [Komponen: 台 (Meja/Panggung)]')],
        'co': 'Dulu dipercaya peradaban umat manusia (atau kehidupan seseroang) <b>bermula</b> dari seorang rahim Wanita (女) yang dipuja bagai di atas panggung (台). <b>Sesuatu mulai terjadi (Intransitif)</b>.'
    },
    {
        'w': '終わる', 'y': 'おわる', 'a': 'Selesai / Berakhir', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '授業が終わりました。', 'ei': 'Pelajaran telah selesai.',
        'ch': [('終', 'お.わる', 'シュウ', '[Radikal: 糸 (Benang)] + [Komponen: 冬 (Musim dingin)]')],
        'co': 'Musim dingin (冬) adalah <b>akhir</b> dari siklus musim tahunan. Sama seperti benang (糸) rajutan yang sudah sampai ke ujung ikatannya, tandanya pekerjaan menjahitmu sudah <b>Selesai/Berakhir</b>.'
    },
    {
        'w': '分かる', 'y': 'わかる', 'a': 'Mengerti / Tahu', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '日本語が分かりますか？', 'ei': 'Apakah Anda mengerti bahasa Jepang?',
        'ch': [('分', 'わ.かる / わ.ける', 'ブン / フン', '[Radikal: 刀 (Pisau)] + [Komponen: 八 (Membelah dua)]')],
        'co': 'Mengambil pisau (刀) untuk membelah (八) masalah ruwet jadi bagian kecil-kecil sehingga struktur dalamnya terlihat jelas. Kalau udah jelas, lu pasti <b>Paham / Mengerti (Wakaru)</b>.'
    },
    {
        'w': '覚える', 'y': 'おぼえる', 'a': 'Mengingat / Menghafal', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '漢字を覚えます。', 'ei': 'Menghafal Kanji.',
        'ch': [('覚', 'おぼ.える / さ.める', 'カク', '[Radikal: 見 (Melihat)] + [Komponen: 𦥯 (Tangan mencengkeram ilmu yang bersinar)]')],
        'co': 'Mata kita melihat (見) lalu tangan kita meraup serpihan cahaya ilmu (𦥯) agar tidak lepas. Memasukkan informasi ke otak secara sadar: <b>Menghafal / Mengingat-ingat</b> materi atau wajah orang.'
    },
    {
        'w': '忘れる', 'y': 'わすれる', 'a': 'Lupa / Melupakan', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '約束を忘れました。', 'ei': 'Lupa akan janji.',
        'ch': [('忘', 'わす.れる', 'ボウ', '[Radikal: 心 (Hati/Pikiran)] + [Komponen: 亡 (Hilang/Mati)]')],
        'co': 'Logika Kanji yang brilian! Jika suatu ingatan di Hati/Pikiranmu (心) sudah Hilang/Mati (亡), itu artinya lu <b>Lupa (Wasureru)</b>. Lupa naruh dompet, lupa mantan, semuanya pakai kata ini.'
    },
    {
        'w': '考える', 'y': 'かんがえる', 'a': 'Berpikir / Merenungkan', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '将来について考えます。', 'ei': 'Berpikir tentang masa depan.',
        'ch': [('考', 'かんが.える', 'コウ', '[Radikal: 老 (Orang Tua)] + [Komponen: 丂 (Napas meliuk-liuk)]')],
        'co': 'Membayangkan seorang Kakek yang sudah makan asam garam (老), menarik napas panjang meliuk-liuk (丂) untuk mencari solusi bijak. Tindakan otak yang dalam: <b>Berpikir analisis / Merenungkan keputusan</b>.'
    },
    {
        'w': '教える', 'y': 'おしえる', 'a': 'Mengajar / Memberitahu', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '英語を教えています。', 'ei': 'Sedang mengajar bahasa Inggris.',
        'ch': [('教', 'おし.える', 'キョウ', '[Radikal: 攵 (Pukulan tongkat)] + [Komponen: 孝 (Berbakti/Anak yang taat pada orang tua)]')],
        'co': 'Orang dewasa mengayunkan tongkat (攵) untuk membimbing anak (孝) ke jalan yang benar. <b>Mengajari ilmu</b>. Uniknya, di Jepang kata ini lazim dipakai untuk <b>Memberitahu informasi/alamat</b> (Kasih tau dong!).'
    },
    {
        'w': '気を付ける', 'y': 'きをつける', 'a': 'Berhati-hati / Memperhatikan', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '車に気を付けてください。', 'ei': 'Tolong berhati-hati terhadap mobil.',
        'ch': [
            ('気', 'き', 'キ', '[Radikal: 气 (Udara/Hawa)] + [Komponen: 乂 (Menyilang)]'),
            ('付', 'つ.ける', 'フ', '[Radikal: 亻 (Orang)] + [Komponen: 寸 (Ukuran/Tangan)]')
        ],
        'co': 'Frasa ajaib ini berarti kamu secara sadar mengambil Energi/Perhatianmu (気) lalu menempelkannya (付ける) kuat-kuat ke suatu objek/pekerjaan. Fokus 100% alias <b>Take Care / Hati-hati</b>.'
    },
    {
        'w': '建てる', 'y': 'たてる', 'a': 'Mendirikan / Membangun', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '新しい家を建てます。', 'ei': 'Membangun rumah baru.',
        'ch': [('建', 'た.てる', 'ケン', '[Radikal: 廴 (Langkah jauh/panjang)] + [Komponen: 聿 (Kuas/Tiang tegak)]')],
        'co': 'Pelafalannya sama dengan 立つ (Berdiri), tapi ini spesifik untuk <b>Konstruksi Arsitektur (Mendirikan gedung/rumah)</b>. Ada unsur berjalan/proses (廴) sambil memancang tiang lurus tinggi (聿).'
    },
    {
        'w': '比べる', 'y': 'くらべる', 'a': 'Membandingkan', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '二つの車を比べます。', 'ei': 'Membandingkan dua mobil.',
        'ch': [('比', 'くら.べる', 'ヒ', '[Radikal: 比 (Rasio/Mensejajarkan dua orang)]')],
        'co': 'Kanji ini adalah gambar dua manusia yang berdiri sejajar (kanan dan kiri). Kamu mensejajarkan barang A dan B, lalu mencari perbedaannya (mana yang lebih murah, lebih bagus). <b>Membandingkan (Compare)</b>.'
    },
    {
        'w': '答える', 'y': 'こたえる', 'a': 'Menjawab', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '質問に答えてください。', 'ei': 'Tolong jawab pertanyaannya.',
        'ch': [('答', 'こた.える', 'トウ', '[Radikal: 竹 (Bambu)] + [Komponen: 合 (Menyatukan/Cocok)]')],
        'co': 'Dua potongan bambu silinder (竹) yang dipotong rapi dan digabungkan (合) sehingga menempel pas tanpa celah. Simbol <b>Jawaban yang benar</b> sangat pas (klop) dengan pertanyaan. <b>Menjawab tes</b>.'
    },
    {
        'w': '見学する', 'y': 'けんがくする', 'a': 'Kunjungan Studi / Observasi', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '工場を見学します。', 'ei': 'Melakukan kunjungan studi ke pabrik.',
        'ch': [
            ('見', 'み.る', 'ケン', '[Radikal: 見 (Melihat)]'),
            ('学', 'まな.ぶ', 'ガク', '[Radikal: 子 (Anak)] + [Komponen: 𦥯 (Atap dan Tangan)]')
        ],
        'co': 'Gampang nebaknya! Kamu Menggunakan matamu untuk <b>Melihat-lihat</b> (見) lapangan / museum / pabrik nyata demi tujuan <b>Belajar</b> (学). (Study Tour / Kunjungan Industri).'
    },
    {
        'w': '練習する', 'y': 'れんしゅうする', 'a': 'Berlatih (Fisik/Skill)', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': 'ピアノを毎日練習します。', 'ei': 'Berlatih piano setiap hari.',
        'ch': [
            ('練', 'ね.る', 'レン', '[Radikal: 糸 (Benang sutra)] + [Komponen: 東 (Timur)]'),
            ('習', 'なら.う', 'シュウ', '[Radikal: 羽 (Sayap)] + [Komponen: 白 (Putih)]')
        ],
        'co': 'Gabungan dari mengasah benang mentah dan burung kecil mengepak sayap terus menerus. Menunjukkan repetisi keras untuk membuang kelemahan. <b>Latihan Rutin (Practice)</b> olahraga atau bahasa.'
    },
    {
        'w': '復習する', 'y': 'ふくしゅうする', 'a': 'Mengulang Pelajaran (Review)', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': 'テストの前に復習します。', 'ei': 'Mengulang materi pelajaran sebelum ujian.',
        'ch': [
            ('復', 'フク', 'フク', '[Radikal: 彳 (Langkah kaki)] + [Komponen: 畐 (Perut penuh)]'),
            ('習', 'なら.う', 'シュウ', '[Radikal: 羽 (Sayap)] + [Komponen: 白 (Putih)]')
        ],
        'co': 'Materi yang dikasih sensei tadi siang dibaca ulang (kembali ke masa lalu/materi sebelumnya) saat malam hari di rumah. <b>Kilas Balik bacaan / Review Pelajaran</b>.'
    },
    {
        'w': '説明する', 'y': 'せつめいする', 'a': 'Menjelaskan / Menerangkan', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '理由を説明してください。', 'ei': 'Tolong jelaskan alasannya.',
        'ch': [
            ('説', 'と.く', 'セツ', '[Radikal: 言 (Kata-kata)] + [Komponen: 兌 (Senyum terbuka)]'),
            ('明', 'あか.るい', 'メイ', '[Radikal: 日 (Matahari)] + [Komponen: 月 (Bulan)]')
        ],
        'co': 'Mengolah kata-kata agar orang yang kebingungan langsung tersenyum paham (説). Penjelasan lu menyinari kegelapan sehingga masalahnya jadi <b>Terang benderang</b> (明). <b>Presentasi / Menjelaskan</b>.'
    },
    {
        'w': '失敗する', 'y': 'しっぱいする', 'a': 'Gagal / Kesalahan', 'g': 3, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '試験で失敗しました。', 'ei': 'Gagal dalam ujian.',
        'ch': [
            ('失', 'うしな.う', 'シツ', '[Radikal: 大 (Besar)] + [Komponen: 丿 (Coretan tergelincir)]'),
            ('敗', 'やぶ.れる', 'パイ', '[Radikal: 貝 (Kerang/Harta)] + [Komponen: 攵 (Memukul)]')
        ],
        'co': 'Kamu melepas kendali dan kehilangan (失) peluang, sehingga pekerjaanmu remuk hancur (敗) seperti kerang uang yang digeprek. Kesalahan telak! <b>Gagal/Fail (Shippai)</b>.'
    },
    {
        'w': '卒業する', 'y': 'そつぎょうする', 'a': 'Lulus Sekolah', 'g': 3, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '来年、大学を卒業します。', 'ei': 'Tahun depan lulus dari universitas.',
        'ch': [
            ('卒', 'ソツ', 'ソツ', '[Radikal: 十 (Sepuluh)] + [Komponen: 衣 (Baju seragam)]'),
            ('業', 'わざ', 'ギョウ', '[Radikal: 木 (Pohon)] + [Komponen: 业 (Papan instrumen)]')
        ],
        'co': 'Kamu sukses merampungkan semua beban Tugas (業) edukasi sampai ke titik Purna/Selesai masa tugas prajurit akademi (卒). Momen penuh haru pelemparan toga. <b>Lulus sekolah/kampus</b>.'
    },
    {
        'w': '質問する', 'y': 'しつもんする', 'a': 'Bertanya (Pertanyaan Akademik)', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '先生に質問します。', 'ei': 'Bertanya kepada guru.',
        'ch': [
            ('質', 'シツ', 'シツ', '[Radikal: 貝 (Kerang/Harta)] + [Komponen: 斤 (Kapak)]'),
            ('問', 'と.う', 'モン', '[Radikal: 門 (Gerbang)] + [Komponen: 口 (Mulut)]')
        ],
        'co': 'Menyelidiki suatu substansi/kualitas mendalam dari benda (質) dengan cara melontarkan pertanyaan tajam (問). Bukan basa-basi nanya nama jalan, tapi nanya <b>Materi / Problem solving akademik</b>.'
    },
    {
        'w': '疲れる', 'y': 'つかれる', 'a': 'Lelah / Capek', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '仕事で疲れました。', 'ei': 'Lelah karena pekerjaan.',
        'ch': [('疲', 'つか.れる', 'ヒ', '[Radikal: 疒 (Penyakit/Badan meriang)] + [Komponen: 皮 (Kulit luar)]')],
        'co': 'Rasa capek itu disamakan dengan <b>Penyakit</b> ringan (疒) di mana otot, tulang, dan kulit (皮) seluruh badan lu ngilu dan tegang semua setelah bekerja. <b>Capek / Lelah secara fisik</b>.'
    }
]
