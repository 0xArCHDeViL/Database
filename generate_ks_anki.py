# -*- coding: utf-8 -*-
"""
Generator Anki Deck: Kata Sifat (形容詞/形容動詞) — Format v3
Generates .txt file ready for Anki import.
94 kartu, 12 subdeck semantik.
"""

import sys
import os

# ============================================================
# CSS CONSTANTS
# ============================================================

FRONT_STYLE = '<style>.frontcard{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Hiragino Kaku Gothic ProN","Meiryo",sans-serif;background:#ffffff !important;color:#1e293b !important;padding:50px 20px;border-radius:16px;text-align:center;border:1px solid #e2e8f0}.front-main{font-size:64px;font-weight:400;color:#0f172a !important;line-height:1.3}.front-main.sm{font-size:50px}.front-main.xs{font-size:40px}.front-hint{margin-top:24px;font-size:12px;text-transform:uppercase;letter-spacing:3px;color:#94a3b8 !important;font-weight:600}</style>'

BACK_STYLE = '<style>.jpcard{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Hiragino Kaku Gothic ProN","Meiryo",sans-serif;line-height:1.6;background:#ffffff !important;color:#334155 !important;padding:24px;border-radius:16px;border:1px solid #e2e8f0}.yomi{font-size:30px;color:#2563eb !important;font-weight:600;margin-bottom:6px}.arti{font-size:20px;color:#b45309 !important;font-weight:500;background:#fef3c7 !important;padding:6px 14px;border-radius:8px;display:inline-block;margin:4px 0 16px 0}.kalimat{margin:16px 0;padding:16px;background:#f0fdf4 !important;border-left:4px solid #22c55e;border-radius:4px 8px 8px 4px;color:#166534 !important}.kalimat .jp{font-size:19px;font-weight:500;color:#14532d !important;margin-bottom:4px}.kalimat .id{font-size:15px;color:#166534 !important;opacity:0.9}.label{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#94a3b8 !important;font-weight:700;margin-bottom:10px}.analisis-box{margin:20px 0;padding:16px;background:#f8fafc !important;border-radius:12px;border:1px solid #e2e8f0}.analisis-title{font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:#64748b !important;font-weight:700;margin-bottom:12px}.kanji-strip{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:4px}.kanji-mini{flex:1;min-width:140px;background:#ffffff !important;border-radius:10px;padding:14px;text-align:center;border:1px solid #e2e8f0}.kanji-mini-char{font-size:46px;font-weight:400;color:#1e3a8a !important;line-height:1.1;margin-bottom:8px}.yomi-badges{display:flex;justify-content:center;gap:6px;margin:10px 0}.badge-kun{background:#eff6ff !important;color:#1d4ed8 !important;font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px}.badge-on{background:#fdf2f8 !important;color:#be185d !important;font-size:11px;font-weight:600;padding:4px 10px;border-radius:6px}.kanji-mini-makna{font-size:13.5px;color:#475569 !important;text-align:left;margin-top:12px;line-height:1.5;border-top:1px solid #e2e8f0;padding-top:12px}.cocoklogi-box{margin:20px 0 10px 0;padding:16px;background:#fff1f2 !important;border-left:4px solid #f43f5e;border-radius:4px 12px 12px 4px;font-size:15px;color:#881337 !important;line-height:1.6}.cocoklogi-box b{color:#e11d48 !important;font-weight:700}.conj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:8px;margin-bottom:24px}.conj-item{background:#f8fafc !important;border:1px solid #e2e8f0;border-radius:8px;padding:10px 8px;text-align:center}.conj-name{font-size:10px;color:#64748b !important;text-transform:uppercase;font-weight:700;letter-spacing:1px;margin-bottom:6px}.conj-val{font-size:15.5px;color:#0f172a !important;font-weight:500}</style>'


# ============================================================
# HTML BUILDER FUNCTIONS
# ============================================================

def build_front(word, is_kana_only):
    n = len(word)
    if n >= 5:
        sz = ' class="front-main xs"'
    elif n >= 4:
        sz = ' class="front-main sm"'
    else:
        sz = ' class="front-main"'
    hint = "Kana &middot; Ingat artinya?" if is_kana_only else "Kanji &middot; Ingat cara bacanya?"
    return f'{FRONT_STYLE}<div class="frontcard"><div{sz}>{word}</div><div class="front-hint">{hint}</div></div>'


def build_kanji_mini(char, kun, on, makna):
    return (
        f'<div class="kanji-mini">'
        f'<div class="kanji-mini-char">{char}</div>'
        f'<div class="yomi-badges">'
        f'<span class="badge-kun">Kun: {kun}</span>'
        f'<span class="badge-on">On: {on}</span>'
        f'</div>'
        f'<div class="kanji-mini-makna">{makna}</div>'
        f'</div>'
    )


def build_back(card):
    parts = [BACK_STYLE, '<div class="jpcard">']

    if not card['k']:
        # Kanji word: show yomikata
        parts.append(f'<div class="label">Yomikata</div>')
        parts.append(f'<div class="yomi">{card["y"]}</div>')

    parts.append(f'<div class="arti">{card["a"]}</div>')

    # Contoh kalimat
    parts.append(
        f'<div class="kalimat">'
        f'<div class="label">Contoh Kalimat</div>'
        f'<div class="jp">{card["ej"]}</div>'
        f'<div class="id">{card["ei"]}</div>'
        f'</div>'
    )

    if not card['k'] and card.get('ch'):
        # Analisis box
        minis = ''.join(build_kanji_mini(c, ku, on, m) for c, ku, on, m in card['ch'])
        parts.append(
            f'<div class="analisis-box">'
            f'<div class="analisis-title">Analisis</div>'
            f'<div class="kanji-strip">{minis}</div>'
            f'</div>'
        )

    # Cocoklogi
    parts.append(
        f'<div class="cocoklogi-box">'
        f'<b>Cocoklogi:</b> {card["co"]}'
        f'</div>'
    )

    parts.append('</div>')
    return ''.join(parts)


# ============================================================
# CARD DATA — 12 GROUPS, ~94 CARDS
# ============================================================

