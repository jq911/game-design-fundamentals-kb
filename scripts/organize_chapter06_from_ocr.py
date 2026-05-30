from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter06_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-06"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 6 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^游戏设计基础\s*\d+$", s):
        continue
    if re.match(r"^第6章\s*通过游戏来盈利\s*\d*$", s):
        continue
    if re.match(r"^第6章.*通过游戏来盈利.*$", s):
        continue
    if s in {"第6章", "通过游戏来盈利", "游戏设计基础"}:
        continue
    if re.match(r"^[A-Za-z]{3,}\d+$", s):
        continue
    if re.match(r"^\d{1,3}\s*$", s):
        continue
    if s == "106汤":
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "一一": "——",
    "自已": "自己",
    "自标": "目标",
    "指辙": "猖獗",
    "庞天": "庞大",
    "惊。": "惊讶。",
    "加人": "加入",
    "充许": "允许",
    "插人": "插入",
    "司时": "同时",
    "好儿个": "好几个",
    "沃尔玛": "沃尔玛",
    "GSCGameWorld": "GSC Game World",
    "AppStore": "App Store",
    "Kickstarter": "Kickstarter",
    "Indiegogo": "Indiegogo",
    "TheDoubleFine": "The Double Fine",
    "MMOG": "MMOG",
    "TheWalkingDead": "The Walking Dead",
    "KentuckyRouteZero": "Kentucky Route Zero",
    "GrimKafka": "Grim Kafka",
    "FinalFantasy": "Final Fantasy",
    "MetalGearSolid": "Metal Gear Solid",
    "PCbang": "PC bang",
    "??": "??",
    "????": "????",
    "??": "Namco",
    "1yd=0.9144m": "1 yd=0.9144 m",
    "6.1直接支付模式": "6.1 直接支付模式",
    "6.1.1零售模式": "6.1.1 零售模式",
    "6.1.2网络销售": "6.1.2 网络销售",
    "6.1.3基于订购的交易模式": "6.1.3 基于订购的交易模式",
    "6.1.4章节销售模式": "6.1.4 章节销售模式",
    "6.1.5众筹": "6.1.5 众筹",
    "6.2＇间接盈利模式": "6.2 间接盈利模式",
    "6.2间接盈利模式": "6.2 间接盈利模式",
    "6.2.1免费增值游戏": "6.2.1 免费增值游戏",
    "6.2.2免费游戏模式": "6.2.2 免费游戏模式",
    "6.2.3广告与赞助": "6.2.3 广告与赞助",
    "6.2.4命题游戏": "6.2.4 命题游戏",
    "6.3世界游戏市场": "6.3 世界游戏市场",
    "：6.3.1传统游戏市场": "6.3.1 传统游戏市场",
    "6.3.1传统游戏市场": "6.3.1 传统游戏市场",
    "6.3.2新兴市场": "6.3.2 新兴市场",
    "6.4本章总结": "6.4 本章总结",
    "6.5设计练习\n\n一习题": "6.5 设计练习——习题",
    "6.5设计练习一习题": "6.5 设计练习——习题",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"6.1","title":"直接支付模式","file":"06-01-direct-payment-models.md","dir":"06-01-direct-payment-models","keywords":"直接支付、零售、网络销售、订购、章节销售、众筹","subs":[
        ("6.1.1","零售模式","06-01-01-retail-model.md"),
        ("6.1.2","网络销售","06-01-02-online-sales.md"),
        ("6.1.3","基于订购的交易模式","06-01-03-subscription-model.md"),
        ("6.1.4","章节销售模式","06-01-04-episodic-sales.md"),
        ("6.1.5","众筹","06-01-05-crowdfunding.md"),
    ]},
    {"num":"6.2","title":"间接盈利模式","file":"06-02-indirect-revenue-models.md","dir":"06-02-indirect-revenue-models","keywords":"间接盈利、免费增值、免费游戏、广告、赞助、命题游戏","subs":[
        ("6.2.1","免费增值游戏","06-02-01-freemium-games.md"),
        ("6.2.2","免费游戏模式","06-02-02-free-to-play-model.md"),
        ("6.2.3","广告与赞助","06-02-03-advertising-and-sponsorship.md"),
        ("6.2.4","命题游戏","06-02-04-commissioned-games.md"),
    ]},
    {"num":"6.3","title":"世界游戏市场","file":"06-03-world-game-markets.md","dir":"06-03-world-game-markets","keywords":"世界市场、传统市场、新兴市场、本地化、文化限制","subs":[
        ("6.3.1","传统游戏市场","06-03-01-traditional-markets.md"),
        ("6.3.2","新兴市场","06-03-02-emerging-markets.md"),
    ]},
    {"num":"6.4","title":"本章总结","file":"06-04-summary.md","keywords":"总结、盈利模式、销售地区、设计影响、游戏理念","subs":[]},
    {"num":"6.5","title":"设计练习——习题","file":"06-05-exercises-questions.md","keywords":"习题、资金来源、推广计划、盈利方式、市场选择","subs":[]},
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
        if re.match(r"^\d+\.\s*", line):
            flush()
            blocks.append(line)
            continue
        if re.match(r"^[a-zA-Z]\.\s*", line):
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
    body = body.replace("???????????", "\n\n#### ???????????\n\n")
    body = re.sub(r"(?m)^(\d+)\.\s*([^\d\n].*)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^([a-zA-Z])\.\s*(.+)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^花钱就能赢：一个坏主意$", r"#### 花钱就能赢：一个坏主意", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 6 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 6 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
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
title: 第 6 章 通过游戏来盈利
---

# 第 6 章 通过游戏来盈利

## 本章定位

本章从商业模式角度讨论游戏设计：游戏如何收费、如何推广、由谁资助、面向哪个市场，都会反过来影响设计目标、内容节奏、更新方式、玩家公平性和本地化策略。

## 复习线索

- 直接支付模式包括零售、网络销售、订购、章节销售和众筹，它们分别带来不同的资金、风险和自由度。
- 间接盈利模式包括免费增值、免费游戏、广告赞助和命题游戏，需要特别注意付费点与玩家体验、公平性的关系。
- “花钱就能赢”会破坏多人游戏的公平基础，是商业设计影响玩法伦理的典型例子。
- 世界市场不只是语言差异，还包含文化品味、审查制度、经济能力、平台习惯和本地化成本。
- 在构思游戏理念时，盈利方式和目标市场应尽早进入设计约束，而不是开发完成后才补充考虑。
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Wrote Chapter 6 pages to {OUT}")
print(f"pages={len(list(OUT.rglob('*.md')))}")
