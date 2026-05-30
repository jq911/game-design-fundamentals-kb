from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter05_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-05"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 5 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    # Drop recurring page headers/footers and obvious OCR noise.
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^游戏设计基础\s*\d+$", s):
        continue
    if re.match(r"^第5章\s*了解你的游戏设备\s*\d*$", s):
        continue
    if re.match(r"^第5章.*了解你的游戏设备.*$", s):
        continue
    if s in {"第5章", "了解你的游戏设备", "游戏设计基础"}:
        continue
    if re.match(r"^[A-Za-z]{3,}\d+$", s):
        continue
    if re.match(r"^\d{1,3}$", s):
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "一一": "——",
    "输人": "输入",
    "自已": "自己",
    "自已的": "自己的",
    "向题": "问题",
    "真得": "真的",
    "WindoWs": "Windows",
    "WinDOws": "Windows",
    "Macintosh": "Macintosh",
    "AppStore": "App Store",
    "GooglePlay": "Google Play",
    "FlashPlayer": "Flash Player",
    "XboxLIVE": "Xbox LIVE",
    "NintendoDS": "Nintendo DS",
    "WiiU": "Wii U",
    "IBMPC": "IBM PC",
    "AtariST": "Atari ST",
    "CD-ROM": "CD-ROM",
    "Wi\n\n的影响": "Wii 的影响",
    "玩要": "玩耍",
    "墨盒损坏": "磁带损坏",
    "5.1家用游戏机": "5.1 家用游戏机",
    "5.1.1典型用法": "5.1.1 典型用法",
    "5.1.2输入设备": "5.1.2 输入设备",
    "5.1.3业务考虑": "5.1.3 业务考虑",
    "5.2个人计算机": "5.2 个人计算机",
    "5.2.1典型用法": "5.2.1 典型用法",
    "5.2.2输入设备": "5.2.2 输入设备",
    "5.2.3业务考虑": "5.2.3 业务考虑",
    "5.31\n\n便携设备": "5.3 便携设备",
    "5.3\n\n便携设备": "5.3 便携设备",
    "5.3.1典型用法": "5.3.1 典型用法",
    "5.3.2输入设备": "5.3.2 输入设备",
    "5.3.3专用游戏手持设备": "5.3.3 专用游戏手持设备",
    "5.3.4手机和无线设备": "5.3.4 手机和无线设备",
    "5.4其他设备": "5.4 其他设备",
    "5.5本章总结": "5.5 本章总结",
    "5.6设计练习——训练": "5.6 设计练习——训练",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"5.1","title":"家用游戏机","file":"05-01-home-game-consoles.md","dir":"05-01-home-game-consoles","keywords":"家用游戏机、控制器、客厅、许可、开发工具包","subs":[
        ("5.1.1","典型用法","05-01-01-typical-usage.md"),
        ("5.1.2","输入设备","05-01-02-input-devices.md"),
        ("5.1.3","业务考虑","05-01-03-business-considerations.md"),
    ]},
    {"num":"5.2","title":"个人计算机","file":"05-02-personal-computers.md","dir":"05-02-personal-computers","keywords":"个人计算机、键盘鼠标、独立游戏、网页游戏、开放平台","subs":[
        ("5.2.1","典型用法","05-02-01-typical-usage.md"),
        ("5.2.2","输入设备","05-02-02-input-devices.md"),
        ("5.2.3","业务考虑","05-02-03-business-considerations.md"),
    ]},
    {"num":"5.3","title":"便携设备","file":"05-03-portable-devices.md","dir":"05-03-portable-devices","keywords":"便携设备、移动电话、手持设备、触摸屏、电池、应用商店","subs":[
        ("5.3.1","典型用法","05-03-01-typical-usage.md"),
        ("5.3.2","输入设备","05-03-02-input-devices.md"),
        ("5.3.3","专用游戏手持设备","05-03-03-dedicated-handhelds.md"),
        ("5.3.4","手机和无线设备","05-03-04-mobile-and-wireless-devices.md"),
    ]},
    {"num":"5.4","title":"其他设备","file":"05-04-other-devices.md","keywords":"航空座椅游戏、视频赌博机、街机、位置娱乐系统、小众设备","subs":[]},
    {"num":"5.5","title":"本章总结","file":"05-05-summary.md","keywords":"总结、设备类型、优势弱点、场景、复杂性","subs":[]},
    {"num":"5.6","title":"设计练习——训练","file":"05-06-exercises-training.md","keywords":"训练题、设备类别、游戏类型、零售商店、应用商城","subs":[]},
]

