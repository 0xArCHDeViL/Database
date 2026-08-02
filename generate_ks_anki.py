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
            ('暑', 'あつ(い)', 'ショ', '[Radikal: 日 (Matahari)] + [Komponen: 者 (Seseorang)]')
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
            ('熱', 'あつ(い)', 'ネツ', '[Radikal: 灬 (Api)] + [Komponen: 埶 (Menanam/Seni)]')
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
            ('寒', 'さむ(い)', 'カン', '[Radikal: 宀 (Atap)] + [Komponen: 井 (Sumur) + 八 (Delapan) + 冫 (Es)]')
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
            ('冷', 'つめ(たい) / ひ(える)', 'レイ', '[Radikal: 冫 (Es)] + [Komponen: 令 (Perintah)]')
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
            ('涼', 'すず(しい)', 'リョウ', '[Radikal: 氵 (Air)] + [Komponen: 京 (Ibukota)]')
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
            ('暖', 'あたた(かい) / あたた(める)', 'ダン', '[Radikal: 日 (Matahari)] + [Komponen: 爰 (Menarik)]')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]')
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
            ('小', 'ちい(さい) / こ / お', 'ショウ', '[Radikal: 小 (Kecil/Tiga titik)]')
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
            ('小', 'ちい(さい) / こ / お', 'ショウ', '[Radikal: 小 (Kecil/Tiga titik)]')
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
            ('長', 'なが(い)', 'チョウ', '[Radikal: 長 (Panjang/Rambut panjang)]')
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
            ('短', 'みじか(い)', 'タン', '[Radikal: 矢 (Anak panah)] + [Komponen: 豆 (Kacang)]')
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
            ('高', 'たか(い)', 'コウ', '[Radikal: 高 (Tinggi/Menara)]')
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
            ('低', 'ひく(い)', 'テイ', '[Radikal: 亻 (Orang)] + [Komponen: 氐 (Akar/Dasar)]')
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
            ('広', 'ひろ(い)', 'コウ', '[Radikal: 广 (Rumah/Tebing)] + [Komponen: ム (Pribadi)]')
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
            ('狭', 'せま(い)', 'キョウ', '[Radikal: 犭 (Anjing/Binatang buas)] + [Komponen: 夾 (Menjepit)]')
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
            ('太', 'ふと(い)', 'タイ / タ', '[Radikal: 大 (Besar)] + [Komponen: 丶 (Titik)]')
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
            ('細', 'ほそ(い) / こま(かい)', 'サイ', '[Radikal: 糸 (Benang)] + [Komponen: 田 (Sawah)]')
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
            ('甘', 'あま(い)', 'カン', '[Radikal: 甘 (Manis)]')
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
            ('辛', 'から(い) / つら(い)', 'シン', '[Radikal: 辛 (Pedas/Pahit)]')
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
            ('苦', 'にが(い) / くる(しい)', 'ク', '[Radikal: 艹 (Rumput)] + [Komponen: 古 (Tua)]')
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
            ('美', 'うつく(しい)', 'ビ', '[Radikal: 美]'),
            ('味', 'あじ', 'ミ', '[Radikal: 口 (Mulut)] + [Komponen: 未 (Belum)]')
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
            ('不', '–', 'フ / ブ', '[Radikal: 不]'),
            ('味', 'あじ', 'ミ', '[Radikal: 口 (Mulut)] + [Komponen: 未 (Belum)]')
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
            ('濃', 'こ(い)', 'ノウ', '[Radikal: 氵 (Air)] + [Komponen: 農 (Pertanian)]')
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
            ('固', 'かた(い) / かた(める)', 'コ', '[Radikal: 囗 (Batas/Kotak)] + [Komponen: 古 (Tua)]')
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
            ('柔', 'やわ(らかい)', 'ジュウ / ニュウ', '[Radikal: 木 (Pohon)] + [Komponen: 矛 (Tombak)]')
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
            ('薄', 'うす(い)', 'ハク', '[Radikal: 艹 (Rumput)] + [Komponen: 溥 (Luas)]')
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
            ('厚', 'あつ(い)', 'コウ', '[Radikal: 厂 (Tebing)] + [Komponen: 日 (Matahari) + 子 (Anak)]')
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
            ('細', 'こま(かい) / ほそ(い)', 'サイ', '[Radikal: 糸 (Benang)] + [Komponen: 田 (Sawah)]')
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
            ('丸', 'まる(い)', 'ガン', '[Radikal: 丶 (Titik)] + [Komponen: 九 (Sembilan)]')
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
            ('赤', 'あか(い)', 'セキ / シャク', '[Radikal: 赤 (Merah)]')
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
            ('黒', 'くろ(い)', 'コク', '[Radikal: 黒 (Hitam)]')
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
            ('白', 'しろ(い)', 'ハク / ビャク', '[Radikal: 白 (Putih)]')
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
            ('好', 'す(き) / この(む)', 'コウ', '[Radikal: 女 (Perempuan)] + [Komponen: 子 (Anak)]')
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
            ('嫌', 'きら(い) / いや', 'ケン / ゲン', '[Radikal: 女 (Perempuan)] + [Komponen: 兼 (Merangkap)]')
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
            ('欲', 'ほ(しい)', 'ヨク', '[Radikal: 欠 (Menguap)] + [Komponen: 谷 (Lembah)]')
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
            ('怖', 'こわ(い)', 'フ', '[Radikal: 忄 (Hati)] + [Komponen: 布 (Kain)]')
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
            ('痛', 'いた(い)', 'ツウ', '[Radikal: 疒 (Sakit)] + [Komponen: 甬 (Terowongan)]')
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
            ('寂', 'さび(しい) / さみ(しい)', 'セキ / ジャク', '[Radikal: 宀 (Atap)] + [Komponen: 叔 (Paman/Muda)]')
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
            ('怠', 'おこた(る) / だる(い)', 'タイ', '[Radikal: 心 (Hati)] + [Komponen: 台 (Mimbar)]')
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
            ('嬉', 'うれ(しい)', 'キ', '[Radikal: 女 (Perempuan)] + [Komponen: 喜 (Gembira)]')
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
            ('悲', 'かな(しい)', 'ヒ', '[Radikal: 心 (Hati)] + [Komponen: 非 (Salah/Tidak)]')
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
            ('馬', 'うま', 'バ', '[Radikal: 馬 (Kuda)]'),
            ('鹿', 'しか', 'ロク', '[Radikal: 鹿 (Rusa)]')
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
            ('元', 'もと', 'ゲン / ガン', '[Radikal: 儿 (Kaki manusia)] + [Komponen: 二 (Dua)]'),
            ('気', '–', 'キ / ケ', '[Radikal: 气 (Udara)] + [Komponen: 乂 (Menyilang)]')
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
            ('優', 'やさ(しい) / すぐ(れる)', 'ユウ', '[Radikal: 亻 (Orang)] + [Komponen: 憂 (Khawatir)]')
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
            ('親', 'おや / した(しい)', 'シン', '[Radikal: 見 (Melihat)] + [Komponen: 亲 (Berdiri di pohon)]'),
            ('切', 'き(る)', 'セツ / サイ', '[Radikal: 刀 (Pisau)] + [Komponen: 七 (Tujuh)]')
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
            ('我', 'われ / わ', 'ガ', '[Radikal: 戈 (Tombak)] + [Komponen: 手 (Tangan)]'),
            ('儘', 'まま', 'ジン', '[Radikal: 亻 (Orang)] + [Komponen: 盡 (Habis)]')
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
            ('可', '–', 'カ', '[Radikal: 可]'),
            ('愛', 'いと(しい)', 'アイ', '[Radikal: 心 (Hati)] + [Komponen: 夊 (Berjalan lambat)]')
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
            ('賑', 'にぎ(わう)', 'シン', '[Radikal: 貝 (Harta)] + [Komponen: 辰 (Naga)]')
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
            ('静', 'しず(か)', 'セイ / ジョウ', '[Radikal: 青 (Biru)] + [Komponen: 争 (Konflik)]')
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
            ('暗', 'くら(い)', 'アン', '[Radikal: 日 (Matahari)] + [Komponen: 音 (Suara)]')
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
            ('明', 'あか(るい) / あき(らか)', 'メイ / ミョウ', '[Radikal: 日 (Matahari)] + [Komponen: 月 (Bulan)]')
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
            ('汚', 'きたな(い) / よご(れる)', 'オ', '[Radikal: 汚]')
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
            ('綺', '–', 'キ', '[Radikal: 糸 (Benang)] + [Komponen: 奇 (Aneh/Unik)]'),
            ('麗', 'うるわ(しい)', 'レイ', '[Radikal: 鹿 (Rusa)] + [Komponen: 丽 (Indah)]')
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
            ('忙', 'いそが(しい)', 'ボウ', '[Radikal: 忄 (Hati)] + [Komponen: 亡 (Meninggal/Hilang)]')
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
            ('古', 'ふる(い)', 'コ', '[Radikal: 口 (Mulut)] + [Komponen: 十 (Sepuluh)]')
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
            ('新', 'あたら(しい) / あら(た)', 'シン', '[Radikal: 斤 (Kapak)] + [Komponen: 亲 (Berdiri di atas pohon)]')
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
            ('便', 'たよ(り)', 'ベン / ビン', '[Radikal: 亻 (Orang)] + [Komponen: 更 (Berubah)]'),
            ('利', 'き(く)', 'リ', '[Radikal: 刂 (Pisau)] + [Komponen: 禾 (Gandum)]')
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
            ('不', '–', 'フ / ブ', '[Radikal: 不]'),
            ('便', 'たよ(り)', 'ベン / ビン', '[Radikal: 亻 (Orang)] + [Komponen: 更 (Berubah)]')
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
            ('丈', 'たけ', 'ジョウ', '[Radikal: 一 (Satu)] + [Komponen: 大 (Besar/Pria)]'),
            ('夫', 'おっと', 'フ / フウ', '[Radikal: 大 (Besar)] + [Komponen: 一 (Satu)]')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]'),
            ('丈', 'たけ', 'ジョウ', '[Radikal: 一 (Satu)] + [Komponen: 大 (Besar/Pria)]'),
            ('夫', 'おっと', 'フ / フウ', '[Radikal: 大 (Besar)] + [Komponen: 一 (Satu)]')
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
            ('変', 'か(わる) / か(える)', 'ヘン', '[Radikal: 攵 (Memukul)] + [Komponen: 亦 (Berubah)]')
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
            ('安', 'やす(い)', 'アン', '[Radikal: 宀 (Atap)] + [Komponen: 女 (Perempuan)]'),
            ('全', 'まった(く) / すべ(て)', 'ゼン', '[Radikal: 入 (Masuk)] + [Komponen: 王 (Permata)]')
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
            ('危', 'あぶ(ない) / あや(うい)', 'キ', '[Radikal: 卩 (Sendi)] + [Komponen: 厄 (Tebing membahayakan)]'),
            ('険', 'けわ(しい)', 'ケン', '[Radikal: 阝 (Bukit)] + [Komponen: 僉 (Semua)]')
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
            ('良', 'よ(い)', 'リョウ', '[Radikal: 艮 (Berhenti/Bagus)] (Bentuk asal: Makanan murni)')
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
            ('悪', 'わる(い)', 'アク / オ', '[Radikal: 心 (Hati)] + [Komponen: 亜 (Menekan)]')
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
            ('凄', 'すご(い) / すさ(まじい)', 'セイ', '[Radikal: 冫 (Es)] + [Komponen: 妻 (Istri)]')
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
            ('素', 'もと', 'ソ / ス', '[Radikal: 糸 (Benang)] + [Komponen: 垂 (Tergantung)]'),
            ('晴', 'は(れる)', 'セイ', '[Radikal: 日 (Matahari)] + [Komponen: 青 (Biru)]')
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
            ('面', 'おも / おもて', 'メン', '[Radikal: 面 (Wajah)]'),
            ('白', 'しろ(い)', 'ハク / ビャク', '[Radikal: 白 (Putih)]')
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
            ('珍', 'めずら(しい)', 'チン', '[Radikal: 王 (Permata)] + [Komponen: 㐱 (Rambut)]')
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
            ('残', 'のこ(る)', 'ザン', '[Radikal: 歹 (Tulang mati)] + [Komponen: 戋 (Tombak)]'),
            ('念', '–', 'ネン', '[Radikal: 心 (Hati)] + [Komponen: 今 (Sekarang)]')
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
            ('結', 'むす(ぶ)', 'ケツ', '[Radikal: 結]'),
            ('構', 'かま(える)', 'コウ', '[Radikal: 木 (Pohon)] + [Komponen: 冓 (Struktur kayu)]')
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
            ('厳', 'きび(しい) / おごそ(か)', 'ゲン / ゴン', '[Radikal: 口 (Mulut)] + [Komponen: 敢 (Berani)] + 厂 (Tebing)')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]'),
            ('事', 'こと', 'ジ / ズ', '[Radikal: 事]')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]'),
            ('切', 'き(る)', 'セツ / サイ', '[Radikal: 刀 (Pisau)] + [Komponen: 七 (Tujuh)]')
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
            ('安', 'やす(い)', 'アン', '[Radikal: 宀 (Atap)] + [Komponen: 女 (Perempuan)]')
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
            ('難', 'むずか(しい) / かた(い)', 'ナン', '[Radikal: 隹 (Burung)] + [Komponen: 𦰩 (Kuning/Tanah kering)]')
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
            ('簡', '–', 'カン', '[Radikal: 竹 (Bambu)] + [Komponen: 間 (Ruang/Jeda)]'),
            ('単', '–', 'タン', '[Radikal: 十 (Sepuluh)] + [Komponen: 吅 (Mulut) + 甲 (Perisai)]')
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
            ('楽', 'たの(しい)', 'ガク / ラク', '[Radikal: 木 (Pohon)] + [Komponen: 白 (Putih) + 幺 (Benang kecil)]')
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
            ('大', 'おお(きい)', 'ダイ / タイ', '[Radikal: 大 (Besar/Orang merentangkan tangan)]'),
            ('変', 'か(わる)', 'ヘン', '[Radikal: 攵 (Memukul)] + [Komponen: 亦 (Berubah)]')
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
            ('早', 'はや(い)', 'ソウ / サッ', '[Radikal: 日 (Matahari)] + [Komponen: 十 (Jarum/Pohon)]')
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
            ('遅', 'おそ(い) / おく(れる)', 'チ', '[Radikal: 辶 (Jalan)] + [Komponen: 犀 (Badak)]')
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
            ('遠', 'とお(い)', 'エン / オン', '[Radikal: 辶 (Jalan)] + [Komponen: 袁 (Jubah panjang)]')
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
            ('近', 'ちか(い)', 'キン', '[Radikal: 辶 (Jalan)] + [Komponen: 斤 (Kapak)]')
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
            ('重', 'おも(い) / かさ(ねる)', 'ジュウ / チョウ', '[Radikal: 里 (Desa/Satuan)] + [Komponen: 千 (Seribu)]')
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
            ('軽', 'かる(い)', 'ケイ', '[Radikal: 車 (Mobil)] + [Komponen: 巠 (Sungai bawah tanah)]')
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
            ('強', 'つよ(い)', 'キョウ / ゴウ', '[Radikal: 弓 (Busur)] + [Komponen: 虫 (Serangga)]')
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
            ('弱', 'よわ(い)', 'ジャク', '[Radikal: 弓 (Busur)] + [Komponen: 彡 (Bulu/Corak)] x2')
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
            ('多', 'おお(い)', 'タ', '[Radikal: 夕 (Malam) x2]')
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
            ('少', 'すく(ない) / すこ(し)', 'ショウ', '[Radikal: 小 (Kecil)] + [Komponen: 丿 (Coretan)]')
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

        w = card['w']
        g_val = card['g'].replace('KS::', '').replace('EXTKS::', '')
        
        na_exceptions = ['綺麗', 'きれい', '嫌い', 'きらい', '有名', 'ゆうめい', '丁寧', 'ていねい', '丈夫', 'じょうぶ']
        
        if w.endswith('い') and w not in na_exceptions:
            grammatical_group = 'I-Keiyoushi (Akhiran -i)'
        else:
            if w in na_exceptions:
                grammatical_group = 'Na-Keiyoushi (Pengecualian -i)'
            else:
                grammatical_group = 'Na-Keiyoushi (Akhiran -na)'
                
        deck_hierarchy = f"Kata Sifat::{grammatical_group}::{g_val}"
        
        line = f"Basic	{deck_hierarchy}	{front}	{back}	{card['t']}"
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
