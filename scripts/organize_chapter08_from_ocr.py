from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter08_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-08"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 8 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^游戏设计基础\s*\d+$", s):
        continue
    if re.match(r"^第8章\s*游戏世界\s*\d*$", s) or re.match(r"^第8章.*游戏世界.*$", s):
        continue
    if s in {"第8章", "游戏世界", "游戏设计基础"}:
        continue
    if re.match(r"^\d{1,3}\s*$", s):
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "一一": "——",
    "一一译者注": "——译者注",
    "已": "已",
    "自已": "自己",
    "自己已": "自己",
    "儿乎": "几乎",
    "儿小时": "几小时",
    "儿秒钟": "几秒钟",
    "儿百个": "几百个",
    "更天": "更大",
    "程序染": "程序渲染",
    "叠夜制": "昼夜制",
    "自前": "目前",
    "贫瘩": "贫瘠",
    "重一架": "中，一架",
    "一胶眼": "一眨眼",
    "体制": "体系",
    "打跨": "打垮",
    "执择": "抉择",
    "天部分": "大部分",
    "插人": "插入",
    "愚味": "愚昧",
    "顶蜂": "顶峰",
    "考去除": "考虑去除",
    "TheBlueDanube": "The Blue Danube",
    "J.R.RTolkien": "J. R. R. Tolkien",
    "AmericanBroadcasting": "American Broadcasting",
    "WideWorldofSports": "Wide World of Sports",
    "BethesdaSoftworks": "Bethesda Softworks",
    "first-personshooter": "first-person shooter",
    "OculusRift": "Oculus Rift",
    "LucasArts": "LucasArts",
    "Maxis小组": "Maxis 小组",
    "BlueByte": "Blue Byte",
    "Activision（动视）公司": "Activision（动视）公司",
    "8.1什么是游戏世界": "8.1 什么是游戏世界",
    "8.2\n\n游戏世界的目的": "8.2 游戏世界的目的",
    "8.2游戏世界的目的": "8.2 游戏世界的目的",
    "8.3\n\n游戏世界的维度": "8.3 游戏世界的维度",
    "8.3游戏世界的维度": "8.3 游戏世界的维度",
    "8.3.1物理维度": "8.3.1 物理维度",
    "8.3.2时间维度": "8.3.2 时间维度",
    "8.3.3环境维度": "8.3.3 环境维度",
    "8.3.4感情维度": "8.3.4 感情维度",
    "8.3.5\n\n道德维度": "8.3.5 道德维度",
    "8.3.5道德维度": "8.3.5 道德维度",
    "8.4现实主义": "8.4 现实主义",
    "8.5本章总结": "8.5 本章总结",
    "8.6设计练习—一训练": "8.6 设计练习——训练",
    "8.6设计练习——训练": "8.6 设计练习——训练",
    "8.7设计练习一一习题": "8.7 设计练习——习题",
    "8.7设计练习——习题": "8.7 设计练习——习题",
    "1.空间维度": "1. 空间维度",
    "·2.大小": "2. 大小",
    "2.大小": "2. 大小",
    "3.界限": "3. 界限",
    "1.可变的时间": "1. 可变的时间",
    "2.反常的时间": "2. 反常的时间",
    "3.让玩家调整时间": "3. 让玩家调整时间",
    "1.文化背景": "1. 文化背景",
    "2.物理环境": "2. 物理环境",
    "3.细节": "3. 细节",
    "4.定义一种风格": "4. 定义一种风格",
    "5.过度使用背景": "5. 过度使用背景",
    "6.灵感来源": "6. 灵感来源",
    "1.影响游戏者的感情": "1. 影响游戏者的感情",
    "2.娱乐的局限性": "2. 娱乐的局限性",
    "3.不能用数字来描述情感": "3. 不能用数字来描述情感",
    "1.道德决策": "1. 道德决策",
    "2.关于游戏暴力的看法": "2. 关于游戏暴力的看法",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"8.1","title":"什么是游戏世界","file":"08-01-what-is-game-world.md","keywords":"游戏世界、魔法圈、想象空间、环境、抽象游戏","subs":[]},
    {"num":"8.2","title":"游戏世界的目的","file":"08-02-purpose-of-game-world.md","keywords":"娱乐价值、幻想、探索、互动环境、销售吸引力","subs":[]},
    {"num":"8.3","title":"游戏世界的维度","file":"08-03-dimensions-of-game-world.md","dir":"08-03-dimensions-of-game-world","keywords":"物理维度、时间维度、环境维度、感情维度、道德维度","subs":[
        ("8.3.1","物理维度","08-03-01-physical-dimension.md"),
        ("8.3.2","时间维度","08-03-02-time-dimension.md"),
        ("8.3.3","环境维度","08-03-03-environmental-dimension.md"),
        ("8.3.4","感情维度","08-03-04-emotional-dimension.md"),
        ("8.3.5","道德维度","08-03-05-moral-dimension.md"),
    ]},
    {"num":"8.4","title":"现实主义","file":"08-04-realism.md","keywords":"现实主义、抽象、仿真、娱乐性、设计目标","subs":[]},
    {"num":"8.5","title":"本章总结","file":"08-05-summary.md","keywords":"总结、游戏世界、维度、现实主义、幻想世界","subs":[]},
    {"num":"8.6","title":"设计练习——训练","file":"08-06-exercises-training.md","keywords":"训练题、情感基调、道德系统、游戏世界分析","subs":[]},
    {"num":"8.7","title":"设计练习——习题","file":"08-07-exercises-questions.md","keywords":"习题、物理维度、时间维度、环境维度、感情维度、道德维度","subs":[]},
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
        if line.startswith(("图8-", "表8-")):
            flush()
            blocks.append(line)
            continue
        if line.startswith(("①", "②", "③")):
            flush()
            blocks.append(line)
            continue
        if line.startswith(("口", "·")):
            flush()
            blocks.append("- " + line[1:].strip())
            continue
        if re.match(r"^\d+[,.，、]\s*", line):
            flush()
            blocks.append(line)
            continue
        if re.match(r"^\d+\.\s+", line):
            flush()
            blocks.append(line)
            continue
        if line.startswith(("设计点拨：", "提示：", "提", "韦佛定律：", "《美国陆军》独特的道德准则")):
            flush()
            blocks.append(line)
            continue
        if buf:
            buf.append(line)
        else:
            buf = [line]
    flush()
    return "\n\n".join(blocks)


