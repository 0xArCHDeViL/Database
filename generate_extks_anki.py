# -*- coding: utf-8 -*-
"""
Generator Anki Deck: EXTKS (Kata Sifat N5 & N4 Lengkap)
Generates .txt file ready for Anki import.
42 kartu, semantic subdecks.
"""

import sys
import os

# ============================================================
# CSS CONSTANTS (Sama dengan KS_Anki_Deck)
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
        parts.append(f'<div class="label">Yomikata</div>')
        parts.append(f'<div class="yomi">{card["y"]}</div>')

    parts.append(f'<div class="arti">{card["a"]}</div>')

    parts.append(
        f'<div class="kalimat">'
        f'<div class="label">Contoh Kalimat</div>'
        f'<div class="jp">{card["ej"]}</div>'
        f'<div class="id">{card["ei"]}</div>'
        f'</div>'
    )

    if not card['k'] and card.get('ch'):
        minis = ''.join(build_kanji_mini(c, ku, on, m) for c, ku, on, m in card['ch'])
        parts.append(
            f'<div class="analisis-box">'
            f'<div class="analisis-title">Analisis</div>'
            f'<div class="kanji-strip">{minis}</div>'
            f'</div>'
        )

    parts.append(
        f'<div class="cocoklogi-box">'
        f'<b>Cocoklogi:</b> {card["co"]}'
        f'</div>'
    )

    parts.append('</div>')
    return ''.join(parts)


# ============================================================
# CARD DATA — EXTKS (42 CARDS)
# ============================================================

