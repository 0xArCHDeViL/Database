# -*- coding: utf-8 -*-
"""
Generator Anki Deck: Kata Kerja (Super Komprehensif)
Mendukung konjugasi otomatis (Masu, Te, Ta, Nai, dll) dan CSS premium.
"""

import sys
import os

# ============================================================
# CONJUGATION ENGINE
# ============================================================

def conjugate_godan(base):
    # base is the dictionary form (e.g., 書く)
    stem = base[:-1]
    last = base[-1]
    
    # Mapping for vowel shifts
    shift_i = {'う':'い', 'く':'き', 'ぐ':'ぎ', 'す':'し', 'つ':'ち', 'ぬ':'に', 'ぶ':'び', 'む':'み', 'る':'り'}
    shift_a = {'う':'わ', 'く':'か', 'ぐ':'が', 'す':'さ', 'つ':'た', 'ぬ':'な', 'ぶ':'ば', 'む':'ま', 'る':'ら'}
    shift_e = {'う':'え', 'く':'け', 'ぐ':'げ', 'す':'せ', 'つ':'て', 'ぬ':'ね', 'ぶ':'べ', 'む':'め', 'る':'れ'}
    shift_o = {'う':'お', 'く':'こ', 'ぐ':'ご', 'す':'そ', 'つ':'と', 'ぬ':'の', 'ぶ':'ぼ', 'む':'も', 'る':'ろ'}
    
    # Te/Ta form rules
    te_ta = {
        'う': ('って', 'った'),
        'つ': ('って', 'った'),
        'る': ('って', 'った'),
        'む': ('んで', 'んだ'),
        'ぶ': ('んで', 'んだ'),
        'ぬ': ('んで', 'んだ'),
        'く': ('いて', 'いた'), # Exception for 行く handled below
        'ぐ': ('いで', 'いだ'),
        'す': ('して', 'した')
    }

    if base == '行く':
        te_form = '行って'
        ta_form = '行った'
    elif base == '行く' or base == 'いく': # Just in case kana is used
        te_form = 'いって'
        ta_form = 'いった'
    else:
        te_form = stem + te_ta[last][0]
        ta_form = stem + te_ta[last][1]

    return {
        'Jisho': base,
        'Masu': stem + shift_i[last] + 'ます',
        'Te': te_form,
        'Ta': ta_form,
        'Nai': stem + shift_a[last] + 'ない',
        'Tai': stem + shift_i[last] + 'たい',
        'Ba': stem + shift_e[last] + 'ば',
        'Ikou': stem + shift_o[last] + 'う',
        'Kanou': stem + shift_e[last] + 'る',
        'Ukemi': stem + shift_a[last] + 'れる',
        'Shieki': stem + shift_a[last] + 'せる'
    }

def conjugate_ichidan(base):
    stem = base[:-1] # Drop る
    return {
        'Jisho': base,
        'Masu': stem + 'ます',
        'Te': stem + 'て',
        'Ta': stem + 'た',
        'Nai': stem + 'ない',
        'Tai': stem + 'たい',
        'Ba': stem + 'れば',
        'Ikou': stem + 'よう',
        'Kanou': stem + 'られる',
        'Ukemi': stem + 'られる',
        'Shieki': stem + 'させる'
    }

def conjugate_irregular(base):
    # Handle する and 来る variants
    if base.endswith('する') or base == '為る':
        # Handle prefix for ~suru verbs
        prefix = base[:-2] if base.endswith('する') else base[:-2] 
        return {
            'Jisho': base,
            'Masu': prefix + 'します',
            'Te': prefix + 'して',
            'Ta': prefix + 'した',
            'Nai': prefix + 'しない',
            'Tai': prefix + 'したい',
            'Ba': prefix + 'すれば',
            'Ikou': prefix + 'しよう',
            'Kanou': prefix + 'できる',
            'Ukemi': prefix + 'される',
            'Shieki': prefix + 'させる'
        }
    elif base == '来る':
        return {
            'Jisho': '来る',
            'Masu': '来ます',
            'Te': '来て',
            'Ta': '来た',
            'Nai': '来ない',
            'Tai': '来たい',
            'Ba': '来れば',
            'Ikou': '来よう',
            'Kanou': '来られる',
            'Ukemi': '来られる',
            'Shieki': '来させる'
        }
    elif base == 'くる':
        return {
            'Jisho': 'くる',
            'Masu': 'きます',
            'Te': 'きて',
            'Ta': 'きた',
            'Nai': 'こない',
            'Tai': 'きたい',
            'Ba': 'くれば',
            'Ikou': 'こよう',
            'Kanou': 'こられる',
            'Ukemi': 'こられる',
            'Shieki': 'こさせる'
        }
    elif base == '持って来る':
        return {
            'Jisho': '持って来る',
            'Masu': '持って来ます',
            'Te': '持って来て',
            'Ta': '持って来た',
            'Nai': '持って来ない',
            'Tai': '持って来たい',
            'Ba': '持って来れば',
            'Ikou': '持って来よう',
            'Kanou': '持って来られる',
            'Ukemi': '持って来られる',
            'Shieki': '持って来させる'
        }
    return {}

