from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter07_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-07"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 7 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^游戏设计基础\s*\d+$", s):
        continue
    if re.match(r"^第7章\s*游戏概念\s*\d*$", s):
        continue
    if re.match(r"^第7章.*游戏概念.*$", s):
        continue
    if s in {"第7章", "游戏概念", "游戏设计基础"}:
        continue
    if re.match(r"^[A-Za-z]{3,}\d+$", s):
        continue
    if re.match(r"^\d{1,3}\s*$", s):
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "一一": "——",
    "自已": "自己",
    "儿分钟": "几分钟",
    "题自": "题目",
    "玩要": "玩耍",
    "米取": "采取",
    "任么样": "什么样",
    "司法管辖区": "司法管辖区",
    "诽谤": "诽谤",
    "谤或": "诽谤或",
    "表象性媒体": "表现性媒体",
    "APatternLanguage": "A Pattern Language",
    "UniqueSellingPoints": "Unique Selling Points",
    "MosesOyeleye": "Moses Oyeleye",
    "LegendofZelda": "Legend of Zelda",
    "PuzzleQuest": "Puzzle Quest",
    "TombRaidergame": "Tomb Raider game",
    "7.1获得一个创意": "7.1 获得一个创意",
    "7.1.1\n\n梦想着梦想": "7.1.1 梦想着梦想",
    "7.1.1梦想着梦想": "7.1.1 梦想着梦想",
    "7.1.2来自其他媒体的游戏创意": "7.1.2 来自其他媒体的游戏创意",
    "7.1.3来自其他游戏的游戏创意": "7.1.3 来自其他游戏的游戏创意",
    "7.1.4如何进行头脑风暴": "7.1.4 如何进行头脑风暴",
    "7.1.5和其他人交流你的梦想": "7.1.5 和其他人交流你的梦想",
    "7.2从创意到游戏概念": "7.2 从创意到游戏概念",
    "7.2.1玩家的角色": "7.2.1 玩家的角色",
    "7.2.2\n\n游戏类型和混合体": "7.2.2 游戏类型和混合体",
    "7.2.2游戏类型和混合体": "7.2.2 游戏类型和混合体",
    "7.2.3定义你的目标人群": "7.2.3 定义你的目标人群",
    "7.2.4游戏进度考虑": "7.2.4 游戏进度考虑",
    "7.3本章总结": "7.3 本章总结",
    "7.4设计练习\n\nJ一训练": "7.4 设计练习——训练",
    "7.4设计练习J一训练": "7.4 设计练习——训练",
    "7.51\n\n设计练习一习题": "7.5 设计练习——习题",
    "7.5设计练习一习题": "7.5 设计练习——习题",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"7.1","title":"获得一个创意","file":"07-01-getting-an-idea.md","dir":"07-01-getting-an-idea","keywords":"创意来源、梦想、其他媒体、其他游戏、头脑风暴、交流愿景","subs":[
        ("7.1.1","梦想着梦想","07-01-01-dreaming-dreams.md"),
        ("7.1.2","来自其他媒体的游戏创意","07-01-02-ideas-from-other-media.md"),
        ("7.1.3","来自其他游戏的游戏创意","07-01-03-ideas-from-other-games.md"),
        ("7.1.4","如何进行头脑风暴","07-01-04-brainstorming.md"),
        ("7.1.5","和其他人交流你的梦想","07-01-05-communicating-your-dream.md"),
    ]},
    {"num":"7.2","title":"从创意到游戏概念","file":"07-02-from-idea-to-game-concept.md","dir":"07-02-from-idea-to-game-concept","keywords":"游戏概念、高级概念文档、玩家角色、游戏类型、目标人群、游戏进度","subs":[
        ("7.2.1","玩家的角色","07-02-01-player-role.md"),
        ("7.2.2","游戏类型和混合体","07-02-02-genres-and-hybrids.md"),
        ("7.2.3","定义你的目标人群","07-02-03-defining-target-audience.md"),
        ("7.2.4","游戏进度考虑","07-02-04-progression-considerations.md"),
    ]},
    {"num":"7.3","title":"本章总结","file":"07-03-summary.md","keywords":"总结、游戏概念、高级概念文档、玩家角色、目标人群","subs":[]},
    {"num":"7.4","title":"设计练习——训练","file":"07-04-exercises-training.md","keywords":"训练题、高级概念文档、玩家角色、混合型游戏","subs":[]},
    {"num":"7.5","title":"设计练习——习题","file":"07-05-exercises-questions.md","keywords":"习题、游戏概念、玩家角色、化身、玩法、目标玩家、设备、背景、关卡、剧情","subs":[]},
]

positions = []
for sec in sections:
    pat = rf"(?m)^{re.escape(sec['num'])}(?![\d.]).*$"
    m = re.search(pat, clean)
    if not m:
        raise RuntimeError(f"Cannot find heading {sec['num']} {sec['title']}")
    positions.append((sec, m.start(), m.end()))

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
        if line.startswith("图7-"):
            flush()
            blocks.append(line)
            continue
        if line.startswith("口"):
            flush()
            blocks.append("- " + line[1:].strip())
            continue
        if re.match(r"^\d+\.\s*", line):
            flush()
            blocks.append(line)
            continue
        if re.match(r"^[a-zA-Z]\.\s*", line):
            flush()
            blocks.append(line)
            continue
        if line.startswith(("设计点拨：", "提示：", "供你参考")):
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
    body = body.replace("提许可和知识产权法不在本书的讨论范围之内。", "提示：许可和知识产权法不在本书的讨论范围之内。")
    body = body.replace("提使用高级概念文档的方法来介绍游戏的一个实用技巧就是，", "提示：使用高级概念文档的方法来介绍游戏的一个实用技巧就是，")
    body = body.replace("提如果能很容易地解释玩家所扮演的角色，", "提示：如果能很容易地解释玩家所扮演的角色，")
    body = body.replace("供你参考以玩家为中心的哲学和目标人群", "#### 供你参考：以玩家为中心的哲学和目标人群")
    body = re.sub(r"(?m)^设计点拨：(.+)$", r"#### 设计点拨：\1", body)
    body = re.sub(r"(?m)^(\d+)\.\s*([^\d\n].*)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^([a-zA-Z])\.\s*(.+)$", r"#### \1. \2", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 7 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 7 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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

chapter_index = """---
title: 第 7 章 游戏概念
---

# 第 7 章 游戏概念

## 本章定位

本章讨论如何把最初的游戏创意推进为可以沟通、评估和继续开发的游戏概念，重点包括创意来源、玩家角色、游戏类型、目标人群、进度结构与高级概念文档。

## 复习线索

- 游戏创意可以来自梦想、其他媒体、其他游戏和头脑风暴，但创意本身还不足以成为游戏概念。
- 把创意转化为概念时，首先要回答“玩家会做什么”和“玩家扮演什么角色”。
- 高级概念文档需要概括游戏内容、玩家角色、模式、类型、目标人群、设备、商业方式和整体流程。
- 类型和混合类型可以帮助沟通预期，但不应在概念阶段过早限制创造力。
- 目标人群和游戏进度结构会影响游戏体验、关卡安排、故事需求和后续设计细节。
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Wrote Chapter 7 pages to {OUT}")
print(f"pages={len(list(OUT.rglob('*.md')))}")
