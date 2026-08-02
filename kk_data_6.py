# -*- coding: utf-8 -*-
# Batch 6: Restored missing entries with premium quality
CARDS = [
    {
        'w': '出来る', 'y': 'できる', 'a': 'Bisa / Jadi (Selesai terbentuk)', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '日本語が少し出来ます。', 'ei': 'Bisa sedikit bahasa Jepang.',
        'ch': [
            ('出', 'で.る', 'シュツ', '[Radikal: 凵 (Wadah terbuka)] + [Komponen: 山 (Gunung)]'),
            ('来', 'く.る', 'ライ', '[Radikal: 木 (Pohon)] + [Komponen: 丷 (Gandum)]')
        ],
        'co': 'Sesuatu yang "keluar (出) datang (来)" ke permukaan berarti sudah terwujud / mampu dilakukan. <b>Bisa / Mampu (Kemampuan)</b>. Juga berarti "selesai jadi" (Roti sudah dekita!).'
    },
    {
        'w': '注意する', 'y': 'ちゅういする', 'a': 'Memperingatkan / Berhati-hati', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '先生が学生に注意します。', 'ei': 'Guru memperingatkan murid.',
        'ch': [
            ('注', 'そそ.ぐ', 'チュウ', '[Radikal: 氵 (Air)] + [Komponen: 主 (Tuan)]'),
            ('意', 'イ', 'イ', '[Radikal: 心 (Hati)] + [Komponen: 音 (Suara)]')
        ],
        'co': 'Menuangkan (注) seluruh pikiran dan niat (意) ke satu titik fokus. <b>Memperingatkan orang lain / Memusatkan perhatian</b>. Beda dengan 気を付ける yang lebih kasual.'
    },
    {
        'w': '出発する', 'y': 'しゅっぱつする', 'a': 'Berangkat / Bertolak', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '明日の朝、出発します。', 'ei': 'Berangkat besok pagi.',
        'ch': [
            ('出', 'で.る', 'シュツ', '[Radikal: 凵 (Wadah terbuka)] + [Komponen: 山 (Gunung)]'),
            ('発', 'はつ', 'ハツ', '[Radikal: 癶 (Kaki mekar)] + [Komponen: 弓 (Busur)]')
        ],
        'co': 'Keluar (出) dari tempat asal dengan kecepatan panah yang dilepas (発). <b>Berangkat / Departure</b> dari stasiun atau rumah menuju tujuan.'
    },
    {
        'w': '到着する', 'y': 'とうちゃくする', 'a': 'Tiba / Sampai (di tujuan)', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '飛行機が空港に到着しました。', 'ei': 'Pesawat telah tiba di bandara.',
        'ch': [
            ('到', 'いた.る', 'トウ', '[Radikal: 刂 (Pisau)] + [Komponen: 至 (Sampai)]'),
            ('着', 'つ.く', 'チャク', '[Radikal: 羊 (Domba)] + [Komponen: 目 (Mata)]')
        ],
        'co': 'Perjalanan panjang akhirnya mencapai (到) titik tujuan dan "menempel" (着) di sana. <b>Tiba di tujuan / Arrival</b>.'
    },
    {
        'w': '運転する', 'y': 'うんてんする', 'a': 'Menyetir / Mengoperasikan', 'g': 3, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '車を運転します。', 'ei': 'Menyetir mobil.',
        'ch': [
            ('運', 'はこ.ぶ', 'ウン', '[Radikal: 辶 (Jalan/Pergerakan)] + [Komponen: 軍 (Tentara)]'),
            ('転', 'ころ.がる', 'テン', '[Radikal: 車 (Mobil/Kereta)] + [Komponen: 云 (Awan/Berputar)]')
        ],
        'co': 'Membuat roda kendaraan berputar (転) dan mengangkut (運) penumpang ke tujuan. <b>Menyetir / Mengendarai kendaraan bermotor</b>.'
    },
    {
        'w': '出張する', 'y': 'しゅっちょうする', 'a': 'Dinas Luar / Business Trip', 'g': 3, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '来週大阪に出張します。', 'ei': 'Minggu depan dinas ke Osaka.',
        'ch': [
            ('出', 'で.る', 'シュツ', '[Radikal: 凵 (Wadah terbuka)] + [Komponen: 山 (Gunung)]'),
            ('張', 'は.る', 'チョウ', '[Radikal: 弓 (Busur)] + [Komponen: 長 (Panjang)]')
        ],
        'co': 'Keluar (出) dari kantor pusat dan membentang (張) sayap ke kota lain demi tugas bisnis. <b>Perjalanan dinas / Business trip</b>.'
    },
    {
        'w': '発見する', 'y': 'はっけんする', 'a': 'Menemukan / Mengungkap', 'g': 3, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '新しい星を発見しました。', 'ei': 'Menemukan bintang baru.',
        'ch': [
            ('発', 'ハツ', 'ハツ', '[Radikal: 癶 (Kaki mekar)] + [Komponen: 弓 (Busur)]'),
            ('見', 'み.る', 'ケン', '[Radikal: 見 (Melihat)]')
        ],
        'co': 'Mata terbuka (見) untuk pertama kalinya (発) menyaksikan sesuatu yang belum pernah diketahui siapapun. <b>Menemukan / Discovery</b>.'
    },
    {
        'w': '持って来る', 'y': 'もってくる', 'a': 'Membawa ke sini', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '本を持って来てください。', 'ei': 'Tolong bawa bukunya ke sini.',
        'ch': [
            ('持', 'も.つ', 'ジ', '[Radikal: 扌 (Tangan)] + [Komponen: 寺 (Kuil)]'),
            ('来', 'く.る', 'ライ', '[Radikal: 木 (Pohon)] + [Komponen: 丷 (Gandum)]')
        ],
        'co': 'Memegang (持) suatu barang lalu membawanya datang (来る) ke lokasi pembicara. Kebalikan dari 持って行く. <b>Membawa ke sini (Bring)</b>.'
    },
    {
        'w': '遣る', 'y': 'やる', 'a': 'Melakukan / Memberi (Kasual)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '宿題をやります。', 'ei': 'Mengerjakan PR.',
        'ch': [('遣', 'や.る / つか.わす', 'ケン', '[Radikal: 辶 (Jalan)]')],
        'co': 'Versi kasual dan serbaguna dari する. Bisa berarti <b>Melakukan (ngerjain PR)</b>, <b>Memberi ke makhluk lebih rendah (kasih makan kucing)</b>, atau <b>Mengirim utusan</b>.'
    },
    {
        'w': '学ぶ', 'y': 'まなぶ', 'a': 'Belajar (Menyerap ilmu)', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '歴史を学びます。', 'ei': 'Belajar sejarah.',
        'ch': [('学', 'まな.ぶ', 'ガク', '[Radikal: 子 (Anak)] + [Komponen: 臼 (Tangan meraba) + 冖 (Atap)]')],
        'co': 'Seorang anak (子) duduk di bawah atap (冖) sambil meraba dan memahami ilmu (臼). Nuansanya lebih mendalam dari 勉強する: <b>Belajar dengan menyerap esensi / Menimba ilmu</b>.'
    },
    {
        'w': '気が付く', 'y': 'きがつく', 'a': 'Menyadari / Tersadar', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '間違いに気が付きました。', 'ei': 'Menyadari kesalahan.',
        'ch': [
            ('気', 'き', 'キ', '[Radikal: 气 (Udara/Hawa)] + [Komponen: 乂 (Menyilang)]'),
            ('付', 'つ.く', 'フ', '[Radikal: 亻 (Orang)] + [Komponen: 寸 (Ukuran/Tangan)]')
        ],
        'co': 'Energi kesadaran (気) secara tiba-tiba MENEMPEL (付く) di otakmu. Beda dengan 気を付ける (sengaja fokus), ini <b>Tersadar secara otomatis/spontan</b>. "Oh iya, gue baru nyadar!"'
    },
    {
        'w': '喜ぶ', 'y': 'よろこぶ', 'a': 'Bergembira / Senang', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': 'プレゼントをもらって喜びました。', 'ei': 'Bergembira menerima hadiah.',
        'ch': [('喜', 'よろこ.ぶ', 'キ', '[Radikal: 口 (Mulut)] + [Komponen: 壴 (Gendang/Musik)]')],
        'co': 'Mulut (口) terbuka lebar menyerukan kebahagiaan diiringi tabuhan gendang pesta (壴). Ekspresi yang sangat tulus: <b>Bergembira / Bersuka cita</b>.'
    },
    {
        'w': '変わる', 'y': 'かわる', 'a': 'Berubah (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '季節が変わります。', 'ei': 'Musim berubah.',
        'ch': [('変', 'か.わる', 'ヘン', '[Radikal: 夂 (Kaki terbalik)] + [Komponen: 言 (Kata) + 攵 (Pukulan)]')],
        'co': 'Sesuatu yang dipukul (攵) dengan perkataan (言) sampai terbalik (夂) menjadi bentuk yang berbeda dari sebelumnya. <b>Berubah secara otomatis (Intransitif)</b>. Musim, warna daun, situasi.'
    },
    {
        'w': '調べる', 'y': 'しらべる', 'a': 'Menyelidiki / Memeriksa', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': 'インターネットで調べます。', 'ei': 'Menyelidiki lewat internet.',
        'ch': [('調', 'しら.べる', 'チョウ', '[Radikal: 言 (Kata)] + [Komponen: 周 (Keliling/Menyeluruh)]')],
        'co': 'Menggunakan kata-kata/pertanyaan (言) untuk menguji dan menyisir secara menyeluruh (周) setiap sudut informasi. <b>Menyelidiki / Riset / Googling</b>.'
    },
    {
        'w': '受ける', 'y': 'うける', 'a': 'Menerima / Mengikuti (Ujian)', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '試験を受けます。', 'ei': 'Mengikuti ujian.',
        'ch': [('受', 'う.ける', 'ジュ', '[Radikal: 又 (Tangan kanan)] + [Komponen: 冖 (Penutup) + 爪 (Cakar/Tangan atas)]')],
        'co': 'Tangan atas (爪) memberikan sesuatu ke bawah, dan tangan bawah (又) menangkapnya. <b>Menerima / Mengikuti ujian / Mendapat pengaruh</b>.'
    },
    {
        'w': '弾く', 'y': 'ひく', 'a': 'Memainkan (Alat musik petik/tekan)', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'ギターを弾きます。', 'ei': 'Memainkan gitar.',
        'ch': [('弾', 'ひ.く / はず.む', 'ダン', '[Radikal: 弓 (Busur)] + [Komponen: 単 (Sederhana/Tunggal)]')],
        'co': 'Jari menarik dan melepas senar busur (弓) yang menggetarkan udara menjadi nada. Khusus untuk <b>Memainkan instrumen senar/keyboard (Piano, Gitar)</b>.'
    },
    {
        'w': '描く', 'y': 'かく', 'a': 'Menggambar / Melukis', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '絵を描きます。', 'ei': 'Menggambar.',
        'ch': [('描', 'か.く / えが.く', 'ビョウ', '[Radikal: 扌 (Tangan)] + [Komponen: 苗 (Bibit tanaman/Pola)]')],
        'co': 'Tangan (扌) yang memegang kuas menorehkan pola tanaman (苗) ke atas kanvas. <b>Menggambar / Melukis seni rupa</b>. (Beda dari 書く yang menulis huruf/kalimat).'
    },
    {
        'w': '旅行する', 'y': 'りょこうする', 'a': 'Berwisata / Travelling', 'g': 3, 'subdeck': 'KK::Pergerakan',
        'ej': '夏休みに旅行します。', 'ei': 'Berwisata saat liburan musim panas.',
        'ch': [
            ('旅', 'たび', 'リョ', '[Radikal: 方 (Arah)] + [Komponen: 氏 (Klan/Garis)]'),
            ('行', 'い.く', 'コウ', '[Radikal: 行 (Jalan simpang empat)]')
        ],
        'co': 'Sekelompok orang berarak (旅) menempuh perjalanan jauh (行) ke tempat asing demi kesenangan. <b>Berwisata / Travelling</b>.'
    },
    {
        'w': 'お喋りする', 'y': 'おしゃべりする', 'a': 'Mengobrol / Ngobrol', 'g': 3, 'subdeck': 'KK::Interaksi Sosial',
        'ej': 'カフェでお喋りします。', 'ei': 'Ngobrol di kafe.',
        'ch': [('喋', 'しゃべ.る', 'チョウ', '[Radikal: 口 (Mulut)] + [Komponen: 葉 (Daun)]')],
        'co': 'Mulut (口) yang terus bergoyang-goyang tak berhenti seperti daun (葉) tertiup angin sepoi-sepoi. <b>Ngobrol santai / Ngerumpi</b>.'
    },
    {
        'w': 'お祈りする', 'y': 'おいのりする', 'a': 'Berdoa / Memohon', 'g': 3, 'subdeck': 'KK::Ungkapan Khusus',
        'ej': '神社でお祈りします。', 'ei': 'Berdoa di kuil Shinto.',
        'ch': [('祈', 'いの.る', 'キ', '[Radikal: 礻 (Altar/Dewa)] + [Komponen: 斤 (Kapak)]')],
        'co': 'Berdiri di depan altar suci (礻) dan mengerahkan seluruh kekuatan hati (斤) untuk memohon perlindungan dewa. <b>Berdoa / Memohon pada Tuhan/Dewa</b>.'
    },
    {
        'w': '迎える', 'y': 'むかえる', 'a': 'Menjemput / Menyambut', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '空港で友達を迎えます。', 'ei': 'Menjemput teman di bandara.',
        'ch': [('迎', 'むか.える', 'ゲイ', '[Radikal: 辶 (Jalan)] + [Komponen: 卬 (Orang mendongak menunggu)]')],
        'co': 'Kamu berjalan (辶) menuju gerbang kedatangan dan mendongakkan kepala (卬) mencari sosok orang yang ditunggu. <b>Menjemput / Menyambut tamu</b>.'
    },
    {
        'w': '殴る', 'y': 'なぐる', 'a': 'Memukul (Dengan tinju)', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '壁を殴りました。', 'ei': 'Memukul dinding.',
        'ch': [('殴', 'なぐ.る', 'オウ', '[Radikal: 殳 (Senjata/Tongkat)] + [Komponen: 区 (Wilayah/Kotak)]')],
        'co': 'Mengayunkan tinju atau tongkat (殳) dan menghantam target (区) dengan keras. <b>Memukul / Menjotos / Menonjok</b> (kekerasan fisik).'
    },
    {
        'w': '蹴る', 'y': 'ける', 'a': 'Menendang', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'ボールを蹴ります。', 'ei': 'Menendang bola.',
        'ch': [('蹴', 'け.る', 'シュウ', '[Radikal: 足 (Kaki)] + [Komponen: 就 (Mendekati/Menuju)]')],
        'co': 'Kaki (足) menghampiri (就) bola lalu mengayunkannya dengan keras ke depan. <b>Menendang (Kick)</b>.'
    },
    {
        'w': '味わう', 'y': 'あじわう', 'a': 'Mengecap / Menikmati rasa', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '日本料理を味わいます。', 'ei': 'Mengecap masakan Jepang.',
        'ch': [('味', 'あじ.わう', 'ミ', '[Radikal: 口 (Mulut)] + [Komponen: 未 (Belum matang)]')],
        'co': 'Memasukkan sesuatu ke mulut (口) dan menguji apakah rasanya sudah matang atau belum (未). <b>Mengecap / Menikmati rasa makanan secara perlahan</b>.'
    }
]
