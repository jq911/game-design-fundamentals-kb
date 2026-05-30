from pathlib import Path
import re

CH = Path('docs/game-design-fundamentals/chapter-04')
patterns = [
    ('standalone_page_number', re.compile(r'(?m)^\s*(6[9]|7[0-9]|8[0-7])\s*$')),
    ('common_ocr_self', re.compile(r'自前|自标|自已|很天|相于|儿乎|儿个人|十儿|为人交|一天玩儿次')),
    ('english_join', re.compile(r'JasonVandenBerghe|BigFive|bigfivepersonalitytest|www\.outofservice\.com/\s+bigfive')),
    ('broken_list_marker', re.compile(r'(?m)^\s*[口�]\s*')),
    ('raw_caption', re.compile(r'(?m)^\s*图4-\d(?!.*说明)')),
    ('mojibake_hint', re.compile(r'[�]')),
]

hits = []
for md in sorted(CH.rglob('*.md')):
    text = md.read_text(encoding='utf-8')
    for name, pat in patterns:
        for m in pat.finditer(text):
            line = text.count('\n', 0, m.start()) + 1
            snippet = text[m.start():m.start()+100].replace('\n', '\\n')
            hits.append((str(md), line, name, snippet))

print(f'hits={len(hits)}')
for h in hits[:200]:
    print(f'{h[0]}:{h[1]} [{h[2]}] {h[3]}')