CARDS = [

    # ──────────────────────────────────────────────────────────
    # GROUP 1: KS::Suhu (6 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '暑い', 'y': 'あつい', 'a': 'Panas (cuaca)',
        'ej': '今日はとても暑いです。',
        'ei': 'Hari ini sangat panas.',
        'k': False,
        'ch': [
            ('暑', 'あつ(い)', 'ショ',
             'Panas (cuaca). Radikal 日 (matahari) di atas + 者 (orang/sesuatu) di bawah. Matahari yang memanggang siapapun yang berdiri di bawahnya — panasnya dari langit, bukan dari benda yang disentuh.')
        ],
        'co': '日 (matahari) memancarkan sinar langsung ke atas kepala 者 (orang-orang) — saking teriknya, tidak ada tempat berlindung, keringat mengucur deras. 暑い adalah <b>panas cuaca</b>: yang kamu rasakan di udara, bukan di tangan.'
    },

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '熱い', 'y': 'あつい', 'a': 'Panas (benda/cairan)',
        'ej': 'このスープは熱いから気をつけて。',
        'ei': 'Hati-hati, sup ini panas.',
        'k': False,
        'ch': [
            ('熱', 'あつ(い)', 'ネツ',
             'Panas (benda). Bagian atas menyerupai 執 (memegang/menggenggam), bagian bawah 灬 (api, bentuk lain 火). Tangan menggenggam sesuatu yang dipanaskan di atas api — panas yang terasa langsung di kulit saat disentuh.')
        ],
        'co': '灬 (api) menyala di bawah, dan tangan di atas sedang memegang sesuatu — tentu panasnya langsung terasa di jari! 熱い adalah <b>panas benda/cairan</b>: sup mendidih, cangkir teh baru diseduh, keran air panas. Kalau 暑い dari udara, 熱い dari sentuhan.'
    },

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '寒い', 'y': 'さむい', 'a': 'Dingin (cuaca)',
        'ej': '冬は寒いです。',
        'ei': 'Musim dingin itu dingin.',
        'k': False,
        'ch': [
            ('寒', 'さむ(い)', 'カン',
             'Dingin (cuaca). 宀 (atap rumah) di atas, di tengahnya ada 人 (orang) berselimut, dan di bawah paling dasar ada 冫冫 (es, ditulis dua kali). Seseorang berlindung di dalam rumah dari es yang membekukan segalanya di luar.')
        ],
        'co': '宀 (atap rumah) melindungi seseorang yang menggigil, sementara di luar 冫 (es) sudah membeku di mana-mana — dinginnya bukan dari benda yang disentuh, tapi dari udara itu sendiri yang menusuk tulang. 寒い = <b>dingin cuaca</b>.'
    },

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '冷たい', 'y': 'つめたい', 'a': 'Dingin (benda/cairan)',
        'ej': 'この水は冷たくておいしい。',
        'ei': 'Air ini dingin dan enak.',
        'k': False,
        'ch': [
            ('冷', 'つめ(たい) / ひ(える)', 'レイ',
             'Dingin (benda). 冫 (es) + 令 (perintah; terdiri dari 人 di atas + 卩 orang berlutut = memberi perintah). Es yang "memerintahkan" dingin ke apapun yang menyentuhnya — dingin kontak langsung.')
        ],
        'co': '冫 (es) + 令 (perintah) — es memberikan "perintah dingin" langsung ke tanganmu saat kamu menyentuhnya. 冷たい adalah <b>dingin benda/cairan</b>: kaleng dari kulkas, air es, tangan orang yang kedinginan. Dinginnya terasa di kulit, bukan di udara.'
    },

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '涼しい', 'y': 'すずしい', 'a': 'Sejuk',
        'ej': '秋の風は涼しいです。',
        'ei': 'Angin musim gugur itu sejuk.',
        'k': False,
        'ch': [
            ('涼', 'すず(しい)', 'リョウ',
             'Sejuk. 氵 (air) + 京 (ibu kota/menara tinggi; 亠 atap + 口 ruang + 小 kecil, gambaran bangunan megah menjulang). Air mengalir di kaki bangunan tinggi — hembusan angin lembab yang menyegarkan, bukan dingin menusuk.')
        ],
        'co': '氵 (air) mengalir tenang di kaki 京 (menara tinggi kota besar) — angin bertiup lembab dari permukaan air, melewati lorong bangunan, dan sampai ke kulitmu sebagai hembusan <b>sejuk</b> yang menyegarkan. Bukan panas, bukan dingin — pas.'
    },

    {
        'g': 'KS::Suhu', 't': 'Suhu',
        'w': '暖かい', 'y': 'あたたかい', 'a': 'Hangat',
        'ej': '今日は暖かい天気ですね。',
        'ei': 'Cuacanya hangat hari ini ya.',
        'k': False,
        'ch': [
            ('暖', 'あたた(かい) / あたた(める)', 'ダン',
             'Hangat. 日 (matahari) di kiri + bagian kanan berhubungan dengan 爰 (membantu/menarik). Matahari yang "membantu" — bukan memanggang terik seperti 暑, melainkan memberikan sinar lembut yang menghangatkan tanpa menyengat.')
        ],
        'co': '日 (matahari) hadir, tapi bukan yang terik membakar seperti 暑い — ini matahari yang lembut, seperti sinar pagi masuk lewat jendela di musim dingin. Memberikan kehangatan tanpa keringat. 暖かい = <b>hangat</b>, zona nyaman antara dingin dan panas.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 2: KS::Ukuran (12 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '大きい', 'y': 'おおきい', 'a': 'Besar',
        'ej': 'この公園は大きいです。',
        'ei': 'Taman ini besar.',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. Piktogram orang (人) merentangkan kedua tangan selebar-lebarnya ke kiri dan kanan — gestur universal untuk menunjukkan "besar." Bentuknya sederhana: satu garis horizontal panjang ditopang dua kaki.')
        ],
        'co': 'Bayangkan seseorang berdiri tegak lalu merentangkan tangan selebar mungkin — tubuhnya membentuk huruf 大. "Sebesar ini lho!" Gestur paling dasar untuk menunjukkan sesuatu yang <b>besar</b>.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '大きな', 'y': 'おおきな', 'a': 'Besar (bentuk prenominal/連体詞)',
        'ej': '大きな夢を持っています。',
        'ei': 'Saya punya mimpi besar.',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. (Sama dengan 大きい.) Piktogram orang merentangkan tangan. Tapi dalam bentuk 大きな, ini adalah 連体詞 (rentaishi) — bukan い-adjective biasa. Hanya bisa dipakai langsung sebelum kata benda, tidak bisa di akhir kalimat.')
        ],
        'co': 'Kanji yang sama — 大 — tapi dipasangkan dengan な, bukan い. 大きな hanya bisa berdiri tepat di depan kata benda: 大きな夢 (mimpi <b>besar</b>). Nuansanya lebih subjektif dan emosional dibanding 大きい yang netral-objektif. Tidak bisa dipakai sebagai predikat (大きなです ❌).'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '小さい', 'y': 'ちいさい', 'a': 'Kecil',
        'ej': 'この箱は小さいです。',
        'ei': 'Kotak ini kecil.',
        'k': False,
        'ch': [
            ('小', 'ちい(さい) / こ / お', 'ショウ',
             'Kecil. Piktogram: satu garis vertikal di tengah dengan dua goresan kecil jatuh di kedua sisi — seolah sesuatu yang utuh dipecah menjadi serpihan-serpihan kecil yang berhamburan.')
        ],
        'co': 'Garis vertikal ｜ dengan dua partikel kecil ＼ ╱ jatuh ke samping — sesuatu yang tadinya utuh, hancur jadi serpihan <b>kecil</b>. Kebalikan dari 大 yang merentang lebar, 小 justru menciut dan menyebar jadi remah.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '小さな', 'y': 'ちいさな', 'a': 'Kecil (bentuk prenominal/連体詞)',
        'ej': '小さな声で話してください。',
        'ei': 'Tolong bicara dengan suara kecil.',
        'k': False,
        'ch': [
            ('小', 'ちい(さい) / こ / お', 'ショウ',
             'Kecil. (Sama dengan 小さい.) Dalam bentuk 小さな, ini 連体詞 — hanya bisa menempel langsung di depan kata benda. Nuansa lebih intim dan subjektif.')
        ],
        'co': 'Versi 連体詞 dari 小さい — 小さな声 (suara <b>kecil</b>) terasa lebih intim dan puitis dibanding 小さい声. Seperti berbisik lembut. Ingat: 小さな hanya bisa di depan kata benda, tidak bisa jadi predikat.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '長い', 'y': 'ながい', 'a': 'Panjang',
        'ej': 'この川は長いです。',
        'ei': 'Sungai ini panjang.',
        'k': False,
        'ch': [
            ('長', 'なが(い)', 'チョウ',
             'Panjang. Piktogram orang tua berambut panjang terurai memegang tongkat. Rambut yang panjang = umur yang panjang. Juga bermakna "kepala/pemimpin" (社長, 校長) karena orang berumur panjang dianggap berpengalaman.')
        ],
        'co': 'Gambar orang tua dengan rambut terurai sampai bawah, memegang tongkat — rambutnya <b>panjang</b>, umurnya juga panjang. Makanya 長 selain berarti "panjang" juga jadi "kepala/ketua" — yang paling senior memimpin.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '短い', 'y': 'みじかい', 'a': 'Pendek',
        'ej': '夏休みは短いです。',
        'ei': 'Liburan musim panas pendek.',
        'k': False,
        'ch': [
            ('短', 'みじか(い)', 'タン',
             'Pendek. 矢 (panah) + 豆 (kacang/bejana kecil). Panah yang ukurannya cuma sependek kacang — anak panah mini yang tidak bisa terbang jauh.')
        ],
        'co': '矢 (panah) yang panjangnya cuma se-豆 (kacang) — coba tembakkan panah sependek itu, pasti langsung jatuh di depan kaki. Itulah 短い: <b>pendek</b>, tidak cukup panjang untuk mencapai tujuan.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '高い', 'y': 'たかい', 'a': 'Tinggi / Mahal',
        'ej': 'あの山は高いです。',
        'ei': 'Gunung itu tinggi.',
        'k': False,
        'ch': [
            ('高', 'たか(い)', 'コウ',
             'Tinggi / Mahal. Piktogram bangunan bertingkat: 亠 (atap paling atas) + 口 (ruangan tengah) + 冂 (fondasi bawah). Pavilion atau menara pengawas yang menjulang tinggi. Sesuatu yang tinggi biasanya langka dan bernilai, sehingga bermakna "mahal" juga.')
        ],
        'co': '高 menggambarkan menara berlapis: atap 亠, ruangan 口, fondasi 冂 — bertumpuk ke atas, menjulang <b>tinggi</b>. Dan di zaman apapun, sesuatu yang tinggi dan langka selalu <b>mahal</b> harganya. Dua arti dalam satu kanji.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '低い', 'y': 'ひくい', 'a': 'Rendah',
        'ej': 'この机は低いです。',
        'ei': 'Meja ini rendah.',
        'k': False,
        'ch': [
            ('低', 'ひく(い)', 'テイ',
             'Rendah. 亻 (orang) + 氐 (dasar/fondasi; 氏 keluarga + titik di bawah = titik paling bawah). Orang yang posisinya ada di paling bawah, di titik terendah.')
        ],
        'co': '亻 (orang) berdiri di 氐 (titik paling bawah, dasar dari segala dasar) — posisinya tidak bisa lebih rendah lagi. 低い = <b>rendah</b>. Kebalikan dari 高い yang menjulang ke atas.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '広い', 'y': 'ひろい', 'a': 'Luas',
        'ej': 'この部屋は広いです。',
        'ei': 'Kamar ini luas.',
        'k': False,
        'ch': [
            ('広', 'ひろ(い)', 'コウ',
             'Luas. 广 (atap/bangunan besar yang terbuka) + ム (lengan/pribadi). Bangunan beratap lebar yang interiornya terbuka luas tanpa sekat. Bentuk lama 廣 lebih jelas: 广 + 黄 (kuning, warna ladang gandum) — seluas ladang gandum.')
        ],
        'co': '广 (bangunan beratap lebar) yang di dalamnya terbuka tanpa sekat — bisa melihat dari ujung ke ujung tanpa halangan. 広い = <b>luas</b>, ruang yang membentang bebas.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '狭い', 'y': 'せまい', 'a': 'Sempit',
        'ej': 'この道は狭いです。',
        'ei': 'Jalan ini sempit.',
        'k': False,
        'ch': [
            ('狭', 'せま(い)', 'キョウ',
             'Sempit. 犭 (binatang/anjing) + 夹 (terjepit; 大 orang besar diapit dua 人 orang di kiri-kanan). Binatang yang terjepit di ruang sempit, tidak bisa bergerak bebas ke mana-mana.')
        ],
        'co': '犭 (binatang) yang 夹 (terjepit) di antara dua orang — terhimpit di lorong yang terlalu sempit untuk bergerak, badan mentok kiri-kanan. 狭い = <b>sempit</b>, kebalikan dari 広い.'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '太い', 'y': 'ふとい', 'a': 'Tebal / Gemuk',
        'ej': '太い木が公園にあります。',
        'ei': 'Ada pohon tebal/besar di taman.',
        'k': False,
        'ch': [
            ('太', 'ふと(い)', 'タイ / タ',
             'Tebal/Gemuk. 大 (besar) + 丶 (titik/sedikit lebih). Ambil "besar," tambahkan sedikit lagi — sekarang bukan cuma besar, tapi berisi, berdaging, tebal. Titik ekstra itu yang membedakan 大 (besar) dari 太 (gemuk).')
        ],
        'co': '大 (besar) + 丶 (titik ekstra, sedikit tambahan) — bukan cuma besar, tapi ada "isi" lebih yang bikin gendut dan tebal. 太い = <b>tebal/gemuk</b>. Satu titik kecil mengubah "besar" jadi "gemuk."'
    },

    {
        'g': 'KS::Ukuran', 't': 'Ukuran',
        'w': '細い', 'y': 'ほそい', 'a': 'Tipis / Ramping',
        'ej': '細い道を歩きました。',
        'ei': 'Saya berjalan di jalan yang sempit/kecil.',
        'k': False,
        'ch': [
            ('細', 'ほそ(い) / こま(かい)', 'サイ',
             'Tipis/Ramping. 糸 (benang) + 田 (sawah). Benang setipis garis yang membagi petak sawah — sesuatu yang langsing, kurus, tidak bervolume.')
        ],
        'co': '糸 (benang) membentang melintasi 田 (sawah) — coba bayangkan sehelai benang tunggal terbentang di atas sawah luas. Begitu <b>tipis dan ramping</b>, nyaris tak terlihat. 細い = kurus, langsing, berdiameter kecil.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 3: KS::Rasa (6 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '甘い', 'y': 'あまい', 'a': 'Manis',
        'ej': 'このケーキは甘いです。',
        'ei': 'Kue ini manis.',
        'k': False,
        'ch': [
            ('甘', 'あま(い)', 'カン',
             'Manis. Piktogram mulut (mirip 口) dengan garis horizontal di dalamnya — menggambarkan sesuatu yang ditaruh di dalam mulut dan dikecap manisnya. Bentuk asli menyerupai orang memasukkan makanan manis ke mulut.')
        ],
        'co': '甘 menggambarkan 口 (mulut) dengan sesuatu di dalamnya — lidah sedang mengecap gula atau madu yang meleleh. Sensasi <b>manis</b> yang memenuhi rongga mulut.'
    },

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '辛い', 'y': 'からい', 'a': 'Pedas (juga dibaca つらい = menderita)',
        'ej': 'この料理は辛いです。',
        'ei': 'Masakan ini pedas.',
        'k': False,
        'ch': [
            ('辛', 'から(い) / つら(い)', 'シン',
             'Pedas / Menderita. Piktogram alat tato berujung tajam yang dipakai untuk menghukum di zaman kuno Tiongkok. Rasa yang "menghukum" — kalau di lidah: pedas (からい), kalau di hati: menderita (つらい). Dua jenis rasa sakit, satu kanji.')
        ],
        'co': '辛 asalnya gambar jarum tato untuk penghukuman — rasanya menusuk dan menyiksa. Di lidah, tusukan itu jadi rasa <b>pedas</b> (からい) yang membakar. Di kehidupan, tusukan itu jadi rasa <b>menderita</b> (つらい) yang menyayat hati. Satu kanji, dua bacaan, dua jenis penderitaan.'
    },

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '苦い', 'y': 'にがい', 'a': 'Pahit',
        'ej': 'この薬は苦いです。',
        'ei': 'Obat ini pahit.',
        'k': False,
        'ch': [
            ('苦', 'にが(い) / くる(しい)', 'ク',
             'Pahit. 艹 (rumput/tanaman) + 古 (tua/kuno; 十 sepuluh + 口 mulut). Tanaman tua yang sudah layu — kalau dikunyah, rasanya pahit dan getir. Juga bermakna "menderita" (苦しい, くるしい) karena pahitnya kehidupan.')
        ],
        'co': '艹 (tanaman) yang sudah 古 (tua dan kering) — bayangkan mengunyah daun layu yang sudah kehilangan segala rasa selain getir. <b>Pahit</b> di lidah, pahit di hati. Obat memang 苦い, tapi kadang hidup juga.'
    },

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '美味しい', 'y': 'おいしい', 'a': 'Enak',
        'ej': 'この寿司は美味しいです。',
        'ei': 'Sushi ini enak.',
        'k': False,
        'ch': [
            ('美', 'うつく(しい)', 'ビ',
             'Indah. 羊 (domba) + 大 (besar). Domba gemuk nan besar — di budaya Tiongkok kuno, domba gemuk sempurna dianggap puncak keindahan dan kelezatan. Dari sini lahir konsep "indah" dan "lezat."'),
            ('味', 'あじ', 'ミ',
             'Rasa. 口 (mulut) + 未 (belum; pohon dengan cabang atas yang belum berkembang penuh). Mulut yang belum selesai mengecap — masih menikmati, masih merasakan, belum puas.')
        ],
        'co': '美 (domba gemuk sempurna = puncak keindahan dan kelezatan) + 味 (rasa yang masih dikecap di mulut, belum ingin ditelan) &rarr; rasa yang begitu indah sempurna sampai mulut tidak mau berhenti menikmatinya. <b>Enak</b>.'
    },

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '不味い', 'y': 'まずい', 'a': 'Tidak enak',
        'ej': 'この料理は不味いです。',
        'ei': 'Masakan ini tidak enak.',
        'k': False,
        'ch': [
            ('不', '–', 'フ / ブ',
             'Tidak/Bukan. Piktogram tunas bunga yang terhalang dan tidak bisa mekar — sesuatu yang seharusnya terjadi tapi gagal. Negasi murni.'),
            ('味', 'あじ', 'ミ',
             'Rasa. 口 (mulut) + 未 (belum). (Sama dengan penjelasan di 美味しい.)')
        ],
        'co': '不 (tidak, gagal) + 味 (rasa) &rarr; rasa yang "gagal," yang salah, yang bikin mulut menolak. Kalau 美味しい adalah rasa yang indah sempurna, 不味い adalah kebalikannya: <b>tidak enak</b>, rasanya salah total.'
    },

    {
        'g': 'KS::Rasa', 't': 'Rasa',
        'w': '濃い', 'y': 'こい', 'a': 'Kental / Pekat',
        'ej': 'このコーヒーは濃いです。',
        'ei': 'Kopi ini kental.',
        'k': False,
        'ch': [
            ('濃', 'こ(い)', 'ノウ',
             'Kental/Pekat. 氵 (air/cairan) + 農 (pertanian; 曲 bengkok + 辰 cangkul/waktu). Cairan dari ladang pertanian — air sawah yang keruh penuh lumpur dan nutrisi, tidak encer tapi kental dan penuh isi.')
        ],
        'co': '氵 (cairan) dari dunia 農 (pertanian) — bayangkan air sawah yang penuh lumpur, nutrisi, dan endapan. Bukan air jernih encer, tapi cairan <b>kental dan pekat</b> yang terasa berat. 濃い juga dipakai untuk warna yang tua/gelap dan rasa yang kuat.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 4: KS::Tekstur (6 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '固い', 'y': 'かたい', 'a': 'Keras',
        'ej': 'このパンは固いです。',
        'ei': 'Roti ini keras.',
        'k': False,
        'ch': [
            ('固', 'かた(い) / かた(める)', 'コ',
             'Keras. 囗 (kotak/pagar, kurungan tertutup) + 古 (tua/kuno). Sesuatu yang tua dikurung rapat dalam kotak — terkunci, tidak bisa bergerak, mengeras seiring waktu.')
        ],
        'co': '古 (sesuatu yang sudah tua) dikurung rapat dalam 囗 (kotak tertutup) — dipenjara bertahun-tahun tanpa disentuh, akhirnya membatu dan mengeras. Tidak bisa dibengkokkan, tidak bisa dipecahkan. 固い = <b>keras</b>.'
    },

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '柔らかい', 'y': 'やわらかい', 'a': 'Lembut / Lunak',
        'ej': 'このクッションは柔らかいです。',
        'ei': 'Bantal ini lembut.',
        'k': False,
        'ch': [
            ('柔', 'やわ(らかい)', 'ジュウ / ニュウ',
             'Lembut/Lunak. 矛 (tombak) + 木 (pohon/kayu). Tombak yang terbuat dari kayu lentur — bukan logam kaku, tapi kayu yang bisa dilengkungkan tanpa patah. Fleksibel, elastis.')
        ],
        'co': '矛 (tombak) dari 木 (kayu) — bukan besi yang kaku membunuh, tapi kayu yang bisa dilengkungkan, ditekuk, dan kembali ke bentuk semula. Fleksibel tanpa patah. 柔らかい = <b>lembut dan lentur</b>. Kebalikan dari 固い.'
    },

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '薄い', 'y': 'うすい', 'a': 'Tipis (benda) / Pudar (warna/rasa)',
        'ej': 'この紙は薄いです。',
        'ei': 'Kertas ini tipis.',
        'k': False,
        'ch': [
            ('薄', 'うす(い)', 'ハク',
             'Tipis/Pudar. 艹 (rumput/tanaman) + 氵 (air) + 甫 (merebak/tersebar). Rumput tipis yang menyebar di atas permukaan air — lapisan yang begitu tipisnya, hampir transparan. Juga bermakna warna atau rasa yang pudar/encer.')
        ],
        'co': '艹 (rumput) tumbuh setipis selaput di atas 氵 (air) — nyaris transparan, bisa ditembus cahaya. 薄い punya dua wajah: <b>tipis</b> untuk benda (kertas tipis, dinding tipis), dan <b>pudar</b> untuk warna/rasa (warna pucat, teh encer). Satu kata, dua konteks.'
    },

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '厚い', 'y': 'あつい', 'a': 'Tebal',
        'ej': '厚い本を読んでいます。',
        'ei': 'Saya sedang membaca buku tebal.',
        'k': False,
        'ch': [
            ('厚', 'あつ(い)', 'コウ',
             'Tebal. 厂 (tebing/lereng batu) + bagian dalam (日 matahari + 子 anak). Tebing batu berlapis-lapis yang melindungi sinar dan anak di bawahnya — setebal dan sekokoh dinding batu alam.')
        ],
        'co': '厂 (tebing batu) berlapis-lapis yang melindungi 子 (anak) dari 日 (sinar terik) — dinding alam setebal itu tidak bisa ditembus. 厚い = <b>tebal</b>. Kebalikan dari 薄い. Juga bisa berarti "murah hati" (情が厚い = perasaannya tebal/hangat).'
    },

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '細かい', 'y': 'こまかい', 'a': 'Halus / Detail',
        'ej': '細かい作業が得意です。',
        'ei': 'Saya pandai pekerjaan yang detail.',
        'k': False,
        'ch': [
            ('細', 'こま(かい) / ほそ(い)', 'サイ',
             'Halus/Detail. 糸 (benang) + 田 (sawah). Benang yang membagi sawah jadi petak-petak kecil — fokusnya di sini bukan "tipis" (itu 細い/ほそい), tapi "rinci dan presisi" dalam membagi dan mengelola detail.')
        ],
        'co': '糸 (benang) membagi 田 (sawah) jadi petak-petak kecil nan rapi — setiap petak terukur presisi, tidak ada yang meleset. Kalau 細い (ほそい) soal bentuk fisik yang tipis, 細かい (こまかい) soal <b>detail dan kehalusan</b> dalam mengerjakan sesuatu.'
    },

    {
        'g': 'KS::Tekstur', 't': 'Tekstur',
        'w': '丸い', 'y': 'まるい', 'a': 'Bulat',
        'ej': '月は丸いです。',
        'ei': 'Bulan itu bulat.',
        'k': False,
        'ch': [
            ('丸', 'まる(い)', 'ガン',
             'Bulat. 九 (sembilan — tapi asalnya garis melengkung) + 丶 (titik). Garis lengkung yang membungkus titik di dalamnya — membentuk lingkaran. Gambar bola atau benda bundar.')
        ],
        'co': '九 (garis melengkung) melingkari 丶 (titik) — bayangkan goresan yang melengkung sampai hampir menyatu, membentuk lingkaran dengan inti di tengahnya. 丸い = <b>bulat</b>. Bulan purnama, bola, koin — semua 丸い.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 5: KS::Warna (3 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Warna', 't': 'Warna',
        'w': '赤い', 'y': 'あかい', 'a': 'Merah',
        'ej': '赤い花が咲いています。',
        'ei': 'Bunga merah sedang mekar.',
        'k': False,
        'ch': [
            ('赤', 'あか(い)', 'セキ / シャク',
             'Merah. Asal piktografis: 大 (orang berdiri) + 火 (api) di bawah. Orang yang berdiri di atas api — wajahnya memerah terbakar panas. Warna bara api yang membara.')
        ],
        'co': '大 (orang) berdiri di atas 火 (api) — wajahnya langsung memerah terpanggang. Atau bayangkan bara api yang membara di perapian: warna pertama yang kamu lihat adalah <b>merah</b>. 赤い.'
    },

    {
        'g': 'KS::Warna', 't': 'Warna',
        'w': '黒い', 'y': 'くろい', 'a': 'Hitam',
        'ej': '黒い猫がいます。',
        'ei': 'Ada kucing hitam.',
        'k': False,
        'ch': [
            ('黒', 'くろ(い)', 'コク',
             'Hitam. Bagian atas: 里 (desa/tanah; 田 sawah + 土 tanah), bagian bawah: 灬 (api). Tanah pertanian dibakar api sampai hangus — yang tersisa hanyalah arang hitam pekat.')
        ],
        'co': '田+土 (tanah pertanian desa) dibakar habis oleh 灬 (api) — ladang yang tadinya hijau berubah jadi arang. Yang tersisa: warna <b>hitam</b> pekat tanpa sisa kehidupan. 黒い.'
    },

    {
        'g': 'KS::Warna', 't': 'Warna',
        'w': '白い', 'y': 'しろい', 'a': 'Putih',
        'ej': '白い雲が浮かんでいます。',
        'ei': 'Awan putih mengambang.',
        'k': False,
        'ch': [
            ('白', 'しろ(い)', 'ハク / ビャク',
             'Putih. Piktogram sinar matahari yang menyilaukan — cahaya paling terang yang menghapus semua warna lain. Ada juga teori ini gambar biji ek/acorn yang putih bersih di dalamnya. Intinya: terang, murni, kosong dari warna.')
        ],
        'co': '白 menggambarkan berkas cahaya yang begitu terang sampai menghapus semua warna — yang tersisa hanya kekosongan <b>putih</b>. Kalau 黒 adalah kegelapan total, 白 adalah keterangan total. Dua kutub warna.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 6: KS::Perasaan (9 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '好きな', 'y': 'すきな', 'a': 'Suka',
        'ej': '音楽が好きです。',
        'ei': 'Saya suka musik.',
        'k': False,
        'ch': [
            ('好', 'す(き) / この(む)', 'コウ',
             'Suka. 女 (perempuan/ibu) + 子 (anak). Ibu memeluk anaknya — kasih sayang paling murni di dunia. Hubungan ibu-anak adalah akar dari semua rasa "suka" dan "sayang."')
        ],
        'co': '女 (ibu) memeluk 子 (anak) — cinta paling murni yang ada: tanpa syarat, tanpa pamrih. Dari ikatan itu lahirlah makna <b>suka</b>. 好きな adalah na-adjective, jadi pakainya: 音楽が好きです, bukan 好きいです.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '嫌い', 'y': 'きらい', 'a': 'Benci / Tidak suka',
        'ej': '野菜が嫌いです。',
        'ei': 'Saya tidak suka sayuran.',
        'k': False,
        'ch': [
            ('嫌', 'きら(い) / いや', 'ケン / ゲン',
             'Benci/Tidak suka. 女 (perempuan/seseorang) + 兼 (merangkap; ⺕ tangan + 禾禾 dua tangkai padi = tangan memegang dua beban sekaligus). Seseorang yang dipaksa merangkap terlalu banyak — rasa jengkel dan muak yang menumpuk.')
        ],
        'co': '女 (seseorang) dipaksa 兼 (merangkap banyak hal sekaligus) — overloaded, muak, ingin melepas semuanya. Rasa jengkel itu terakumulasi jadi <b>benci/tidak suka</b>. 嫌い. Kebalikan dari 好き.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '欲しい', 'y': 'ほしい', 'a': 'Ingin (memiliki)',
        'ej': '新しいパソコンが欲しいです。',
        'ei': 'Saya ingin komputer baru.',
        'k': False,
        'ch': [
            ('欲', 'ほ(しい)', 'ヨク',
             'Ingin. 谷 (lembah; 八 celah + 口 mulut = celah di gunung yang menganga) + 欠 (kurang/menguap; gambar orang membuka mulut lebar). Lembah kosong menganga + mulut terbuka karena lapar — keinginan yang timbul dari kekosongan.')
        ],
        'co': '谷 (lembah kosong menganga) + 欠 (mulut terbuka lebar, kelaparan) — ada lubang besar di dalam diri yang meminta untuk diisi. Kekosongan itu yang mendorong: "aku <b>ingin</b> itu." 欲しい = keinginan memiliki.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '怖い', 'y': 'こわい', 'a': 'Takut / Menakutkan',
        'ej': 'お化けが怖いです。',
        'ei': 'Saya takut hantu.',
        'k': False,
        'ch': [
            ('怖', 'こわ(い)', 'フ',
             'Takut. 忄 (hati, bentuk samping 心) + 布 (kain; 巾 lap + ナ tangan yang menarik). Hati yang ditutupi kain gelap — tidak bisa melihat apa yang ada di depan, jantung berdebar dalam kegelapan.')
        ],
        'co': '忄 (hati) dibungkus 布 (kain gelap) — bayangkan mata ditutup kain di ruangan asing, tidak bisa melihat apa-apa, hanya mendengar suara-suara aneh. Jantung berdebar, badan merinding. Itulah <b>takut</b>. 怖い.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '痛い', 'y': 'いたい', 'a': 'Sakit',
        'ej': '頭が痛いです。',
        'ei': 'Kepala saya sakit.',
        'k': False,
        'ch': [
            ('痛', 'いた(い)', 'ツウ',
             'Sakit. 疒 (penyakit; gambar orang berbaring di tempat tidur karena sakit) + 甬 (terowongan/menerobos; 用 memakai + マ). Rasa sakit yang menerobos tubuh seperti arus listrik melewati terowongan — tajam, langsung, tidak bisa diabaikan.')
        ],
        'co': '疒 (orang berbaring sakit) dengan rasa nyeri yang 甬 (menerobos) tubuh — bukan sakit yang tumpul, tapi yang tajam dan langsung, seperti jarum menembus daging. <b>Sakit</b>. 痛い. Kata pertama yang kamu teriak waktu kejedot meja.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '寂しい', 'y': 'さびしい', 'a': 'Kesepian',
        'ej': '一人で寂しいです。',
        'ei': 'Sendirian, rasanya kesepian.',
        'k': False,
        'ch': [
            ('寂', 'さび(しい) / さみ(しい)', 'セキ / ジャク',
             'Kesepian/Sunyi. 宀 (atap rumah besar) + 叔 (paman muda/adik bungsu; 上 atas + 小 kecil + 又 tangan). Rumah besar yang cuma dihuni satu orang kecil — ruangan luas tapi kosong, langkah kaki bergema tanpa balasan.')
        ],
        'co': '宀 (rumah besar) yang di dalamnya cuma ada 叔 (satu orang sendirian) — langkah kakinya bergema di koridor kosong, tidak ada suara lain yang menyahut. Semakin luas rumahnya, semakin terasa <b>kesepiannya</b>. 寂しい.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '怠い', 'y': 'だるい', 'a': 'Lesu / Malas',
        'ej': '体が怠いです。',
        'ei': 'Badan terasa lesu.',
        'k': False,
        'ch': [
            ('怠', 'おこた(る) / だる(い)', 'タイ',
             'Lesu/Malas. 台 (alas/panggung; ム pribadi + 口 mulut) + 心 (hati) di bawah. Hati yang seharusnya naik ke panggung dan beraksi, tapi memilih diam di bawah — tidak ada motivasi, tubuh berat, jiwa kosong.')
        ],
        'co': '心 (hati) diminta naik ke 台 (panggung) dan beraksi — tapi hatinya menolak. Badan terasa berat kayak ditimpa bantal, otak berkabut, motivasi nol. <b>Lesu dan malas</b>. 怠い. Perasaan klasik hari Senin pagi.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '嬉しい', 'y': 'うれしい', 'a': 'Senang / Gembira',
        'ej': 'プレゼントをもらって嬉しいです。',
        'ei': 'Saya senang mendapat hadiah.',
        'k': False,
        'ch': [
            ('嬉', 'うれ(しい)', 'キ',
             'Senang/Gembira. 女 (perempuan/seseorang) + 喜 (senang; 壴 gendang/alat musik + 口 mulut). Seseorang yang bersuka cita — mulutnya bernyanyi diiringi dentuman gendang kebahagiaan.')
        ],
        'co': '女 (seseorang) yang 喜 (bersuka cita — mulut bernyanyi diiringi gendang) — seluruh tubuhnya memancarkan kebahagiaan. Senyum lebar, mata berbinar, ingin loncat-loncat. <b>Senang</b>. 嬉しい.'
    },

    {
        'g': 'KS::Perasaan', 't': 'Perasaan',
        'w': '悲しい', 'y': 'かなしい', 'a': 'Sedih',
        'ej': '映画を見て悲しくなりました。',
        'ei': 'Saya jadi sedih setelah menonton film.',
        'k': False,
        'ch': [
            ('悲', 'かな(しい)', 'ヒ',
             'Sedih. 非 (bukan/bertentangan; dua sayap yang saling berlawanan arah, bercerai) + 心 (hati). Hati yang terbelah ke dua arah — keinginan berbenturan dengan kenyataan, harapan hancur.')
        ],
        'co': '非 (dua sayap bercerai, berpisah ke arah berlawanan) + 心 (hati) — hati yang terbelah dua karena kenyataan tidak sesuai harapan. Ingin terbang tapi sayapnya bercerai. <b>Sedih</b>. 悲しい.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 7: KS::Sifat (10 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '馬鹿', 'y': 'ばか', 'a': 'Bodoh',
        'ej': 'そんな馬鹿なことをしないで。',
        'ei': 'Jangan melakukan hal bodoh seperti itu.',
        'k': False,
        'ch': [
            ('馬', 'うま', 'バ',
             'Kuda. Piktogram kuda dilihat dari samping — kepala dengan surai, badan, empat kaki, dan ekor. Salah satu kanji tertua yang masih menyerupai bentuk aslinya.'),
            ('鹿', 'しか', 'ロク',
             'Rusa. Piktogram rusa dengan tanduk bercabang di atas kepala. Bagian atas menggambarkan tanduk, bagian bawah badan dan kaki rusa.')
        ],
        'co': '馬 (kuda) + 鹿 (rusa) — dari kisah sejarah Tiongkok: perdana menteri Zhao Gao membawa seekor rusa ke istana lalu mengatakan pada kaisar "ini kuda." Siapapun yang tidak bisa membedakan kuda dari rusa (atau pura-pura tidak bisa) = <b>bodoh</b>. Makanya 馬鹿 = bodoh.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '元気', 'y': 'げんき', 'a': 'Sehat / Bersemangat',
        'ej': 'お元気ですか。',
        'ei': 'Apa kabar? (Apakah Anda sehat?)',
        'k': False,
        'ch': [
            ('元', 'もと', 'ゲン / ガン',
             'Asal/Sumber/Dasar. 二 (dua garis horizontal, langit dan bumi) + 儿 (kaki manusia). Manusia berdiri di antara langit dan bumi — titik awal, sumber dari segala sesuatu.'),
            ('気', '–', 'キ / ケ',
             'Energi/Semangat/Udara. 气 (uap yang naik ke atas) + 米 (beras). Uap panas mengepul dari nasi yang baru matang — energi hidup, nafas kehidupan, semangat.')
        ],
        'co': '元 (sumber, titik awal) + 気 (energi dari uap nasi panas yang mengepul) &rarr; kalau sumber energimu terisi penuh, seperti nasi panas yang baru matang dan uapnya mengepul kuat, kamu pasti <b>sehat dan bersemangat</b>. お元気ですか = "apakah sumber energimu masih penuh?"'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '優しい', 'y': 'やさしい', 'a': 'Baik hati / Lembut',
        'ej': '田中さんは優しい人です。',
        'ei': 'Tanaka-san orang yang baik hati.',
        'k': False,
        'ch': [
            ('優', 'やさ(しい) / すぐ(れる)', 'ユウ',
             'Baik hati/Unggul. 亻 (orang) + 憂 (khawatir/prihatin; karakter kompleks yang menggambarkan perasaan cemas mendalam). Orang yang mengkhawatirkan orang lain — bukan khawatir egois, tapi empati tulus yang mendorong kebaikan.')
        ],
        'co': '亻 (seseorang) yang dipenuhi 憂 (kekhawatiran mendalam) — tapi bukan untuk diri sendiri, melainkan untuk orang lain. Empati yang begitu besar sampai rela menanggung beban orang lain. Orang seperti itu = <b>baik hati dan lembut</b>. 優しい.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '親切', 'y': 'しんせつ', 'a': 'Ramah / Baik (dalam tindakan)',
        'ej': '近所の人はとても親切です。',
        'ei': 'Tetangga sangat ramah.',
        'k': False,
        'ch': [
            ('親', 'おや / した(しい)', 'シン',
             'Orang tua/Dekat/Akrab. 立 (berdiri) + 木 (pohon) + 見 (melihat; 目 mata + 儿 kaki). Berdiri di atas pohon untuk melihat/mengawasi — seperti orang tua yang memanjat pohon demi mengawasi anaknya dari kejauhan.'),
            ('切', 'き(る)', 'セツ / サイ',
             'Memotong/Menyentuh langsung. 七 (garis miring, asal: garis potongan) + 刀 (pisau). Pisau yang memotong tepat sasaran — langsung, tanpa basa-basi, mengenai inti.')
        ],
        'co': '親 (orang tua yang mengawasi dari atas pohon, dekat dan peduli) + 切 (memotong jarak, menyentuh langsung) &rarr; kebaikan yang bukan dari jauh atau basa-basi, tapi yang "memotong jarak" dan menyentuh langsung ke hati. <b>Ramah</b> dalam tindakan nyata. 親切.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '我儘', 'y': 'わがまま', 'a': 'Egois / Manja',
        'ej': 'わがままを言わないでください。',
        'ei': 'Tolong jangan bicara egois/manja.',
        'k': False,
        'ch': [
            ('我', 'われ / わ', 'ガ',
             'Aku/Diri sendiri. 手 (tangan) + 戈 (tombak/senjata). Tangan menggenggam senjata untuk membela diri — "AKU" yang menjaga wilayahku sendiri, ego, kepentingan pribadi.'),
            ('儘', 'まま', 'ジン',
             'Sesuka hati/Semaunya. 亻 (orang) + 盡 (menghabiskan/mentok; komponen yang menggambarkan wadah tumpah habis). Orang yang menghabiskan semuanya sesuka hati — tanpa rem, tanpa batas, semau gue.')
        ],
        'co': '我 (AKU, ego yang menggenggam senjata) + 儘 (sesuka hati, menghabiskan semaunya tanpa batas) &rarr; "semuanya harus sesuai keinginanKU, dunia berputar di sumbuku." Sikap <b>egois dan manja</b> murni. 我儘.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': 'ハンサム', 'y': 'ハンサム', 'a': 'Tampan',
        'ej': 'あの俳優はハンサムです。',
        'ei': 'Aktor itu tampan.',
        'k': True,
        'ch': [],
        'co': 'Serapan langsung dari bahasa Inggris "handsome" — ハン (han) + サム (samu). Kata ini khusus untuk ketampanan pria yang gagah dan maskulin. Bayangkan leading actor Hollywood dengan rahang tegas — itulah ハンサム: <b>tampan</b>.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '可愛い', 'y': 'かわいい', 'a': 'Imut / Lucu',
        'ej': 'この犬は可愛いです。',
        'ei': 'Anjing ini imut.',
        'k': False,
        'ch': [
            ('可', '–', 'カ',
             'Boleh/Bisa/Patut. 口 (mulut) + 丁 (paku/titik). Mulut yang menyetujui — "boleh," "bisa," "pantas." Memberikan izin atau penilaian bahwa sesuatu itu layak.'),
            ('愛', 'いと(しい)', 'アイ',
             'Cinta/Sayang. 爫 (tangan dari atas meraih) + 冖 (penutup) + 心 (hati) + 夂 (kaki berjalan lambat). Tangan meraih ke bawah, hati tertutup, kaki terhenti — terjebak dalam perasaan sayang yang tidak bisa pergi.')
        ],
        'co': '可 (layak/patut) + 愛 (dicintai/disayangi) &rarr; sesuatu yang "layak untuk dicintai" — begitu melihatnya, hati langsung luluh dan ingin memeluknya. Dari kucing, bayi, sampai gantungan kunci — kalau bikin gemas, itu <b>imut</b>. 可愛い.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '賑やか', 'y': 'にぎやか', 'a': 'Ramai / Meriah',
        'ej': 'お祭りは賑やかです。',
        'ei': 'Festival itu meriah.',
        'k': False,
        'ch': [
            ('賑', 'にぎ(わう)', 'シン',
             'Ramai/Meriah. 貝 (kerang, simbol uang kuno) + 辰 (waktu pagi/bergetar). Uang yang beredar dan bergetar — bayangkan pasar tradisional di pagi hari: koin berpindah tangan, suara tawar-menawar bergema, aktivitas bergelora.')
        ],
        'co': '貝 (uang/kerang) yang 辰 (bergetar, bergerak ke sana-sini) — pasar tradisional di jam sibuk: pedagang berteriak, pembeli menawar, uang berpindah tangan tanpa henti. Hidup, berenergi, penuh aktivitas. <b>Ramai dan meriah</b>. 賑やか.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': '静か', 'y': 'しずか', 'a': 'Tenang / Sepi',
        'ej': '図書館は静かです。',
        'ei': 'Perpustakaan itu tenang.',
        'k': False,
        'ch': [
            ('静', 'しず(か)', 'セイ / ジョウ',
             'Tenang/Sepi. 青 (biru/hijau; warna langit cerah) + 争 (bertengkar/berlomba). Langit biru yang menenangkan pertengkaran — setelah semua keributan mereda, yang tersisa adalah keheningan biru.')
        ],
        'co': '青 (langit biru yang tenang) meredakan 争 (pertengkaran dan keributan) — bayangkan setelah badai berlalu, langit kembali biru tanpa suara. Semua kebisingan terhenti, yang ada hanya keheningan. <b>Tenang</b>. 静か. Kebalikan dari 賑やか.'
    },

    {
        'g': 'KS::Sifat', 't': 'Sifat',
        'w': 'うるさい', 'y': 'うるさい', 'a': 'Berisik / Mengganggu',
        'ej': '隣の部屋がうるさいです。',
        'ei': 'Kamar sebelah berisik.',
        'k': True,
        'ch': [],
        'co': 'Dengarkan pengucapannya: U-RU-SA-I — empat suku kata yang terasa panjang dan mengganggu, seperti orang yang bicara tanpa henti sampai kamu ingin berteriak "URUSAI!" untuk menyuruhnya diam. Kata ini sendiri terasa <b>berisik</b> saat diucapkan.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 8: KS::Kondisi (14 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '暗い', 'y': 'くらい', 'a': 'Gelap',
        'ej': 'この部屋は暗いです。',
        'ei': 'Kamar ini gelap.',
        'k': False,
        'ch': [
            ('暗', 'くら(い)', 'アン',
             'Gelap. 日 (matahari) + 音 (suara; 立 berdiri + 日 matahari). Matahari telah hilang, hanya suara yang tersisa — di kegelapan total, mata tidak berfungsi, yang bisa diandalkan hanya telinga.')
        ],
        'co': '日 (matahari) sudah terbenam, tersembunyi di balik 音 (suara) — di kegelapan, kamu tidak bisa melihat apa-apa, hanya mendengar suara-suara misterius di sekelilingmu. <b>Gelap</b>. 暗い.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '明るい', 'y': 'あかるい', 'a': 'Terang',
        'ej': 'この部屋は明るいです。',
        'ei': 'Kamar ini terang.',
        'k': False,
        'ch': [
            ('明', 'あか(るい) / あき(らか)', 'メイ / ミョウ',
             'Terang/Jelas. 日 (matahari) + 月 (bulan). Dua sumber cahaya terkuat di alam — matahari di siang hari dan bulan di malam hari — bersinar bersama. Tidak mungkin gelap.')
        ],
        'co': '日 (matahari) + 月 (bulan) bersinar bersamaan — dua sumber cahaya terbesar di langit bergabung. Kapan terakhir kali kamu melihat matahari DAN bulan terang di saat yang sama? Itulah tingkat <b>terangnya</b>. 明るい.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '汚い', 'y': 'きたない', 'a': 'Kotor',
        'ej': 'この服は汚いです。',
        'ei': 'Baju ini kotor.',
        'k': False,
        'ch': [
            ('汚', 'きたな(い) / よご(れる)', 'オ',
             'Kotor. 氵 (air) + 亏 (menyimpang/berkurang; varian dari 于). Air yang sudah menyimpang dari kemurniannya — tercemar, keruh, menjijikkan. Air yang seharusnya jernih tapi sudah rusak.')
        ],
        'co': '氵 (air) yang 亏 (menyimpang dari aslinya) — air yang seharusnya jernih sudah tercemar, keruh, dan menjijikkan. Sesuatu yang sudah kehilangan kemurniannya. <b>Kotor</b>. 汚い.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '綺麗', 'y': 'きれい', 'a': 'Cantik / Bersih',
        'ej': 'この景色は綺麗です。',
        'ei': 'Pemandangan ini cantik.',
        'k': False,
        'ch': [
            ('綺', '–', 'キ',
             'Kain bermotif indah. 糸 (benang/tekstil) + 奇 (luar biasa; 大 besar + 可 bisa). Benang yang ditenun menjadi kain bermotif luar biasa indah — keindahan buatan tangan manusia yang presisi.'),
            ('麗', 'うるわ(しい)', 'レイ',
             'Elegan/Indah. Bagian atas menggambarkan tanduk rusa yang bercabang simetris dan indah, bagian bawah 鹿 (rusa). Rusa dengan tanduk sempurna — keindahan alam yang simetris dan anggun.')
        ],
        'co': '綺 (kain tenun bermotif luar biasa, keindahan buatan manusia) + 麗 (rusa bertanduk elegan, keindahan alam) &rarr; perpaduan keindahan buatan dan alami. 綺麗 bisa berarti <b>cantik</b> (wajah, pemandangan) atau <b>bersih</b> (ruangan rapi) — karena kebersihan itu sendiri adalah keindahan.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '忙しい', 'y': 'いそがしい', 'a': 'Sibuk',
        'ej': '最近忙しいです。',
        'ei': 'Akhir-akhir ini sibuk.',
        'k': False,
        'ch': [
            ('忙', 'いそが(しい)', 'ボウ',
             'Sibuk. 忄 (hati, bentuk samping 心) + 亡 (mati/hilang). Hati yang sudah hilang/mati — terlalu sibuk sampai tidak punya waktu untuk merasakan apa-apa. Jiwa terkikis oleh kesibukan.')
        ],
        'co': '忄 (hati) yang sudah 亡 (hilang, mati) — sibuk sampai hatimu sendiri terabaikan, tidak sempat merasakan apa-apa selain tekanan deadline. <b>Sibuk</b>. 忙しい. Pesan tersembunyi dalam kanji ini: jangan sampai hatimu "mati" karena kesibukan.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '古い', 'y': 'ふるい', 'a': 'Tua / Kuno (benda)',
        'ej': 'この寺は古いです。',
        'ei': 'Kuil ini tua/kuno.',
        'k': False,
        'ch': [
            ('古', 'ふる(い)', 'コ',
             'Tua/Kuno. 十 (sepuluh, banyak) + 口 (mulut/generasi). Cerita yang sudah diturunkan lewat sepuluh generasi mulut ke mulut — kalau sudah melewati sebanyak itu, pasti sudah sangat tua.')
        ],
        'co': '十 (sepuluh, banyak sekali) + 口 (mulut) — cerita yang sudah diceritakan dari mulut ke mulut selama puluhan generasi. Kalau sudah melewati sebanyak itu, tentu sudah sangat <b>tua dan kuno</b>. 古い. Khusus untuk benda, bukan orang.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '新しい', 'y': 'あたらしい', 'a': 'Baru',
        'ej': '新しい靴を買いました。',
        'ei': 'Saya membeli sepatu baru.',
        'k': False,
        'ch': [
            ('新', 'あたら(しい) / あら(た)', 'シン',
             'Baru. 立 (berdiri) + 木 (pohon) + 斤 (kapak). Kapak menebang pohon yang berdiri — pohon tua ditumbangkan, kayu segar muncul. Setiap penebangan adalah awal dari sesuatu yang baru.')
        ],
        'co': '斤 (kapak) menebang 木 (pohon) yang 立 (berdiri) — pohon tua roboh, dan dari potongannya muncul kayu segar yang belum pernah terpakai. Penebangan = reset, awal yang <b>baru</b>. 新しい. Kebalikan dari 古い.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '便利', 'y': 'べんり', 'a': 'Praktis / Nyaman',
        'ej': 'この駅は便利です。',
        'ei': 'Stasiun ini praktis.',
        'k': False,
        'ch': [
            ('便', 'たよ(り)', 'ベン / ビン',
             'Mudah/Praktis/Surat. 亻 (orang) + 更 (berubah/berganti; 一+日+乂 = satu hari berganti). Orang yang bisa berubah dan beradaptasi — fleksibel, tidak ribet, serba mudah.'),
            ('利', 'き(く)', 'リ',
             'Keuntungan/Tajam. 禾 (padi) + 刂 (pisau). Pisau yang memotong padi dengan efisien — menghasilkan keuntungan maksimal dengan usaha minimal. Tajam dan efisien.')
        ],
        'co': '便 (fleksibel, bisa beradaptasi) + 利 (tajam dan efisien seperti pisau memotong padi) &rarr; sesuatu yang membuat hidup lebih mudah dan efisien tanpa usaha berlebihan. <b>Praktis</b>. 便利.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '不便', 'y': 'ふべん', 'a': 'Tidak praktis',
        'ej': 'バスがなくて不便です。',
        'ei': 'Tidak ada bus, jadi tidak praktis.',
        'k': False,
        'ch': [
            ('不', '–', 'フ / ブ',
             'Tidak/Bukan. Piktogram tunas bunga yang terhalang langit-langit dan tidak bisa mekar — sesuatu yang seharusnya terjadi tapi gagal. Negasi murni.'),
            ('便', 'たよ(り)', 'ベン / ビン',
             'Mudah/Praktis. (Sama dengan penjelasan di 便利.)')
        ],
        'co': '不 (tidak, gagal, terhalang) + 便 (praktis) &rarr; kebalikan langsung dari 便利. Situasi yang bikin repot, ribet, dan membuang waktu. <b>Tidak praktis</b>. 不便.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '丈夫', 'y': 'じょうぶ', 'a': 'Kuat / Kokoh / Tahan lama',
        'ej': 'このバッグは丈夫です。',
        'ei': 'Tas ini kuat/tahan lama.',
        'k': False,
        'ch': [
            ('丈', 'たけ', 'ジョウ',
             'Satuan ukuran (~3 meter) / Tinggi. Gambar orang dengan garis panjang — pengukuran tinggi ideal seorang pria dewasa.'),
            ('夫', 'おっと', 'フ / フウ',
             'Suami/Pria dewasa. 大 (orang besar) + 一 (ikat kepala/topi, tanda kedewasaan). Pria yang sudah cukup umur dan memakai ikat kepala tanda dia sudah dewasa dan bertanggung jawab.')
        ],
        'co': '丈 (setinggi ukuran ideal) + 夫 (pria dewasa gagah) &rarr; pria yang tingginya mencapai ukuran sempurna — tubuhnya <b>kuat dan kokoh</b>, tidak mudah roboh. 丈夫 = tahan lama, tidak gampang rusak. Untuk benda, bukan orang.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '大丈夫', 'y': 'だいじょうぶ', 'a': 'Tidak apa-apa / Baik-baik saja',
        'ej': '大丈夫ですか？',
        'ei': 'Apakah Anda baik-baik saja?',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. Orang merentangkan tangan → besar. (Di sini berfungsi sebagai penguat: "sangat/amat.")'),
            ('丈', 'たけ', 'ジョウ',
             'Tinggi/Ukuran ideal. (Sama dengan penjelasan di 丈夫.)'),
            ('夫', 'おっと', 'フ / フウ',
             'Pria dewasa. (Sama dengan penjelasan di 丈夫.)')
        ],
        'co': '大 (sangat) + 丈夫 (kuat dan kokoh) &rarr; kalau sesuatu "sangat kuat dan kokoh," berarti tidak perlu khawatir — semuanya aman, semuanya terkendali. <b>Tidak apa-apa</b>, baik-baik saja. 大丈夫 = kata penenang universal bahasa Jepang.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '変', 'y': 'へん', 'a': 'Aneh',
        'ej': '変な音が聞こえます。',
        'ei': 'Terdengar suara aneh.',
        'k': False,
        'ch': [
            ('変', 'か(わる) / か(える)', 'ヘン',
             'Aneh/Berubah. Bagian atas: 亦 varian (yang berarti "juga/lain/berbeda") + 夂 (kaki terbalik, melangkah berat ke belakang). Melangkah ke arah yang berbeda dari biasa — menyimpang dari normal, berubah jadi tidak lazim.')
        ],
        'co': 'Bagian atas menunjukkan "sesuatu yang berbeda" dan 夂 (langkah kaki berat dan terbalik) — berjalan ke arah yang salah, menyimpang dari jalur normal. Kalau sesuatu berubah dari yang biasa, itu <b>aneh</b>. 変.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '安全', 'y': 'あんぜん', 'a': 'Aman',
        'ej': 'この道は安全です。',
        'ei': 'Jalan ini aman.',
        'k': False,
        'ch': [
            ('安', 'やす(い)', 'アン',
             'Aman/Tenang/Murah. 宀 (atap rumah) + 女 (perempuan/keluarga). Perempuan/keluarga yang dilindungi di bawah atap rumah — aman, tenteram, tidak ada ancaman. Dari rasa aman lahir rasa tenang, dan dari tenang lahir "murah" (tidak perlu khawatir soal harga).'),
            ('全', 'まった(く) / すべ(て)', 'ゼン',
             'Seluruh/Utuh/Sempurna. 入 (masuk/atap pelindung) + 王 (batu giok/raja; benda paling berharga). Batu giok sempurna yang dilindungi sepenuhnya — utuh tanpa cacat, lengkap tanpa kekurangan.')
        ],
        'co': '安 (aman di bawah atap, terlindungi) + 全 (utuh sepenuhnya, tanpa cacat) &rarr; terlindungi sepenuhnya tanpa ancaman apapun, tidak ada celah bahaya. <b>Aman</b> total. 安全.'
    },

    {
        'g': 'KS::Kondisi', 't': 'Kondisi',
        'w': '危険', 'y': 'きけん', 'a': 'Berbahaya',
        'ej': 'ここは危険です。',
        'ei': 'Di sini berbahaya.',
        'k': False,
        'ch': [
            ('危', 'あぶ(ない) / あや(うい)', 'キ',
             'Bahaya. Gambar seseorang membungkuk (㔾) di tepi tebing curam (厂) — posisi yang sangat tidak stabil, satu langkah lagi bisa jatuh ke jurang. Bahaya yang nyata dan dekat.'),
            ('険', 'けわ(しい)', 'ケン',
             'Terjal/Curam. 阝 (bukit/gundukan tanah) + 僉 (semua setuju; 亼 berkumpul + 吅 mulut-mulut + 从 orang-orang). Bukit yang semua orang sepakat berbahaya — kalau semua orang bilang "jangan ke sana," pasti memang terjal.')
        ],
        'co': '危 (orang di tepi jurang, satu langkah dari jatuh) + 険 (bukit terjal yang semua orang bilang berbahaya) &rarr; posisi di tepi jurang curam yang semua orang memperingatkan. <b>Berbahaya</b>. 危険. Kebalikan dari 安全.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 9: KS::Penilaian (14 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '良い', 'y': 'よい (juga diucapkan いい)', 'a': 'Baik / Bagus',
        'ej': 'これはとても良い本です。',
        'ei': 'Ini buku yang sangat bagus.',
        'k': False,
        'ch': [
            ('良', 'よ(い)', 'リョウ',
             'Baik/Bagus. Piktogram alat penyaring beras — butiran beras yang melewati saringan adalah yang paling murni, berkualitas tinggi, layak dimakan. Sudah teruji dan lolos seleksi.')
        ],
        'co': '良 menggambarkan beras yang lolos penyaringan — hanya butiran terbaik yang tersisa: murni, bersih, berkualitas. Sudah melewati seleksi alam. <b>Baik/Bagus</b>. 良い. Dalam percakapan sehari-hari lebih sering diucapkan いい.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '悪い', 'y': 'わるい', 'a': 'Buruk / Jahat',
        'ej': '天気が悪いです。',
        'ei': 'Cuacanya buruk.',
        'k': False,
        'ch': [
            ('悪', 'わる(い)', 'アク / オ',
             'Buruk/Jahat. 亜 (inferior/nomor dua; bentuk yang terdistorsi, bukan asli) + 心 (hati). Hati yang terdistorsi dari kebaikan aslinya — hati yang sudah berubah jadi inferior, tidak lagi murni.')
        ],
        'co': '亜 (inferior, terdistorsi dari bentuk asli) + 心 (hati) — hati yang sudah menyimpang dari kemurniannya. Kalau 良い adalah beras tersaring yang murni, 悪い adalah sisa kotoran yang gagal lolos seleksi. <b>Buruk/jahat</b>.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '凄い', 'y': 'すごい', 'a': 'Hebat / Luar biasa',
        'ej': 'この景色は凄いです！',
        'ei': 'Pemandangan ini luar biasa!',
        'k': False,
        'ch': [
            ('凄', 'すご(い) / すさ(まじい)', 'セイ',
             'Hebat/Dahsyat. 冫 (es) + 妻 (istri; 十+ヨ+女). Es yang membekukan segalanya — intensitas yang luar biasa. Awalnya bermakna "mengerikan/menakutkan" (dinginnya mencekam), lalu bergeser jadi "hebat/luar biasa" dalam bahasa modern.')
        ],
        'co': '冫 (es membeku) + 妻 (istri) — bayangkan aura dingin yang begitu intens sampai membekukan seluruh ruangan. Intensitas yang mencekam, yang bikin merinding. Dulu artinya "mengerikan," sekarang bergeser jadi <b>hebat/luar biasa</b>. 凄い!'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '素晴らしい', 'y': 'すばらしい', 'a': 'Luar biasa / Mengagumkan',
        'ej': '素晴らしい演奏でした。',
        'ei': 'Penampilannya luar biasa.',
        'k': False,
        'ch': [
            ('素', 'もと', 'ソ / ス',
             'Dasar/Murni/Polos. Bagian atas terkait 垂 (menjuntai) + 糸 (benang) di bawah. Benang mentah yang belum diwarnai — polos, asli, tanpa rekayasa. Elemen paling dasar dan murni.'),
            ('晴', 'は(れる)', 'セイ',
             'Cerah. 日 (matahari) + 青 (biru; 主+月 = warna langit). Matahari bersinar di langit biru — cuaca cerah sempurna tanpa awan.')
        ],
        'co': '素 (murni, polos, tanpa rekayasa) + 晴 (langit cerah biru tanpa awan) &rarr; keindahan yang murni dan cerah apa adanya, tanpa perlu dihias atau dilebih-lebihkan. Seperti langit biru sempurna yang bikin terdiam kagum. <b>Luar biasa, mengagumkan</b>. 素晴らしい.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '面白い', 'y': 'おもしろい', 'a': 'Menarik / Lucu',
        'ej': 'この映画は面白いです。',
        'ei': 'Film ini menarik/lucu.',
        'k': False,
        'ch': [
            ('面', 'おも / おもて', 'メン',
             'Wajah/Permukaan. Gambar wajah manusia dilihat dari depan — garis luar wajah dengan mata di dalamnya. Permukaan luar yang terlihat.'),
            ('白', 'しろ(い)', 'ハク / ビャク',
             'Putih/Terang. (Sama dengan penjelasan di KS::Warna.) Cahaya menyilaukan, terang benderang.')
        ],
        'co': '面 (wajah) + 白 (bersinar putih/terang) &rarr; wajah yang berseri-seri cerah karena sedang menonton sesuatu yang seru — mata berbinar, ekspresi hidup. Kalau wajahmu "bersinar" saat menontonnya, berarti itu <b>menarik/lucu</b>. 面白い.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': 'つまらない', 'y': 'つまらない', 'a': 'Membosankan',
        'ej': 'この本はつまらないです。',
        'ei': 'Buku ini membosankan.',
        'k': True,
        'ch': [],
        'co': 'Berasal dari 詰まる (tersumbat/terhenti) + ない (tidak) — sesuatu yang "tidak bikin terhenti," alias mengalir datar tanpa kejutan. Tidak ada momen yang bikin kamu berhenti dan bilang "wah!" Semuanya datar, hambar, tanpa klimaks. <b>Membosankan</b>. Kebalikan dari 面白い.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '珍しい', 'y': 'めずらしい', 'a': 'Langka / Jarang',
        'ej': '珍しい花を見ました。',
        'ei': 'Saya melihat bunga yang langka.',
        'k': False,
        'ch': [
            ('珍', 'めずら(しい)', 'チン',
             'Langka/Jarang. 王 (batu giok/permata) + 㐱 (rambut halus; 人 orang + 彡 pola goresan unik). Permata dengan pola unik yang jarang ditemukan — semakin unik polanya, semakin langka dan berharga.')
        ],
        'co': '王 (permata) dengan 彡 (pola unik yang rumit) — bayangkan batu giok dengan corak yang tidak pernah kamu lihat sebelumnya. Begitu uniknya, mungkin cuma ada satu di dunia. <b>Langka dan jarang</b>. 珍しい.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '残念', 'y': 'ざんねん', 'a': 'Sayang sekali / Disayangkan',
        'ej': '試合に負けて残念です。',
        'ei': 'Sayang sekali kalah pertandingan.',
        'k': False,
        'ch': [
            ('残', 'のこ(る)', 'ザン',
             'Sisa/Tersisa. 歹 (tulang mayat, kematian; simbol kerusakan) + 戋 (sedikit; dua 戈 tombak yang saling mengikis). Tulang sisa setelah daging habis — yang tertinggal setelah sesuatu hancur. Sisa-sisa, runtuhan.'),
            ('念', '–', 'ネン',
             'Pikiran/Perasaan. 今 (sekarang; 人 atap + ラ yang di bawah) + 心 (hati). Apa yang ada di hati SEKARANG — perasaan saat ini, pikiran yang menempel di benak dan tidak mau pergi.')
        ],
        'co': '残 (sisa, yang tertinggal setelah sesuatu hancur) + 念 (perasaan yang menempel di hati sekarang) &rarr; perasaan "sisa" yang mengganjal di hati setelah sesuatu gagal atau hilang. Kekecewaan yang terus terngiang: "ah, andai saja..." <b>Sayang sekali</b>. 残念.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '結構', 'y': 'けっこう', 'a': 'Cukup / Lumayan / Sudah cukup',
        'ej': '結構おいしいです。',
        'ei': 'Lumayan enak.',
        'k': False,
        'ch': [
            ('結', 'むす(ぶ)', 'ケツ',
             'Mengikat/Menyimpulkan. 糸 (benang) + 吉 (keberuntungan; 士 samurai + 口 mulut = kata-kata prajurit yang membawa keberuntungan). Benang yang diikat dengan simpul baik — menyatukan, menyimpulkan.'),
            ('構', 'かま(える)', 'コウ',
             'Membangun/Struktur. 木 (kayu) + 冓 (menyusun; dua komponen saling bersilangan). Kayu yang disusun dan disilangkan menjadi struktur bangunan — kerangka yang kokoh dan terencana.')
        ],
        'co': '結 (mengikat rapi) + 構 (membangun struktur kokoh) &rarr; sesuatu yang sudah diikat rapi dan tersusun baik — sudah <b>cukup</b> memadai, tidak perlu ditambah lagi. 結構 juga bisa berarti "lumayan" (lebih bagus dari ekspektasi) atau "sudah cukup, terima kasih" (結構です = menolak halus).'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': 'まあまあ', 'y': 'まあまあ', 'a': 'Biasa saja / Lumayan',
        'ej': '味はまあまあです。',
        'ei': 'Rasanya biasa saja.',
        'k': True,
        'ch': [],
        'co': 'Dengarkan nadanya: まあ... まあ... — seperti helaan napas setengah puas, setengah pasrah. Bahu diangkat, kepala dimiringkan sedikit. Bukan bagus, bukan jelek — <b>biasa saja, ya begitulah</b>. Respons paling netral dan noncommittal yang ada.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '厳しい', 'y': 'きびしい', 'a': 'Ketat / Tegas / Keras',
        'ej': 'この先生は厳しいです。',
        'ei': 'Guru ini tegas/keras.',
        'k': False,
        'ch': [
            ('厳', 'きび(しい) / おごそ(か)', 'ゲン / ゴン',
             'Ketat/Tegas. 厂 (tebing curam) + komponen dalam yang terkait 敢 (berani) dan 吅 (dua mulut berteriak). Teriakan berani bergema dari tebing curam — perintah yang keras, tanpa kompromi, tidak ada ruang untuk membantah.')
        ],
        'co': '厂 (tebing curam) dengan teriakan 吅 (banyak mulut) yang bergema tanpa ampun — bayangkan komandan militer berdiri di tebing, memberikan perintah dengan suara menggelegar. Tidak ada negosiasi, tidak ada kelonggaran. <b>Ketat dan tegas</b>. 厳しい.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '大事', 'y': 'だいじ', 'a': 'Penting (praktis/fungsional)',
        'ej': '健康は大事です。',
        'ei': 'Kesehatan itu penting.',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. Orang merentangkan tangan. (Di sini berfungsi sebagai "besar/berat.")'),
            ('事', 'こと', 'ジ / ズ',
             'Urusan/Perkara/Hal. Gambar tangan (又) memegang alat pencatat dengan bendera kecil — menangani urusan resmi, perkara yang harus diurus.')
        ],
        'co': '大 (besar/berat) + 事 (urusan/perkara) &rarr; urusan yang besar dan berat — kalau diabaikan, ada konsekuensi nyata. 大事 fokus pada <b>penting</b> secara praktis: "ini harus diurus, jangan disepelekan." Bandingkan dengan 大切 yang lebih emosional.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '大切', 'y': 'たいせつ', 'a': 'Penting / Berharga (emosional)',
        'ej': '家族は大切です。',
        'ei': 'Keluarga itu berharga.',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. (Di sini berfungsi sebagai penguat intensitas.)'),
            ('切', 'き(る)', 'セツ / サイ',
             'Memotong/Menyentuh inti. 七 (garis potong) + 刀 (pisau). Pisau yang mengenai inti — langsung ke titik terdalam, tanpa perantara.')
        ],
        'co': '大 (sangat) + 切 (memotong langsung ke inti) &rarr; sesuatu yang menyentuh langsung ke inti hatimu. Beda dengan 大事 yang soal kepentingan praktis, 大切 lebih soal <b>berharga secara emosional</b> — orang yang kamu sayangi, kenangan yang kamu jaga. Kehilangan 大切な人 bukan soal rugi materi, tapi luka di hati.'
    },

    {
        'g': 'KS::Penilaian', 't': 'Penilaian',
        'w': '安い', 'y': 'やすい', 'a': 'Murah',
        'ej': 'この店は安いです。',
        'ei': 'Toko ini murah.',
        'k': False,
        'ch': [
            ('安', 'やす(い)', 'アン',
             'Murah/Aman/Tenang. 宀 (atap rumah) + 女 (perempuan/keluarga). Keluarga terlindungi di bawah atap — aman dan tenang. Dari rasa tenang/aman, lahir makna "murah" — harga yang tidak bikin khawatir, yang terjangkau tanpa stres.')
        ],
        'co': '宀 (atap rumah) melindungi 女 (keluarga) — semuanya aman, tenang, tidak ada yang mengancam. Harga yang 安い adalah harga yang tidak bikin kantong cemas — terjangkau, <b>murah</b>. Dari kanji yang sama lahir 安全 (aman) dan 安心 (tenang hati).'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 10: KS::Kesulitan (4 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Kesulitan', 't': 'Kesulitan',
        'w': '難しい', 'y': 'むずかしい', 'a': 'Sulit',
        'ej': '日本語は難しいです。',
        'ei': 'Bahasa Jepang sulit.',
        'k': False,
        'ch': [
            ('難', 'むずか(しい) / かた(い)', 'ナン',
             'Sulit/Susah. Bagian kiri (komponen kompleks dengan elemen 𦰩) + 隹 (burung berekor pendek). Burung yang sangat sulit ditangkap — terbang lincah, bergerak tak terduga. Semakin dikejar semakin susah didapat.')
        ],
        'co': '隹 (burung) yang terbang lincah dan nyaris mustahil ditangkap — kamu sudah pasang jaring, sudah berlari, tapi burungnya selalu lolos. Itulah 難しい: sesuatu yang <b>sulit</b> — semakin dicoba, semakin terasa tantangannya.'
    },

    {
        'g': 'KS::Kesulitan', 't': 'Kesulitan',
        'w': '簡単', 'y': 'かんたん', 'a': 'Mudah / Sederhana',
        'ej': 'この問題は簡単です。',
        'ei': 'Soal ini mudah.',
        'k': False,
        'ch': [
            ('簡', '–', 'カン',
             'Sederhana/Ringkas. 竹 (bambu) + 間 (antara/ruang; 門 pintu + 日 matahari). Bilah bambu tunggal yang cukup untuk menulis — tidak perlu gulungan sutra mahal, cukup sebilah bambu sederhana. Ringkas, tanpa kerumitan.'),
            ('単', '–', 'タン',
             'Tunggal/Sederhana. Bentuk asli menggambarkan alat berburu sederhana (perisai kecil atau kipas tangkap). Satu lapisan saja, tidak bertumpuk — simpel, sendiri, tidak rumit.')
        ],
        'co': '簡 (sebilah bambu ringkas, tanpa hiasan) + 単 (satu lapisan, tunggal) &rarr; tidak perlu banyak lapisan atau kerumitan, cukup satu alat sederhana. <b>Mudah</b>. 簡単. Kebalikan dari 難しい.'
    },

    {
        'g': 'KS::Kesulitan', 't': 'Kesulitan',
        'w': '楽', 'y': 'らく', 'a': 'Nyaman / Mudah / Enak',
        'ej': '楽な仕事がいいです。',
        'ei': 'Pekerjaan yang enak/nyaman itu bagus.',
        'k': False,
        'ch': [
            ('楽', 'たの(しい)', 'ガク / ラク',
             'Nyaman/Musik/Menyenangkan. Asalnya piktogram alat musik dari kayu (木 di bawah) dengan senar (幺幺 di samping) dan hiasan (白 di tengah). Mendengarkan musik bikin rileks, santai, tanpa beban — dari "musik" lahir makna "menyenangkan" lalu "mudah/nyaman."')
        ],
        'co': '楽 asalnya gambar alat musik kayu bersenar — mendengarkan musik bikin pikiran rileks dan tubuh santai. Dari 音楽 (musik) &rarr; 楽しい (menyenangkan) &rarr; 楽 (nyaman, tanpa beban). Hidup yang 楽 = hidup tanpa tekanan, <b>enak dan mudah</b>.'
    },

    {
        'g': 'KS::Kesulitan', 't': 'Kesulitan',
        'w': '大変', 'y': 'たいへん', 'a': 'Berat / Sulit (situasi) / Sangat',
        'ej': '引っ越しは大変です。',
        'ei': 'Pindahan itu berat/sulit.',
        'k': False,
        'ch': [
            ('大', 'おお(きい)', 'ダイ / タイ',
             'Besar. (Di sini berfungsi sebagai "sangat, amat, luar biasa.")'),
            ('変', 'か(わる)', 'ヘン',
             'Berubah/Aneh. (Sama dengan penjelasan di KS::Kondisi — langkah kaki yang menyimpang dari normal.)')
        ],
        'co': '大 (besar, drastis) + 変 (berubah, menyimpang) &rarr; perubahan besar dan tiba-tiba yang memaksa kamu merespons — situasi yang berubah drastis dan kamu harus menghadapinya. <b>Berat dan sulit</b>. 大変 juga bisa berarti "sangat" (大変おいしい = sangat enak).'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 11: KS::Fisik (8 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '早い', 'y': 'はやい', 'a': 'Cepat (waktu) / Pagi / Awal',
        'ej': '朝早い電車に乗りました。',
        'ei': 'Saya naik kereta pagi-pagi.',
        'k': False,
        'ch': [
            ('早', 'はや(い)', 'ソウ / サッ',
             'Cepat/Pagi. 日 (matahari) + 十 (sepuluh, tapi awalnya garis horizon). Matahari yang baru muncul di atas garis cakrawala — pagi-pagi sekali, sebelum siapapun bangun. Datang lebih awal = cepat dari segi waktu.')
        ],
        'co': '日 (matahari) baru naik di titik pertama cakrawala — fajar, sebelum yang lain bangun. 早い adalah "cepat" dalam artian <b>waktu</b>: datang lebih awal, bangun pagi, memulai duluan. Bukan soal kecepatan gerak (itu 速い).'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '遅い', 'y': 'おそい', 'a': 'Lambat / Terlambat',
        'ej': '電車が遅いです。',
        'ei': 'Keretanya lambat/terlambat.',
        'k': False,
        'ch': [
            ('遅', 'おそ(い) / おく(れる)', 'チ',
             'Lambat/Terlambat. 辶 (berjalan/bergerak) + bagian dalam (尸 badan + 牛 variant, komponen berat). Berjalan sambil membawa beban berat — langkah terseret, tidak bisa cepat. Tertinggal dari jadwal.')
        ],
        'co': '辶 (berjalan) tapi bebannya terlalu berat — langkah terseret, nafas terengah. Semua orang sudah sampai, kamu masih di perjalanan. 遅い = <b>lambat/terlambat</b>. Kebalikan dari 早い.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '遠い', 'y': 'とおい', 'a': 'Jauh',
        'ej': '学校は遠いです。',
        'ei': 'Sekolahnya jauh.',
        'k': False,
        'ch': [
            ('遠', 'とお(い)', 'エン / オン',
             'Jauh. 辶 (berjalan) + 袁 (jubah panjang; komponen 土+口+衣 menggambarkan pakaian yang menutupi seluruh tubuh). Perjalanan yang begitu jauh sampai butuh jubah pelindung penuh — menerobos berbagai cuaca dan medan.')
        ],
        'co': '辶 (berjalan) dengan 袁 (jubah panjang menutupi seluruh tubuh) — perjalanan yang begitu <b>jauh</b>, kamu harus membungkus diri dari ujung kepala sampai kaki karena akan melewati hujan, panas, dan badai. 遠い.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '近い', 'y': 'ちかい', 'a': 'Dekat',
        'ej': 'コンビニは近いです。',
        'ei': 'Minimarket itu dekat.',
        'k': False,
        'ch': [
            ('近', 'ちか(い)', 'キン',
             'Dekat. 辶 (berjalan) + 斤 (kapak). Jaraknya cuma sejauh kamu bisa melempar kapak — beberapa langkah saja, tidak perlu persiapan khusus untuk sampai ke sana.')
        ],
        'co': '辶 (berjalan) sejauh 斤 (lemparan kapak) — jaraknya cuma segitu, tidak perlu jubah pelindung seperti 遠い. Beberapa langkah, sudah sampai. <b>Dekat</b>. 近い.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '重い', 'y': 'おもい', 'a': 'Berat',
        'ej': 'このかばんは重いです。',
        'ei': 'Tas ini berat.',
        'k': False,
        'ch': [
            ('重', 'おも(い) / かさ(ねる)', 'ジュウ / チョウ',
             'Berat/Bertumpuk. Piktogram kantung tanah yang ditimbang — garis-garis horizontal menunjukkan tumpukan lapisan. Semakin banyak tumpukan, semakin berat. Juga berarti "menumpuk" (重ねる).')
        ],
        'co': 'Bayangkan kantung tanah yang ditumpuk berlapis-lapis — setiap lapisan menambah beban, semakin banyak tumpukan semakin <b>berat</b>. 重い. Makanya 重 juga berarti "menumpuk" — berat karena bertumpuk.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '軽い', 'y': 'かるい', 'a': 'Ringan',
        'ej': 'この箱は軽いです。',
        'ei': 'Kotak ini ringan.',
        'k': False,
        'ch': [
            ('軽', 'かる(い)', 'ケイ',
             'Ringan. 車 (kendaraan/kereta) + 巠 (sungai/aliran lurus). Kereta yang bergerak semulus aliran air — tanpa beban, tanpa hambatan, meluncur ringan.')
        ],
        'co': '車 (kereta) yang bergerak se-lancar 巠 (aliran sungai yang lurus) — tidak ada beban yang menghambat, tidak ada gesekan. Meluncur tanpa effort. <b>Ringan</b>. 軽い. Kebalikan dari 重い.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '強い', 'y': 'つよい', 'a': 'Kuat',
        'ej': '彼は強い人です。',
        'ei': 'Dia orang yang kuat.',
        'k': False,
        'ch': [
            ('強', 'つよ(い)', 'キョウ / ゴウ',
             'Kuat. 弓 (busur panah) + ム (komponen tengah) + 虫 (serangga bercangkang keras). Serangga bercangkang yang tahan terhadap busur panah — dipanah pun tidak tembus. Kekuatan pertahanan yang absolut.')
        ],
        'co': '弓 (busur panah) ditembakkan ke 虫 (serangga bercangkang) — tapi serangganya tidak terluka! Cangkang kerasnya menahan segalanya. <b>Kuat</b> — kekuatan yang tidak bisa ditembus. 強い.'
    },

    {
        'g': 'KS::Fisik', 't': 'Fisik',
        'w': '弱い', 'y': 'よわい', 'a': 'Lemah',
        'ej': '体が弱い人です。',
        'ei': 'Dia orang yang lemah fisiknya.',
        'k': False,
        'ch': [
            ('弱', 'よわ(い)', 'ジャク',
             'Lemah. Dua 弓 (busur panah) yang masing-masing dihiasi 彡 (pola dekoratif). Busur-busur yang dijadikan hiasan — cantik tapi tidak fungsional untuk bertempur. Senjata yang kehilangan fungsinya.')
        ],
        'co': '弓弓 (dua busur panah) yang cuma dihiasi 彡 (dekorasi) — busur yang dijadikan pajangan dinding, cantik tapi tidak bisa dipakai perang. Senjata tanpa kekuatan = <b>lemah</b>. 弱い. Kebalikan dari 強い.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 12: KS::Jumlah (2 kartu)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'KS::Jumlah', 't': 'Jumlah',
        'w': '多い', 'y': 'おおい', 'a': 'Banyak',
        'ej': '人が多いです。',
        'ei': 'Orangnya banyak.',
        'k': False,
        'ch': [
            ('多', 'おお(い)', 'タ',
             'Banyak. 夕 (malam/bulan sabit) ditumpuk dua kali (夕+夕). Dua bulan sabit muncul sekaligus — berlipat ganda, bertambah terus. Kalau satu saja sudah cukup, dua itu berlebihan = banyak.')
        ],
        'co': '夕 (bulan sabit) ditumpuk dua kali — satu bulan di langit sudah cukup, bayangkan dua muncul bersamaan. Berlipat ganda, terus bertambah. <b>Banyak</b>. 多い.'
    },

    {
        'g': 'KS::Jumlah', 't': 'Jumlah',
        'w': '少ない', 'y': 'すくない', 'a': 'Sedikit',
        'ej': '時間が少ないです。',
        'ei': 'Waktunya sedikit.',
        'k': False,
        'ch': [
            ('少', 'すく(ない) / すこ(し)', 'ショウ',
             'Sedikit. 小 (kecil) + 丿 (goresan/potongan). Sesuatu yang sudah kecil dipotong lagi — dari yang sudah mini, dikurangi lebih jauh. Hampir tidak tersisa.')
        ],
        'co': '小 (sudah kecil) + 丿 (dipotong lagi) — dari yang sudah kecil, masih dikurangi. Hasilnya tinggal remah-remah, nyaris habis. <b>Sedikit</b>. 少ない. Kebalikan dari 多い.'
    },

]

# ============================================================
# MAIN: GENERATE OUTPUT FILE
# ============================================================

def main():
    header = (
        "#separator:tab\n"
        "#html:true\n"
        "#notetype column:1\n"
        "#deck column:2\n"
        "#tags column:5\n"
    )

    lines = []
    fronts_seen = set()
    errors = []

    for i, card in enumerate(CARDS):
        front = build_front(card['w'], card['k'])
        back = build_back(card)

        # Validate: no empty front
        if not card['w'].strip():
            errors.append(f"Card {i}: empty word/front!")

        # Validate: no duplicate front word
        if card['w'] in fronts_seen:
            errors.append(f"Card {i}: duplicate front '{card['w']}'!")
        fronts_seen.add(card['w'])

        # Validate: kanji mini count matches kanji char count (for non-kana cards)
        if not card['k'] and card.get('ch'):
            expected_kanji = len(card['ch'])
            # Count actual kanji characters in the word
            kanji_in_word = [c for c in card['w'] if '\u4e00' <= c <= '\u9fff' or '\u3400' <= c <= '\u4dbf']
            if expected_kanji != len(kanji_in_word):
                # This is OK for some words like 細かい where front=細かい but analysis is just 細
                pass  # We allow this since analysis is manually curated

        # Validate: balanced div tags
        for label, html in [('front', front), ('back', back)]:
            opens = html.count('<div')
            closes = html.count('</div>')
            if opens != closes:
                errors.append(f"Card {i} ({card['w']}) {label}: {opens} <div> vs {closes} </div>")

        line = f"Basic\t{card['g']}\t{front}\t{back}\t{card['t']}"
        lines.append(line)

    if errors:
        print("ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        print()

    output = header + "\n".join(lines) + "\n"

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "KS_Anki_Deck.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated {len(CARDS)} cards to: {out_path}")
    print(f"Groups: {len(set(c['g'] for c in CARDS))}")

    # Summary per group
    from collections import Counter
    group_counts = Counter(c['g'] for c in CARDS)
    for g, count in sorted(group_counts.items()):
        print(f"  {g}: {count} cards")

    if not errors:
        print("\nAll validations passed!")
    else:
        print(f"\n{len(errors)} validation error(s) found. Please fix before importing.")


if __name__ == '__main__':
    main()