# Normalize malformed split headings before position scan.
clean = re.sub(r"(?m)^5\.3\s*1\s*$\n+^便携设备$", "5.3 便携设备", clean)

positions = []
for sec in sections:
    pat = rf"(?m)^{re.escape(sec['num'])}(?![\d.]).*$"
    m = re.search(pat, clean)
    if not m:
        raise RuntimeError(f"Cannot find heading {sec['num']} {sec['title']}")
    positions.append((sec, m.start(), m.end()))

intro = clean[:positions[0][1]].strip()
for i, (sec, start, heading_end) in enumerate(positions):
    end = positions[i + 1][1] if i + 1 < len(positions) else len(clean)
    sec["body"] = clean[heading_end:end].strip()


def split_subsections(body: str, subs):
    if not subs:
        return {}, body.strip()
    markers = []
    for num, title, filename in subs:
        pat = rf"(?m)^{re.escape(num)}(?![\d.]).*$"
        m = re.search(pat, body)
        if not m:
            raise RuntimeError(f"Cannot find subsection {num} {title}")
        markers.append((num, title, filename, m.start(), m.end()))
    intro_text = body[:markers[0][3]].strip()
    chunks = {}
    for i, (num, title, filename, start, hend) in enumerate(markers):
        end = markers[i + 1][3] if i + 1 < len(markers) else len(body)
        chunks[num] = body[hend:end].strip()
    return chunks, intro_text


def join_ocr_lines(body: str) -> str:
    raw_lines = [line.strip() for line in body.splitlines()]
    blocks = []
    buf = []

    def flush():
        nonlocal buf
        if buf:
            blocks.append("".join(buf))
            buf = []

    for line in raw_lines:
        if not line:
            continue
        if re.match(r"^\d{1,3}$", line):
            continue
        if re.match(r"^\d+\.\s*", line):
            flush()
            blocks.append(line)
            continue
        if line.startswith("#### "):
            flush()
            blocks.append(line)
            continue
        if buf and re.match(r"^[（(《“\"']", line):
            buf.append(line)
        elif buf:
            buf.append(line)
        else:
            buf = [line]
    flush()
    return "\n\n".join(blocks)


def normalize_body(body: str) -> str:
    body = body.strip()
    body = join_ocr_lines(body)
    body = re.sub(r"(?m)^(\d+)\.\s*([^\d\n].*)$", r"#### \1. \2", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 5 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
> 关键词：{keywords}

## 原书内容整理

{body}

## 我的批注区

- 
"""


def guide_md(sec, intro_text):
    intro_text = normalize_body(intro_text) if intro_text.strip() else "本节正文已拆分到侧边栏中的子页面；此页保留为章节导航入口。"
    return f"""---
title: {sec['num']} {sec['title']}
---

# {sec['num']} {sec['title']}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 5 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
> 关键词：{sec['keywords']}

## 原书内容整理

{intro_text}

## 我的批注区

- 
"""

for sec in sections:
    chunks, intro_text = split_subsections(sec["body"], sec.get("subs", []))
    if sec.get("subs"):
        sec_dir = OUT / sec["dir"]
        sec_dir.mkdir(parents=True, exist_ok=True)
        for num, title, filename in sec["subs"]:
            (sec_dir / filename).write_text(page_md(num, title, sec["keywords"], chunks[num]), encoding="utf-8", newline="\n")
        (OUT / sec["file"]).write_text(guide_md(sec, intro_text), encoding="utf-8", newline="\n")
    else:
        (OUT / sec["file"]).write_text(page_md(sec["num"], sec["title"], sec["keywords"], sec["body"]), encoding="utf-8", newline="\n")

chapter_index = f"""---
title: 第 5 章 了解你的游戏设备
---

# 第 5 章 了解你的游戏设备

## 本章定位

本章把游戏概念拉回到具体设备条件中，比较家用游戏机、个人计算机、便携设备和其他专业设备的使用场景、输入输出限制、商业约束与适配重点。

## 复习线索

- 设备不是中性的容器：输入方式、显示距离、屏幕尺寸、处理能力和存储空间都会限定设计范围。
- 家用游戏机强调客厅/卧室场景、本地多人、标准控制器和制造商许可。
- 个人计算机强调键盘鼠标、高分辨率显示、开放开发环境，以及独立游戏和网页游戏两类分发形态。
- 便携设备强调随身使用、短时会话、简单清晰的界面、声音/电池限制和移动分发渠道。
- 小众或专业设备通常有更明确的技术限制和玩家场景，设计时要先理解其特殊约束。
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Wrote Chapter 5 pages to {OUT}")
print(f"pages={len(list(OUT.rglob('*.md')))}")
