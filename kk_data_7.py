# -*- coding: utf-8 -*-
# Batch 7: Restored missing entries with premium quality
CARDS = [
    {
        'w': '溜まる', 'y': 'たまる', 'a': 'Menumpuk / Tertimbun (Intransitif)', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'ストレスが溜まっています。', 'ei': 'Stres sedang menumpuk.',
        'ch': [('溜', 'た.まる', 'リュウ', '[Radikal: 氵 (Air)] + [Komponen: 留 (Tertahan)]')],
        'co': 'Air (氵) yang mengalir tapi tertahan (留) di suatu wadah sehingga volumenya terus bertambah. <b>Menumpuk / Tertimbun secara otomatis</b> (stres, pekerjaan, uang tabungan).'
    },
    {
        'w': '通る', 'y': 'とおる', 'a': 'Melewati / Melintas', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'この道を通ります。', 'ei': 'Melewati jalan ini.',
        'ch': [('通', 'とお.る / かよ.う', 'ツウ', '[Radikal: 辶 (Jalan)] + [Komponen: 甬 (Tabung/Lorong)]')],
        'co': 'Berjalan (辶) menembus lorong/tabung pipa (甬) dari ujung satu ke ujung lainnya tanpa berhenti. <b>Melewati / Melintas (Intransitif)</b>.'
    },
    {
        'w': '通う', 'y': 'かよう', 'a': 'Bolak-balik / Commute', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': '電車で学校に通っています。', 'ei': 'Bolak-balik ke sekolah naik kereta.',
        'ch': [('通', 'かよ.う', 'ツウ', '[Radikal: 辶 (Jalan)] + [Komponen: 甬 (Lorong)]')],
        'co': 'Kanji yang sama dengan 通る, tapi bacaan Kayou menekankan REPETISI. Kamu melewati rute yang SAMA setiap hari (rumah ↔ kantor/sekolah). <b>Commute / Bolak-balik rutin</b>.'
    },
    {
        'w': '迷う', 'y': 'まよう', 'a': 'Tersesat / Bimbang', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': '道に迷いました。', 'ei': 'Tersesat di jalan.',
        'ch': [('迷', 'まよ.う', 'メイ', '[Radikal: 辶 (Jalan)] + [Komponen: 米 (Beras/Percabangan)]')],
        'co': 'Berjalan (辶) tapi jalannya bercabang ke segala arah seperti butiran beras menyebar (米). Nggak tau harus belok kanan atau kiri! <b>Tersesat / Bimbang memilih</b>.'
    },
    {
        'w': '戻す', 'y': 'もどす', 'a': 'Mengembalikan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '本を棚に戻してください。', 'ei': 'Tolong kembalikan buku ke rak.',
        'ch': [('戻', 'もど.す / もど.る', 'レイ', '[Radikal: 戸 (Pintu)] + [Komponen: 大 (Besar)]')],
        'co': 'Mendorong pintu besar (大) kembali ke posisi asalnya di kusen (戸). <b>Mengembalikan benda ke tempat semula (Transitif)</b>.'
    },
    {
        'w': '戻る', 'y': 'もどる', 'a': 'Kembali (Intransitif)', 'g': 1, 'subdeck': 'KK::Pergerakan',
        'ej': 'すぐ戻ります。', 'ei': 'Segera kembali.',
        'ch': [('戻', 'もど.る', 'レイ', '[Radikal: 戸 (Pintu)] + [Komponen: 大 (Besar)]')],
        'co': 'Versi intransitif dari 戻す. Kamu sendiri yang berjalan kembali melewati pintu (戸) menuju rumah/posisi awal. <b>Kembali / Pulang</b>.'
    },
    {
        'w': '壊す', 'y': 'こわす', 'a': 'Merusak / Menghancurkan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'おもちゃを壊しました。', 'ei': 'Merusak mainan.',
        'ch': [('壊', 'こわ.す', 'カイ', '[Radikal: 土 (Tanah)] + [Komponen: 懐 (Kantong/Menghancurkan)]')],
        'co': 'Menghantam struktur bangunan dari tanah (土) hingga runtuh menjadi puing. Subjek lah yang secara aktif <b>Merusak / Menghancurkan benda (Transitif)</b>.'
    },
    {
        'w': '壊れる', 'y': 'こわれる', 'a': 'Rusak / Hancur (Intransitif)', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'パソコンが壊れました。', 'ei': 'Komputer rusak.',
        'ch': [('壊', 'こわ.れる', 'カイ', '[Radikal: 壊 (Hancur)]')],
        'co': 'Versi intransitif. Benda itu <b>Rusak/Hancur sendiri</b> tanpa ada yang sengaja merusaknya. "Laptopku rusak!" (bukan "aku merusaknya").'
    },
    {
        'w': '空く', 'y': 'あく', 'a': 'Kosong / Luang', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'お腹が空きました。', 'ei': 'Perut kosong (lapar).',
        'ch': [('空', 'あ.く / そら', 'クウ', '[Radikal: 穴 (Lubang)] + [Komponen: 工 (Pekerjaan/Alat)]')],
        'co': 'Lubang (穴) yang digali dengan alat (工) semakin dalam sampai isinya habis. <b>Jadi kosong / Tersedia / Lapar (perut kosong)</b>.'
    },
    {
        'w': '行う', 'y': 'おこなう', 'a': 'Melaksanakan / Menyelenggarakan', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '会議を行います。', 'ei': 'Menyelenggarakan rapat.',
        'ch': [('行', 'おこな.う / い.く', 'コウ / ギョウ', '[Radikal: 行 (Pergi/Berjalan)]')],
        'co': 'Bacaan Okonau lebih formal daripada する. Digunakan untuk <b>Melaksanakan acara resmi / Menyelenggarakan</b> (rapat, upacara, festival).'
    },
    {
        'w': '選ぶ', 'y': 'えらぶ', 'a': 'Memilih', 'g': 1, 'subdeck': 'KK::Kognitif Pendidikan',
        'ej': '好きな色を選んでください。', 'ei': 'Tolong pilih warna yang disukai.',
        'ch': [('選', 'えら.ぶ', 'セン', '[Radikal: 辶 (Jalan)] + [Komponen: 巽 (Dua orang bersisian/Angin)]')],
        'co': 'Berdiri di persimpangan jalan (辶) dan harus menentukan satu dari banyak opsi. <b>Memilih / Menyeleksi</b>.'
    },
    {
        'w': '外す', 'y': 'はずす', 'a': 'Melepas / Menanggalkan', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'メガネを外します。', 'ei': 'Melepas kacamata.',
        'ch': [('外', 'はず.す / そと', 'ガイ', '[Radikal: 夕 (Malam)] + [Komponen: 卜 (Ramalan)]')],
        'co': 'Malam hari (夕) sang peramal (卜) salah prediksi — hasilnya meleset ke <b>luar</b> target. <b>Melepas aksesori (kacamata, jam) / Meleset dari sasaran</b>.'
    },
    {
        'w': '要る', 'y': 'いる', 'a': 'Butuh / Perlu', 'g': 1, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': 'パスポートが要ります。', 'ei': 'Butuh paspor.',
        'ch': [('要', 'い.る', 'ヨウ', '[Radikal: 覀 (Penutup kepala)] + [Komponen: 女 (Wanita)]')],
        'co': 'Awas jangan bingung sama いる (ada/benda hidup)! 要る ditulis pakai Kanji dan bermakna <b>Membutuhkan / Diperlukan</b>. Gol 1 (要ります, 要らない).'
    },
    {
        'w': '離す', 'y': 'はなす', 'a': 'Melepaskan / Menjauhkan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '手を離してください。', 'ei': 'Tolong lepaskan tangannya.',
        'ch': [('離', 'はな.す', 'リ', '[Radikal: 隹 (Burung)] + [Komponen: 离 (Binatang aneh/Terpisah)]')],
        'co': 'Seekor burung (隹) yang dicengkeram tangan akhirnya dibebaskan dan <b>terbang menjauh</b>. <b>Melepaskan pegangan / Menjauhkan dua benda (Transitif)</b>. Homonim dengan 話す (berbicara)!'
    },
    {
        'w': '思う', 'y': 'おもう', 'a': 'Berpikir / Merasa (Subyektif)', 'g': 1, 'subdeck': 'KK::Sensori Emosi',
        'ej': 'いい天気だと思います。', 'ei': 'Saya rasa cuacanya bagus.',
        'ch': [('思', 'おも.う', 'シ', '[Radikal: 心 (Hati)] + [Komponen: 田 (Sawah/Otak)]')],
        'co': 'Otak/kepala (田) dan hati (心) bekerja sama mengolah opini subyektif. Beda dengan 考える (analisis logis), 思う lebih pada <b>Merasa / Berpendapat subyektif</b>. "Gue rasa..."'
    },
    {
        'w': '倒す', 'y': 'たおす', 'a': 'Merobohkan / Mengalahkan', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': '敵を倒しました。', 'ei': 'Mengalahkan musuh.',
        'ch': [('倒', 'たお.す', 'トウ', '[Radikal: 亻 (Orang)] + [Komponen: 到 (Sampai/Tiba)]')],
        'co': 'Seseorang (亻) didorong sampai (到) tumbang rata dengan tanah. <b>Merobohkan / Mengalahkan musuh (Transitif)</b>. Juga dipakai dalam game: "Boss defeated!"'
    },
    {
        'w': '流す', 'y': 'ながす', 'a': 'Mengalirkan / Membuang (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '水を流します。', 'ei': 'Mengalirkan air (flush).',
        'ch': [('流', 'なが.す', 'リュウ', '[Radikal: 氵 (Air)] + [Komponen: 㐬 (Anak lahir/Mengalir deras)]')],
        'co': 'Kamu membuka keran sehingga air (氵) mengalir deras (㐬) menghanyutkan semua yang menghalangi. <b>Mengalirkan / Menyiram toilet (Flush)</b>.'
    },
    {
        'w': '打つ', 'y': 'うつ', 'a': 'Memukul / Mengetik', 'g': 1, 'subdeck': 'KK::Aktivitas Fisik',
        'ej': 'キーボードを打ちます。', 'ei': 'Mengetik di keyboard.',
        'ch': [('打', 'う.つ', 'ダ', '[Radikal: 扌 (Tangan)] + [Komponen: 丁 (Paku)]')],
        'co': 'Tangan (扌) menghantam paku (丁) dengan palu. <b>Memukul benda keras / Mengetik keyboard / Memukul bola (baseball)</b>.'
    },
    {
        'w': '逃げる', 'y': 'にげる', 'a': 'Melarikan diri / Kabur', 'g': 2, 'subdeck': 'KK::Pergerakan',
        'ej': '猫が逃げました。', 'ei': 'Kucing melarikan diri.',
        'ch': [('逃', 'に.げる', 'トウ', '[Radikal: 辶 (Jalan)] + [Komponen: 兆 (Retak/Pecah)]')],
        'co': 'Tanah mulai retak (兆) tanda gempa besar! Kamu berlari secepat mungkin (辶) menjauhi zona bahaya. <b>Kabur / Melarikan diri / Escape</b>.'
    },
    {
        'w': '足す', 'y': 'たす', 'a': 'Menambah', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '砂糖を足してください。', 'ei': 'Tolong tambahkan gula.',
        'ch': [('足', 'た.す / あし', 'ソク', '[Radikal: 足 (Kaki)]')],
        'co': 'Kaki (足) yang awalnya gontai lemas, setelah ditambah nutrisi jadi penuh bertenaga. <b>Menambah / Plus (+)</b>. Lawannya 引く (mengurangi).'
    },
    {
        'w': '分ける', 'y': 'わける', 'a': 'Membagi / Memisahkan (Transitif)', 'g': 2, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ケーキを二つに分けます。', 'ei': 'Membagi kue menjadi dua.',
        'ch': [('分', 'わ.ける', 'ブン', '[Radikal: 刀 (Pisau)] + [Komponen: 八 (Membelah)]')],
        'co': 'Versi transitif dari 分かる. Kamu mengambil pisau (刀) dan secara aktif membelah (八) benda utuh menjadi potongan-potongan. <b>Membagi / Memisahkan</b>.'
    },
    {
        'w': '生きる', 'y': 'いきる', 'a': 'Hidup / Bernyawa', 'g': 2, 'subdeck': 'KK::Perubahan Kondisi',
        'ej': '一人で生きていけます。', 'ei': 'Bisa hidup sendiri.',
        'ch': [('生', 'い.きる / う.まれる', 'セイ', '[Radikal: 生 (Kehidupan)]')],
        'co': 'Piktogram tunas kecil yang menerobos keluar dari permukaan tanah menuju cahaya matahari. Simbol universal: <b>Hidup / Eksis / Bernyawa</b>.'
    },
    {
        'w': '消す', 'y': 'けす', 'a': 'Menghapus / Mematikan (Transitif)', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '電気を消してください。', 'ei': 'Tolong matikan lampu.',
        'ch': [('消', 'け.す', 'ショウ', '[Radikal: 氵 (Air)] + [Komponen: 肖 (Menyerupai/Menipis)]')],
        'co': 'Air (氵) yang disiramkan membuat sesuatu menipis (肖) sampai lenyap total. <b>Mematikan lampu/api / Menghapus tulisan / Menghilangkan jejak</b>.'
    },
    {
        'w': '押す', 'y': 'おす', 'a': 'Menekan / Mendorong', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ボタンを押します。', 'ei': 'Menekan tombol.',
        'ch': [('押', 'お.す', 'オウ', '[Radikal: 扌 (Tangan)] + [Komponen: 甲 (Perisai/Cangkang)]')],
        'co': 'Tangan (扌) menekan/mendorong permukaan keras layaknya perisai (甲) dengan tekanan kuat. <b>Menekan tombol / Mendorong pintu / Cap stempel</b>.'
    },
    {
        'w': '引く', 'y': 'ひく', 'a': 'Menarik / Mengurangi', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': 'ドアを引いてください。', 'ei': 'Tolong tarik pintunya.',
        'ch': [('引', 'ひ.く', 'イン', '[Radikal: 弓 (Busur)] + [Komponen: | (Tali)]')],
        'co': 'Menarik tali (|) busur panah (弓) ke belakang. Lawannya 押す (dorong). <b>Menarik pintu / Mengurangi (Minus) / Menarik perhatian</b>.'
    },
    {
        'w': '開く', 'y': 'ひらく', 'a': 'Membuka (Lebar) / Mengadakan', 'g': 1, 'subdeck': 'KK::Pekerjaan Tugas',
        'ej': '花が開きました。', 'ei': 'Bunga mekar (terbuka).',
        'ch': [('開', 'ひら.く / あ.ける', 'カイ', '[Radikal: 門 (Gerbang)] + [Komponen: 幵 (Dua palang terbuka)]')],
        'co': 'Beda dengan 開ける (Akeru, Gol 2, spesifik buka pintu/tutup), 開く (Hiraku, Gol 1) lebih luas: <b>Membuka lebar / Mekar / Mengadakan pesta</b>.'
    }
]
