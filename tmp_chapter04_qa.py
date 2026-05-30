from pathlib import Path
import re

root = Path('docs/game-design-fundamentals/chapter-04')
issues = []
soft = []
files = sorted(root.rglob('*.md'))

for md in files:
    text = md.read_text(encoding='utf-8')
    for forbidden in ['阅读提示', '子小节目录', '本节开篇', '!!! note']:
        if forbidden in text:
            issues.append((str(md), 'forbidden-helper', forbidden))
    for token in ['title:', '# ', '## 原书内容整理', 'chapter-pager--bottom', '## 我的批注区']:
        if token not in text:
            issues.append((str(md), 'missing-structure-token', token))
    if re.search(r'(?m)^\d+\s*游戏设计基础$', text):
        issues.append((str(md), 'page-header-leftover', '数字 + 游戏设计基础'))
    if re.search(r'(?m)^第4章', text):
        issues.append((str(md), 'page-header-leftover', '第4章'))

for md in files:
    in_fig = False
    for i, line in enumerate(md.read_text(encoding='utf-8').splitlines(), 1):
        s = line.strip()
        if s.startswith('<figure'):
            in_fig = True
        if not in_fig and re.match(r'^图4-\d', s):
            # Allow prose references such as “图4-3说明了以上情况。”; flag only standalone captions.
            if not re.match(r'^图4-\d\s*说明', s):
                soft.append((str(md), i, s[:120]))
        if s.startswith('</figure>'):
            in_fig = False

report = [
    '# Chapter 04 QA Report',
    '',
    f'- files: {len(files)}',
    f'- hard issues: {len(issues)}',
    f'- figure captions awaiting screenshots: {len(soft)}',
    '',
]
if issues:
    for path, kind, detail in issues:
        report.append(f'- `{path}` `{kind}`: {detail}')
else:
    report.append('No hard structural/helper issues found by automated scan.')
if soft:
    report.append('\n## Figure Captions Awaiting Screenshot Extraction\n')
    for path, line, s in soft:
        report.append(f'- `{path}` line {line}: {s}')

out = Path('tmp_chapter04_qa_report.md')
out.write_text('\n'.join(report) + '\n', encoding='utf-8')
print(out.resolve())
print('\n'.join(report[:60]))
