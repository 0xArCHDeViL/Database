# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '消す', 'y': 'けす', 'a': 'Menghapus / Mematikan (Api, Listrik)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'テレビを消します。', 'ei': 'Mematikan TV.',
        'ch': [('消', 'け(す) / き(える)', 'ショウ', 'Padam/Lari. 氵 (air) + 肖 (daging yang menciut kecil/meredup). Cairan yang meredam bara api sampai mati total.')],
        'co': 'Air (氵) mengguyur daging api/nyawa listrik sehingga porsinya mengkerut menciut (肖). Kamu bertindak memutuskan siklus dayanya. <b>Mematikan benda elektronik, api rokok, atau menghapus noda papan</b>.'
    },
    {
        'w': '押す', 'y': 'おす', 'a': 'Menekan / Mendorong (Tombol, Stempel)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'ボタンを押してください。', 'ei': 'Tolong tekan tombolnya.',
        'ch': [('押', 'お(す)', 'オウ', 'Menekan/Stempel. 扌 (tangan) + 甲 (cangkang keras kura-kura/tameng). Tangan yang mendorong berat/keras cangkang baju zirah.')],
        'co': 'Kerahkan otot 扌 (tanganmu) untuk memberikan dorongan lurus ke arah cangkang keras (甲) pintu, tombol darurat, stempel dokumen. Jari telunjukmu memicu hal besar! <b>Menekan ke dalam (Push)</b>.'
    },
    {
        'w': '引く', 'y': 'ひく', 'a': 'Menarik (Tali, Garis, Diskon)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'ドアを引きます。', 'ei': 'Menarik pintu.',
        'ch': [('引', 'ひ(く)', 'イン', 'Menarik. 弓 (busur panah) + 丨 (tali tegak ditarik mundur). Meregangkan tali ke belakang.')],
        'co': 'Jangan ketukar 弾く (bermain piano/gitar). Ini murni <b>menarik senar (丨) busur secara kencang mendekati dada (Pull)</b>. Pintu ditarik mundur, garis lurus ditarik, harga barang ditarik turun (diskon).'
    },
    {
        'w': '被る', 'y': 'かぶる', 'a': 'Memakai (Khusus Kepala/Topi)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '帽子を被ります。', 'ei': 'Memakai topi.',
        'ch': [('被', 'かぶ(る)', 'ヒ', 'Mengenakan/Ditutupi selimut. 衤 (pakaian kerah ganda) + 皮 (kulit yang ditelanjangi/kulit luar). Memberikan selubung kulit ganti.')],
        'co': 'Kalauを着る itu kemeja, 被る itu ibarat cangkang payung yang <b>menyelubungi/Menutupi dari atas turun ke kepala</b> (topi, helm). Awas, akhiran -ru tapi <b>Golongan 1! (Kabutte, Kaburanai)</b>.'
    },
    {
        'w': '開く', 'y': 'ひらく', 'a': 'Membuka (Lebar merentang, misal Buku/Bunga)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '本を開いてください。', 'ei': 'Tolong buka bukunya.',
        'ch': [('開', 'ひら(く) / あ(ける)', 'カイ', 'Membuka (dua arah).')],
        'co': 'Berbeda dengan 開ける yang buka pintu satu arah. 開く ini menunjuk pada objek yang dilipat (buku, majalah, bunga, payung), lalu direntangkan simetris ke kiri-kanan. <b>Membentangkan/Membuka lipatan (Open)</b>.'
    },
    {
        'w': '閉じる', 'y': 'とじる', 'a': 'Menutup (Melipat kembali, misal Mata/Buku)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '目を閉じます。', 'ei': 'Menutup mata.',
        'ch': [('閉', 'と(じる) / し(める)', 'ヘイ', 'Menutup.')],
        'co': 'Lawan dari ひらく (Hiraku). Halaman buku yang sudah menganga direntang, sekarang dirapatkan lagi engselnya (とじる). <b>Melipat, mengatupkan, atau Menutup kelopak matamu</b>.'
    },
    {
        'w': '上げる', 'y': 'あげる', 'a': 'Menaikkan / Memberi (ke orang lain)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '手を上げます。 / プレゼントを上げます。', 'ei': 'Menaikkan tangan. / Memberikan kado.',
        'ch': [('上', 'あ(げる) / うえ', 'ジョウ', 'Atas/Naik. Garis pendek tegak di atas garis dasar lurus 一.')],
        'co': 'Garis vertikal yang menanjak naik di atas plafon. <b>Mengangkat derajat / posisi benda ke udara (Menaikkan)</b>. Karena dianggap mulia, punya arti kedua: <b>Memberi persembahan</b>.'
    },
    {
        'w': '下げる', 'y': 'さげる', 'a': 'Menurunkan (Posisi, Harga, Suhu)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '温度を下げてください。', 'ei': 'Tolong turunkan suhunya.',
        'ch': [('下', 'さ(げる) / した', 'カ / ゲ', 'Bawah/Turun. Garis tegak kebalik di bawah tanah 一.')],
        'co': 'Aksi tanganmu dengan kuat (transitif) <b>menekan ke Bawah derajat sesuatu</b>. Suhu AC digeser remote-nya, harga ditawar murah, piring kosong digeser dari meja.'
    },
    {
        'w': '辞める', 'y': 'やめる', 'a': 'Berhenti / Mengundurkan diri (Pekerjaan/Status)', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '会社を辞めました。', 'ei': 'Berhenti bekerja dari perusahaan.',
        'ch': [('辞', 'や(める) / じ', 'ジ', 'Mengundurkan diri / Kata-kata menolak. 舌 (lidah/kata) + 辛 (jarum/hukuman/pahit).')],
        'co': 'Awas! Pelafalannya sama (Yameru), tapi 辞める (Kanji menolak kata pahit) dipakai khusus untuk <b>Resign / Berhenti Bekerja selamanya</b>. (Kalau 止める itu menghentikan mesin motor).'
    },
    {
        'w': '会う', 'y': 'あう', 'a': 'Bertemu (Orang)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '友達に会います。', 'ei': 'Bertemu teman.',
        'ch': [('会', 'あ(う)', 'カイ', 'Bertemu/Berkumpul. 人 (dua orang) bernaung mengobrol seru di bawah satu atap 亼.')],
        'co': 'Kanji ini jelas: Dua entitas manusia (亻) bersepakat ngopi atau bertegur sapa di bawah satu titik (亼). <b>Pertemuan Manusia Berjodoh (Meet up)</b>.'
    },
    {
        'w': '合う', 'y': 'あう', 'a': 'Cocok / Serasi / Bergabung (Benda/Pikiran)', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': 'この靴は足に合います。', 'ei': 'Sepatu ini cocok (pas) di kaki.',
        'ch': [('合', 'あ(う)', 'ゴウ', 'Cocok/Menyatukan. 亼 (mengumpulkan/tutup) + 口 (wadah mulut). Menutup botol yang ukurannya pas simetris.')],
        'co': 'Pelafalan sama (Au). Tapi ini tentang bongkahan puzzle tak bernyawa yang masuk lubang secara simetris klik (合). <b>Baju yang ukurannya Pas, atau Opini yang cocok masuk akal (Suit / Fit)</b>.'
    },
    {
        'w': '付き合う', 'y': 'つきあう', 'a': 'Berpacaran / Menemani pergaulan', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '彼女と付き合っています。', 'ei': 'Sedang berpacaran dengannya (pacar perempuan).',
        'ch': [
            ('付', 'つ(き)', 'フ', 'Menempel terus (Lem / Bayangan).'),
            ('合', 'あ(う)', 'ゴウ', 'Cocok / Pas.')
        ],
        'co': 'Gabungan maut: Sosokmu selalu mengekori menempel erat (付) padanya karena kalian sudah merasa klop secara emosi dan hobi (合). <b>Berpacaran saling mesra / atau sekadar Nongkrong menemani kolega kerja minum-minum santai</b>.'
    },
    {
        'w': '結婚する', 'y': 'けっこんする', 'a': 'Menikah', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '来月、結婚します。', 'ei': 'Bulan depan menikah.',
        'ch': [
            ('結', 'むす(ぶ)', 'ケツ', 'Mengikat (tali merah nasib). 糸 (benang) + 吉 (keberuntungan sakti). Simpul nasib.'),
            ('婚', '–', 'コン', 'Pernikahan. 女 (wanita) + 昏 (senja / gelap). Tradisi Tiongkok kuno mengantarkan pengantin wanita saat matahari terbenam (sore hari).')
        ],
        'co': 'Melakukan ikatan simpul benang (結) bersama sang mempelai perempuan (女) di waktu senja sakral berdua (昏). Ya, janji sehidup semati <b>(Pernikahan sah resmi / Marry)</b>.'
    },
    {
        'w': '婚約する', 'y': 'こんやくする', 'a': 'Bertunangan (Lamaran masuk)', 'g': 3, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '私たちは婚約しました。', 'ei': 'Kami berdua telah bertunangan.',
        'ch': [
            ('婚', '–', 'コン', 'Pernikahan (Wanita + Senja).'),
            ('約', 'やく', 'ヤク', 'Janji / Kontrak. 糸 (benang tak terlihat) + 勺 (menyendok menyatukan kaitan).')
        ],
        'co': 'Memasukkan kaitan cincin (約) secara verbal atau simbolis sebelum benar-benar menggelar perayaan suci Pernikahan (婚). Kamu sudah DP atau di-booking duluan oleh calonmu. <b>Bertunangan (Engaged)</b>.'
    },
    {
        'w': '回す', 'y': 'まわす', 'a': 'Memutar (Benda - Transitif)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '時計の針を回します。', 'ei': 'Memutar jarum jam.',
        'ch': [('回', 'まわ(す)', 'カイ', 'Berputar. 囗 (lingkaran pusaran luar) + 口 (pusaran dalam). Pusaran air arus air bergelung putar-putar.')],
        'co': 'Dua lingkaran spiral beranak di dalam pusaran abadi (回). Tanganmu memegang tuas kenop (radio/mesin gacha/gasing), lalu merotasi poros tersebut 360 derajat tiada putusnya. <b>Aksi Memutar objek (Turn / Spin)</b>.'
    },
    {
        'w': '無くす', 'y': 'なくす', 'a': 'Menghilangkan / Kehilangan (Barang)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': 'パスポートを無くしました。', 'ei': 'Menghilangkan / Kehilangan paspor.',
        'ch': [('無', 'な(くす)', 'ム', 'Tidak ada / Tiada / Kosong murni. 𠂛 (menari berayun memegang jumbai di atas bara api 灬 untuk meminta hujan hingga lenyap kerasukan).')],
        'co': 'Kamu asyik pegang dompet, tetiba di tengah mall "Hah! Kok Kosong Melompong (無) sakuku?". <b>Kamulah tersangka utama (sengaja atau tidak) yang Menyebabkan Lenyapnya Barang itu.</b>'
    },
    {
        'w': '思い出す', 'y': 'おもいだす', 'a': 'Mengingat kembali / Teringat', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '昔のことを思い出します。', 'ei': 'Mengingat kembali masa lalu.',
        'ch': [
            ('思', 'おも(う)', 'シ', 'Pikiran (Otak + Hati).'),
            ('出', 'だ(す)', 'シュツ', 'Mengeluarkan sesuatu yang terkubur.')
        ],
        'co': 'Menggali memori/pikiran (思) yang sudah lama mengendap di dasar selokan batinmu, lalu menariknya paksa memancar Keluar (出) secara nyata di layar matamu saat ini. "AHA! Dulu begini lho!" <b>(Recall / Remember memori)</b>.'
    },
    {
        'w': '急ぐ', 'y': 'いそぐ', 'a': 'Terburu-buru / Bergegas', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '時間がないので急ぎます。', 'ei': 'Karena tidak ada waktu, saya terburu-buru.',
        'ch': [('急', 'いそ(ぐ)', 'キュウ', 'Gawat/Terburu. 刍 (kemasan rumput kering yang dipegang tangan menekan maju/mendesak) + 心 (jantung hati). Detak jantung yang berdebar didesak paksa (adrenalin).')],
        'co': 'Jantung (心) mu dipompa sangat kencang, adrenalin mendesak (刍) dada mau meledak gara-gara kamu telat naik gerbong Shinkansen. Keringat dingin netes tiada henti! <b>Hurry up / Ngebut lari tergopoh (Isoide!)</b>.'
    },
    {
        'w': '履く', 'y': 'はく', 'a': 'Memakai (Khusus Bawah Pinggang: Sepatu/Celana)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '靴を履きます。', 'ei': 'Memakai sepatu.',
        'ch': [('履', 'は(く)', 'リ', 'Memakai (Alas kaki)/Jejak. 尸 (bokong/kaki turun menapak) + 復 (kanji usang: melangkah keluar memakai sendal kulit tenunan 彳 bolak-balik).')],
        'co': 'Pelafalan sama persis dengan 吐く (Haku = Muntah). Tapi ini 履く, aksi <b>Memasukkan kaki ke dalam tabung</b> celana, kaos kaki, atau menyelipkan tapak kakimu ke lubang sepatu bawah pinggang.'
    },
    {
        'w': '動く', 'y': 'うごく', 'a': 'Bergerak / Mesin Menyala', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'エレベーターが動きます。', 'ei': 'Lift (telah menyala dan) bergerak.',
        'ch': [('動', 'うご(く)', 'ドウ', 'Bergerak. 重 (karung yang beratnya menekan) + 力 (tenaga lengan memindahkan beban). Dinamika gaya tarik.')],
        'co': 'Meskipun bebannya segede karung gajah (重), ditendang pakai tenaga nuklir (力) maka benda itu berpindah koordinat GPS! Artinya <b>Objek beralih posisi (Berpindah) atau Indikator mesin (nyala dinamis bukan mati)</b>.'
    },
    {
        'w': '吸う', 'y': 'すう', 'a': 'Menghisap (Rokok / Napas)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': 'タバコを吸います。', 'ei': 'Menghisap rokok.',
        'ch': [('吸', 'す(う)', 'キュウ', 'Menghisap/Menyedot. 口 (mulut menganga) + 及 (tangan mengejar memanjangkan tarikan dari belakang mengejar objek kabur).')],
        'co': 'Mulut (口) diubah jadi moncong vacuum cleaner ajaib yang menarik paksa (及) partikel debu asap di depannya, sampai menyusup turun ke dasar paru-paru terdalam (inhale). <b>Menghirup Oksigen atau Menghisap sebatang asap</b>.'
    },
    {
        'w': '上手くなる', 'y': 'うまくなる', 'a': 'Menjadi Mahir / Semakin Jago', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '日本語が上手くなりました。', 'ei': 'Telah menjadi mahir (bahasa) Jepang.',
        'ch': [
            ('上', 'う', 'ジョウ', 'Atas / Posisi tinggi.'),
            ('手', 'ま', 'シュ', 'Tangan / Skill.')
        ],
        'co': 'Gabungan Kata Sifat-Na (上手 = Jago / Tangan di atas awan mahirnya) dengan kata kerja なる (Menjadi). Artinya level skill RPG kamu dari noob cupu, perlahan berevolusi menanjak. <b>"Naik level jadi Master/Mahir"</b>.'
    },
    {
        'w': '剥く', 'y': 'むく', 'a': 'Mengupas (Kulit Buah/Bawang)', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'みかんを剥きます。', 'ei': 'Mengupas (kulit) jeruk.',
        'ch': [('剥', 'む(く) / は(がす)', 'ハク', 'Mengelupas/Mencungkil. 彔 (memahat/menakik lapisan luaran air mendidih mencair berpisah) + 刂 (pisau tajam). Sayatan menyobek perisai luar.')],
        'co': 'Pisau runcing berdarah dingin (刂) merobek menakik perlindungan jaket armor perisai luar perlindungan (彔). Isinya telanjang terburai terbuka nampak montok. <b>Mengupas lapis luar jeruk, pisang, atau kabel listrik tebal (Peel off)</b>.'
    },
    {
        'w': '渡る', 'y': 'わたる', 'a': 'Menyeberang (Jembatan / Jalan)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '橋を渡ります。', 'ei': 'Menyeberang jembatan.',
        'ch': [('渡', 'わた(る)', 'ト', 'Menyeberang mengarungi sungai. 氵 (air) + 度 (mengukur bentangan dengan langkah kaki / melintasi zona).')],
        'co': 'Awal mula diciptakan melambangkan kapal yang mendayung memecah sungai (氵) dari dermaga A melintasi jembatan ukur (度) menuju dermaga seberang (B). <b>Menyambangi daratan lawan, nyeberang di Zebra Cross maut (Cross the street)</b>.'
    },
    {
        'w': '曲がる', 'y': 'まがる', 'a': 'Berbelok / Membengkok (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '右へ曲がります。', 'ei': 'Berbelok ke kanan.',
        'ch': [('曲', 'ま(がる)', 'キョク', 'Bengkok/Meliuk/Melodi. Piktogram keranjang anyaman bambu lentur L siku tertekuk kotak (ditekuk paksa tidak patah lurus).')],
        'co': 'Jalanan lurus terpaksa di-engsel ditekuk membentuk sikutan siku U (曲) karena pilar raksasa menghalangi aspal lurus. Mobil tidak nabrak maju lurus, tapi badannya terseret ikutan manuver. <b>Berbelok tikungan tajam (Turn Right/Left)</b>.'
    },
    {
        'w': '止まる', 'y': 'とまる', 'a': 'Berhenti / Terparkir (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '車が止まりました。', 'ei': 'Mobil (telah) berhenti.',
        'ch': [('止', 'と(まる)', 'シ', 'Berhenti total menancap tanah. Piktogram jejak telapak kaki jari tegak yang injak aspal keras, membeku.')],
        'co': 'Kaki yang lagi asyik jogging (Berlari), langsung mendadak ngerem (止), tapaknya lengket di semen. Ban mobil terpelanting beku. Aksi otomatis di mana laju benda ter-STOP murni (Tomaru = Benda Berhenti Sendiri/Rem otomatis).'
    },
    {
        'w': '触る', 'y': 'さわる', 'a': 'Menyentuh / Memegang (Rabaan pelan)', 'g': 1, 'subdeck': 'KK::Aktivitas_Fisik',
        'ej': '絵に触らないでください。', 'ei': 'Tolong jangan menyentuh lukisan.',
        'ch': [('触', 'さわ(る)', 'ショク', 'Menyentuh (Tanduk). 角 (tanduk menonjol lancip kumbang/binatang) + 虫 (serangga berantena sensitif meraba udara mangsa).')],
        'co': 'Tanduk kumbang (角) yang super sensitif di ujung kepalanya (虫) meraba-raba dinding licin. Bukan menggenggam keras (を持つ) , melainkan rabaan kepo geli di ujung kulit jari iseng! <b>"Tolong tangannya jangan nyentuh-nyentuh ya! (Touch)"</b>.'
    },
    {
        'w': '忘れる', 'y': 'わすれる', 'a': 'Melupakan / Kelupaan', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '宿題を忘れました。', 'ei': 'Telah melupakan (kelupaan) PR.',
        'ch': [('忘', 'わす(れる)', 'ボウ', 'Melupakan amnesia. 亡 (menghilang tiada bekas / melayang kabur / arwah mati) + 心 (memori getaran sel-sel otak hati).')],
        'co': 'Coba bayangkan ruang brankas memori di dalam hati kecilmu (心). Data-datanya mendadak nguap melayang keluar lari menghilang (亡) entah rongsok kemana. <b>File Not Found di otak. "Duh, PR ku ketinggalan memori lupa!" (Forget)</b>.'
    },
    {
        'w': '点ける', 'y': 'つける', 'a': 'Menyalakan (Lampu, TV, Api)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '電気を点けます。', 'ei': 'Menyalakan listrik / lampu.',
        'ch': [('点', 'つ(ける)', 'テン', 'Titik hitam / Api bara. 占 (meramal tulang patah melubang titik fokus) + 灬 (empat jilatan api membara di dasar panci). Api mungil yang menyala membakar.')],
        'co': 'Dari 4 titik bara kecil meronta-ronta menyala terang di tengah gulita (灬). Kamu menekan saklar steker listrik dan... BYAR! <b>Lampu pijar bersinar menerangi hidupmu (Turn On mesin terang). Golongan 2 Tsukeru lho!</b>'
    },
    {
        'w': '掛ける', 'y': 'かける', 'a': 'Menggantungkan / Mengalungkan / Menelepon', 'g': 2, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': '壁にカレンダーを掛けます。 / 電話を掛ける。', 'ei': 'Menggantungkan kalender di dinding. / Menelepon (menggantung gagang).',
        'ch': [('掛', 'か(ける)', 'カイ', 'Menyantol/Tergantung/Pasang kaitan. 扌 (tangan menjejalkan) + 卦 (menganyam ramalan batang bambu bertumpuk-tumpuk menyilang ke batas paku).')],
        'co': 'Satu kata 1000 arti! Tangan (扌) yang melemparkan / menyantolkan kait jaring / gagang telpon / kacamata (卦) numpang nyangkut gelantungan di suatu dudukan atas tebing. <b>(Hang on / Hook up sesuatu pada penyangga telinga/paku dinding)</b>.'
    },
    {
        'w': '変える', 'y': 'かえる', 'a': 'Mengubah (Wujud/Rencana) - Transitif', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '予定を変えます。', 'ei': 'Mengubah rencana jadwal.',
        'ch': [('変', 'か(える) / へん', 'ヘン', 'Berubah jadi aneh/Modifikasi rongsok. Tangan mengurai tali bundet 夂 memintal jaring kacau.')],
        'co': 'Kamu sebagai Bos Direktur memporak-porandakan tatanan jadwal benang ruwet (変). Yang asalnya hari Senin, kamu tendang diganti secara mutlak menjadi hari Rabu. <b>Kamu biang kerok yang "Mengubah (Change)" struktur wujud awal. Gol 2 (Kaete)!</b>'
    },
    {
        'w': '降ろす', 'y': 'おろす', 'a': 'Menarik Uang / Menurunkan (Barang/Penumpang)', 'g': 1, 'subdeck': 'KK::Pekerjaan_Tugas',
        'ej': 'お金を降ろします。', 'ei': 'Menarik (menurunkan saldo) uang.',
        'ch': [('降', 'お(ろす) / お(りる)', 'コウ', 'Turun dari puncak. 阝 (bukit gunung tinggi) tempat asal terjun meluncur 夂 ke lembah palung curam.')],
        'co': 'Kadang ditulis 下ろす. Benda / Saldo Bank yang asalnya ngendon berlimpah tinggi di brankas mesin ATM, kamu paksa "Terjun" (降) ngucur masuk kantong dompet aspalmu. <b>Turunkan penumpang (bus) atau Cairin Uang Tarikan keras</b>.'
    },
    {
        'w': '返す', 'y': 'かえす', 'a': 'Mengembalikan (Barang Pinjaman)', 'g': 1, 'subdeck': 'KK::Interaksi_Sosial',
        'ej': '図書館に本を返します。', 'ei': 'Mengembalikan buku ke perpustakaan.',
        'ch': [('返', 'かえ(す)', 'ヘン', 'Membalik/Kembali hal awal. 辶 (jalan mundur melintasi) + 反 (terbalik tebing memutar 180 derajat jungkir). Memantul jalan balik.')],
        'co': 'Barang komik/uang yang udah sukses nangkring ngerampok rumahmu (反), dipaksa ditendang dikirim jalan mundur (辶) ke rumah bos yang berhak (sang empunya sah). <b>(Return barang pinjaman) Kaeshimasu!</b>'
    },
    {
        'w': '汚す', 'y': 'よごす', 'a': 'Mengotori (Sengaja/Transitif)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '服を汚しました。', 'ei': 'Telah (tidak sengaja) mengotori baju.',
        'ch': [('汚', 'よご(す) / きたな(い)', 'オ', 'Kotor/Bernoda jelek. 氵 (air lumpur / genangan busuk hitam) + 亏 (napas melengkung tertahan / hal tak rata cacat). Benda putih mulus bernoda noda hitam.')],
        'co': 'Ugh, kamu si tangan ceroboh numpahin genangan air comberan hitam luntur (氵) ke baju Gucci putih kinclongmu (亏). Otomatis kain rusak kucel. <b>Kamu biang yang bikin kotor dekil penuh noda! (Yogosu - Transitif).</b>'
    },
    {
        'w': '汚れる', 'y': 'よごれる', 'a': 'Menjadi Kotor (Otomatis/Intransitif)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '手が汚れました。', 'ei': 'Tangannya menjadi kotor.',
        'ch': [('汚', 'よご(れる)', 'オ', 'Benda Kucel. Lumpur air menodai baju suci.')],
        'co': 'Nah yang ini Golongan 2 (Yogoreru)! Objek malang bajumu yang polos suci itu diam-diam menyerap debu noda kelam seiring pemakaian, jadi kumal secara ajaib alamiah (pasif). <b>Terkotori keadaan (Dirtied automatically).</b>'
    },
    {
        'w': '無くなる', 'y': 'なくなる', 'a': 'Menghilang (Hilang)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '財布が無くなりました。', 'ei': 'Dompetnya (telah) hilang.',
        'ch': [('無', 'な(い)', 'ム', 'Kosong tiada (Mantra api melenyapkan bara menari).')],
        'co': 'Beda Kanji dengan 亡くなる (Orang Meninggal). 無 (Kosong) + なる (menjadi). Barang di meja yang tadinya berwujud fisik padat 3D, mendadak berubah siluman lenyap dari dimensi realita. <b>Wujudnya Menguap ilang tak bersisa (Lost/Gone)!</b>'
    },
    {
        'w': '産む', 'y': 'うむ', 'a': 'Melahirkan (Bayi / Telur)', 'g': 1, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '鶏が卵を産みます。', 'ei': 'Ayam bertelur / melahirkan telur.',
        'ch': [('産', 'う(む) / さん', 'サン', 'Produksi beranak melahirkan (Pabrik biologi). 彦 (dahi pria / anak keturunan merangkak panggul membengkak) + 生 (kelahiran tunas pucuk baru hidup). Ibu mengejan keras.')],
        'co': 'Beda kanji tipis dengan 生む (membuahkan hasil abstrak). Ini 産 (Kelahiran Fisik Sakit Mulas). Ibu/Unggas yang mengejan membongkar panggul (彦) demi mendorong keluar nyawa daging tangisan kehidupan baru (生). <b>Beranak (Birth) Umu.</b>'
    },
    {
        'w': '生まれる', 'y': 'うまれる', 'a': 'Lahir (Ke dunia)', 'g': 2, 'subdeck': 'KK::Perubahan_Kondisi',
        'ej': '赤ちゃんが生まれました。', 'ei': 'Bayi (telah) lahir.',
        'ch': [('生', 'う(まれる)', 'セイ', 'Kelahiran nyawa suci. Tunas tanaman pucuk hijau (屮) yang baru saja berhasil memecah kerak lapisan kulit bumi datar (一) menyambut mentari sinar. Puitis banget.')],
        'co': 'Sang orok bayi (tunas) tidak peduli penderitaan sang ibu. Ia hanya tahu dirinya meluncur memandang tangisan cemerlang perdananya di hamparan bumi bersinar. <b>Keadaan Di-lahir-kan (Be born) / Umareru Gol 2.</b>'
    },
    {
        'w': '慣れる', 'y': 'なれる', 'a': 'Terbiasa (Adaptasi lingkungan)', 'g': 2, 'subdeck': 'KK::Kondisi_Status',
        'ej': '日本の生活に慣れました。', 'ei': 'Telah terbiasa dengan kehidupan Jepang.',
        'ch': [('慣', 'な(れる)', 'カン', 'Rutinitas menumpuk terbiasa (Hati yang tebal kebal). 忄 (jantung mental nurani memori) + 貫 (uang keping kuno logam menusuk tali renteng memanjang berulang repetisi numpuk). Hati yang ditusuk rutinitas repetisi.')],
        'co': 'Jantung mental nuranimu (忄) di-spam ditusuk (貫) ribuan beban budaya Jepang / macet yang repetitif tiap detik tiada akhir. Otakmu adaptasi mematikan rasa kejutnya, beralih jadi mode autopilot ngantuk. <b>"Yah elah biasa aja kali" (Get used to it / Terbiasa)!</b>'
    },
    {
        'w': '乗る', 'y': 'のる', 'a': 'Menaiki (Kendaraan / Pijakan Atas)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '電車に乗ります。', 'ei': 'Naik (ke dalam) kereta.',
        'ch': [('乗', 'の(る)', 'ジョウ', 'Menunggang tunggangan. (Piktogram orang posisi mengangkang lebar kaki membelah 舛 / berjongkok menjepit dahan tebal pohon / punggung kuda kayu 木 untuk bermanuver stabil melaju).')],
        'co': 'Pantatmu mengangkang menunggangi pelana gahar kuda bergetar liar / gerbong kereta (乗) layaknya cowboy sakti nangkring menyeimbangkan kaki di pijakan platform berjalan! <b>Naik menduduki kendaraan / lift eskalator (Ride on).</b>'
    },
    {
        'w': '掛かる', 'y': 'かかる', 'a': 'Membutuhkan (Waktu / Uang) / Tersangkut', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': '東京まで３時間掛かります。', 'ei': 'Membutuhkan waktu 3 jam sampai Tokyo.',
        'ch': [('掛', 'か(かる)', 'カイ', 'Tergantung menyangkut tebing (Kaitan jaring tebing).')],
        'co': 'Kok sama Kanjinya sama 掛ける? Kakeru (Transitif gantung kalender), Kakaru (Intransitif dompetmu/waktumu TERSANGKUT disita perjalanannya). Uangmu melayang 1 juta nyangkut di tol. Waktumu ludes nggantung di bus nunggu nyampe tujuan! <b>Makan Waktu / Nelan Biaya Banyak!</b>'
    },
    {
        'w': '分かる', 'y': 'わかる', 'a': 'Mengerti / Memahami', 'g': 1, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '日本語が分かります。', 'ei': 'Mengerti (bahasa) Jepang.',
        'ch': [('分', 'わ(かる)', 'ブン', 'Membelah jeroan. Pisau (刀) membelah melon (八).')],
        'co': 'Lah kok kanji "Membelah"? Betul! Orang cerdas itu membelah keruwetan masalah benang kusut dengan pisau ketajamannya (分). Setelah diurai keping per keping serpihannya jelas nyata transparan telanjang! Itulah esensi <b>"AHA! Paham terang benderang (Understand/I see)!"</b>'
    },
    {
        'w': '降りる', 'y': 'おりる', 'a': 'Menuruni (Turun dari kendaraan)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': 'バスを降ります。', 'ei': 'Turun dari bus.',
        'ch': [('降', 'お(りる)', 'コウ', 'Terjun turun bukit ngesot. (Bukit tinggi tempat dewa meluncur 夂 turun kaki).')],
        'co': 'Oriru itu eksklusif Golongan 2 (Orite, Orinai)! Kakimu menjejak gravitasi ke bawah curam bukit (降), meninggalkan singgasana empuk kursi bus menuju kerasnya aspal pijakan realita! <b>Lawan kata dari 乗る. "Turun woii udah nyampe terminal!"</b>'
    },
    {
        'w': '込む', 'y': 'こむ', 'a': 'Penuh Sesak / Macet', 'g': 1, 'subdeck': 'KK::Kondisi_Status',
        'ej': '電車が込んでいます。', 'ei': 'Keretanya (sedang keadaan) penuh sesak.',
        'ch': [('込', 'こ(む)', '–', 'Terjejal sesak membeludak (KOKUJI/Kanji bikinan asli Jepang ajaib). 辶 (jalan/melaju maju ruang) + 入 (masuk merangsek memompa desak menumpuk).')],
        'co': 'Orang-orang (入) maksa maju jalan dorong-dorongan masuk (辶) dalam gerbong sarden sempit mungil sumpek ngap eungap. Melesak tumpang tindih berdesak tumpah ruah <b>Sumpel membludak / Jalanan Macet Gila (Crowded).</b>'
    },
    {
        'w': '間違える', 'y': 'まちがえる', 'a': 'Salah / Keliru / Melakukan Kesalahan', 'g': 2, 'subdeck': 'KK::Kognitif_Pendidikan',
        'ej': '答えを間違えました。', 'ei': 'Saya (telah keliru) salah jawaban.',
        'ch': [
            ('間', 'ま', 'カン', 'Ruang sela waktu / Jarak pintu (Matahari ngintip sela pintu).'),
            ('違', 'ちが(える)', 'イ', 'Menyimpang lari jalan berlawanan punggung beda.')
        ],
        'co': 'Tindak tanduk pilihan jawaban aslimu (違) meleset keluar sela jauh dari gerbang target celah kunci kebenaran (間). Nyasar blangsak masuk jurang salah perhitungan total zonk. Kamu sebagai subjek <b>Bikin Eror Keliru ceroboh! Machigaeru Gol 2.</b>'
    },
    {
        'w': '風邪を引く', 'y': 'かぜをひく', 'a': 'Masuk Angin / Kena Flu', 'g': 1, 'subdeck': 'KK::Ungkapan_Khusus',
        'ej': '風邪を引いたみたいです。', 'ei': 'Sepertinya (saya) masuk angin.',
        'ch': [
            ('風', 'かぜ', 'フウ', 'Angin berhembus 虫 parasit wabah penyusup masuk kulit.'),
            ('邪', '–', 'ジャ', 'Kejahatan iblis taring penyimpangan ilmu hitam nyasar.'),
            ('引', 'ひ(く)', 'イン', 'Menarik seret tali busur belakang curi masuk dada.')
        ],
        'co': 'Hati-hati frasa maut ini (Kaze wo hiku)! Zaman purba konon penyakit ditiupkan setan Angin Jahat beracun (風邪 Kaze). Kamu tanpa sadar Menarik/Menghirup (引く Hiku) hawa kutukan flu setan itu nancep nyedot ke dalam rongga paru-parumu! <b>Hatchi! Bersin Kena Flu Demam.</b>'
    },
    {
        'w': '咳が出る', 'y': 'せきがでる', 'a': 'Batuk (Mengeluarkan batuk)', 'g': 2, 'subdeck': 'KK::Ungkapan_Khusus',
        'ej': '咳が止まらない。咳が出ます。', 'ei': 'Batuknya tidak berhenti. Batuk keluar.',
        'ch': [
            ('咳', 'せき', 'ガイ', 'Batuk. 口 (mulut nganga) + 亥 (babi hutan berbulu ngorok kasar menahan sesak). Lendir di tenggorokan.'),
            ('出', 'で(る)', 'シュツ', 'Keluar mendesak dari kuncup tanah lubang.')
        ],
        'co': 'Lendir iblis tersangkut nempel gatal di pipa amandel, membuat tenggorokan berdengkur mendengus kasar memompa babi ngorok (亥). Mulutmu mendesak memuntahkannya meloncat (出る) muncrat keluar. <b>Uhuk-uhuk! Batuk (Cough).</b>'
    },
    {
        'w': '病気に罹る', 'y': 'びょうきにかかる', 'a': 'Jatuh Sakit / Terkena Penyakit', 'g': 1, 'subdeck': 'KK::Ungkapan_Khusus',
        'ej': '重い病気に罹りました。', 'ei': 'Terkena (tersangkut) penyakit berat.',
        'ch': [
            ('病', 'びょう', 'ビョウ', 'Sakit. 疒 (ranjang tempat orang sakit baring) + 丙 (api meradang deman suhu naik pinggang).'),
            ('気', 'き', 'キ', 'Hawa batin chi pernapasan raga mental.'),
            ('罹', 'かか(る)', 'リ', 'Terkena / Jaring. 罒 (jaring perangkap sangkar elang di atas) + 惟 (burung merana). Burung tersangkut duka jaring di udara.')
        ],
        'co': 'Banyak yang nulis Byouki ni Naru (menjadi sakit). TAPI Kalo Kakaru (Tersangkut), itu puitis ngeri parah! Jaring pukat harimau sangkar dewa wabah (罹) menerkam menyergap mencengkeram nasib kesehatan tubuh hawa apimu meradang (病気) sampai kau tumbang pasrah menggelepar nyangkut tepar <b>Terserang Kena Penyakit (Terjangkit)!</b>'
    },
    {
        'w': '頭痛がする', 'y': 'ずつうがする', 'a': 'Pusing / Sakit Kepala', 'g': 3, 'subdeck': 'KK::Ungkapan_Khusus',
        'ej': '今日はずっと頭痛がします。', 'ei': 'Hari ini pusing terus (timbul rasa sakit kepala).',
        'ch': [
            ('頭', 'あたま / ず', 'トウ / ズ', 'Kepala kacang nangkring biji tumpuan.'),
            ('痛', 'いた(い) / つう', 'ツウ', 'Sakit meradang. 疒 (ranjang kasur medis sakit derita) + 甬 (lorong terowongan tembus tulang ditusuk gema panjang).')
        ],
        'co': 'Bisa bilang Atama ga itai. TAPI "Zutsuu ga suru" itu ibarat bom waktu! Hantu lorong gaib (甬) menusuk saraf-saraf batok tempurung kepalamu (頭) sehingga bantal kasur rawat inap (疒) melambaikan tangan padamu. "Suru" di sini bermakna = Timbul gejalanya. <b>Nyut-nyutan Pusing Tujuh Keliling (Headache)!</b>'
    },
    {
        'w': '挫く', 'y': 'くじく', 'a': 'Keseleo / Terkilir (Sendi Patah Arang)', 'g': 1, 'subdeck': 'KK::Ungkapan_Khusus',
        'ej': '足首を挫きました。', 'ei': 'Pergelangan kaki keseleo/terkilir.',
        'ch': [('挫', 'くじ(く)', 'ザ', 'Patah semangat/Keseleo tekuk. 扌 (tangan meraba perih sendi) + 坐 (dua orang duduk diam bersimpuh bersila di atas tanah 土 terpuruk tak berdaya bangkit lumpuh).')],
        'co': 'Lagi semangat lari nabrak aspal bolong, engsel sendi melintir bunyi KRAAAK patah urat menyimpang! Langkah lumpuh terpuruk duduk ngesot di tanah sedih nelangsa (坐). Engsel tulangnya muter keluar lintasan rel tulang rawan. <b>Keseleo parah bikin nangis jejeritan terkilir bengkak (Sprain)!</b>'
    }
]
