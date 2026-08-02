# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '弾く', 'y': 'ひく', 'a': 'Bermain (Alat musik piano / gitar)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'ピアノを弾きます。', 'ei': 'Bermain piano.',
        'ch': [('弾', 'ひ(く) / たま', 'ダン', 'Bermain alat musik/Peluru. 弓 (busur) + 単 (tombak berujung berat). Senjata pegas yang bisa dilontarkan atau dipetik senarnya.')],
        'co': 'Jangan tertukar dengan 引く (menarik). Memainkan alat musik senar/ditekan (gitar, piano, biola) rasanya seperti <b>memetik senar busur panah</b> yang direntangkan (弓). Makanya pakai Kanji 弾.'
    },
    {
        'w': '描く', 'y': 'かく', 'a': 'Menggambar / Melukis', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '絵を描きます。', 'ei': 'Menggambar/melukis gambar.',
        'ch': [('描', 'えが(く) / か(く)', 'ビョウ', 'Menggambar. 扌 (tangan) + 苗 (tanaman padi/garis-garis sawah). Tangan membuat coretan sketsa.')],
        'co': 'Sama-sama kaku (menulis), bedanya 書く adalah memindahkan aksara/huruf, sedangkan 描く (dari tangan dan lahan 苗) adalah <b>Menggoreskan kuas pelukis untuk membentuk gambar/ilustrasi/pemandangan alam</b>.'
    },
    {
        'w': '登る', 'y': 'のぼる', 'a': 'Mendaki (Gunung) / Memanjat', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '富士山に登ります。', 'ei': 'Mendaki Gunung Fuji.',
        'ch': [('登', 'のぼ(る)', 'トウ / ト', 'Mendaki. 癶 (dua telapak kaki yang melangkah keluar) + 豆 (kacang/wadah persembahan gunung). Mendaki bukit suci untuk ritual.')],
        'co': 'Langkah kaki bertumpu (癶) memaksa badan naik ke atas permukaan yang sangat tinggi. Kata ini dikhususkan secara agung untuk <b>Mendaki Gunung, tebing, atau memanjat pohon</b>.'
    },
    {
        'w': '歌う', 'y': 'うたう', 'a': 'Bernyanyi', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '歌を歌います。', 'ei': 'Menyanyikan lagu.',
        'ch': [('歌', 'うた / うた(う)', 'カ', 'Lagu / Bernyanyi. 哥 (dua mulut bersahutan/nada panjang) + 欠 (mulut ternganga membuka lebar).')],
        'co': 'Banyak sekali mulut yang menganga (欠 & 哥) melantunkan melodi panjang secara paduan. Aksi <b>Mengeluarkan suara nyanyian merdu</b> dari rongga mulut.'
    },
    {
        'w': '集める', 'y': 'あつめる', 'a': 'Mengumpulkan (Koleksi / Barang - Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '切手を集めます。', 'ei': 'Mengumpulkan perangko.',
        'ch': [('集', 'あつ(める) / あつ(まる)', 'シュウ', 'Berkumpul. 隹 (berbagai jenis burung kecil) bertengger di atas 木 (pohon).')],
        'co': 'Layaknya mengumpulkan berbagai ragam burung-burung (隹) untuk ditaruh di satu dahan pohon (木). Kamu subjeknya bertindak aktif <b>Menyortir dan Mengumpulkan benda jadi satu koleksi</b>.'
    },
    {
        'w': '旅行する', 'y': 'りょこうする', 'a': 'Berlibur / Traveling', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '海外へ旅行します。', 'ei': 'Traveling ke luar negeri.',
        'ch': [
            ('旅', 'たび', 'リョ', 'Piknik/Perjalanan. 方 (arah/bendera regu) + orang yang berbaris. Tur kelompok.'),
            ('行', 'い(く)', 'コウ', 'Pergi.')
        ],
        'co': 'Melakukan perjalanan jauh (行) dengan rombongan yang berjalan di bawah satu bendera pemandu pariwisata (旅). <b>Jalan-jalan keluar daerah atau luar negeri (piknik asyik)</b>.'
    },
    {
        'w': '降る', 'y': 'ふる', 'a': 'Turun (Hujan / Salju)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '雨が降ります。', 'ei': 'Turun hujan.',
        'ch': [('降', 'お(りる) / ふ(る)', 'コウ', 'Turun. 阝 (bukit) + 夂 (kaki turun terbalik) + 丰 (meluncur). Sesuatu yang meluncur/terjun dari tempat tinggi di bukit.')],
        'co': 'Bisa dibaca oriru (turun kendaraan), tapi untuk cuaca dari langit dibaca "Furu". Rintik air hujan yang <b>terjun bebas menghunjam bumi</b> dari langit.'
    },
    {
        'w': 'お喋りする', 'y': 'おしゃべりする', 'a': 'Mengobrol / Ngerumpi', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': 'カフェで友達とお喋りします。', 'ei': 'Mengobrol dengan teman di kafe.',
        'ch': [('喋', 'しゃべ(る)', 'チョウ', 'Mengoceh. 口 (mulut) + 葉 (daun). Kata-kata ringan dan bertebaran bebas layaknya daun-daunan.')],
        'co': 'Kalau 話す sekadar berbicara formal. Menggunakan 喋る ibarat daun tipis yang ditiup angin, pembicaraan ini nggak ada isinya, sangat kasual, ngalor-ngidul. <b>Ngerumpi / Asyik mengobrol</b>.'
    },
    {
        'w': 'お祈りする', 'y': 'おいのりする', 'a': 'Berdoa / Sembahyang', 'g': 3, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '教会でお祈りします。', 'ei': 'Berdoa di gereja.',
        'ch': [('祈', 'いの(る)', 'キ', 'Berdoa. 礻 (altar dewa) + 斤 (kapak ukur/sangat pas). Memanjatkan doa dengan tulus di altar pemujaan.')],
        'co': 'Seseorang berlutut memohon di depan meja sesajen altar suci (礻). Kata-katanya diucapkan. Tentu saja itu artinya <b>Bersembahyang memanjatkan doa suci</b>.'
    },
    {
        'w': '行く', 'y': 'いく', 'a': 'Pergi', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '学校へ行きます。', 'ei': 'Pergi ke sekolah.',
        'ch': [('行', 'い(く) / ゆ(く)', 'コウ', 'Pergi. Piktogram persimpangan jalan perempatan empat arah.')],
        'co': 'Bentuknya yang melambangkan persimpangan jalan (彳 + 亍). Subjek bergerak pindah posisi secara mantap ke arah luar. <b>Satu-satunya kata kerja pengecualian Konjugasi "Ite" -> Iku menjadi Itte (bukan Iite)!</b>'
    },
    {
        'w': '帰る', 'y': 'かえる', 'a': 'Pulang (ke Asal)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '家へ帰ります。', 'ei': 'Pulang ke rumah.',
        'ch': [('帰', 'かえ(る)', 'キ', 'Pulang. 刂 (bendera rombongan yang kembali bertumpuk).')],
        'co': 'Berbalik arah untuk kembali ke "titik asal/kandang", baik itu rumah maupun negara asal. <b>Awas! Akhiran ~eru tapi ini Golongan 1</b> (Kaette, Kaeranai)!'
    },
    {
        'w': '出す', 'y': 'だす', 'a': 'Mengeluarkan (Barang / Tugas) - Transitif', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '宿題を出してください。', 'ei': 'Tolong keluarkan/kumpulkan PR.',
        'ch': [('出', 'で(る) / だ(す)', 'シュツ', 'Keluar. Piktogram tanaman berkuncup (山) yang muncul/menembus lubang (凵).')],
        'co': 'Tanaman (山) yang menembus tanah mendesak keluar (凵). Kamu menekan dan mendorong (dasu) dompet dari saku. <b>Mengeluarkan benda ke tempat terang, atau mengumpulkan tugas</b>.'
    },
    {
        'w': '払う', 'y': 'はらう', 'a': 'Membayar / Mengusir debu', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': 'お金を払います。', 'ei': 'Membayar uang.',
        'ch': [('払', 'はら(う)', 'フツ', 'Menyapu/Membayar. 扌 (tangan) + ム (siku orang/melengkung). Tangan yang menyapu bersih, menyingkirkan sesuatu dengan cepat.')],
        'co': 'Tanganmu (扌) yang menyapu/memberikan uang secepat kilat ke atas kasir sehingga melegakan tunggakanmu. Mirip mengusir debu dari meja. <b>Melunasi tagihan / Membayar</b>.'
    },
    {
        'w': '迎える', 'y': 'むかえる', 'a': 'Menjemput / Menyambut', 'g': 2, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '駅まで友達を迎えに行きます。', 'ei': 'Pergi menjemput teman sampai ke stasiun.',
        'ch': [('迎', 'むか(える)', 'ゲイ', 'Menyambut. 辶 (jalan) + 卬 (orang yang menatap tinggi-tinggi/membuka gerbang). Berjalan menuju orang tamu kehormatan.')],
        'co': 'Kamu berjalan mendekati perbatasan/bandara (辶) untuk menyapa seseorang yang sedang turun tiba. Tujuannya membawanya masuk dengan hangat. <b>Menjemput atau Menyambut kedatangan</b>.'
    },
    {
        'w': '送る', 'y': 'おくる', 'a': 'Mengirim / Mengantar ke lokasi', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '荷物を送ります。 / 家まで送ります。', 'ei': 'Mengirim barang paket. / Mengantarkan sampai ke rumah.',
        'ch': [('送', 'おく(る)', 'ソウ', 'Mengirim. 辶 (jalan/menggerakkan) + 关 (tangan memegang obor penerang jalan). Mengiringi dari belakang.')],
        'co': 'Kamu berjalan memegang obor di belakang seseorang untuk mengawalnya, atau mempercayakan barang ke kurir yang berlari di jalanan. <b>Mengantarkan (Drop off) atau Mengirim paket</b>.'
    },
    {
        'w': '勝つ', 'y': 'かつ', 'a': 'Menang', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '試合に勝ちました。', 'ei': 'Menang dalam pertandingan.',
        'ch': [('勝', 'か(つ)', 'ショウ', 'Kemenangan. 月 (tubuh berotot) + 劵 (menggunakan paksaan/tenaga ekstra). Mengalahkan kekuatan orang lain.')],
        'co': 'Tubuh penuh otot bertenaga kuli super kuat (月). Menghantam musuh menggunakan segenap tenaga (劵) sampai mendominasi mereka. Pastilah kamu <b>Menang mutlak (Victory)</b>.'
    },
    {
        'w': '負ける', 'y': 'まける', 'a': 'Kalah / Memberi diskon', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'テニスの試合に負けました。', 'ei': 'Kalah dalam pertandingan tenis.',
        'ch': [('負', 'ま(ける) / お(う)', 'フ', 'Kalah/Menanggung beban. 貝 (uang/barang berat) + 𠂉 (orang tertekuk/membungkuk). Menyerah di bawah beban hutang/kekuatan musuh.')],
        'co': 'Manusia tertekuk tak berdaya ditimpa karung 貝 (harta jarahan musuh). Membungkuk kehabisan nafas, pasrah merelakan semuanya. <b>Kalah (Losing)</b>.'
    },
    {
        'w': '殴る', 'y': 'なぐる', 'a': 'Memukul (Pakai kepalan tangan keras)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '怒って壁を殴りました。', 'ei': 'Marah lalu menonjok dinding.',
        'ch': [('殴', 'なぐ(る)', 'オウ', 'Memukul. 区 (kotak terkurung rapi) + 殳 (tombak yang diayun). Senjata tumpul keras penusuk dari jarak dekat.')],
        'co': 'Senjata gada tombak ayun (殳) yang dihantamkan beruntun bagai kotak-kotak petinju. Kalau 打つ (memukul lembut), 殴る ini tonjokan kekerasan jalanan. <b>Meninju/Memukul kasar</b>.'
    },
    {
        'w': '蹴る', 'y': 'ける', 'a': 'Menendang', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'ボールを蹴ります。', 'ei': 'Menendang bola.',
        'ch': [('蹴', 'け(る)', 'シュウ', 'Menendang. 足 (kaki) + 就 (burung/sasaran cepat). Kaki yang meluncur melesat menuju sasaran.')],
        'co': 'Daya ayun Kaki (足) yang menabrak bola secepat elang menyambar mangsa (就). Awas, meskipun keru, ini <b>Golongan 1</b>! Konjugasinya: kette, keranai.'
    },
    {
        'w': '味わう', 'y': 'あじわう', 'a': 'Mencicipi / Menikmati', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '美味しいワインを味わいます。', 'ei': 'Mencicipi/menikmati wine yang enak.',
        'ch': [('味', 'あじ / あじ(わう)', 'ミ', 'Rasa. 口 (mulut) + 未 (belum matang/ujung dahan pohon). Mencoba sesuatu yang asing di mulut.')],
        'co': 'Kanji dasar Rasa (味). Kamu tak sekadar makan, tapi menahan makanan itu di lidah, meresapi molekul rasanya. <b>Mengulum untuk mencicipi dan menikmati nuansa mendalam</b>.'
    },
    {
        'w': '溜まる', 'y': 'たまる', 'a': 'Terkumpul / Bertumpuk (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'ストレスが溜まりました。', 'ei': 'Stres (telah) menumpuk.',
        'ch': [('溜', 'た(まる)', 'リュウ', 'Genangan/Bertumpuk. 氵 (air) + 留 (berhenti/menetap). Air yang tidak mengalir ke laut namun menumpuk jadi kubangan/waduk.')],
        'co': 'Bayangkan air kolam kotor (氵) yang tertahan (留) dan semakin hari terus menggenang. Sampah, Cucian, Stres, semua yang <b>menumpuk</b> secara perlahan. (Tamatte, tamaranai).'
    },
    {
        'w': '決まる', 'y': 'きまる', 'a': 'Diputuskan / Ditetapkan (Otomatis/Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '出発の日が決まりました。', 'ei': 'Hari keberangkatan (telah) diputuskan.',
        'ch': [('決', 'き(める) / き(まる)', 'ケツ', 'Memutuskan/Garis keras. 氵 (air bendungan) + 夬 (membedah lurus). Air bah bendungan yang dipotong agar alirannya ditetapkan satu arah pasti.')],
        'co': 'Aliran air (氵) dilepaskan (夬). Bendungan telah jebol menuju takdir baru yang tak bisa dicegah lagi. Rencana A batal, Plan B disahkan. Sesuatu yang <b>Telah diputuskan / fix</b> tanpa bisa kau ganggu gugat.'
    },
    {
        'w': '決める', 'y': 'きめる', 'a': 'Memutuskan / Menetapkan (Transitif)', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': 'メニューを決めます。', 'ei': 'Memutuskan / menetapkan menu.',
        'ch': [('決', 'き(める)', 'ケツ', 'Memutuskan/Menjebol.')],
        'co': 'Kamulah subjek aktifnya (bukan benda mati)! Kamu dengan wewenangmu merobohkan keraguan dan menunjuk satu jawaban. "Aku <b>memilih/memutuskan</b> paket hemat." (Kimete).'
    },
    {
        'w': '通る', 'y': 'とおる', 'a': 'Melewati / Lulus / Tembus', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'この道を車が通ります。', 'ei': 'Mobil melewati jalan ini.',
        'ch': [('通', 'とお(る) / かよ(う)', 'ツウ', 'Melewati/Komunikasi. 辶 (jalan) + 甬 (saluran air plong lurus tembus). Sesuatu yang melaju tanpa rintangan menembus terowongan lurus.')],
        'co': 'Mobil ngebut di jalan tol mulus tanpa macet, menembus (辶) terowongan lurus tiada ujung (甬). <b>Melintasi dari titik A menembus titik B</b>. Gol 1 (tootte).'
    },
    {
        'w': '通う', 'y': 'かよう', 'a': 'Pergi-Pulang Rutin / Komuter', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '毎日バスで大学に通います。', 'ei': 'Pergi-pulang (komuter) ke universitas naik bus tiap hari.',
        'ch': [('通', 'かよ(う)', 'ツウ', 'Melewati/Lancar.')],
        'co': 'Jalur yang sama bolak-balik ditempuh ibarat saluran darah (通). Bukan sekadar pergi, tapi <b>Ngantor/Ngampus rutin bolak-balik PP tiap hari/tiap minggu</b>. "Aduh, capek ngelajo nih!"'
    },
    {
        'w': '迷う', 'y': 'まよう', 'a': 'Bingung / Tersesat', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '道に迷いました。', 'ei': 'Tersesat di jalan.',
        'ch': [('迷', 'まよ(う)', 'メイ', 'Tersesat/Bingung. 辶 (jalan) + 米 (butiran beras/tersebar ke segala arah). Butiran pasir di simpang jalan, membuat langkah linglung.')],
        'co': 'Di tengah perjalanan jauh (辶), kamu menemukan butiran beras yang bertaburan (米) membingungkan pandangan arah matamu. "Mana yang bener sih?". <b>Dilema bingung (menu) atau Tersesat buta arah (jalan)</b>.'
    },
    {
        'w': '困る', 'y': 'こまる', 'a': 'Kesulitan / Repot / Terganggu', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': 'お金がなくて困ります。', 'ei': 'Saya kesulitan/repot karena tidak punya uang.',
        'ch': [('困', 'こま(る)', 'コン', 'Kesulitan. 囗 (kotak pagar/kurungan) + 木 (pohon). Pohon yang tumbuh terjepit di dalam ruang sempit berpagar tinggi sehingga tidak bisa mekar daun.')],
        'co': 'Pohon merana terkurung kaku dalam pagar beton (囗). Akarnya mentok, dahannya nyangkut. Tak bisa maju apalagi lari. Situasi yang bikin <b>pusing, ribet, dan kerepotan total (terjepit batas)</b>.'
    },
    {
        'w': '戻す', 'y': 'もどす', 'a': 'Mengembalikan (Barang / Posisi) - Transitif', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '本を本棚に戻します。', 'ei': 'Mengembalikan buku ke rak buku.',
        'ch': [('戻', 'もど(る) / もど(す)', 'レイ', 'Kembali/Balik. 戶 (pintu) + 大 (anjing besar yang menunduk ke bawah kaki). Anjing piaraan yang pulang dan meringkuk menyundul pintu.')],
        'co': 'Ada barang yang tergeser keluar dari pintunya, lalu kamu bertindak aktif menyuruh "anjing benda (大)" itu berbalik kembali melangkah masuk gerbang (戶) ke asalnya. <b>Kamu yang mengembalikan barang A.</b>'
    },
    {
        'w': '戻る', 'y': 'もどる', 'a': 'Kembali / Balik Badan (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'すぐ席に戻ります。', 'ei': 'Akan segera kembali ke kursi/meja.',
        'ch': [('戻', 'もど(る)', 'レイ', 'Kembali/Memutar arah.')],
        'co': 'Tubuh manusia atau barang secara fisik bergerak mundur untuk menempati titik yang sudah ia tinggalkan sebelumnya. "Aku (si Pembicara) segera <b>Kembali / Putar arah</b> menuju posisi awal."'
    },
    {
        'w': '壊す', 'y': 'こわす', 'a': 'Merusakkan / Menghancurkan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '時計を壊してしまいました。', 'ei': 'Terlanjur (nggak sengaja) merusakkan jam.',
        'ch': [('壊', 'こわ(す)', 'カイ', 'Hancur/Roboh. 土 (tanah/batu lempung) + 褱 (kain bungkus menyembunyikan pakaian airmata). Tembok tanah yang menangis luluh lantak.')],
        'co': 'Tangan usil atau pukulan gada besi-mu menabrak struktur mesin/tembok (土). "KRAAK!", baut-baut rontok berjatuhan. <b>Kamulah tersangka yang menghancurkannya (Sengaja / Ceroboh)</b>.'
    },
    {
        'w': '壊れる', 'y': 'こわれる', 'a': 'Rusak / Hancur (Intransitif)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'カメラが壊れました。', 'ei': 'Kameranya rusak.',
        'ch': [('壊', 'こわ(れる)', 'カイ', 'Hancur/Runtuh.')],
        'co': 'Kamera atau HP tiba-tiba layarnya retak blank hitam saat dicas. Bukan salahmu, tapi benda malang (土) itu yang umurnya pendek atau aus. <b>Kondisi benda menjadi Rusak pasif otomatis</b>. (Kowarete).'
    },
    {
        'w': '空く', 'y': 'あく', 'a': 'Kosong / Luang / Berlubang', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '席が空いています。', 'ei': 'Kursinya (sedang) kosong.',
        'ch': [('空', 'そら / あ(く) / から', 'クウ', 'Kosong/Langit. 穴 (lubang terowongan gua atas) + 工 (garis ukur/pekerjaan buatan dewa). Gua raksasa tak terukur.')],
        'co': 'Kanji asalnya berarti Langit yang tidak dihalangi rintangan bintang apapun (空). Karena tak bersinggungan apapun, bergeser makna jadi celah <b>Kekosongan / Bangku kosong / Waktu senggang</b>.'
    },
    {
        'w': '行う', 'y': 'おこなう', 'a': 'Menyelenggarakan / Melaksanakan Acara', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '明日、試験を行います。', 'ei': 'Besok (kami) akan menyelenggarakan ujian.',
        'ch': [('行', 'おこな(う)', 'コウ / アン', 'Melaksanakan/Menyelenggarakan (Beda pelafalan dengan Iku/Pergi, tapi kanjinya sama 彳亍 persimpangan jalan).')],
        'co': 'Sama Kanji, beda aura! 行く (Iku) itu jalan kaki. 行う (Okonau) adalah memandu ribuan orang melewati jalan dengan tata letak sakral. <b>Melangsungkan event festival, pesta, atau ujian (resmi)</b>.'
    },
    {
        'w': '選ぶ', 'y': 'えらぶ', 'a': 'Memilih / Menyeleksi', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '好きなケーキを選んでください。', 'ei': 'Tolong pilih kue yang disukai.',
        'ch': [('選', 'えら(ぶ)', 'セン', 'Memilih. 辶 (jalan pelan-pelan keliling) + 巽 (dua balok berderet, orang meletakkan sesajen persembahan). Berkeliling untuk mengambil opsi terbaik.')],
        'co': 'Ada banyak kotak/pilihan berjajar (巽). Kamu mondar-mandir (辶) mengelus dagu sambil memandangi mereka satu persatu, lalu menunjuk satu biji the best. <b>Menyeleksi Pilihan Ganda (Choose)</b>.'
    },
    {
        'w': '咲く', 'y': 'さく', 'a': 'Mekar (Bunga)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '春に桜が咲きます。', 'ei': 'Bunga Sakura mekar di musim semi.',
        'ch': [('咲', 'さ(く)', 'ショウ', 'Mekar/Tertawa (Kuno). 口 (mulut tertawa) + 关 (kepala babi condong miring yang menggeliat menengadah). Mulut terbuka tersenyum.')],
        'co': 'Dulu berarti mulut tertawa. Bunga sakura yang sebelumnya kuncup rapat kini menengadahkan tangkainya (关) dan merekah mengembang bagai mulut yang sedang tersenyum ceria (口). <b>Bunga yang bermekaran</b>.'
    },
    {
        'w': '吹く', 'y': 'ふく', 'a': 'Bertiup (Angin) / Meniup', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '強い風が吹いています。', 'ei': 'Angin kencang sedang bertiup.',
        'ch': [('吹', 'ふ(く)', 'スイ', 'Meniup. 口 (mulut) + 欠 (orang merentangkan badan lalu bernapas lega).')],
        'co': 'Mulut raksasa langit (口) dan hembusan udara (欠) yang menyeruak keluar mendinginkan segalanya. Berlaku untuk <b>Hembusan udara kencang (Angin)</b> dan aksi bibir orang main seruling/meniup lilin.'
    },
    {
        'w': '外す', 'y': 'はずす', 'a': 'Melepas (Kacamata) / Absen dari kursi', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '時計を外します。 / 席を外しています。', 'ei': 'Melepas jam tangan. / (Dia sedang) tidak ada di mejanya (absen).',
        'ch': [('外', 'はず(す) / そと', 'ガイ', 'Luar/Melenceng. 夕 (bulan sabit/malam) + 卜 (ramalan meramal tempurung). Ramalan yang dilakukan di luar rumah dalam gelap.')],
        'co': 'Punya makna membuang sesuatu ke "LUAR" batas (外). Mencopot aksesoris kaitan (cincin, jam, kacamata) ke luar badan (bukan脱ぐlepas baju). Arti ke-2: Badanmu yang melangkah keluar minggat dari meja kersa. <b>Melepaskan kaitan / Meninggalkan meja sejenak</b>.'
    },
    {
        'w': '要る', 'y': 'いる', 'a': 'Membutuhkan / Diperlukan', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': 'ビザが要ります。', 'ei': 'Membutuhkan visa.',
        'ch': [('要', 'い(る) / かなめ', 'ヨウ', 'Penting/Membutuhkan. 西 (keranjang pinggang) + 女 (perempuan). Tangan yang memeluk pinggang wanita (inti penyangga).')],
        'co': 'Inti penopang yang kalau tidak ada, semua ambruk (要). Sama seperti Iru (居る Ada hidup), TAPI 要る adalah <b>Golongan 1</b>! Konjugasinya: itte (bukan ite), iranai (bukan inai). <b>Memerlukan / Butuh</b>.'
    },
    {
        'w': '離す', 'y': 'はなす', 'a': 'Melepaskan genggaman / Menjauhkan', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '手を離さないで。', 'ei': 'Jangan lepaskan tanganku.',
        'ch': [('離', 'はな(す)', 'リ', 'Terpisah/Burung Li. 隹 (burung kecil) terbang di dekat 凶 (bahaya jebakan hewan jaring).')],
        'co': 'Burung yang terlepas dari cengkeraman jaring (隹). Beda huruf dengan 話す (Bicara). Ini bermakna merenggangkan (離) pelukan atau membiarkan objek menjauh secara jarak meter. <b>Melepaskan genggaman (tali, pacar)</b>.'
    },
    {
        'w': '落とす', 'y': 'おとす', 'a': 'Menjatuhkan (Transitif) / Menghilangkan', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '財布を落としました。', 'ei': 'Telah menjatuhkan (menghilangkan) dompet.',
        'ch': [('落', 'お(とす)', 'ラク', 'Gugur/Jatuh (Daun berjatuhan).')],
        'co': 'Kamu (subjek) sedang bengong memegang gelas. Tiba-tiba jarimu lengah dan GUBRAK! Kausengaja maupun kelupaan membiarkan kaitan benda rontok ke tanah. <b>Kamu yang menjatuhkan dompet (sehingga hilang)</b>.'
    },
    {
        'w': '思う', 'y': 'おもう', 'a': 'Memikirkan / Merasa / Menganggap', 'g': 1, 'subdeck': 'KK::Sensori_Emosi',
        'ej': '美味しいと思います。', 'ei': 'Saya pikir/merasa (itu) enak.',
        'ch': [('思', 'おも(う)', 'シ', 'Berpikir/Otak. 田 (ubah bentuk dari 囟 otak besar berserat) + 心 (hati). Analisa akal dipadu getaran batin (perasaan).')],
        'co': 'Sebuah fungsi otak (田) yang bertumpu pada batin nurani terdalam manusia (心). Jadi maknanya tidak kaku ilmiah seperti 考える (Kangae). Ini murni insting: <b>Aku merasa (I think/feel that...)</b>.'
    },
    {
        'w': '倒す', 'y': 'たおす', 'a': 'Merobohkan / Mengalahkan (Bos musuh)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '木を倒す。 / ボスを倒す。', 'ei': 'Merobohkan pohon. / Mengalahkan bos.',
        'ch': [('倒', 'たお(す) / たお(れる)', 'トウ', 'Roboh/Jatuh terbalik. 亻 (orang) + 到 (tiba mendadak). Orang yang dihempaskan tiba-tiba jungkir balik tertembak.')],
        'co': 'Gara-gara tinjuanmu, orang yang tegak berdiri itu kepalanya membentur lantai dan jatuh terlentang (倒). Serangan yang <b>Merobohkan pohon, pion bowling, atau Bos Terakhir (Victory K.O)</b>!'
    },
    {
        'w': '流す', 'y': 'ながす', 'a': 'Mengalirkan / Membilas (Toilet) / Menangis', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'トイレの水を流します。', 'ei': 'Mengalirkan air (membilas flush) toilet.',
        'ch': [('流', 'なが(す) / なが(れる)', 'リュウ', 'Mengalir. 氵 (air) + 𠫓 (bayi lahir sungsang keluar). Air ketuban/janin yang mengalir halus merosot ke bawah tanpa tahanan.')],
        'co': 'Cairan (氵) dipaksa mengarungi lereng, meluncur menyapu benda di depannya. Seperti menyiramkan (流) tumpahan air ke WC atau mengucurkan tetesan airmata penyesalan (Namida wo nagasu).'
    },
    {
        'w': '打つ', 'y': 'うつ', 'a': 'Memukul (Benda tumpul ringan) / Mengetik', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'パソコンを打ちます。 / ボールを打つ。', 'ei': 'Mengetik laptop. / Memukul bola kasti.',
        'ch': [('打', 'う(つ)', 'ダ', 'Memukul perlahan. 扌 (tangan) + 丁 (paku lurus presisi). Ketukan berirama menancapkan paku tajam/nada.')],
        'co': 'Gaya pukulannya (扌) itu tek tok tek tok dengan akurasi presisi paku kecil (丁). Beda dengan 殴る yang buat kekerasan. 打つ dipakai untuk main kasti (baseball), palu paku, sampai <b>Mengetik tuts keyboard</b>!'
    },
    {
        'w': '逃げる', 'y': 'にげる', 'a': 'Kabur / Melarikan diri', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '泥棒が逃げました。', 'ei': 'Pencuri itu kabur.',
        'ch': [('逃', 'に(げる)', 'トウ', 'Kabur. 辶 (jalan kaki menjauh pelan) + 兆 (ramalan sial/retakan cangkang kura-kura membelah dua pertanda bahaya).')],
        'co': 'Langkah gesit si pencuri melesat di aspal jalan (辶) karena dia melihat sinyal marabahaya merah (兆 polisi datang). Tergesa-gesa menjauhi tkp. <b>Melarikan diri/Minggat secepatnya</b>. (Nigete).'
    },
    {
        'w': '走る', 'y': 'はしる', 'a': 'Berlari', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '道で走らないでください。', 'ei': 'Tolong jangan berlari di jalan.',
        'ch': [('走', 'はし(る)', 'ソウ', 'Berlari. 土 (tanah orang mengayun lengan besar) + 止 (tapak kaki menjejak kencang bumi).')],
        'co': 'Kanji asalnya mengukir orang yang mengayunkan dua tangan menghentak tanah kuat-kuat! Kecepatan maksimal melampaui jalan cepat (歩). Awas, ini akhiran RU tapi konjugasi <b>Golongan 1 (Hashitte)</b>!'
    },
    {
        'w': '足す', 'y': 'たす', 'a': 'Menambahkan / Menambah (Matematika)', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '塩を少し足します。 / １足す１は２。', 'ei': 'Menambah garam sedikit. / Satu tambah satu sama dengan dua.',
        'ch': [('足', 'た(す) / あし', 'ソク', 'Kaki/Menambah cukup. 口 (lutut tertekuk/cukup) + 止 (telapak kaki di atas tanah). Kaki melangkah menutup kekurangan.')],
        'co': 'Kaki yang berjalan menempuh satu langkah lagi menambal celah kosong agar pas sempurna (足). Kamu (subjek) beraksi memberi tuangan ekstra (garam). <b>Plus/Plus/Menambah (Add)</b>.'
    },
    {
        'w': '分ける', 'y': 'わける', 'a': 'Membagi / Memisahkan (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'ケーキを３つに分けます。', 'ei': 'Membagi kue menjadi tiga potong.',
        'ch': [('分', 'わ(ける) / わ(かる)', 'ブン', 'Membagi/Bagian. 八 (dua bilah menyebar/terbelah) + 刀 (pisau pemotong daging tajam).')],
        'co': 'Pisau golok maut (刀) mengiris melintang memecah (八) roti utuh menjadi pecahan simetris berserakan. Kamulah sang pemotong. <b>Membagikan porsi kepada kawan (Share/Divide)</b>.'
    },
    {
        'w': '飛ぶ', 'y': 'とぶ', 'a': 'Terbang / Melompat terbang', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '鳥が空を飛んでいます。', 'ei': 'Burung sedang terbang di langit.',
        'ch': [('飛', 'と(ぶ)', 'ヒ', 'Terbang/Melesat. (Piktogram sepasang sayap atas bawah 升升 mengepak dan bulu-bulunya meliuk-liuk tertiup angin angkasa).')],
        'co': 'Dua keping sayap simetris mengepak membelah atmosfer! Murni aksi melawan beban bumi. Benda apapun yang tak menyentuh lantai dan bermanuver di udara (burung, nyamuk, rudal) disebut <b>Terbang bebas</b>.'
    },
    {
        'w': '生きる', 'y': 'いきる', 'a': 'Hidup / Bernyawa (Melangsungkan hidup)', 'g': 2, 'subdeck': 'KK::Kondisi_Status',
        'ej': '１００歳まで生きたいです。', 'ei': 'Saya ingin hidup sampai 100 tahun.',
        'ch': [('生', 'い(きる) / う(む) / なま', 'セイ / ショウ', 'Kehidupan baru/Lahir. Piktogram tunas (屮) yang baru pecah dari tanah datar gersang (一).')],
        'co': 'Bersemi! Energi murni (生) menyeruak melepaskan napas melangsungkan getaran batin <b>(Bertahan Hidup panjang umur)</b>. Sangat spiritual dan puitis. Golongan 2 ya (Ikite).'
    }
]
