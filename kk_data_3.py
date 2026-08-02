# -*- coding: utf-8 -*-
CARDS = [
    {
        'w': '持つ', 'y': 'もつ', 'a': 'Membawa / Memegang', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'カバンを持ちます。', 'ei': 'Membawa tas.',
        'ch': [('持', 'も.つ', 'ジ', '[Radikal: 扌 (Tangan)] + [Komponen: 寺 (Kuil/Pejabat)]')],
        'co': 'Tangan (扌) yang sedang bersiap memegang dupa atau persembahan saat pergi ke Kuil (寺). Ini adalah asal mula makna <b>Membawa / Memegang sesuatu</b> secara fisik.'
    },
    {
        'w': '待つ', 'y': 'まつ', 'a': 'Menunggu', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '友達を待っています。', 'ei': 'Sedang menunggu teman.',
        'ch': [('待', 'ま.つ', 'タイ', '[Radikal: 彳 (Jalan/Langkah)] + [Komponen: 寺 (Kuil/Tempat)]')],
        'co': 'Zaman dulu, kuil (寺) sering dijadikan sebagai titik kumpul orang-orang. Kamu melangkah (彳) ke sana lalu berhenti berjalan untuk <b>Menunggu (Matsu)</b> kedatangan rombongan.'
    },
    {
        'w': '呼ぶ', 'y': 'よぶ', 'a': 'Memanggil', 'g': 1, 'subdeck': 'KK::Interaksi Sosial',
        'ej': 'タクシーを呼びます。', 'ei': 'Memanggil taksi.',
        'ch': [('呼', 'よ.ぶ', 'コ', '[Radikal: 口 (Mulut)] + [Komponen: 乎 (Seruan nafas/Teriakan)]')],
        'co': 'Menggunakan mulut (口) untuk membuang napas panjang (乎) membentuk suara teriakan nyaring ke arah kejauhan. <b>Memanggil (Yobu)</b> orang atau taksi dari jarak jauh.'
    },
    {
        'w': '飛ぶ', 'y': 'とぶ', 'a': 'Terbang / Melompat', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '鳥が空を飛んでいます。', 'ei': 'Burung sedang terbang di langit.',
        'ch': [('飛', 'と.ぶ', 'ヒ', '[Radikal: 飛 (Terbang)]')],
        'co': 'Kanji ini benar-benar terlihat seperti burung yang sayap kanan dan kirinya (升 升) sedang mengepak dengan leher terangkat ke atas. <b>Burung Terbang</b>.'
    },
    {
        'w': '降る', 'y': 'ふる', 'a': 'Turun (Hujan/Salju)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '雨が降っています。', 'ei': 'Hujan sedang turun.',
        'ch': [('降', 'ふ.る / お.りる', 'コウ', '[Radikal: 阝 (Bukit/Langit)] + [Komponen: 夅 (Jejak kaki menurun)]')],
        'co': 'Ada objek (air hujan/salju) yang menuruni (夅) tebing tinggi atau langit (阝) menuju ke bumi. Secara natural digunakan untuk <b>Hujan turun (Ame ga furu)</b>.'
    },
    {
        'w': '降りる', 'y': 'おりる', 'a': 'Turun (Dari kendaraan)', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '電車を降ります。', 'ei': 'Turun dari kereta.',
        'ch': [('降', 'お.りる / ふ.る', 'コウ', '[Radikal: 阝 (Bukit/Tebing)] + [Komponen: 夅 (Jejak kaki turun)]')],
        'co': 'Sama persis dengan Kanji turun hujan (Furu), tapi jika subjeknya manusia (Oriru), ini berarti kamu meletakkan kakimu keluar dari kendaraan / menuruni tangga. <b>Turun kendaraan</b>.'
    },
    {
        'w': '登る', 'y': 'のぼる', 'a': 'Mendaki', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '山に登ります。', 'ei': 'Mendaki gunung.',
        'ch': [('登', 'のぼ.る', 'トウ / ト', '[Radikal: 癶 (Dua kaki melangkah)] + [Komponen: 豆 (Altar pengorbanan)]')],
        'co': 'Dua telapak kaki (癶) menapaki anak tangga satu per satu menuju altar pemujaan atau puncak gunung (豆). Membutuhkan *effort* lebih dari sekadar jalan biasa. <b>Mendaki gunung (Noboru)</b>.'
    },
    {
        'w': '入る', 'y': 'はいる', 'a': 'Masuk (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '部屋に入ります。', 'ei': 'Masuk ke kamar.',
        'ch': [('入', 'はい.る / い.れる', 'ニュウ', '[Radikal: 入 (Masuk)]')],
        'co': 'Berbeda dengan 人 (orang), kanji MasuK (入) garis panjangnya ada di Kanan. Melambangkan panah yang menembus masuk membelah permukaan. <b>Kamu melangkah masuk</b>.'
    },
    {
        'w': '入れる', 'y': 'いれる', 'a': 'Memasukkan (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'カバンに本を入れます。', 'ei': 'Memasukkan buku ke dalam tas.',
        'ch': [('入', 'い.れる / はい.る', 'ニュウ', '[Radikal: 入 (Masuk)]')],
        'co': 'Versi transitif dari Hairu (Masuk). Kamu mengambil suatu objek dan memaksa objek tersebut melewati celah untuk <b>dimasukkan</b> ke dalam tas/kotak.'
    },
    {
        'w': '出る', 'y': 'でる', 'a': 'Keluar / Muncul', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '家を出ます。', 'ei': 'Keluar dari rumah.',
        'ch': [('出', 'で.る / だ.す', 'シュツ', '[Radikal: 凵 (Wadah/Lubang)] + [Komponen: 屮 (Tunas tanaman)]')],
        'co': 'Lihat bagian tengahnya ada tanaman vertikal (屮) yang tumbuh menembus wadah pot (凵) menuju cahaya luar. <b>Kamu keluar dari ruangan / munculnya matahari</b>.'
    },
    {
        'w': '出す', 'y': 'だす', 'a': 'Mengeluarkan / Menyerahkan', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '財布からお金を出します。', 'ei': 'Mengeluarkan uang dari dompet.',
        'ch': [('出', 'だ.す / で.る', 'シュツ', '[Radikal: 出 (Keluar)]')],
        'co': 'Transitif dari Deru. Kamu menjangkau ke dalam dompet/laci, mencabut paksa barang tersebut ke luar. Bisa juga dipakai untuk <b>Menyerahkan PR (Shukudai o dasu)</b>.'
    },
    {
        'w': '歩く', 'y': 'あるく', 'a': 'Berjalan kaki', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '公園を歩きます。', 'ei': 'Berjalan-jalan di taman.',
        'ch': [('歩', 'ある.く', 'ホ / ブ', '[Radikal: 止 (Kaki berhenti)] + [Komponen: 少ない -> 步 (Kaki kiri dan kanan melangkah bergantian)]')],
        'co': 'Zaman dulu digambar dari 2 jejak kaki (kanan dan kiri) yang diayunkan selangkah demi selangkah (止). Mengayunkan langkah dengan kecepatan normal manusia: <b>Berjalan kaki (Aruku)</b>.'
    },
    {
        'w': '走る', 'y': 'はしる', 'a': 'Berlari', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '駅まで走ります。', 'ei': 'Berlari sampai stasiun.',
        'ch': [('走', 'はし.る', 'ソウ', '[Radikal: 走 (Lari)]')],
        'co': 'Sosok tanah (土) di atas dan kaki (疋) di bawah. Sosok orang mengayunkan kaki berototnya di atas lintasan tanah dengan tempo sangat tinggi. <b>Berlari (Hashiru)</b>.'
    },
    {
        'w': '脱ぐ', 'y': 'ぬぐ', 'a': 'Melepas (Pakaian / Sepatu)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '靴を脱いでください。', 'ei': 'Tolong lepaskan sepatu.',
        'ch': [('脱', 'ぬ.ぐ', 'ダツ', '[Radikal: 月 (Daging/Tubuh)] + [Komponen: 兌 (Membuka / Melepaskan)]')],
        'co': 'Melepaskan sesuatu yang mengikat tubuh/daging (月) menjadi terbebas dan lega layaknya senyum (兌). Digunakan saat kamu masuk rumah Jepang dan harus <b>Mencopot/Melepas sepatu/jaket</b>.'
    },
    {
        'w': '着る', 'y': 'きる', 'a': 'Memakai (Baju atas)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '新しいシャツを着ます。', 'ei': 'Memakai kemeja baru.',
        'ch': [('着', 'き.る / つ.く', 'チャク', '[Radikal: 羊 (Bulu domba/Pakaian)] + [Komponen: 目 (Mata / Terlihat)]')],
        'co': 'Kamu membungkus tubuhmu dengan mantel bulu domba tebal (羊). <b>Memakai pakaian (hanya untuk bagian Torso / Atas)</b>. Awas! Konjugasinya Kiru ini adalah Gol 2 (Kite, Kinai) beda sama Kiru (potong).'
    },
    {
        'w': '履く', 'y': 'はく', 'a': 'Memakai (Sepatu / Baju bawah)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '靴を履きます。', 'ei': 'Memakai sepatu.',
        'ch': [('履', 'は.く', 'リ', '[Radikal: 尸 (Tubuh jongkok)] + [Komponen: 復 (Berulang/Jalan)]')],
        'co': 'Kalau 着る buat jaket/baju atas, kalau 履く buat <b>Memakai apa pun yang dimasukkan lewat bawah paha</b> (celana panjang, kaos kaki, sepatu, sandal).'
    },
    {
        'w': '被る', 'y': 'かぶる', 'a': 'Memakai (Topi)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '帽子を被ります。', 'ei': 'Memakai topi.',
        'ch': [('被', 'かぶ.る', 'ヒ', '[Radikal: 衤 (Pakaian)] + [Komponen: 皮 (Kulit luar / Menutupi)]')],
        'co': 'Hanya digunakan saat meletakkan sesuatu ke atas kepala (seperti topi menutupi kulit kepala/皮). <b>Memakai Topi / Kupluk / Helm</b>.'
    },
    {
        'w': '閉じる', 'y': 'とじる', 'a': 'Menutup (Buku / Mata)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '本を閉じてください。', 'ei': 'Tolong tutup bukunya.',
        'ch': [('閉', 'と.じる / し.める', 'ヘイ', '[Radikal: 門 (Gerbang)]')],
        'co': 'Berbeda dengan 閉める (Shimeru) yang mengunci pintu secara fisik, 閉じる (Tojiru) digunakan untuk <b>Menutup lembaran benda pipih</b> (buku, majalah, kelopak mata, laptop).'
    },
    {
        'w': '歌う', 'y': 'うたう', 'a': 'Menyanyi', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'カラオケで歌います。', 'ei': 'Menyanyi di karaoke.',
        'ch': [('歌', 'うた.う', 'カ', '[Radikal: 欠 (Buka mulut)] + [Komponen: 哥 (Nyanyian/Irama bersahutan)]')],
        'co': 'Membuka mulut lebar-lebar (欠) untuk memancarkan pita suara nada yang bersahut-sahutan naik turun (哥). Sangat deskriptif: <b>Menyanyi dengan suara keras</b>.'
    },
    {
        'w': '踊る', 'y': 'おどる', 'a': 'Menari', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '音楽に合わせて踊ります。', 'ei': 'Menari mengikuti irama musik.',
        'ch': [('踊', 'おど.る', 'ヨウ', '[Radikal: 足 (Kaki)] + [Komponen: 甬 (Tabung berongga / Melonjak)]')],
        'co': 'Kakimu (足) diangkat, melompat, melenting, dan mengayun ke berbagai arah. Tubuhmu merespon alunan lagu. <b>Menari / Dance (Odoru)</b>.'
    },
    {
        'w': '泣く', 'y': 'なく', 'a': 'Menangis', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '映画を見て泣きました。', 'ei': 'Menonton film lalu menangis.',
        'ch': [('泣', 'な.く', 'キュウ', '[Radikal: 氵 (Air)] + [Komponen: 立 (Berdiri tegak)]')],
        'co': 'Bayangkan aliran sungai <b>air</b> mata (氵) yang mengucur sangat deras secara vertikal (tegak / 立) dari pelupuk matamu ke dagu. Ekspresi kesedihan yang tumpah: <b>Menangis</b>.'
    },
    {
        'w': '笑う', 'y': 'わらう', 'a': 'Tertawa / Tersenyum', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '面白い話を聞いて笑います。', 'ei': 'Mendengar cerita lucu lalu tertawa.',
        'ch': [('笑', 'わら.う', 'ショウ', '[Radikal: 竹 (Bambu)] + [Komponen: 夭 (Orang menari / meliuk)]')],
        'co': 'Mata yang menyipit melengkung ke bawah seperti lengkungan ruas bambu (竹), dan tubuh yang berguncang senang menahan tawa (夭). <b>Tertawa atau Tersenyum tulus</b>.'
    },
    {
        'w': '怒る', 'y': 'おこる', 'a': 'Marah', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '父が怒っています。', 'ei': 'Ayah sedang marah.',
        'ch': [('怒', 'おこ.る', 'ド', '[Radikal: 心 (Hati)] + [Komponen: 奴 (Budak/Status rendah)]')],
        'co': 'Perasaan mendidih di dalam Hati (心) melihat seseorang bertindak layaknya bawahan bodoh (奴). Emosi yang tidak terkendali: <b>Marah besar / Ngomel</b>.'
    },
    {
        'w': '困る', 'y': 'こまる', 'a': 'Kesulitan / Bingung (Mati langkah)', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': 'お金がなくて困っています。', 'ei': 'Saya kesulitan/bingung karena tidak punya uang.',
        'ch': [('困', 'こま.る', 'コン', '[Radikal: 囗 (Pagar kurungan)] + [Komponen: 木 (Pohon)]')],
        'co': 'Pohon (木) yang terus meninggi tapi dipenjara dalam kotak (囗). Ia tertahan, terbentur sana-sini, tidak bisa berkembang bebas. <b>Pusing / Terhimpit masalah / Bingung ga nemu jalan keluar</b>.'
    },
    {
        'w': '急ぐ', 'y': 'いそぐ', 'a': 'Bergegas / Buru-buru', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '時間がないので、急ぎます。', 'ei': 'Karena tidak ada waktu, saya bergegas.',
        'ch': [('急', 'いそ.ぐ', 'キュウ', '[Radikal: 心 (Hati/Perasaan)] + [Komponen: 刍 (Pisau membabat rumput liar)]')],
        'co': 'Hati/Jantungmu (心) berdebar kencang, memaksa tubuh bergerak membabat halangan seperti memotong rumput dengan pisau (刍). Diburu waktu: <b>Bergegas cepat / Terburu-buru</b>.'
    }
]
