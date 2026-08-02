# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '上げる', 'y': 'あげる', 'a': 'Memberikan / Menaikkan', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '友達にプレゼントを上げました。', 'ei': 'Memberikan kado kepada teman.',
        'ch': [('上', 'あ.げる / うえ', 'ジョウ', '[Radikal: 一 (Garis dasar)] + [Komponen: 卜 (Tongkat tegak ke atas)]')],
        'co': 'Ada sebuah garis dasar (tanah), dan ada garis vertikal yang menonjol ke <b>Atas</b> melampaui garis tersebut. Saat kau <b>Memberi</b> barang ke orang lain, tanganmu <b>Terangkat</b> (Menaikkan barang). Ini untuk "Aku memberi ke dia" / "Dia memberi ke dia".'
    },
    {
        'w': '呉れる', 'y': 'くれる', 'a': 'Memberikan (Kepadaku)', 'g': 2, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '母が時計をくれました。', 'ei': 'Ibu memberikanku jam tangan.',
        'ch': [('呉', 'く.れる', 'ゴ', '[Radikal: 口 (Mulut)] + [Komponen: 夨 (Kepala miring memohon)]')],
        'co': 'Kanji ini jarang ditulis di N5/N4, cukup くれる. Tapi <b>Kureru</b> wajib dihafal! Arah transaksinya: <b>Orang Luar -> Ke Arahku (Lingkaranku)</b>. (Sensei memberikan buku KE SAYA).'
    },
    {
        'w': '貰う', 'y': 'もらう', 'a': 'Menerima', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '父から車を貰いました。', 'ei': 'Menerima mobil dari ayah.',
        'ch': [('貰', 'もら.う', 'セイ', '[Radikal: 貝 (Uang)] + [Komponen: 世 (Generasi/Waktu yang lama)]')],
        'co': 'Subjek kalimat ini adalah PIHAK PENERIMA. Harta atau barang berharga (貝) diwariskan antar-generasi (世). Kamu yang berada di ujung siklus ini <b>Menerima (Morau)</b> hasil pemberian dari pihak pemberi.'
    },
    {
        'w': '送る', 'y': 'おくる', 'a': 'Mengirim (Benda / Orang)', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '荷物を送りました。', 'ei': 'Telah mengirim barang paketan.',
        'ch': [('送', 'おく.る', 'ソウ', '[Radikal: 辶 (Jalan)] + [Komponen: 关 (Obor/Api di atas kayu)]')],
        'co': 'Menyusuri jalan (辶) di malam hari berbekal nyala obor terang (关) untuk memastikan barang/orang sampai di tujuan dengan selamat. <b>Mengirim paket (Kirim) / Mengantar orang pulang</b>.'
    },
    {
        'w': '払う', 'y': 'はらう', 'a': 'Membayar / Menyapu', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'レジでお金を払います。', 'ei': 'Membayar uang di kasir.',
        'ch': [('払', 'はら.う', 'フツ', '[Radikal: 扌 (Tangan)] + [Komponen: ム (Pribadi/Bentuk melengkung siku)]')],
        'co': 'Tangan (扌) yang menekuk lalu mengusap sesuatu sampai lenyap. Dulu artinya "menyapu/menyingkirkan debu", namun berevolusi menjadi menyingkirkan tagihan hutang. <b>Membayar Tagihan (Bayar)</b>.'
    },
    {
        'w': '頼む', 'y': 'たのむ', 'a': 'Meminta tolong / Memesan', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': 'レストランでピザを頼みます。', 'ei': 'Memesan pizza di restoran.',
        'ch': [('頼', 'たの.む', 'ライ', '[Radikal: 頁 (Kepala)] + [Komponen: 束 (Buntelan/Kerang bertumpuk)]')],
        'co': 'Kamu menundukkan kepala (頁) dan bersandar/bergantung pada sumber daya yang besar (束) milik orang lain. <b>Mengandalkan / Meminta tolong</b>, atau di konteks kafe berarti <b>Memesan pesanan (Order)</b>.'
    },
    {
        'w': '勤める', 'y': 'つとめる', 'a': 'Bekerja (Sebagai karyawan)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '銀行に勤めています。', 'ei': 'Bekerja di bank (sebagai karyawan).',
        'ch': [('勤', 'つと.める', 'キン', '[Radikal: 力 (Tenaga)] + [Komponen: 堇 (Kuning tua/Keringat/Kerja keras)]')],
        'co': 'Bedanya dengan Hataraku (bekerja umum)? <b>Tsutomeru</b> lebih fokus pada loyalitas <b>Menjabat/Bertugas (Pekerja Kantoran / Staf instansi)</b>. Kamu harus mendedikasikan tenaga (力) penuh untuk bos. (Pakai partikel <b>NI</b>).'
    },
    {
        'w': '間に合う', 'y': 'まにあう', 'a': 'Tepat Waktu / Keburu', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '電車に間に合いました。', 'ei': 'Tepat waktu keburu naik kereta.',
        'ch': [
            ('間', 'ま / あいだ', 'カン', '[Radikal: 門 (Gerbang)] + [Komponen: 日 (Matahari)]'),
            ('合', 'あ.う', 'ゴウ', '[Radikal: 口 (Mulut)] + [Komponen: 亼 (Mengumpulkan)]')
        ],
        'co': 'Ruang waktu luang (間) yang kamu miliki <b>Pas/Cocok</b> (合) dengan jadwal kedatangan bus atau batas *deadline*. Artinya: <b>Waktunya Keburu / Tepat waktu nyampe</b>. (Partikel Ni).'
    },
    {
        'w': '遅れる', 'y': 'おくれる', 'a': 'Terlambat / Telat', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '授業に遅れました。', 'ei': 'Terlambat masuk kelas.',
        'ch': [('遅', 'おく.れる / おそ.い', 'チ', '[Radikal: 辶 (Jalan)] + [Komponen: 犀 (Badak)]')],
        'co': 'Bayangkan ada seekor badak (犀) besar yang berjalan (辶) sangat pelan menembus jalanan macet. Makanya kamu jadi <b>Telat / Terlambat</b> dari jadwal. (Partikel Ni).'
    },
    {
        'w': '勝つ', 'y': 'かつ', 'a': 'Menang', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '試合に勝ちました。', 'ei': 'Menang dalam pertandingan.',
        'ch': [('勝', 'か.つ / まさ.る', 'ショウ', '[Radikal: 力 (Kekuatan)] + [Komponen: 朕 (Tubuh raja menyembul) -> 月+龹]')],
        'co': 'Menggunakan tenaga lengan yang berotot besar (力) untuk mengangkat perahu kargo yang berat. Kekuatan di atas rata-rata yang menggilas lawan. <b>Menang</b>.'
    },
    {
        'w': '負ける', 'y': 'まける', 'a': 'Kalah', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'ゲームに負けました。', 'ei': 'Kalah dalam game.',
        'ch': [('負', 'ま.ける / お.う', 'フ', '[Radikal: 貝 (Harta)] + [Komponen: 刀 (Pisau) / ⺈]')],
        'co': 'Seorang prajurit takluk dan terpaksa memanggul beban kerang harta (貝) sebagai pampasan perang, lalu punggungnya dihantam senjata (⺈). <b>Tunduk / Kalah telak</b>.'
    },
    {
        'w': '咲く', 'y': 'さく', 'a': 'Mekar (Bunga)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '桜の花が咲きました。', 'ei': 'Bunga sakura telah mekar.',
        'ch': [('咲', 'さ.く', 'ショウ', '[Radikal: 口 (Mulut/Tunas)] + [Komponen: 关 (Ujung atas mekar/tersenyum)]')],
        'co': 'Dulu kanji ini sering diartikan "tertawa" pada bambu. Tapi sekarang dipakai eksklusif untuk kuncup tanaman yang "tersenyum/terbuka" (关) ibarat bentuk <b>Bunga yang Sedang Mekar (Saku)</b>.'
    },
    {
        'w': '吹く', 'y': 'ふく', 'a': 'Bertiup (Angin) / Meniup', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '風が強く吹いています。', 'ei': 'Angin bertiup kencang.',
        'ch': [('吹', 'ふ.く', 'スイ', '[Radikal: 口 (Mulut)] + [Komponen: 欠 (Menguap / Nafas besar)]')],
        'co': 'Kamu membuka mulut (口) lebar-lebar layaknya orang kurang tidur (欠), tapi alih-alih menguap, kamu <b>Meniup</b> lilin atau seruling. Dipakai juga untuk <b>Angin Bertiup (Kaze ga fuku)</b>.'
    },
    {
        'w': '晴れる', 'y': 'はれる', 'a': 'Cerah (Cuaca) / Menjadi Terang', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '明日は晴れるでしょう。', 'ei': 'Besok sepertinya cuaca akan cerah.',
        'ch': [('晴', 'は.れる', 'セイ', '[Radikal: 日 (Matahari)] + [Komponen: 青 (Biru murni / Bersih)]')],
        'co': 'Awan tebal kelabu telah minggir, kini Matahari (日) bersinar memancarkan warna langit yang Biru (青) bersih nan jernih. Cuaca <b>Cerah ceria (Hareru)</b>, bebas beban pikiran.'
    },
    {
        'w': '曇る', 'y': 'くもる', 'a': 'Mendung / Berawan', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '空が曇っています。', 'ei': 'Langit sedang mendung.',
        'ch': [('曇', 'くも.る', 'ドン', '[Radikal: 日 (Matahari)] + [Komponen: 雲 (Awan)]')],
        'co': 'Matahari (日) bersembunyi terhalang oleh gumpalan Awan (雲) hitam tebal yang sedang membawa uap air. Suasana jadi redup gelap. Cuaca <b>Mendung / Berawan</b>.'
    },
    {
        'w': '治る', 'y': 'なおる', 'a': 'Sembuh (Penyakit)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '風邪が治りました。', 'ei': 'Masuk anginnya sudah sembuh.',
        'ch': [('治', 'なお.る / おさ.める', 'ジ / チ', '[Radikal: 氵 (Air)] + [Komponen: 台 (Panggung/Dasar)]')],
        'co': 'Menyembuhkan badan ibarat meregulasi debit <b>air (氵)</b> bah agar sungai kembali damai di atas bantalannya (台). Ini spesifik untuk <b>Sembuh dari penyakit (Intransitif)</b>. (Beda dgn なおす/Memperbaiki benda).'
    },
    {
        'w': '直す', 'y': 'なおす', 'a': 'Memperbaiki (Benda/Kesalahan)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '壊れた時計を直します。', 'ei': 'Memperbaiki jam yang rusak.',
        'ch': [('直', 'なお.す / なお.る', 'チョク', '[Radikal: 目 (Mata)] + [Komponen: 乚 (Lurus) / 十 (Lurus sempurna)]')],
        'co': 'Membuat sesuatu yang bengkok/rusak jadi <b>Lurus (直) dan Berfungsi Benar</b> kembali. (Transitif -> Subjek yang turun tangan <b>Memperbaiki / Reparasi</b>). Bacanya sama (Naosu) dgn 治す(Menyembuhkan).'
    },
    {
        'w': '続く', 'y': 'つづく', 'a': 'Berlanjut (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '雨がまだ続いています。', 'ei': 'Hujan masih berlanjut (belum reda).',
        'ch': [('続', 'つづ.く', 'ゾク', '[Radikal: 糸 (Benang)] + [Komponen: 売 (Menjual / Melangkah lurus)]')],
        'co': 'Bayangkan sebuah untaian benang merah (糸) yang terus diikat dan ditarik tiada akhir oleh pedagang (売). Menyiratkan suatu kegiatan/fenomena <b>masih terus Berlanjut secara otomatis</b>.'
    },
    {
        'w': '続ける', 'y': 'つづける', 'a': 'Melanjutkan (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '勉強を続けます。', 'ei': 'Melanjutkan belajar.',
        'ch': [('続', 'つづ.ける', 'ゾク', '[Radikal: 続 (Lanjut)]')],
        'co': 'Versi <b>Transitif</b> dari Tsuzuku. Kamu lah subjek yang *memaksakan diri* atau <b>secara sadar Melanjutkan</b> suatu perbuatan (misal: "aku akan melanjutkan main game ini", bukan gamenya yang berlanjut sendiri).'
    },
    {
        'w': '集まる', 'y': 'あつまる', 'a': 'Berkumpul (Intransitif)', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': '広場に人が集まります。', 'ei': 'Orang-orang berkumpul di alun-alun.',
        'ch': [('集', 'あつ.まる', 'シュウ', '[Radikal: 隹 (Burung berekor pendek)] + [Komponen: 木 (Pohon)]')],
        'co': 'Ketika senja tiba, ribuan burung murai (隹) beterbangan mendarat dan <b>Berkumpul memadat</b> bertumpuk di dahan-dahan sebatang pohon (木) untuk tidur. <b>Orang/Barang saling Berkumpul (Intransitif)</b>.'
    },
    {
        'w': '集める', 'y': 'あつめる', 'a': 'Mengumpulkan (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '趣味で切手を集めています。', 'ei': 'Mengumpulkan prangko sebagai hobi.',
        'ch': [('集', 'あつ.める', 'シュウ', '[Radikal: 集 (Kumpul)]')],
        'co': 'Kalau Atsumaru itu barangnya yang datang ngumpul sendiri, <b>Atsumeru</b> itu Elu-nya (subjek) yang turun tangan memungut / <b>Mengumpulkan (koleksi)</b> kepingan puzzle dari berbagai penjuru.'
    },
    {
        'w': '決まる', 'y': 'きまる', 'a': 'Ditentukan / Diputuskan (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '試合の日が来月に決まりました。', 'ei': 'Hari pertandingan telah diputuskan bulan depan.',
        'ch': [('決', 'き.まる / き.める', 'ケツ', '[Radikal: 氵 (Air)] + [Komponen: 夬 (Tangan mematahkan/Membelah)]')],
        'co': 'Membobol tanggul agar aliran air (氵) memancar dengan arah yang mutlak tak bisa diubah lagi (夬). Suatu rencana atau tanggal ujian yang <b>sudah Diputuskan / Ditetapkan oleh pihak lain secara *fix*</b>.'
    },
    {
        'w': '決める', 'y': 'きめる', 'a': 'Menentukan / Memutuskan (Transitif)', 'g': 2, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': 'メニューを決めましょう。', 'ei': 'Mari kita tentukan menunya.',
        'ch': [('決', 'き.める', 'ケツ', '[Radikal: 決 (Putus)]')],
        'co': 'Versi transitif dari Kimaru. Kaulah bosnya! Kau memotong keraguan, menganalisis opsi, dan <b>secara sadar Menentukan / Memutuskan</i> jalan keluarnya. "Aku yang pilih!"'
    },
    {
        'w': '落ちる', 'y': 'おちる', 'a': 'Jatuh (Gugur / Turun kasta)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '木からりんごが落ちました。', 'ei': 'Apel jatuh dari pohon.',
        'ch': [('落', 'お.ちる', 'ラク', '[Radikal: 艹 (Rumput/Tanaman)] + [Komponen: 洛 (Hujan mendadak di kota)]')],
        'co': 'Musim gugur, daun-daun (艹) berlepasan dan <b>Gugur berjatuhan</b> menimpa air (氵) dengan deras (各). Segala benda langit / status yang <b>Jatuh merosot (Intransitif)</b>. Hati-hati, Golongan 2!'
    },
    {
        'w': '落とす', 'y': 'おとす', 'a': 'Menjatuhkan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'スマホを落として壊してしまった。', 'ei': 'Menjatuhkan smartphone lalu hancur.',
        'ch': [('落', 'お.とす', 'ラク', '[Radikal: 落 (Jatuh)]')],
        'co': 'Bentuk Transitif. Tanganmu licin atau ceroboh, sehingga secara aktif <b>Menjatuhkan</b> barang penting (dompet/hp) ke lantai. Awas, yang ini beda golongan dengan Ochiru, Otosu ini adalah <b>Golongan 1</b>.'
    }
]
