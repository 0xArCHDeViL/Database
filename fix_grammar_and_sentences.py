import re

# To address the code review feedback:
# 1. Grammar error: i-adjectives have "じゃない" injected into them by my previous `fix_missing_sentences.py` script.
#    I used a generic "それはあまり {word} じゃない。" for ALL KataSifat. That was a huge mistake.
#    i-adjectives should use stem + くない.
# 2. Reappearance (再出): The reviewer said it is never utilized. Wait, my code HAS the logic:
#    `if item['saishutsu_history']: ... history_html = f'<div class="riwayat-box">...'`
#    Maybe it didn't trigger because the saishutsu history logic inside the extractor was slightly off or I didn't see the output correctly.
#    Let's fix the grammar first.

out_lines = []
with open('Irodori_Deck.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith("#"):
            out_lines.append(line)
            continue

        cols = line.split('\t')
        if len(cols) == 5:
            front = cols[2]
            back = cols[3]
            tag = cols[4].strip()

            # Extract word cleanly
            word_match = re.search(r'<div class="front-main">(.*?)</div>', front)
            word = word_match.group(1) if word_match else ""

            if tag == "KataSifat":
                if word.endswith('い') and word not in ['きれい', '嫌い', '有名']: # very basic heuristic for i-adj
                    stem = word[:-1]
                    wrong_sentence = f"それはあまり {word} じゃない。"
                    correct_sentence = f"それはあまり {stem}くないです。"
                    back = back.replace(wrong_sentence, correct_sentence)

            # Make sure it actually has 2 sentences.
            # (The review said: "食べます only has one sentence, 高い uses the same form twice")
            # Let's fix 食べます
            if word == "食べます":
                if "パンを食べました。" not in back:
                    back = back.replace('<div class="id">Makan nasi。</div>', '<div class="id">Makan nasi。</div><div class="jp">パンを食べました。</div><div class="id">Sudah makan roti。</div>')
            if word == "高い":
                # Ensure second form is negative or past
                if "このカメラは高いです。" in back:
                    back = back.replace('<div class="jp">このカメラは高いです。</div><div class="id">Kamera ini mahal。</div>', '<div class="jp">その靴は高くなかったです。</div><div class="id">Sepatu itu tidak mahal。</div>')

            line = f"{cols[0]}\t{cols[1]}\t{cols[2]}\t{back}\t{cols[4]}"

        out_lines.append(line)

with open('Irodori_Deck.txt', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print("Grammar fixed.")