def get_conjugations(base, group):
    if group == 1:
        return conjugate_godan(base)
    elif group == 2:
        return conjugate_ichidan(base)
    elif group == 3:
        return conjugate_irregular(base)
    return {}

# ============================================================
# ============================================================
# CSS CONSTANTS (Sama dengan KS_Anki_Deck dan EXTKS_Anki_Deck)
# ============================================================

FRONT_STYLE = '<style>@import url(\'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Noto+Sans+JP:wght@400;700;900&display=swap\');.frontcard{font-family:\'Inter\',\'Noto Sans JP\',sans-serif;background:linear-gradient(135deg,#ffffff 0%,#f8fafc 100%) !important;color:#0f172a !important;padding:40px 20px;border-radius:24px;text-align:center;border:1px solid #e2e8f0;box-shadow:0 10px 30px -5px rgba(0,0,0,0.05),inset 0 2px 4px rgba(255,255,255,0.8)}.front-main{font-size:64px;font-weight:900;color:#1e293b !important;line-height:1.2;letter-spacing:-1px;text-shadow:0 2px 10px rgba(0,0,0,0.03)}.front-main.sm{font-size:52px}.front-main.xs{font-size:42px}.front-hint{margin-top:24px;font-size:13px;text-transform:uppercase;letter-spacing:4px;color:#94a3b8 !important;font-weight:700}.badge-group{display:inline-block;padding:6px 16px;border-radius:20px;font-size:12px;font-weight:bold;color:white !important;margin-bottom:20px;box-shadow:0 4px 12px rgba(0,0,0,0.1);letter-spacing:1px;text-transform:uppercase}.g1{background:linear-gradient(135deg,#3b82f6,#1d4ed8) !important}.g2{background:linear-gradient(135deg,#ef4444,#b91c1c) !important}.g3{background:linear-gradient(135deg,#8b5cf6,#6d28d9) !important}</style>'

BACK_STYLE = '<style>@import url(\'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=Noto+Sans+JP:wght@400;700;900&display=swap\');.jpcard{font-family:\'Inter\',\'Noto Sans JP\',sans-serif;line-height:1.6;background:#ffffff !important;color:#1e293b !important;padding:24px;border-radius:16px;box-shadow:0 10px 40px -10px rgba(0,0,0,0.1);border:1px solid #f1f5f9}.yomi{font-size:28px;color:#2563eb !important;font-weight:900;margin-bottom:6px;letter-spacing:-0.5px}.arti{font-size:22px;color:#b45309 !important;font-weight:700;background:#fef3c7 !important;padding:6px 16px;border-radius:10px;display:inline-block;margin:8px 0 16px 0;box-shadow:inset 0 0 0 1px #fde68a}.kalimat{margin:16px 0;padding:16px 20px;background:#f0fdf4 !important;border-left:6px solid #22c55e;border-radius:0 12px 12px 0;color:#14532d !important;box-shadow:0 2px 8px rgba(34,197,94,0.05)}.kalimat .jp{font-size:19px;font-weight:700;color:#166534 !important;margin-bottom:4px}.kalimat .id{font-size:15px;color:#15803d !important;font-weight:400}.label{font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#64748b !important;font-weight:700;margin-bottom:10px;display:flex;align-items:center}.label::before{content:"■";margin-right:8px;color:#cbd5e1 !important;font-size:10px}.analisis-box{margin:20px 0;padding:20px;background:#f8fafc !important;border-radius:16px;border:1px solid #e2e8f0}.analisis-title{font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#64748b !important;font-weight:700;margin-bottom:16px;display:flex;align-items:center}.analisis-title::before{content:"■";margin-right:8px;color:#cbd5e1 !important;font-size:10px}.kanji-strip{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:8px}.kanji-mini{flex:1;min-width:140px;background:#ffffff !important;border-radius:12px;padding:16px;text-align:center;border:1px solid #e2e8f0;box-shadow:0 4px 6px -1px rgba(0,0,0,0.02)}.kanji-mini-char{font-size:46px;font-weight:900;color:#1e3a8a !important;line-height:1.1;margin-bottom:8px}.yomi-badges{display:flex;justify-content:center;gap:6px;margin:12px 0}.badge-kun{background:#dbeafe !important;color:#1d4ed8 !important;font-size:11.5px;font-weight:700;padding:4px 10px;border-radius:8px}.badge-on{background:#fce7f3 !important;color:#be185d !important;font-size:11.5px;font-weight:700;padding:4px 10px;border-radius:8px}.kanji-mini-makna{font-size:13.5px;color:#475569 !important;text-align:left;margin-top:12px;line-height:1.6;border-top:1px solid #f1f5f9;padding-top:12px}.cocoklogi-box{margin:24px 0 12px 0;padding:20px;background:linear-gradient(135deg,#fff1f2 0%,#fdf2f8 100%) !important;border-left:6px solid #e11d48;border-radius:0 16px 16px 0;font-size:15.5px;color:#881337 !important;line-height:1.7;box-shadow:0 4px 12px rgba(225,29,72,0.05)}.cocoklogi-box b{color:#be123c !important;font-weight:900}.conj-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:12px;margin-bottom:24px}.conj-item{background:#f8fafc !important;border:1px solid #e2e8f0;border-radius:12px;padding:12px 8px;text-align:center;transition:all 0.2s ease}.conj-item:hover{transform:translateY(-2px);box-shadow:0 6px 12px rgba(0,0,0,0.05);border-color:#cbd5e1}.conj-name{font-size:11px;color:#64748b !important;text-transform:uppercase;font-weight:800;letter-spacing:1px;margin-bottom:6px}.conj-val{font-size:16px;color:#0f172a !important;font-weight:700}</style>'