def normalize_body(body: str) -> str:
    body = body.strip()
    body = join_ocr_lines(body)
    body = body.replace("提“子弹时间”", "提示：“子弹时间”")
    body = body.replace("提艺术风格的选择", "提示：艺术风格的选择")
    body = body.replace("提如果你喜欢数学", "提示：如果你喜欢数学")
    body = body.replace("提严肃的游戏通常", "提示：严肃的游戏通常")
    body = re.sub(r"(?m)^设计点拨：(.+)$", r"#### 设计点拨：\1", body)
    body = re.sub(r"(?m)^提示：(.+)$", r"#### 提示：\1", body)
    body = re.sub(r"(?m)^韦佛定律：(.+)$", r"> 韦佛定律：\1", body)
    body = re.sub(r"(?m)^《美国陆军》独特的道德准则$", r"#### 《美国陆军》独特的道德准则", body)
    body = re.sub(r"(?m)^(\d+)\.\s+([^\d\n].*)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^(\d+)[,，、]\s*(.+)$", r"#### \1. \2", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 8 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 8 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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
title: 第 8 章 游戏世界
---

# 第 8 章 游戏世界

## 本章定位

本章讨论游戏世界的定义、用途和设计维度，说明游戏世界如何通过物理、时间、环境、感情、道德和现实主义等层面共同支撑玩家的幻想与游戏可玩性。

## 复习线索

- 游戏世界是玩家进入魔法圈后愿意相信的想象空间，不只是画面和声音的总和。
- 游戏世界既能提供探索和互动的乐趣，也能成为吸引玩家购买和进入游戏的核心幻想。
- 物理维度决定空间、规模和边界；时间维度决定时间如何流逝、跳跃或被玩家调整。
- 环境维度涉及文化背景、物理环境、细节、风格和灵感来源，是艺术与音频设计的基础。
- 感情维度与道德维度决定玩家在世界中会产生怎样的情绪，以及什么行为被奖励或惩罚。
- 现实主义不是单一指标，而是不同设计层面在“抽象—写实”之间的取舍。
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Generated {len(list(OUT.rglob('*.md')))} markdown files in {OUT}")
