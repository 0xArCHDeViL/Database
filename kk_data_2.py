# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '脱ぐ', 'y': 'ぬぐ', 'a': 'Melepas (Pakaian / Sepatu)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '靴を脱いでください。', 'ei': 'Tolong lepaskan sepatu.',
        'ch': [('脱', 'ぬ(ぐ) / ぬ(げる)', 'ダツ', 'Melepaskan. 月 (daging/tubuh) + 兌 (berubah/terlepas). Tubuh yang membebaskan diri/melepaskan sesuatu.')],
        'co': 'Tubuh (月) yang melepaskan ikatan (兌). Mengeluarkan badan dari kurungan kain atau sepatu. Ini dipakai khusus untuk <b>Melepas baju, celana, atau alas kaki</b>. Beda dengan 外す (melepas jam/kacamata).'
    },
    {
        'w': '入る', 'y': 'はいる', 'a': 'Masuk (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '部屋に入ります。', 'ei': 'Masuk ke kamar.',
        'ch': [('入', 'はい(る) / い(れる)', 'ニュウ', 'Masuk. (Piktogram ujung panah yang masuk/menembus ke dalam wadah atau celah).')],
        'co': 'Garis ujung panah menancap masuk. <b>Masuk ke dalam</b> ruang atau area. Awas jebakan N5: Meski berakhiran "iru", kata ini adalah <b>Golongan 1</b> (haitte, hairanai), BUKAN Golongan 2!'
    },
    {
        'w': '話す', 'y': 'はなす', 'a': 'Berbicara / Menceritakan', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '先生と話します。', 'ei': 'Berbicara dengan guru.',
        'ch': [('話', 'はな(す) / はなし', 'ワ', 'Bicara/Cerita. 言 (kata-kata) + 舌 (lidah). Lidah yang merangkai kata-kata menjadi tuturan yang hidup.')],
        'co': 'Kalau 言う (iu) itu sekadar melontarkan ucapan singkat, 話す (hanasu) adalah aksi mengolah kata (言) menggunakan lidah (舌) secara interaktif atau bercerita panjang. <b>Berbincang/Bicara</b>.'
    },
    {
        'w': '待つ', 'y': 'まつ', 'a': 'Menunggu', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': '駅で友達を待ちます。', 'ei': 'Menunggu teman di stasiun.',
        'ch': [('待', 'ま(つ)', 'タイ', 'Menunggu. 彳 (langkah berjalan) + 寺 (kuil/tempat singgah). Orang yang berhenti berjalan di halaman kuil untuk diam menunggu sesuatu.')],
        'co': 'Langkah kaki (彳) yang terhenti sejenak di depan kuil (寺). Kamu berdiam diri di satu titik sambil mengharapkan seseorang datang. <b>Menunggu</b>.'
    },
    {
        'w': '持つ', 'y': 'もつ', 'a': 'Memegang / Membawa', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'かばんを持ちます。', 'ei': 'Membawa/Memegang tas.',
        'ch': [('持', 'も(つ)', 'ジ', 'Membawa/Memegang. 扌 (tangan) + 寺 (kuil/berhenti tetap). Tangan yang menggenggam barang erat-erat dan menahannya tetap tidak jatuh.')],
        'co': 'Tangan (扌) yang menjaga (寺) suatu barang agar terus melekat bersamanya. Arti dasarnya <b>Memegang</b> erat (di tangan), dan meluas jadi <b>Membawa (barang)</b>. '
    },
    {
        'w': '持って行く', 'y': 'もっていく', 'a': 'Membawa Pergi (Barang)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '傘を持って行きます。', 'ei': 'Membawa pergi payung (ke tujuan).',
        'ch': [
            ('持', 'も(つ)', 'ジ', 'Memegang.'),
            ('行', 'い(く) / ゆ(く)', 'コウ / ギョウ', 'Pergi. 彳 (persimpangan jalan/langkah kaki).')
        ],
        'co': 'Gabungan dari 持つ (Memegang di tangan) + 行く (Pergi ke arah sana). Kamu berjalan menjauh dari pembicara sambil menenteng barang. <b>Membawa Pergi</b>.'
    },
    {
        'w': '開ける', 'y': 'あける', 'a': 'Membuka (Transitif)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '窓を開けてください。', 'ei': 'Tolong buka jendelanya.',
        'ch': [('開', 'あ(ける) / ひら(く)', 'カイ', 'Membuka. 門 (gerbang) + 幵 (dua tiang yang rata/tangan yang merentangkan). Membuka daun gerbang lebar-lebar.')],
        'co': 'Tanganmu terentang lurus untuk mendorong dua sisi daun pintu gerbang (門). Aksi fisiknya adalah <b>Membuka</b> (pintu, jendela, buku). Golongan 2 (akete).'
    },
    {
        'w': '入れる', 'y': 'いれる', 'a': 'Memasukkan (Transitif)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '砂糖をコーヒーに入れます。', 'ei': 'Memasukkan gula ke kopi.',
        'ch': [('入', 'い(れる) / はい(る)', 'ニュウ', 'Memasukkan / Masuk.')],
        'co': 'Kanji panah menancap ke dalam wadah (入). Bedanya dengan 入る (Masuk secara otomatis), 入れる adalah kamu secara sengaja <b>memasukkan</b> objek A ke wadah B. Ini Golongan 2 lho (irete, irenai)!'
    },
    {
        'w': '片付ける', 'y': 'かたづける', 'a': 'Merapikan / Membereskan', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '机の上を片付けます。', 'ei': 'Merapikan bagian atas meja.',
        'ch': [
            ('片', 'かた', 'ヘン', 'Sebelah / Kepingan. Kayu utuh yang dibelah jadi dua, sebelah kanannya.'),
            ('付', 'つ(ける)', 'フ', 'Menempelkan. 亻 (orang) menyerahkan barang ke 寸 (tangan) orang lain.')
        ],
        'co': 'Mengambil kepingan-kepingan barang berserakan (片) lalu menempelkannya/mengembalikannya (付) ke rak atau posisi aslinya. Aksi <b>Membereskan / Merapikan ruangan</b>.'
    },
    {
        'w': '借りる', 'y': 'かりる', 'a': 'Meminjam', 'g': 2, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '図書館で本を借ります。', 'ei': 'Meminjam buku di perpustakaan.',
        'ch': [('借', 'か(りる)', 'シャク', 'Meminjam. 亻 (orang) + 昔 (masa lalu/tumpukan daging kuno). Orang yang mengambil barang sementara untuk diakumulasikan (pinjam).')],
        'co': 'Ingat terus pasangannya: 貸す (Kasu = Kasih pinjam orang lain). 借りる (Kariru) = <b>Kamu sendiri yang meminjam barang (dari orang lain)</b>. Karena Gol 2, bentuk Tenya (karite) dan Nainya (karinai).'
    },
    {
        'w': '着替える', 'y': 'きがえる', 'a': 'Ganti Baju', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'パジャマに着替えます。', 'ei': 'Berganti pakaian ke piyama.',
        'ch': [
            ('着', 'き(る)', 'チャク', 'Memakai baju atas.'),
            ('替', 'か(える)', 'タイ', 'Mengganti. 夫 (dua orang laki-laki sejajar) + 曰 (matahari/kata). Dua hal yang ditukar posisinya secara setara.')
        ],
        'co': 'Baju yang kamu pakai (着) kamu tanggalkan, lalu menukarnya (替) secara utuh dengan baju setelan baru. <b>Ganti seragam / Ganti baju</b>.'
    },
    {
        'w': '閉める', 'y': 'しめる', 'a': 'Menutup (Transitif)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'ドアを閉めます。', 'ei': 'Menutup pintu.',
        'ch': [('閉', 'し(める) / と(じる)', 'ヘイ', 'Menutup. 門 (gerbang) + 才 (palang kayu menyilang). Pintu gerbang yang dikunci dengan palang penghalang.')],
        'co': 'Memasang palang gembok (才) pada pintu gerbang (門) sehingga rapat dan tak bisa ditembus. Tentu saja itu artinya aksi <b>Menutup (pintu, jendela)</b>.'
    },
    {
        'w': '捨てる', 'y': 'すてる', 'a': 'Membuang', 'g': 2, 'subdeck': 'KK::Rumah_Tangga',
        'ej': 'ゴミを捨てます。', 'ei': 'Membuang sampah.',
        'ch': [('捨', 'す(てる)', 'シャ', 'Membuang. 扌 (tangan) + 舎 (gubuk/tempat singgah). Meninggalkan gubuk di belakang.')],
        'co': 'Tangan (扌) yang melepaskan benda tidak berguna dan meninggalkannya seperti gubuk usang (舎). <b>Membuang</b> sampah ke tempatnya atau membuang barang rongsok.'
    },
    {
        'w': '並べる', 'y': 'ならべる', 'a': 'Menjejerkan / Menyusun berbaris (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '本を棚に並べます。', 'ei': 'Menjejerkan buku di rak.',
        'ch': [('並', 'なら(べる)', 'ヘイ', 'Berjejer/Berbaris. (Piktogram dua orang berdiri berdampingan secara merata/rata).')],
        'co': 'Kamu bertindak menyusun objek-objek agar sejajar seperti orang berbaris (並). <b>Menderetkan / Menjejerkan</b> piring, buku, atau sepatu. Ini transitif, kamulah subjek pelakunya.'
    },
    {
        'w': '見せる', 'y': 'みせる', 'a': 'Memperlihatkan / Menunjukkan', 'g': 2, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': 'パスポートを見せてください。', 'ei': 'Tolong perlihatkan paspor Anda.',
        'ch': [('見', 'み(る) / み(せる)', 'ケン', 'Melihat/Memperlihatkan. 目 (mata) di atas 儿 (kaki orang yang berjalan melihat-lihat).')],
        'co': 'Berasal dari kata 見る (melihat). Tapi ada imbuhan "seru", sehingga maknanya beralih kausatif: membuat orang lain melihat sesuatu milikmu. <b>Memperlihatkan / Menunjukkan</b>.'
    },
    {
        'w': '見る', 'y': 'みる', 'a': 'Melihat / Menonton', 'g': 2, 'subdeck': 'KK::Sensori_Emosi',
        'ej': 'テレビを見ます。', 'ei': 'Menonton TV.',
        'ch': [('見', 'み(る)', 'ケン', 'Melihat.')],
        'co': 'Aktivitas penglihatan mata (目) secara visual dasar. Baik itu <b>Melihat</b> burung terbang, atau <b>Menonton</b> film di bioskop. Karena cuman 2 huruf, ingat ya ini Golongan 2 (Mite, Minai)!'
    },
    {
        'w': '着る', 'y': 'きる', 'a': 'Memakai / Mengenakan (Pakaian atas)', 'g': 2, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'シャツを着ます。', 'ei': 'Mengenakan kemeja.',
        'ch': [('着', 'き(る)', 'チャク', 'Mengenakan/Tiba. 羊 (bulu domba/pakaian hangat) + 目 (mata/tanda). Menempelkan baju wool ke badan sebagai pelindung.')],
        'co': 'Awas! Pelafalannya sama dengan 切る (memotong, Gol 1), tapi 着る (mengenakan baju atas) adalah <b>Golongan 2</b> (kite, kinai). Hanya berlaku untuk baju (kemeja, jas, kaos).'
    },
    {
        'w': '出来る', 'y': 'できる', 'a': 'Bisa (melakukan) / Selesai dibuat / Terjadi', 'g': 2, 'subdeck': 'KK::Kondisi_Status',
        'ej': '日本語が出来ます。 / 晩ご飯が出来ました。', 'ei': 'Bisa (berbahasa) Jepang. / Makan malam sudah jadi/siap.',
        'ch': [
            ('出', 'で(る) / だ(す)', 'シュツ', 'Keluar.'),
            ('来', 'く(る)', 'ライ', 'Datang.')
        ],
        'co': 'Keluar (出) dan Datang (来). Sesuatu yang "terwujud dan muncul ke permukaan". Punya 2 makna besar: <b>Mampu/Bisa</b> (karena potensimu keluar), dan <b>Selesai Dibuat</b> (nasinya sudah muncul di meja).'
    },
    {
        'w': '落ちる', 'y': 'おちる', 'a': 'Jatuh (dari atas ke bawah - Intransitif)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '木からりんごが落ちます。', 'ei': 'Apel jatuh dari pohon.',
        'ch': [('落', 'お(ちる)', 'ラク', 'Jatuh / Gugur. 艹 (tanaman) + 氵 (air hujan) + 各 (masing-masing/turun). Daun-daunan yang rontok diguyur hujan.')],
        'co': 'Bagai daun 艹 yang terlepas (rontok) karena tak kuat diterpa basahnya hujan deras. Kondisi di mana gravitasi menarik benda ke bawah secara pasif. <b>Jatuh</b> (ujian pun bisa ochi-ru alias tidak lulus).'
    },
    {
        'w': '注意する', 'y': 'ちゅういする', 'a': 'Memperingatkan / Berhati-hati', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '車に注意します。 / 先生が注意しました。', 'ei': 'Berhati-hati pada mobil. / Guru memberikan teguran.',
        'ch': [
            ('注', 'そそ(ぐ)', 'チュウ', 'Menuang / Mengarahkan. 氵 (air) + 主 (tuan/fokus). Menuangkan air terus-menerus ke satu titik utama.'),
            ('意', 'い', 'イ', 'Pikiran / Niat. 音 (suara) + 心 (hati). Suara dari dalam lubuk hati/fokus batin.')
        ],
        'co': 'Menuangkan/Mengarahkan (注) seluruh perhatian batinmu (意) pada suatu objek agar tidak celaka. <b>Berhati-hati</b>. Tapi kalau ke orang lain, artinya "memberi peringatan / menegur kelakuan".'
    },
    {
        'w': '出発する', 'y': 'しゅっぱつする', 'a': 'Berangkat', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '東京へ出発します。', 'ei': 'Berangkat ke Tokyo.',
        'ch': [
            ('出', 'で(る)', 'シュツ', 'Keluar.'),
            ('発', 'はっ', 'ハツ', 'Melontarkan / Memulai. 癶 (langkah kaki menjauh) + 弓 (busur) + 殳 (tombak). Melepaskan anak panah melesat menjauh.')
        ],
        'co': 'Keluar (出) menembus gerbang dan melesat maju (発) seperti panah menuju lokasi target. Kata yang elegan dan resmi untuk kereta, bus, atau manusia yang memulai perjalanan/<b>Berangkat</b>.'
    },
    {
        'w': '到着する', 'y': 'とうちゃくする', 'a': 'Tiba / Sampai', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '京都に到着しました。', 'ei': 'Telah tiba di Kyoto.',
        'ch': [
            ('到', 'いた(る)', 'トウ', 'Mencapai / Sampai. 至 (ujung tanah/sampai) + 刂 (pisau/memotong). Mencapai garis akhir dengan tegas.'),
            ('着', 'つ(く)', 'チャク', 'Tiba / Menempel.')
        ],
        'co': 'Lawan dari 出発. Menempuh perjalanan hingga mencapai titik akhir (到) lalu memarkirkan/menempelkan pijakan di sana (着). <b>Tiba atau Sampai di tujuan</b>.'
    },
    {
        'w': '運転する', 'y': 'うんてんする', 'a': 'Mengendarai / Mengemudi', 'g': 3, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '車を運転します。', 'ei': 'Mengemudikan mobil.',
        'ch': [
            ('運', 'はこ(ぶ)', 'ウン', 'Membawa/Menjalankan.'),
            ('転', 'ころ(がる)', 'テン', 'Berputar. 車 (mobil/roda) + 云 (awan/berotasi). Roda kendaraan yang berputar.')
        ],
        'co': 'Kamu bertindak memandu (運) roda gandar berputar (転) agar melaju membawa beban dengan selamat. Bisa setir mobil, kereta api, atau mengontrol alat berat berat. <b>Mengendarai / Mengoperasikan</b>.'
    },
    {
        'w': '出張する', 'y': 'しゅっちょうする', 'a': 'Dinas Luar Kota / Perjalanan Bisnis', 'g': 3, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '大阪へ出張します。', 'ei': 'Dinas luar kota ke Osaka.',
        'ch': [
            ('出', 'で(る)', 'シュツ', 'Keluar.'),
            ('張', 'は(る)', 'チョウ', 'Meregangkan / Meluaskan. 弓 (busur) + 長 (panjang). Menarik tali busur panjang-panjang, atau meluaskan kekuasaan ke tempat jauh.')
        ],
        'co': 'Keluar dari markas (出) dan merentangkan jangkauan penugasanmu jauh ke luar wilayah (張). Kamu bepergian bukan untuk main-main, tapi dibayar kantor. <b>Perjalanan Bisnis</b>.'
    },
    {
        'w': '発見する', 'y': 'はっけんする', 'a': 'Menemukan (Hal baru / Sesuatu yang tersembunyi)', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '新しい星を発見しました。', 'ei': 'Menemukan bintang (planet) baru.',
        'ch': [
            ('発', 'はっ', 'ハツ', 'Memunculkan / Mengeluarkan (sesuatu yang tersembunyi).'),
            ('見', 'み(る)', 'ケン', 'Melihat.')
        ],
        'co': 'Sesuatu yang asalnya tersembunyi, tiba-tiba memunculkan dirinya (発) dan berhasil kamu lihat (見) dengan mata kepalamu. Ini levelnya ilmiah atau penemuan besar, bukan sekadar menemukan kunci hilang. <b>Penemuan (Discover)</b>.'
    },
    {
        'w': '持って来る', 'y': 'もってくる', 'a': 'Datang Membawa (Barang)', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': 'パーティーに飲み物を持って来ました。', 'ei': 'Membawa minuman ke pesta (dan datang ke mari).',
        'ch': [
            ('持', 'も(つ)', 'ジ', 'Memegang.'),
            ('来', 'く(る)', 'ライ', 'Datang.')
        ],
        'co': 'Gabungan dari 持つ (memegang) dan 来る (datang ke mari mendekati pembicara). Kamu mendatangi lokasi ini sambil menenteng barang. <b>Datang Membawa</b>. Ireguler form: Motte kimasu.'
    },
    {
        'w': '遣る', 'y': 'やる', 'a': 'Melakukan (Kasual) / Memberi (ke bawahan/hewan)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '宿題をやる。 / 猫に餌をやる。', 'ei': 'Melakukan (mengerjakan) PR. / Memberi makan kucing.',
        'ch': [('遣', 'や(る) / つか(う)', 'ケン', 'Mengutus/Melakukan. 辶 (jalan) + 𠂤 (gundukan/barisan) yang diselipkan. Menyuruh orang bawahan pergi menyelesaikan tugas.')],
        'co': 'Biasanya ditulis tanpa kanji (やる). Bentuk agak kasar dari する (melakukan), seperti "Bakal gue lakuin!". Arti kedua yang sangat sering muncul: <b>Memberi sesuatu (kepada hewan/tanaman peliharaan/anak kecil)</b>.'
    },
    {
        'w': '習う', 'y': 'ならう', 'a': 'Mempelajari (dari orang lain)', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '先生から日本語を習います。', 'ei': 'Mempelajari bahasa Jepang dari guru.',
        'ch': [('習', 'なら(う)', 'シュウ', 'Mempelajari / Berlatih. 羽 (sayap) + 白 (aslinya matahari atau sarang putih). Anak burung kecil mengepak-ngepakkan sayap berkali-kali untuk belajar terbang.')],
        'co': 'Layaknya anak burung (羽) yang menirukan induknya terbang tanpa henti. <b>Mempelajari skill/materi langsung dengan dibimbing guru/mentor</b>.'
    },
    {
        'w': '学ぶ', 'y': 'まなぶ', 'a': 'Belajar (Ilmu yang mendalam/terstruktur)', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '大学で経済を学びます。', 'ei': 'Mempelajari ilmu ekonomi di universitas.',
        'ch': [('学', 'まな(ぶ)', 'ガク', 'Belajar/Sekolah. 龸 (ilmu/hiasan atap sekolah) + 子 (anak). Anak yang sedang meresap ilmu di bawah atap sekolah.')],
        'co': 'Mirip 勉強 (memaksakan diri) tapi 学ぶ lebih positif dan berkelas. Anak kecil (子) yang dijemput masuk ke gerbang pengetahuan akademis murni (seperti universitas atau etika). <b>Mendalami ilmu</b>.'
    },
    {
        'w': '気が付く', 'y': 'きがつく', 'a': 'Menyadari / Tersadar (Akan sesuatu)', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '間違いに気が付きました。', 'ei': 'Telah menyadari kesalahannya.',
        'ch': [
            ('気', 'き', 'キ', 'Hawa/Perasaan.'),
            ('付', 'つ(く)', 'フ', 'Menempel/Melekat.')
        ],
        'co': 'Perhatian atau hawa pikiranmu (気) secara tiba-tiba tertempel (付) pada sebuah fakta tersembunyi yang tadinya luput dari matamu. "Oh iya, dompetku ketinggalan!" -> <b>Tersadar / Menyadari</b>.'
    },
    {
        'w': '立つ', 'y': 'たつ', 'a': 'Berdiri', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '椅子から立ちます。', 'ei': 'Berdiri dari kursi.',
        'ch': [('立', 'た(つ)', 'リツ', 'Berdiri. Piktogram orang besar yang berdiri tegak (大) menapak di atas tanah (一).')],
        'co': 'Bentuknya tegak lurus sempurna ibarat pilar (亠) yang menancap mantap ke dasar bumi (一). Sangat jelas, aksi ini merubah postur dari duduk/baring menjadi posisi <b>Berdiri tegak vertikal</b>.'
    },
    {
        'w': '喜ぶ', 'y': 'よろこぶ', 'a': 'Berbahagia / Gembira / Menerima dengan senang', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': 'プレゼントをもらって喜びました。', 'ei': 'Dia berbahagia/gembira setelah menerima hadiah.',
        'ch': [('喜', 'よろこ(ぶ)', 'キ', 'Bahagia/Gembira. 鼓 (drum kulit) dipukul membahana di atas 口 (mulut tertawa/piring sesajen). Perayaan riang.')],
        'co': 'Orang zaman dulu memukul drum gembira dan tertawa lebar (口) saat panen. 嬉しい (Ureshii - kata sifat) itu perasaannya, 喜ぶ (Yorokobu) adalah tindakan memperlihatkan bahwa dirimu sedang <b>Berbahagia kegirangan</b>.'
    },
    {
        'w': '変わる', 'y': 'かわる', 'a': 'Berubah / Berganti (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '信号が赤に変わりました。', 'ei': 'Lampu lalu lintas berubah menjadi merah.',
        'ch': [('変', 'か(わる)', 'ヘン', 'Berubah/Aneh. 亦 (berjalan/tanda ganda) + 夂 (langkah kaki menyeret). Benang kusut yang diurai tangan, berpindah bentuk.')],
        'co': 'Wujud atau keadaan yang melompat dari wujud A menjadi bentuk B (secara otomatis/keadaan). <b>Berubah bentuk, ganti shift, atau berganti jadwal</b>.'
    },
    {
        'w': '笑う', 'y': 'わらう', 'a': 'Tertawa / Tersenyum (Lebar)', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '面白いテレビを見て笑います。', 'ei': 'Tertawa menonton TV yang lucu.',
        'ch': [('笑', 'わら(う)', 'ショウ', 'Tertawa. 竹 (bambu bergoyang ditiup angin) + 夭 (orang yang melengkung badannya ke depan saking asyiknya tertawa).')],
        'co': 'Pernah melihat pohon bambu bergoyang kencang disapu angin? Seperti itulah badan seseorang yang terguncang hebat gara-gara lawakan pecah! <b>Tertawa terbahak-bahak</b>.'
    },
    {
        'w': '調べる', 'y': 'しらべる', 'a': 'Mencari tahu / Menyelidiki / Memeriksa', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '辞書で単語を調べます。', 'ei': 'Mencari (tahu) kosakata di kamus.',
        'ch': [('調', 'しら(べる)', 'チョウ', 'Memeriksa / Menyetel nada. 言 (kata-kata) + 周 (tersebar luas keliling/tepat dan selaras). Mencocokkan harmoni secara mendetail.')],
        'co': 'Mengumpulkan seluruh kata-kata dan informasi dari berbagai penjuru (周) untuk mencocokkan fakta dan memastikan tidak ada yang palsu. <b>Memeriksa berkas atau Mencari informasi di Google/kamus</b>.'
    },
    {
        'w': '受ける', 'y': 'うける', 'a': 'Menerima / Mengikuti (Ujian/Interview)', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '明日、試験を受けます。', 'ei': 'Besok akan mengikuti (menerima) ujian.',
        'ch': [('受', 'う(ける)', 'ジュ', 'Menerima. 爫 (tangan dari atas) + 冖 (wadah) + 又 (tangan dari bawah). Satu tangan memberi barang ke wadah, tangan lain menyambutnya dari bawah.')],
        'co': 'Membuka dua belah tangan (爪 & 又) untuk menampung sesuatu yang diserahkan padamu. Bisa bermakna <b>Menerima perlakuan/pengaruh</b>, tapi di N5/N4 paling sering muncul artinya: <b>Mengikuti (Take an Exam)</b>.'
    },
    {
        'w': '考える', 'y': 'かんがえる', 'a': 'Memikirkan / Mempertimbangkan', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '将来について考えます。', 'ei': 'Memikirkan tentang masa depan.',
        'ch': [('考', 'かんが(える)', 'コウ', 'Memikirkan / Tua. 老 (orang tua bungkuk dengan tongkat) yang dimodifikasi. Orang tua yang merenung bijaksana menimbang masalah.')],
        'co': 'Menyandarkan dagu dengan bijaksana seperti kakek tua yang penuh pengalaman masa lalu. Kamu merenung, memproses opsi dalam otak dengan dalam, dan menimbang keputusan. <b>Berpikir / Memikirkan opsi logis</b>.'
    },
    {
        'w': '覚える', 'y': 'おぼえる', 'a': 'Mengingat / Menghafal', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '漢字を覚えます。', 'ei': 'Menghafal (dan mengingat) Kanji.',
        'ch': [('覚', 'おぼ(える) / さま(す)', 'カク', 'Sadar / Mengingat. (Kanji ini versi disederhanakan dari piktogram melihat 见 ke dalam sekolah/ilmu yang rumit 𦥯). Menyimpan memori penglihatan secara sadar.')],
        'co': 'Menanamkan pelajaran atau informasi ke dalam benak agar tetap tersimpan rapi dan kapan pun dipanggil bisa keluar. <b>Mengingat-ingat / Menghafal materi pelajaran (memorize)</b>.'
    },
    {
        'w': '教える', 'y': 'おしえる', 'a': 'Mengajari / Memberitahu', 'g': 2, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '道や日本語を教えます。', 'ei': 'Mengajari bahasa Jepang dan memberitahu jalan.',
        'ch': [('教', 'おし(える)', 'キョウ', 'Mengajar/Agama. 孝 (anak berbakti di bawah pimpinan orang tua) + 攵 (tangan memegang tongkat). Memukul perlahan untuk mendidik moral secara disiplin.')],
        'co': 'Dulu pendidikan cukup keras: orang dewasa memegang tongkat (攵) membimbing anak (子). Mentransfer kepintaran padanya. Punya 2 makna kuat di Jepang: <b>Mengajari ilmu</b> dan <b>Memberitahu info/alamat/rahasia (kasih tau dong!)</b>.'
    },
    {
        'w': '気を付ける', 'y': 'きをつける', 'a': 'Berhati-hati / Memperhatikan', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '風邪を引かないように気を付けます。', 'ei': 'Berhati-hati agar tidak masuk angin.',
        'ch': [
            ('気', 'き', 'キ', 'Hawa/Perasaan.'),
            ('付', 'つ(ける)', 'フ', 'Menempelkan.')
        ],
        'co': 'Bandingkan dengan 気が付く (tersadar otomatis)! Kalau 気を付ける, kamu (subjek) secara SENGAJA mengambil hawa pikiranmu (気) lalu menempelkannya (付ける) ekstra kuat pada masalah itu. "Bawa motornya yang bener!" = <b>Berhati-hati awas (take care)</b>.'
    },
    {
        'w': '建てる', 'y': 'たてる', 'a': 'Mendirikan / Membangun', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '新しい家を建てます。', 'ei': 'Membangun rumah baru.',
        'ch': [('建', 'た(てる)', 'ケン', 'Membangun. 廴 (langkah pelan yang mengitari) + 聿 (kuas tangan/tiang lurus). Mengitari pondasi dan menegakkan tiang lurus penyangga langit.')],
        'co': 'Pelafalannya sama (Tateru) dengan 立てる (mendirikan). Tapi 建てる dikhususkan untuk <b>Mendirikan konstruksi bangunan arsitektur megah (rumah, gedung, menara)</b> dari nol.'
    },
    {
        'w': '比べる', 'y': 'くらべる', 'a': 'Membandingkan', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '二つの車を比べます。', 'ei': 'Membandingkan dua mobil.',
        'ch': [('比', 'くら(べる)', 'ヒ', 'Membandingkan/Rasio. (Piktogram dua orang berdampingan menghadap ke satu arah). Jejeran sejajar.')],
        'co': 'Mensejajarkan (比) produk A dan produk B berdampingan di sebelah kanan dan kiri, lalu kamu amati: "Wah yang ini lebih murah, yang ini layarnya lecet." <b>Membandingkan komparasi fitur</b>.'
    },
    {
        'w': '答える', 'y': 'こたえる', 'a': 'Menjawab', 'g': 2, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '質問に答えます。', 'ei': 'Menjawab pertanyaan.',
        'ch': [('答', 'こた(える)', 'トウ', 'Menjawab / Solusi. 竹 (bambu) + 合 (cocok/menyatukan). Sambungan tabung bambu yang dipasangkan pas. Jawaban yang cocok dengan pertanyaan.')],
        'co': 'Potongan bambu (竹) atas dan bambu bawah ditutup hingga rapi berpadu (合) dengan mantap. Solusi yang sangat pas dan memuaskan kebingungan penanya. <b>Menjawab tes atau interogasi</b>.'
    },
    {
        'w': '見学する', 'y': 'けんがくする', 'a': 'Kunjungan Studi / Mengamati untuk belajar', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '工場を見学します。', 'ei': 'Melakukan kunjungan studi ke pabrik.',
        'ch': [
            ('見', 'み(る)', 'ケン', 'Melihat.'),
            ('学', 'まな(ぶ)', 'ガク', 'Belajar.')
        ],
        'co': 'Bukan turis nyasar. Menggunakan matamu Melihat-lihat (見) fasilitas lapangan nyata, agar Belajar (学) memverifikasi teori sekolah. <b>Kunjungan industri / Study Tour</b> (Kengaku).'
    },
    {
        'w': '練習する', 'y': 'れんしゅうする', 'a': 'Berlatih (Fisik / Praktik)', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': 'ピアノを毎日練習します。', 'ei': 'Berlatih piano setiap hari.',
        'ch': [
            ('練', 'ね(る)', 'レン', 'Melatih/Mengasah. 糸 (benang sutra) yang disortir, dibersihkan dan dipintal berulang-ulang dari kepompong.'),
            ('習', 'なら(う)', 'シュウ', 'Mempelajari (dari latihan kepakan burung).')
        ],
        'co': 'Mengasah bakat secara terus-menerus dan teratur membuang kelemahan ibarat benang sutra murni (練) dan mengepak sayap terus menerus (習). <b>Latihan/Practice rutin (olahraga, musik, kanji)</b>.'
    },
    {
        'w': '復習する', 'y': 'ふくしゅうする', 'a': 'Mengulang Pelajaran', 'g': 3, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': 'テストの前に復習します。', 'ei': 'Mengulang materi pelajaran sebelum ujian.',
        'ch': [
            ('復', 'ふたた(び)', 'フク', 'Mengulang/Kembali. 彳 (langkah berjalan) + 𢀻 (berjalan kembali ke tempat asal di jalan berliku).'),
            ('習', 'なら(う)', 'シュウ', 'Mempelajari.')
        ],
        'co': 'Materi yang sudah dijarkan dosen siang tadi tidak dibiarkan terbang. Kamu berbalik ke belakang (復) dan membedah ulang pelajari (習) buku itu. <b>Review pelajaran di rumah/Kilas balik bacaan</b>.'
    },
    {
        'w': '説明する', 'y': 'せつめいする', 'a': 'Menjelaskan / Menerangkan', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '理由を説明してください。', 'ei': 'Tolong jelaskan alasannya.',
        'ch': [
            ('説', 'と(く)', 'セツ', 'Menjelaskan/Teori. 言 (kata-kata) + 兌 (berubah bentuk/senyum yang memuaskan). Teori memuaskan yang mengurai masalah.'),
            ('明', 'あか(るい)', 'メイ', 'Terang. 日 (matahari) bersanding 月 (bulan). Sangat jelas tanpa bayangan gelap.')
        ],
        'co': 'Kamu mengolah kata-kata (説) di mulut untuk menyinari hati orang yang buta pengetahuan sampai pikirannya menjadi <b>Terang benderang (明)</b>. Aksi <b>Menjelaskan / Presentasi materi</b>.'
    },
    {
        'w': '失敗する', 'y': 'しっぱいする', 'a': 'Gagal / Melakukan Kesalahan', 'g': 3, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '試験に失敗しました。', 'ei': 'Gagal dalam ujian.',
        'ch': [
            ('失', 'うしな(う)', 'シツ', 'Kehilangan. 手 (tangan) menjatuhkan anak panah/sesuatu lolos dari genggaman.'),
            ('敗', 'やぶ(れる)', 'パイ / ハイ', 'Kalah/Hancur. 貝 (uang logam hancur) dipukul pakai tongkat 攵.')
        ],
        'co': 'Kamu melepaskan/kehilangan (失) kendali dari tanganmu, sehingga proyek atau ujian itu hancur berantakan menelan kerugian (敗). Kesempatan itu lenyap selamanya. <b>Gagal (Fail)</b>.'
    },
    {
        'w': '卒業する', 'y': 'そつぎょうする', 'a': 'Lulus Sekolah', 'g': 3, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '来年、大学を卒業します。', 'ei': 'Tahun depan lulus dari universitas.',
        'ch': [
            ('卒', '–', 'ソツ', 'Lulus / Prajurit berbaris. Baju seragam prajurit yang dikumpulkan jadi tumpukan (purna tugas).'),
            ('業', '–', 'ギョウ', 'Tugas Pendidikan / Pekerjaan.')
        ],
        'co': 'Menyelesaikan sebuah tugas edukasi (業) secara tuntas dengan nilai memuaskan. Merayakan purna tugas sebagai murid yang sah di wisuda berbaris (卒). <b>Lulus institusi pendidikan resmi (SD sampai Kampus)</b>.'
    },
    {
        'w': '質問する', 'y': 'しつもんする', 'a': 'Bertanya', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '先生に質問します。', 'ei': 'Bertanya kepada guru.',
        'ch': [
            ('質', '–', 'シツ', 'Kualitas / Menggadaikan. Tumpukan dua kapak/barang di atas uang 貝 (jaminan/gadai inti kebenaran).'),
            ('問', 'と(う)', 'モン', 'Bertanya. 門 (gerbang) + 口 (mulut). Mulut yang bersuara mencari celah di pintu gerbang.')
        ],
        'co': 'Menyelidiki substansi materi (質) dengan cara menginterogasi / melontarkan unek-unek ucapan rasa penasaran (問). <b>Mengajukan pertanyaan / Questioning (shitsumon ga arimasu)</b>.'
    }
]