# ============================================================
# HTML BUILDER FUNCTIONS
# ============================================================

def build_front(word, group):
    n = len(word)
    if n >= 5:
        sz = ' class="front-main xs"'
    elif n >= 4:
        sz = ' class="front-main sm"'
    else:
        sz = ' class="front-main"'
    hint = "Kanji &middot; Konjugasi &middot; Arti"
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

    # Conjugation Table
    parts.append('<div class="label">Perubahan Bentuk (Konjugasi)</div>')
    parts.append('<div class="conj-grid">')
    
    conj = get_conjugations(card['w'], card['g'])
    
    forms = [
        ('Kamus / Jisho', 'Jisho'),
        ('Sambung / Te', 'Te'), ('Lampau / Ta', 'Ta'),
        ('Negatif / Nai', 'Nai'), ('Keinginan / Tai', 'Tai'),
        ('Pengandaian / Ba', 'Ba'), ('Ajakan / Ikou', 'Ikou'),
        ('Bisa / Kanou', 'Kanou'), ('Pasif / Ukemi', 'Ukemi'),
        ('Kausatif / Shieki', 'Shieki')
    ]
    
    for label, key in forms:
        val = conj.get(key, '-')
        parts.append(
            f'<div class="conj-item">'
            f'<div class="conj-name">{label}</div>'
            f'<div class="conj-val">{val}</div>'
            f'</div>'
        )
    parts.append('</div>')

    if card.get('ch'):
        minis = ''.join(build_kanji_mini(c, ku, on, m) for c, ku, on, m in card['ch'])
        parts.append(
            f'<div class="analisis-box">'
            f'<div class="analisis-title">Analisis Kanji</div>'
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


def main():
    import glob
    import importlib.util
    
    # Load data from kk_data_1.py, kk_data_2.py, etc.
    data_files = sorted(glob.glob('kk_data_*.py'))
    all_cards = []
    
    for f in data_files:
        spec = importlib.util.spec_from_file_location("module.name", f)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        all_cards.extend(module.CARDS)
        
    print(f"Loaded {len(all_cards)} cards from {len(data_files)} data files.")

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

    for i, card in enumerate(all_cards):
        # Allow multiple contexts by checking combining Word + Arti or Word + Yomi
        unique_key = f"{card['w']}_{card['y']}_{card['a']}"
        
        conj = get_conjugations(card['w'], card['g'])
        masu_form = conj.get('Masu', card['w'])
        
        front = build_front(masu_form, card['g'])
        back = build_back(card)

        if not card['w'].strip():
            errors.append(f"Card {i}: empty word/front!")

        if unique_key in fronts_seen:
            errors.append(f"Card {i}: duplicate entry '{unique_key}'!")
        fronts_seen.add(unique_key)

        # Remove any physical newlines in the front/back HTML so Anki doesn't split the record
        front = front.replace('\n', ' ').replace('\r', '')
        back = back.replace('\n', ' ').replace('\r', '')
        
        # Ensure subdeck uses spaces instead of underscores for UI/UX
        clean_subdeck = card['subdeck'].replace('_', ' ')
        line = f"Basic\t{clean_subdeck}\t{front}\t{back}\tKata Kerja"
        lines.append(line)

    if errors:
        print("ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        print()

    output = header + "\n".join(lines) + "\n"

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "KK_Anki_Deck.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Generated {len(all_cards)} KK cards to: {out_path}")

if __name__ == '__main__':
    main()
