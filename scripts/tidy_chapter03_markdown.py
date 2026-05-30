from pathlib import Path
import re

root = Path('docs/game-design-fundamentals/chapter-03')
files = sorted(root.rglob('*.md'))
block_start = '<!-- chapter-pager:start -->'


def is_boundary(s: str) -> bool:
    if not s:
        return False
    return (
        s.startswith('#') or
        s.startswith('>') or
        s.startswith('<') or
        s.startswith('</') or
        s.startswith('<!--') or
        s.startswith('```') or
        s.startswith('|') or
        s == '-' or
        s.startswith('## 我的批注区')
    )


def is_list_start(s: str) -> bool:
    return s.startswith('- ') or bool(re.match(r'^(?:\d+\.|[一二三四五六七八九十]+[、.])\s*', s)) or s.startswith('口')


def join_pair(a: str, b: str) -> str:
    a = a.rstrip()
    b = b.strip()
    if not a:
        return b
    if not b:
        return a
    if re.search(r'[A-Za-z0-9]$', a) and re.match(r'^[A-Za-z0-9]', b):
        return a + ' ' + b
    return a + b


def flush_para(buf, out):
    if not buf:
        return
    if all(is_list_start(x.strip()) for x in buf):
        out.extend(x.strip() for x in buf)
    else:
        text = buf[0].strip()
        for x in buf[1:]:
            text = join_pair(text, x)
        out.append(text)
    buf.clear()


for p in files:
    old = p.read_text(encoding='utf-8')
    lines = old.splitlines()
    out = []
    buf = []
    in_body = False
    in_fig = False
    in_frontmatter = False
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if i == 0 and s == '---':
            in_frontmatter = True
            out.append(line)
            i += 1
            continue
        if in_frontmatter:
            out.append(line)
            if i > 0 and s == '---':
                in_frontmatter = False
            i += 1
            continue
        if s == '## 原书内容整理':
            flush_para(buf, out)
            out.append(line)
            in_body = True
            i += 1
            continue
        if in_body and s == block_start:
            flush_para(buf, out)
            in_body = False
            out.append(line)
            i += 1
            continue
        if not in_body:
            out.append(line)
            i += 1
            continue
        if s.startswith('<figure'):
            flush_para(buf, out)
            if out and out[-1].strip() != '':
                out.append('')
            in_fig = True
            out.append(line)
            i += 1
            continue
        if in_fig:
            out.append(line)
            if s.startswith('</figure>'):
                in_fig = False
                out.append('')
            i += 1
            continue
        if s == '':
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ''
            if not buf:
                if out and out[-1].strip() != '' and (is_boundary(out[-1].strip()) or is_boundary(nxt) or nxt == ''):
                    out.append(line)
            else:
                if is_boundary(nxt) or is_list_start(nxt):
                    flush_para(buf, out)
                    out.append('')
            i += 1
            continue
        if is_boundary(s):
            flush_para(buf, out)
            out.append(line)
            i += 1
            continue
        if is_list_start(s):
            flush_para(buf, out)
            buf.append(s)
            i += 1
            continue
        buf.append(s)
        i += 1
    flush_para(buf, out)
    new = '\n'.join(out).rstrip() + '\n'
    if new != old:
        p.write_text(new, encoding='utf-8', newline='\n')
        print('tidied', p)