CARDS = [

    # ──────────────────────────────────────────────────────────
    # GROUP 1: EXTKS::Warna (3)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Warna', 't': 'Warna',
        'w': '青い', 'y': 'あおい', 'a': 'Biru / Hijau',
        'ej': '空が青いです。', 'ei': 'Langitnya biru.', 'k': False,
        'ch': [('青', 'あお', 'セイ / ショウ', 'Biru/Hijau. 主 (tuan/utama) + 月 (bulan). Warna utama dari alam (langit, laut, rumput) yang terpantul indah di bawah sinar bulan. Dulu orang Jepang menyebut biru dan hijau dengan kata yang sama: 青 (ao).')],
        'co': 'Warna <b>utama</b> (主) yang menghiasi alam di bawah cahaya <b>bulan</b> (月). Langit yang cerah itu 青い, apel hijau pun disebut 青リンゴ. <b>Biru</b> yang mencakup hijau alam.'
    },
    {
        'g': 'EXTKS::Warna', 't': 'Warna',
        'w': '黄色い', 'y': 'きいろい', 'a': 'Kuning',
        'ej': '黄色いシャツを着ています。', 'ei': 'Saya memakai kemeja kuning.', 'k': False,
        'ch': [('黄', 'き', 'コウ / オウ', 'Kuning. Piktogram manusia (大) yang memakai perhiasan giok/api berkilauan di lehernya. Atau melambangkan ladang tanah subur (tanah liat kuning) di Tiongkok kuno.')],
        'co': 'Bayangkan perhiasan bercahaya yang dikenakan di leher — memancarkan warna keemasan yang terang. Warna tanah panen yang subur, atau warna perhiasan cerah: <b>Kuning</b>.'
    },
    {
        'g': 'EXTKS::Warna', 't': 'Warna',
        'w': '茶色い', 'y': 'ちゃいろい', 'a': 'Cokelat',
        'ej': '犬は茶色いです。', 'ei': 'Anjing itu berwarna cokelat.', 'k': False,
        'ch': [('茶', 'ちゃ / さ', 'チャ', 'Teh. 艹 (tanaman) + 人 (orang) + 木 (pohon). Daun tanaman yang dipetik orang dari semak pohon untuk diseduh menjadi teh.')],
        'co': '艹 (tanaman) yang dipetik 人 (orang) dari pinggir 木 (pohon). Seduhannya menghasilkan warna pekat alami. 茶 (teh) + 色 (warna) = warna air teh alias <b>Cokelat</b>.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 2: EXTKS::Suhu & Rasa (3)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Suhu', 't': 'Suhu',
        'w': '温い', 'y': 'ぬるい', 'a': 'Hangat Kuku / Lukewarm',
        'ej': 'お茶が温くなりました。', 'ei': 'Tehnya menjadi hangat kuku (tidak panas lagi).', 'k': False,
        'ch': [('温', 'あたた(かい) / ぬる(い)', 'オン', 'Hangat/Hangat Kuku. 氵 (air) + 皿 (mangkuk) + 囚 (kurungan). Air di dalam mangkuk tertutup (dikurung) sehingga kehangatannya tertahan.')],
        'co': 'Kalau 暖かい untuk udara, 温かい (あたたかい) untuk suhu benda yang nyaman. Tapi kalau dibaca <b>ぬるい</b>, artinya negatif: minuman yang seharusnya panas atau dingin malah jadi <b>suam-suam kuku</b> alias nanggung.'
    },
    {
        'g': 'EXTKS::Rasa', 't': 'Rasa',
        'w': '酸っぱい', 'y': 'すっぱい', 'a': 'Asam',
        'ej': 'レモンは酸っぱいです。', 'ei': 'Lemon itu asam.', 'k': False,
        'ch': [('酸', 'す(っぱい)', 'サン', 'Asam/Oksigen. 酉 (kendi arak) + 夋 (berjalan pelan/menusuk). Arak di dalam kendi yang dibiarkan terlalu lama sampai mengalami fermentasi ekstra, mengubah rasanya menjadi tajam menusuk lidah.')],
        'co': '酉 (arak) yang sudah kedaluwarsa — alih-alih mabuk, lidahmu malah tertusuk rasa <b>asam</b> cuka yang bikin merem melek. 酸っぱい.'
    },
    {
        'g': 'EXTKS::Rasa', 't': 'Rasa',
        'w': '塩っぱい', 'y': 'しょっぱい', 'a': 'Asin',
        'ej': 'このスープは塩っぱいです。', 'ei': 'Sup ini asin.', 'k': False,
        'ch': [('塩', 'しお', 'エン', 'Garam. 土 (tanah) + 人 (orang) + 鹵 (kristal garam) + 皿 (wadah). Orang yang mengekstrak/memanen kristal garam dari tanah tambak, mengumpulkannya di atas wadah.')],
        'co': 'Ini kata sifat turunan dari 塩 (garam). Ditambah "pai" di belakangnya jadi しょっぱい. Murni mendeskripsikan rasa <b>asin</b> atau bisa kiasan untuk orang yang pelit/kikir.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 3: EXTKS::Ukuran & Kesulitan (3)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Ukuran', 't': 'Ukuran',
        'w': '深い', 'y': 'ふかい', 'a': 'Dalam (air/pemikiran)',
        'ej': 'この川は深いです。', 'ei': 'Sungai ini dalam.', 'k': False,
        'ch': [('深', 'ふか(い)', 'シン', 'Dalam. 氵 (air) + 罙 (mencari/menyelidiki ke dalam lubang gelap). Air yang permukaannya harus diselami jauh ke bawah untuk mencapai dasar.')],
        'co': '氵 (air) yang seolah ada 穴 (lubang) tak berujung di bawahnya. Kamu harus menyelam jauh ke dasar untuk menemukannya. Bukan hanya untuk air, <b>深い</b> juga berlaku untuk pemikiran, makna, atau ikatan yang <b>dalam</b>.'
    },
    {
        'g': 'EXTKS::Ukuran', 't': 'Ukuran',
        'w': '浅い', 'y': 'あさい', 'a': 'Dangkal / Cetek',
        'ej': 'このプールは浅いです。', 'ei': 'Kolam renang ini dangkal.', 'k': False,
        'ch': [('浅', 'あさ(い)', 'セン', 'Dangkal. 氵 (air) + 戔 (kecil/sedikit/sisa, dua buah tombak yang saling mengikis). Air yang hanya tersisa sedikit, ukurannya menciut dari dasarnya.')],
        'co': '氵 (air) yang volumenya terkikis (戔) sehingga cuma tinggal sisa-sisa selutut. <b>Dangkal</b>. Sama seperti 深い, ini bisa dipakai untuk "pemikiran yang dangkal/cetek".'
    },
    {
        'g': 'EXTKS::Kesulitan', 't': 'Kesulitan',
        'w': '易しい', 'y': 'やさしい', 'a': 'Mudah / Gampang',
        'ej': 'このテストは易しいです。', 'ei': 'Ujian ini mudah.', 'k': False,
        'ch': [('易', 'やさ(しい) / か(える)', 'エキ / イ', 'Mudah/Berubah. Piktogram hewan bunglon/kadal yang mudah berubah warna. Atau matahari (日) dengan sinar menyebar (勿). Intinya: Sesuatu yang gampang beradaptasi/diubah.')],
        'co': 'Bacanya sama-sama "yasashii" dengan 優しい (baik hati), tapi 易しい (bunglon yang gampang berubah) artinya <b>mudah/gampang</b> diselesaikan. Kebalikan dari 難しい (sulit).'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 4: EXTKS::Sifat (5)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Sifat', 't': 'Sifat',
        'w': '大人しい', 'y': 'おとなしい', 'a': 'Pendiam / Penurut / Kalem',
        'ej': '彼は大人しい人です。', 'ei': 'Dia orang yang pendiam.', 'k': False,
        'ch': [('大', 'おお(きい)', 'ダイ', 'Besar.'), ('人', 'ひと', 'ジン', 'Orang.')],
        'co': '大人 (Orang Dewasa) + しい (bersifat seperti). Orang yang bertingkah seperti orang dewasa yang matang: tidak pecicilan, tidak berisik, dan tenang. <b>Pendiam / Penurut</b>.'
    },
    {
        'g': 'EXTKS::Sifat', 't': 'Sifat',
        'w': '真面目な', 'y': 'まじめな', 'a': 'Serius / Rajin / Sungguh-sungguh',
        'ej': '彼女は真面目な学生です。', 'ei': 'Dia adalah siswa yang rajin/serius.', 'k': False,
        'ch': [
            ('真', 'ま / まこと', 'シン', 'Kebenaran/Asli. Sesuatu yang lurus dan tidak menyimpang.'),
            ('面', 'おもて', 'メン', 'Wajah/Topeng.'),
            ('目', 'め', 'モク', 'Mata.')
        ],
        'co': '真 (Kebenaran) terpancar di 面 (Wajah) dan 目 (Mata). Raut wajah yang jujur tanpa ada niat bermain-main. Sifat orang yang bekerja tanpa tipu muslihat. <b>Serius / Rajin / Tekun</b>.'
    },
    {
        'g': 'EXTKS::Sifat', 't': 'Sifat',
        'w': '熱心な', 'y': 'ねっしんな', 'a': 'Antusias / Bersemangat / Giat',
        'ej': '彼は仕事に熱心です。', 'ei': 'Dia sangat antusias dengan pekerjaannya.', 'k': False,
        'ch': [
            ('熱', 'あつ(い)', 'ネツ', 'Panas/Demam.'),
            ('心', 'こころ', 'シン', 'Hati/Perasaan.')
        ],
        'co': '熱 (Panas/Api) yang menyala di dalam 心 (Hati). Orang yang mengerjakan sesuatu dengan gairah yang membara, tidak pernah setengah-setengah. <b>Antusias / Giat</b>.'
    },
    {
        'g': 'EXTKS::Sifat', 't': 'Sifat',
        'w': '丁寧な', 'y': 'ていねいな', 'a': 'Sopan / Rapi / Teliti',
        'ej': '丁寧に字を書きます。', 'ei': 'Menulis huruf dengan rapi/teliti.', 'k': False,
        'ch': [
            ('丁', '–', 'テイ', 'Paku/Tepat/Presisi.'),
            ('寧', '–', 'ネイ', 'Tenang/Damai. 宀 (atap) + 心 (hati) + 皿 (wadah piring). Suasana damai dan tenang di dalam rumah.')
        ],
        'co': 'Melakukan segala hal dengan 丁 (tepat, presisi, tanpa meleset) untuk menjaga 寧 (suasana damai dan rukun). Tidak kasar, tutur kata halus, pekerjaan rapi. <b>Sopan dan Teliti</b>.'
    },
    {
        'g': 'EXTKS::Sifat', 't': 'Sifat',
        'w': '親しい', 'y': 'したしい', 'a': 'Akrab / Dekat (Hubungan)',
        'ej': '親しい友達と遊びます。', 'ei': 'Bermain dengan teman akrab.', 'k': False,
        'ch': [('親', 'おや / した(しい)', 'シン', 'Orang tua/Dekat. 立 (berdiri) + 木 (pohon) + 見 (melihat). Mengawasi dari atas pohon seperti orang tua.')],
        'co': 'Dari kanji 親 (orang tua) yang bermakna ikatan batin terkuat. Teman yang 親しい adalah teman yang ikatan emosionalnya sudah sedekat keluarga. <b>Akrab / Intim</b>.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 5: EXTKS::Perasaan (7)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '楽しい', 'y': 'たのしい', 'a': 'Menyenangkan / Seru',
        'ej': 'パーティーは楽しいです。', 'ei': 'Pestanya menyenangkan.', 'k': False,
        'ch': [('楽', 'たの(しい) / らく', 'ガク / ラク', 'Musik/Nyaman/Menyenangkan. Gambar alat musik bersenar dari kayu (木). Mendengarkan musik memberi hiburan bagi jiwa.')],
        'co': 'Berasal dari 音楽 (musik). Suasana di mana ada musik, tawa, dan hiburan tanpa beban. Beda dengan 嬉しい (bahagia karena mendapat sesuatu), 楽しい adalah proses menikmati momen yang <b>seru dan menyenangkan</b>.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '眠い', 'y': 'ねむい', 'a': 'Mengantuk',
        'ej': '夜遅くまで起きていたから眠いです。', 'ei': 'Karena begadang sampai larut malam, saya mengantuk.', 'k': False,
        'ch': [('眠', 'ねむ(い)', 'ミン', 'Tidur/Mengantuk. 目 (mata) + 民 (rakyat; piktogram mata yang ditusuk/buta). Mata yang tertutup rapat, kehilangan penglihatan sementara seperti tidur.')],
        'co': '目 (mata) yang menjadi 民 (gelap/buta sementara). Kelopak mata terasa berat dan menutup perlahan karena lelah. <b>Mengantuk</b>.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '恥ずかしい', 'y': 'はずかしい', 'a': 'Malu / Memalukan',
        'ej': 'みんなの前で話すのは恥ずかしいです。', 'ei': 'Berbicara di depan semua orang itu memalukan/bikin malu.', 'k': False,
        'ch': [('恥', 'はじ / はず(かしい)', 'チ', 'Malu. 耳 (telinga) + 心 (hati). Reaksi tubuh saat merasa malu.')],
        'co': 'Saat kamu berbuat salah di depan umum, 心 (hati) berdebar kencang dan 耳 (telinga) langsung memerah terbakar. Itulah reaksi fisik dari rasa <b>Malu</b>.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '苦しい', 'y': 'くるしい', 'a': 'Menderita / Sesak / Tersiksa',
        'ej': '息が苦しいです。', 'ei': 'Napas terasa sesak/tersiksa.', 'k': False,
        'ch': [('苦', 'にが(い) / くる(しい)', 'ク', 'Pahit/Menderita. 艹 (tanaman) + 古 (tua). Tanaman tua yang rasanya sangat pahit saat ditelan.')],
        'co': 'Kanji yang sama dengan 苦い (pahit). Kalau にがい adalah pahit di lidah, くるしい adalah "pahit" yang menyumbat dada — rasa sesak napas, penderitaan finansial, atau tersiksa batin. <b>Menderita</b>.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '心配な', 'y': 'しんぱいな', 'a': 'Khawatir / Cemas',
        'ej': 'テストの結果が心配です。', 'ei': 'Saya khawatir dengan hasil ujian.', 'k': False,
        'ch': [
            ('心', 'こころ', 'シン', 'Hati.'),
            ('配', 'くば(る)', 'ハイ', 'Membagikan. 酉 (kendi) + 己 (diri/ular). Membagi-bagikan minuman/perhatian.')
        ],
        'co': '心 (hati) yang terus 配 (dibagi-bagi) ke berbagai arah — pikiranmu bercabang memikirkan A, B, C secara bersamaan sehingga kamu tidak bisa tenang. Perasaan hati yang terpecah = <b>Khawatir</b>.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '嫌な', 'y': 'いやな', 'a': 'Tidak menyenangkan / Menjijikkan / Enggan',
        'ej': '嫌な予感がします。', 'ei': 'Saya punya firasat buruk/tidak enak.', 'k': False,
        'ch': [('嫌', 'きら(い) / いや', 'ケン / ゲン', 'Benci/Jijik. 女 (perempuan) + 兼 (merangkap banyak). Tekanan yang menumpuk bikin muak.')],
        'co': 'Kalau 嫌い (きらい) artinya "aku tidak suka benda itu", 嫌な (いやな) menggambarkan perasaan <b>jijik/enggan/tidak enak</b> saat menghadapi sesuatu. Bau yang いや, tugas yang いや. Bikin ingin menghindar.'
    },
    {
        'g': 'EXTKS::Perasaan', 't': 'Perasaan',
        'w': '可哀想な', 'y': 'かわいそうな', 'a': 'Kasihan / Memprihatinkan',
        'ej': 'その捨て猫は可哀想です。', 'ei': 'Kucing terbuang itu kasihan.', 'k': False,
        'ch': [
            ('可', '–', 'カ', 'Patut/Layak.'),
            ('哀', 'あわ(れ)', 'アイ', 'Sedih/Meratap. 口 (mulut) meratap dari dalam 衣 (baju pelayat).'),
            ('想', 'おも(う)', 'ソウ', 'Membayangkan/Pikiran.')
        ],
        'co': '可 (Sangat patut) + 哀 (ditangisi/dikasihani) + 想 (dalam pikiran). Saat kamu melihat sesuatu dan berpikir bahwa itu sangat layak untuk ditangisi penderitaannya. <b>Kasihan</b>.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 6: EXTKS::Penilaian (7)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '美しい', 'y': 'うつくしい', 'a': 'Indah / Sangat Cantik',
        'ej': '美しい景色を見ました。', 'ei': 'Saya melihat pemandangan yang indah.', 'k': False,
        'ch': [('美', 'うつく(しい)', 'ビ', 'Indah/Cantik. 羊 (domba) + 大 (besar). Domba yang gemuk dan besar di zaman Tiongkok kuno dianggap sebagai standar keindahan estetis.')],
        'co': 'Kalau 綺麗 (kirei) itu "cantik/rapi", 美しい (utsukushii) adalah <b>keindahan</b> yang lebih puitis, mendalam, dan estetis. Keindahan alam, karya seni, atau hati manusia.'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '正しい', 'y': 'ただしい', 'a': 'Benar / Tepat / Adil',
        'ej': '正しい答えを選んでください。', 'ei': 'Silakan pilih jawaban yang benar.', 'k': False,
        'ch': [('正', 'ただ(しい)', 'セイ / ショウ', 'Benar/Lurus. 一 (garis tujuan/target) + 止 (kaki melangkah/berhenti). Langkah kaki yang menuju tepat lurus ke garis target tanpa berbelok.')],
        'co': 'Langkah kaki (止) yang melangkah tepat ke satu target kebenaran (一) tanpa menyimpang ke kebohongan. Sesuatu yang mutlak secara moral atau fakta. <b>Benar dan Tepat</b>.'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '酷い', 'y': 'ひどい', 'a': 'Kejam / Mengerikan / Parah',
        'ej': '酷い雨が降っています。', 'ei': 'Hujan turun dengan parah/deras sekali.', 'k': False,
        'ch': [('酷', 'ひど(い)', 'コク', 'Kejam/Parah. 酉 (arak/botol alkohol) + 告 (melapor/mengumumkan). Alkohol yang sangat keras dan tajam, menyiksa tenggorokan. Menyiksa/kejam.')],
        'co': 'Awalnya bermakna "minuman beralkohol yang terlalu keras menyiksa", lalu maknanya bergeser untuk segala sesuatu yang tingkatannya di luar batas toleransi. Cuaca <b>parah</b>, atau orang yang <b>kejam</b>.'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '可笑しい', 'y': 'おかしい', 'a': 'Lucu / Aneh / Ganjil',
        'ej': '彼の話は可笑しいです。', 'ei': 'Ceritanya lucu (atau aneh).', 'k': False,
        'ch': [
            ('可', '–', 'カ', 'Patut/Boleh.'),
            ('笑', 'わら(う)', 'ショウ', 'Tertawa. 竹 (bambu) bergoyang ditiup angin + 夭 (orang melengkung kegirangan).')
        ],
        'co': 'Sesuatu yang "patut (可) ditertawakan (笑)". Punya dua wajah: bisa bermakna humor (<b>lucu bikin ketawa</b>), atau keganjilan logika (<b>aneh, kok begini?</b>). "Mesinnya rusak, suaranya okashii."'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '立派な', 'y': 'りっぱな', 'a': 'Megah / Hebat / Terpuji',
        'ej': '立派な家ですね。', 'ei': 'Rumah yang megah ya.', 'k': False,
        'ch': [
            ('立', 'た(つ)', 'リツ', 'Berdiri tegak.'),
            ('派', '–', 'ハ', 'Aliran/Cabang. 氵 (air) + turunan/cabang.')
        ],
        'co': '立 (berdiri tegak sendiri) + 派 (aliran). Sesuatu yang memiliki kelas/alirannya sendiri yang kokoh berdiri dan membuat orang segan. Bangunan yang <b>megah</b> atau kelakuan yang <b>terpuji/pantas dicontoh</b>.'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '駄目な', 'y': 'だめな', 'a': 'Tidak boleh / Sia-sia / Tidak berguna',
        'ej': 'ここでタバコを吸っては駄目です。', 'ei': 'Tidak boleh merokok di sini.', 'k': False,
        'ch': [
            ('駄', '–', 'ダ', 'Kuda beban. 馬 (kuda) + 太 (gemuk/berat). Kuda yang menanggung beban berat.'),
            ('目', 'め', 'モク', 'Mata / Titik / Tanda.')
        ],
        'co': 'Asalnya dari dunia perjudian "Go" (titik buta). Tapi cocoklogi mudahnya: Kuda beban (駄) yang sudah kehabisan tenaga memperlihatkan tanda (目) bahwa ia tidak kuat lagi. Sama sekali <b>tidak berguna</b> atau <b>jangan dilakukan (dilarang)</b>.'
    },
    {
        'g': 'EXTKS::Penilaian', 't': 'Penilaian',
        'w': '格好いい', 'y': 'かっこいい', 'a': 'Keren / Gagah / Tampan (Gaya)',
        'ej': 'あの車は格好いいです。', 'ei': 'Mobil itu keren.', 'k': False,
        'ch': [
            ('格', '–', 'カク', 'Status/Bentuk/Aturan.'),
            ('好', 'この(む)', 'コウ', 'Suka/Bagus.')
        ],
        'co': 'Bentuk/penampilannya (格) sangat disukai/bagus (好), ditambah kata いい (bagus). Gabungan sempurnanya jadi "kakkoii". Kalau ハンサム itu murni fitur wajah pria, かっこいい itu keseluruhan gaya (vibe) yang <b>keren</b>, bisa untuk cowok, cewek, atau benda.'
    },

    # ──────────────────────────────────────────────────────────
    # GROUP 7: EXTKS::Kondisi (14)
    # ──────────────────────────────────────────────────────────

    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '若い', 'y': 'わかい', 'a': 'Muda',
        'ej': '彼はまだ若いです。', 'ei': 'Dia masih muda.', 'k': False,
        'ch': [('若', 'わか(い)', 'ジャク', 'Muda. 艹 (tanaman/rumput) + 右 (tangan). Tangan yang sedang merawat atau mengumpulkan pucuk tanaman yang baru tumbuh merambat.')],
        'co': 'Seperti 艹 (pucuk tanaman) yang baru saja tumbuh, masih lentur, hijau, dan penuh energi kehidupan. Belum lapuk oleh waktu. <b>Muda</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '詳しい', 'y': 'くわしい', 'a': 'Terperinci / Detail / Berpengetahuan',
        'ej': 'この地図は詳しいです。', 'ei': 'Peta ini terperinci/detail.', 'k': False,
        'ch': [('詳', 'くわ(しい)', 'ショウ', 'Terperinci/Detail. 言 (kata-kata/penjelasan) + 羊 (domba). Kata-kata yang isinya "gemuk" dan padat memuaskan seperti domba persembahan.')],
        'co': 'Penjelasan (言) yang daging isinya sangat melimpah (羊 - domba gemuk). Semua seluk-beluknya dibahas tanpa ada yang terlewat. <b>Sangat detail</b> atau "tahu banyak soal suatu hal".'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '激しい', 'y': 'はげしい', 'a': 'Sengit / Hebat (Intensitas) / Dahsyat',
        'ej': '激しい雨が降っています。', 'ei': 'Hujan deras/dahsyat sedang turun.', 'k': False,
        'ch': [('激', 'はげ(しい)', 'ゲキ', 'Sengit/Dahsyat. 氵 (air) + 敫 (putih bersinar/melesat; 白 putih + 放 melepas). Arus air deras yang menabrak batu karang hingga cipratannya memutih melesat.')],
        'co': 'Bayangkan 氵 (ombak air laut) yang menabrak tebing karang hingga hancur dan buihnya memercik hebat ke mana-mana. Kekuatan alam yang tidak terkendali. <b>Sengit / Dahsyat</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '暇な', 'y': 'ひまな', 'a': 'Luang / Senggang',
        'ej': '明日は暇ですか。', 'ei': 'Apakah besok kamu luang?', 'k': False,
        'ch': [('暇', 'ひま', 'カ', 'Waktu Luang. 日 (matahari/waktu hari) + 叚 (meminjam/kelonggaran). Waktu kelonggaran yang dipinjamkan dari jadwal sibuk.')],
        'co': 'Hari (日) di mana kamu mendapat kelonggaran (叚) dari segala kewajiban. Tidak ada pekerjaan, tidak ada jadwal. Waktu yang benar-benar <b>senggang</b>. Kebalikan dari 忙しい.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '有名な', 'y': 'ゆうめいな', 'a': 'Terkenal / Populer',
        'ej': '彼は有名な歌手です。', 'ei': 'Dia penyanyi terkenal.', 'k': False,
        'ch': [
            ('有', 'あ(る)', 'ユウ', 'Ada. ナ (tangan kanan) memegang 月 (daging). Kepemilikan (memiliki daging = kaya/ada).'),
            ('名', 'な', 'メイ', 'Nama. 夕 (malam gelap) + 口 (mulut berteriak menyebut nama agar tak tabrakan).')
        ],
        'co': 'Namanya (名) "ada" (有) di mana-mana. Ke mana pun kamu pergi, orang mengetahui namanya. Tentu saja itu artinya <b>Terkenal</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '盛んな', 'y': 'さかんな', 'a': 'Berkembang pesat / Makmur / Aktif',
        'ej': 'この町は工業が盛んです。', 'ei': 'Kota ini industrinya berkembang pesat.', 'k': False,
        'ch': [('盛', 'さか(ん) / も(る)', 'セイ / ジョウ', 'Melimpah/Makmur. 皿 (piring wadah) + 成 (berhasil/jadi). Makanan yang ditaruh di piring hingga menumpuk menggunung sukses.')],
        'co': 'Sesuatu yang diisi ke 皿 (piring) hingga menggunung dan tumpah ruah. Kelimpahan dan produktivitas yang luar biasa. Bisnis atau kegiatan yang <b>sangat aktif / berkembang pesat</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '複雑な', 'y': 'ふくざつな', 'a': 'Rumit / Kusut',
        'ej': 'その問題は複雑です。', 'ei': 'Masalah itu rumit.', 'k': False,
        'ch': [
            ('複', '–', 'フク', 'Ganda/Berlapis. 衤 (pakaian) + 復 (kembali/berulang). Pakaian tebal yang berlapis-lapis.'),
            ('雑', '–', 'ザツ', 'Campur aduk. 衣 (pakaian) + 隹 (berbagai jenis burung). Banyak hal tak beraturan berkumpul jadi satu.')
        ],
        'co': 'Sudah 複 (berlapis-lapis), ditambah 雑 (berbagai macam elemen campur aduk tidak beraturan). Sangat kusut, susunan kabel yang berantakan, atau situasi penuh dilema. <b>Rumit</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '十分な', 'y': 'じゅうぶんな', 'a': 'Cukup / Memadai / Penuh',
        'ej': '時間は十分あります。', 'ei': 'Waktunya cukup (ada banyak).', 'k': False,
        'ch': [
            ('十', 'じゅう', 'ジュウ', 'Sepuluh / Sempurna.'),
            ('分', 'わ(ける)', 'ブン / フン', 'Bagian.')
        ],
        'co': 'Skor maksimal. Dari 10 bagian, kamu mendapatkan 10 bagian (100%). Semuanya terpenuhi, tidak ada kekurangan sedikitpun. <b>Cukup dan Memadai</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '特別な', 'y': 'とくべつな', 'a': 'Spesial / Khusus',
        'ej': '今日は特別な日です。', 'ei': 'Hari ini adalah hari yang spesial.', 'k': False,
        'ch': [
            ('特', '–', 'トク', 'Spesial. 牜 (sapi) + 寺 (kuil/pemerintahan). Sapi jantan besar kualitas super yang dipersembahkan secara khusus.'),
            ('別', 'わか(れる)', 'ベツ', 'Berbeda/Pisah. Memotong dengan pisau 刂 (dao) untuk memisahkan.')
        ],
        'co': 'Sapi unggulan (特) yang dipisahkan (別) dari kawanan hewan ternak biasa. Sesuatu yang mendapat perlakuan beda dari yang umum. <b>Spesial / Khusus</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '不思議な', 'y': 'ふしぎな', 'a': 'Ajaib / Misterius',
        'ej': '不思議な夢を見ました。', 'ei': 'Saya melihat mimpi yang ajaib/aneh.', 'k': False,
        'ch': [
            ('不', '–', 'フ', 'Tidak.'),
            ('思', 'おも(う)', 'シ', 'Berpikir/Merenung.'),
            ('議', '–', 'ギ', 'Berunding/Membahas.')
        ],
        'co': 'Secara harfiah: Tidak (不) bisa dipikirkan secara nalar (思), dan tidak ada gunanya diperdebatkan (議). Di luar jangkauan logika manusia. <b>Misterius atau Ajaib</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '無駄な', 'y': 'むだな', 'a': 'Sia-sia / Percuma / Pemborosan',
        'ej': '無駄な時間を過ごした。', 'ei': 'Menghabiskan waktu dengan sia-sia.', 'k': False,
        'ch': [
            ('無', 'な(い)', 'ム', 'Tidak ada.'),
            ('駄', '–', 'ダ', 'Kuda beban.')
        ],
        'co': 'Menuntun kuda beban (駄) perjalanan jauh mendaki gunung, tapi ternyata muatannya "Tidak ada" (無). Tenaga kuda habis, tapi tidak bawa barang = cape deeh. <b>Sia-sia dan Percuma</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '邪魔な', 'y': 'じゃまな', 'a': 'Menghalangi / Mengganggu',
        'ej': 'そこにいると邪魔です。', 'ei': 'Kalau kamu di situ, menghalangi (jalan).', 'k': False,
        'ch': [
            ('邪', '–', 'ジャ', 'Jahat/Menyimpang. 牙 (taring) + 阝 (kota/tempat).'),
            ('魔', '–', 'マ', 'Iblis/Roh jahat. 麻 (tanaman rami beracun/membius) + 鬼 (setan/hantu).')
        ],
        'co': 'Asalnya istilah Buddha untuk godaan Iblis Jahat (邪魔) yang menghalangi pencerahan biksu. Sekarang dipakai untuk kotak kardus di tengah jalan yang bikin kamu tersandung. Sama-sama <b>Mengganggu / Menghalangi</b>.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '適当な', 'y': 'てきとうな', 'a': 'Tepat / Cocok ATAU Asal-asalan (slang)',
        'ej': '適当な服を選んで。 (Pilih baju yang cocok) / 適当にやる。 (Kerjakan asal-asalan).', 'ei': 'Pilih baju yang cocok. / Dikerjakan asal-asalan.', 'k': False,
        'ch': [
            ('適', '–', 'テキ', 'Cocok/Sesuai.'),
            ('当', 'あ(たる)', 'トウ', 'Tepat sasaran.')
        ],
        'co': 'Secara harfiah artinya "Cocok (適) dan Tepat sasaran (当)". Tapi dalam bahasa lisan modern, orang Jepang sering membolak-balikkannya menjadi: "yang penting asal kena aja", jadilah bermakna <b>Asal-asalan / Sembarangan</b>. Punya 2 kepribadian.'
    },
    {
        'g': 'EXTKS::Kondisi', 't': 'Kondisi',
        'w': '色々な', 'y': 'いろいろな', 'a': 'Bermacam-macam / Berbagai',
        'ej': '色々な人がいます。', 'ei': 'Ada bermacam-macam orang.', 'k': False,
        'ch': [('色', 'いろ', 'ショク', 'Warna/Penampilan. 勹 (membungkuk) + 巴 (ular/orang). Orang saling menempel, memerah wajahnya.')],
        'co': 'Tanda "々" mengulang kanji di depannya. Warna (色) + Warna (々). Ada merah, kuning, hijau. Mewakili <b>Bermacam-macam</b> variasi dalam bentuk apapun (bukan cuma warna fisik).'
    }

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

        if not card['w'].strip():
            errors.append(f"Card {i}: empty word/front!")

        if card['w'] in fronts_seen:
            errors.append(f"Card {i}: duplicate front '{card['w']}'!")
        fronts_seen.add(card['w'])

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

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EXTKS_Anki_Deck.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated {len(CARDS)} EXTKS cards to: {out_path}")
    print(f"Groups: {len(set(c['g'] for c in CARDS))}")

    from collections import Counter
    group_counts = Counter(c['g'] for c in CARDS)
    for g, count in sorted(group_counts.items()):
        print(f"  {g}: {count} cards")

    if not errors:
        print("\nAll EXTKS validations passed!")
    else:
        print(f"\n{len(errors)} validation error(s) found. Please fix before importing.")


if __name__ == '__main__':
    main()
