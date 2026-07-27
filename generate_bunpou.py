import re
import os

css_front = """<style>
.frontcard{font-family:-apple-system,'Hiragino Sans','Yu Gothic',sans-serif;
  background:#ffffff !important;color:#18181b !important;
  padding:26px 20px;border-radius:12px;text-align:center;
  border:1px solid #e4e4e7}
.front-num{font-size:11px;color:#a1a1aa !important;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;margin-bottom:12px}
.front-main{font-size:30px;font-weight:700;color:#18181b !important;
  line-height:1.5;letter-spacing:0.3px}
.front-hint{margin-top:16px;font-size:10.5px;text-transform:uppercase;
  letter-spacing:1.8px;color:#a1a1aa !important;font-weight:700}
</style>"""

css_back = """<style>
.bp{font-family:-apple-system,'Hiragino Sans','Yu Gothic',sans-serif;
  background:#ffffff !important;color:#18181b !important;
  border-radius:12px;overflow:hidden;border:1px solid #e4e4e7}
.bp-head{padding:14px 18px;background:#18181b !important}
.bp-head-num{font-size:11px;font-weight:700;letter-spacing:1.5px;
  color:#a1a1aa !important;text-transform:uppercase}
.bp-head-rumus{font-size:17px;font-weight:700;color:#ffffff !important;
  margin-top:2px}
.bp-body{padding:16px 18px}
.bp-section{margin-bottom:14px}
.bp-section:last-child{margin-bottom:0}
.bp-k{font-size:10px;font-weight:700;letter-spacing:1.2px;
  text-transform:uppercase;color:#a1a1aa !important;margin-bottom:5px;
  display:flex;align-items:center;gap:5px}
.bp-k::before{content:'';width:3px;height:11px;background:#3b82f6;
  border-radius:2px;display:inline-block}
.bp-target{font-size:14.5px;color:#3f3f46 !important;line-height:1.55}
.bp-target b{color:#18181b !important}
.bp-contoh{background:#fafafa !important;border-radius:8px;padding:4px 12px}
.bp-contoh-item{padding:8px 0;border-bottom:1px solid #ececec}
.bp-contoh-item:last-child{border-bottom:none}
.bp-contoh-jp{font-size:15px;color:#18181b !important;font-weight:500}
.bp-contoh-id{font-size:12.5px;color:#71717a !important;margin-top:1px}
.bp-tips{font-size:13px;color:#3f3f46 !important;line-height:1.65;
  background:#eff6ff !important;border-radius:8px;padding:11px 13px}
.bp-tips b{color:#1d4ed8 !important;font-weight:700}
.bp-warn{font-size:13px;color:#3f3f46 !important;line-height:1.65;
  background:#fef2f2 !important;border-left:3px solid #ef4444;
  border-radius:6px;padding:10px 12px;margin-top:9px}
.bp-warn b{color:#b91c1c !important;font-weight:700}
</style>"""

def split_jp_id(line):
    line = line.replace('*', '').strip()
    if not line.endswith(')'):
        return line, ""

    depth = 0
    for i in range(len(line)-1, -1, -1):
        if line[i] == ')':
            depth += 1
        elif line[i] == '(':
            depth -= 1
            if depth == 0:
                jp = line[:i].strip()
                id_ = line[i+1:-1].strip()
                return jp, id_
    return line, ""

