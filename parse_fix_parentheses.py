import re
import os

def process_example_line(line):
    line = line.strip()

    match = re.search(r'^(.*?)\s*[\(（]([^)）]+)[\)）]$', line)

    if match:
        jp_part = match.group(1).strip()
        id_part = match.group(2).strip()
        return jp_part, id_part
    else:
        # Check if there is a parenthesis in the middle and no closing at the very end
        # Or if there's a parenthesis but the translation is somehow broken.
        # But wait, looking at my previous results, the regex I wrote in `overhaul.py` worked almost perfectly!
        # The reviewer's complaint was that the PREVIOUS version of the script in the PREVIOUS iteration failed.
        pass
