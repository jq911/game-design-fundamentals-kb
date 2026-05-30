from pathlib import Path
import re

root = Path('docs/game-design-fundamentals/chapter-03')
docs = Path('docs')
issues=[]
for md in sorted(root.rglob('*.md')):
    text=md.read_text(encoding='utf-8')
    for forbidden in ['阅读提示','子小节目录','本节开篇','!!! note']:
        if forbidden in text:
            issues.append((str(md),'forbidden-helper',forbidden))
    for token in ['title:', '# ', '## 原书内容整理', 'chapter-pager--bottom', '## 我的批注区']:
        if token not in text:
            issues.append((str(md),'missing-structure-token',token))
    # bare figure captions still expected until screenshot insertion; report but don't count as hard issue
soft=[]
for md in sorted(root.rglob('*.md')):
    in_fig=False
    for i,line in enumerate(md.read_text(encoding='utf-8').splitlines(),1):
        s=line.strip()
        if s.startswith('<figure'): in_fig=True
        if not in_fig and re.match(r'^图3-\d',s):
            soft.append((str(md),i,s[:100]))
        if s.startswith('</figure>'): in_fig=False
report=['# Chapter 03 QA Report','',f'- files: {len(list(root.rglob("*.md")))}',f'- hard issues: {len(issues)}',f'- figure captions awaiting screenshots: {len(soft)}','']
if issues:
    for x in issues: report.append(f'- `{x[0]}` `{x[1]}`: {x[2]}')
else:
    report.append('No hard structural/helper issues found by automated scan.')
if soft:
    report.append('\n## Figure Captions Awaiting Screenshot Extraction\n')
    for path,line,s in soft:
        report.append(f'- `{path}` line {line}: {s}')
out=Path('tmp_chapter03_qa_report.md')
out.write_text('\n'.join(report)+'\n',encoding='utf-8')
print(out.resolve())
print('\n'.join(report[:40]))