def parse_md(filepath, bab_num):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    patterns = re.split(r'### 【(\d+)】', content)[1:]

    cards = []

    for i in range(0, len(patterns), 2):
        num = patterns[i].strip()
        body = patterns[i+1]

        # Extract title/rumus
        title_match = re.match(r'(.+)', body.strip())
        title = title_match.group(1).strip() if title_match else ""

        # Extract target
        target_match = re.search(r'🎯 \*\*Target:\*\*(.*?)(?=\n🛠️|\n📝|\n💡|\n>|\n---|$)', body, re.DOTALL)
        target = target_match.group(1).strip() if target_match else ""
        target_sentences = re.split(r'(?<=[.!?])\s+', target)
        target = " ".join(target_sentences[:2]).strip()
        target = re.sub(r'"([^"]+)"', r'<b>"\1"</b>', target)

        # Extract rumus hack (for front) - only match until the end of the line
        rumus_match = re.search(r'🛠️ \*\*Rumus Hack:\*\*(.*?)(?=\n|$)', body)
        rumus = rumus_match.group(1).strip() if rumus_match else title

        # Extract warnings/tips from blockquotes
        warn_text = " ".join([line.strip()[1:].strip() for line in body.split('\n') if line.strip().startswith('>')])
        warn_text = re.sub(r'^\*\*(.*?)\*\* ', r'<b>\1</b> ', warn_text) # replace markdown bold with HTML bold

        tips = "Pahami pola ini dengan mengamati contoh penggunaannya."
        warn_box = ""
        if warn_text:
             warn_box = f'<div class="bp-warn"><b>Awas:</b> {warn_text}</div>'
             tips = "Perhatikan perbedaan dan pengecualian pada pola ini."

        # Extract examples
        examples_text = ""
        contoh_basic = re.search(r'(?:📝 \*\*Contoh Basic:\*\*|\*\*Contoh asli[^\n]*)(.*?)(?=\n💡|\n>|\n---|$)', body, re.DOTALL)
        if contoh_basic: examples_text += contoh_basic.group(1) + "\n"

        contoh_lateral = re.search(r'💡 \*\*Contoh Lateral.*?:(.*?)(?=\n>|\n---|$)', body, re.DOTALL)
        if contoh_lateral: examples_text += contoh_lateral.group(1)

        raw_examples = [x.strip() for x in examples_text.split('\n') if x.strip()]

        examples_html = ""
        count = 0

        for line in raw_examples:
            line = re.sub(r'^- ', '', line).strip()
            if not line: continue

            jp, id_ = split_jp_id(line)

            examples_html += f'<div class="bp-contoh-item"><div class="bp-contoh-jp">{jp}</div><div class="bp-contoh-id">{id_}</div></div>'
            count += 1
            if count >= 4:
                break

        front_font_style = ""
        if len(rumus) > 25:
             front_font_style = ' style="font-size:24px;"'

        front_html = f'{css_front}<div class="frontcard"><div class="front-num">Pola {num} &middot; Bab {bab_num}</div><div class="front-main"{front_font_style}>{rumus}</div><div class="front-hint">Bunpou &middot; Fungsi &amp; cara pakainya?</div></div>'

        back_html = f'{css_back}<div class="bp"><div class="bp-head"><div class="bp-head-num">Pola {num} &middot; Bab {bab_num}</div><div class="bp-head-rumus">{title}</div></div><div class="bp-body"><div class="bp-section"><div class="bp-k">Fungsi</div><div class="bp-target">{target}</div></div>'

        if examples_html:
            back_html += f'<div class="bp-section"><div class="bp-k">Contoh</div><div class="bp-contoh">{examples_html}</div></div>'

        back_html += f'<div class="bp-section"><div class="bp-k">Tips Cepat Hapal</div><div class="bp-tips">{tips}{warn_box}</div></div></div></div>'

        # Remove newlines for TSV format
        front_html = front_html.replace('\n', '')
        back_html = back_html.replace('\n', '')

        cards.append(f'Basic\tBab 0{bab_num}::Bunpou\t{front_html}\t{back_html}\tBunpou')

    return cards

def write_deck(cards, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("#separator:tab\n")
        f.write("#html:true\n")
        f.write("#notetype column:1\n")
        f.write("#deck column:2\n")
        f.write("#tags column:5\n")
        for card in cards:
            f.write(card + "\n")

babs = [1, 2, 3]
for bab in babs:
    input_path = f"BAB_0{bab}/bunpou.md"
    output_path = f"BAB_{bab}/BAB_{bab}_bunpou.txt"
    if os.path.exists(input_path):
        cards = parse_md(input_path, bab)
        write_deck(cards, output_path)
        print(f"Generated {output_path} with {len(cards)} cards.")
    else:
        print(f"File {input_path} not found.")
