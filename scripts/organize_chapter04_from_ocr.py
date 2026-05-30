from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter04_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-04"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 4 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    # Drop recurring page headers/footers.
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^第4章\s*了解你的玩家\s*\d*$", s):
        continue
    if re.match(r"^第4章.*了解你的玩家.*$", s):
        continue
    if s in {"第4章", "了解你的玩家", "游戏设计基础"}:
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "4.1VandenBerghe的5种游戏领域": "4.1 VandenBerghe 的 5 种游戏领域",
    "4.1.1五因素模型": "4.1.1 五因素模型",
    "4.1.25种游戏领域": "4.1.2 5种游戏领域",
    "4.1.3另一个领域：讲故事的态度": "4.1.3 另一个领域：讲故事的态度",
    "4.2人口统计分类": "4.2 人口统计分类",
    "4.2.1男人和女人": "4.2.1 男人和女人",
    "4.2.2\n\n男孩和女孩": "4.2.2 男孩和女孩",
    "4.2.3女孩的游戏": "4.2.3 女孩的游戏",
    "4.3\n\n玩家贡献": "4.3 玩家贡献",
    "4.4二元性思维的危害": "4.4 二元性思维的危害",
    "4.4.1从统计学角度研究玩家群体": "4.4.1 从统计学角度研究玩家群体",
    "4.4.2致力于包容性，而不是普遍性": "4.4.2 致力于包容性，而不是普遍性",
    "4.5本章总结": "4.5 本章总结",
    "4.6设计练习一训练": "4.6 设计练习——训练",
    "设计练习\n\n一习题\n\n4.7": "4.7 设计练习——习题",
    "4.7\n\n为你的游戏选择": "4.7 设计练习——习题\n\n为你的游戏选择",
    "JasonVandenBerghe": "Jason VandenBerghe",
    "VandenBerghe": "VandenBerghe",
    "Ubisof": "Ubisoft",
    "TheBigFive": "The Big Five",
    "Opennesstoexperience": "Openness to experience",
    "facebook": "Facebook",
    "SheriGranerRay": "Sheri Graner Ray",
    "CarolynHandlerMiller": "Carolyn Handler Miller",
    "KayeElling": "Kaye Elling",
    "BlitzGames": "Blitz Games",
    "Bratz：RockAngelz": "Bratz: Rock Angelz",
    "JesycaDurchin": "Jesyca Durchin",
    "HeroicWomentoInspireGameDesigners": "Heroic Women to Inspire Game Designers",
    "FromCasual\n\ntoCore": "From Casual to Core",
    "AStatisticalMechanismforStudyingGamerDedication": "A Statistical Mechanism for Studying Gamer Dedication",
    "bigfivepersonalitytest": "big five personality test",
    "自已": "自己",
    "自标": "目标",
    "投人": "投入",
    "进人": "进入",
    "加人": "加入",
    "一一": "——",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)

clean = clean.replace("口", "- ")
clean = clean.replace("：越偶然", "越偶然")
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"4.1","title":"VandenBerghe 的 5 种游戏领域","file":"04-01-vandenberghe-five-domains.md","dir":"04-01-vandenberghe-five-domains","keywords":"玩家动机、五因素模型、OCEAN、游戏领域、故事态度","subs":[
        ("4.1.1","五因素模型","04-01-01-five-factor-model.md"),
        ("4.1.2","5种游戏领域","04-01-02-five-game-domains.md"),
        ("4.1.3","另一个领域：讲故事的态度","04-01-03-story-attitude.md"),
    ]},
    {"num":"4.2","title":"人口统计分类","file":"04-02-demographics.md","dir":"04-02-demographics","keywords":"人口统计、性别包容、儿童玩家、女孩游戏、目标玩家","subs":[
        ("4.2.1","男人和女人","04-02-01-men-and-women.md"),
        ("4.2.2","男孩和女孩","04-02-02-boys-and-girls.md"),
        ("4.2.3","女孩的游戏","04-02-03-games-for-girls.md"),
    ]},
    {"num":"4.3","title":"玩家贡献","file":"04-03-player-dedication.md","keywords":"玩家贡献、骨灰玩家、休闲玩家、投入度、目标市场","subs":[]},
    {"num":"4.4","title":"二元性思维的危害","file":"04-04-binary-thinking.md","dir":"04-04-binary-thinking","keywords":"二元性思维、玩家群体、统计分布、包容性、排除性元素","subs":[
        ("4.4.1","从统计学角度研究玩家群体","04-04-01-statistical-player-groups.md"),
        ("4.4.2","致力于包容性，而不是普遍性","04-04-02-inclusiveness-not-universality.md"),
    ]},
    {"num":"4.5","title":"本章总结","file":"04-05-summary.md","keywords":"总结、玩家领域、人口统计、贡献程度、包容性","subs":[]},
    {"num":"4.6","title":"设计练习——训练","file":"04-06-exercises-training.md","keywords":"训练题、大五测试、排除性元素、市场特性","subs":[]},
    {"num":"4.7","title":"设计练习——习题","file":"04-07-exercises-questions.md","keywords":"思考题、目标玩家、年龄区间、性别、投入度","subs":[]},
]

# Normalize malformed split heading before position scan.
clean = re.sub(r"(?m)^4\.2\.2\s*$\n+^男孩和女孩$", "4.2.2 男孩和女孩", clean)
clean = re.sub(r"(?m)^4\.3\s*$\n+^玩家贡献$", "4.3 玩家贡献", clean)
clean = re.sub(r"(?m)^4\.7\s*$\n+^为你的游戏选择", "4.7 设计练习——习题\n\n为你的游戏选择", clean)

positions = []
for sec in sections:
    # Match by section number only; OCR heading text can vary slightly.
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
        # Match by subsection number only; OCR heading text can vary slightly.
        pat = rf"(?m)^{re.escape(num)}(?![\d.]).*$"
        m = re.search(pat, body)
        if not m:
            raise RuntimeError(f"Cannot find subsection {num} {title}")
        markers.append((num, title, filename, m.start(), m.end()))
    intro = body[:markers[0][3]].strip()
    chunks = {}
    for i, (num, title, filename, start, hend) in enumerate(markers):
        end = markers[i + 1][3] if i + 1 < len(markers) else len(body)
        chunks[num] = body[hend:end].strip()
    return chunks, intro


def normalize_body(body: str) -> str:
    body = body.strip()
    # Convert numbered internal subheads like 1.性别包容性 / a.女孩... to h4.
    body = re.sub(r"(?m)^(\d+)\.\s*([^\d\n].*)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^([a-z])\.\s*(.+)$", r"#### \1. \2", body)
    body = re.sub(r"(?m)^设计点拨[:：]?(.*)$", r"#### 设计点拨\1", body)
    body = re.sub(r"(?m)^提(《|想|\w)", r"提示：\1", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 4 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
> 关键词：{keywords}

## 原书内容整理

{body}

## 我的批注区

- 
"""


def guide_md(sec, intro):
    intro = normalize_body(intro) if intro.strip() else "本节正文已拆分到侧边栏中的子页面；此页保留为章节导航入口。"
    return f"""---
title: {sec['num']} {sec['title']}
---

# {sec['num']} {sec['title']}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 4 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。  
> 关键词：{sec['keywords']}

## 原书内容整理

{intro}

## 我的批注区

- 
"""

for sec in sections:
    chunks, intro = split_subsections(sec["body"], sec.get("subs", []))
    if sec.get("subs"):
        sec_dir = OUT / sec["dir"]
        sec_dir.mkdir(parents=True, exist_ok=True)
        for num, title, filename in sec["subs"]:
            (sec_dir / filename).write_text(page_md(num, title, sec["keywords"], chunks[num]), encoding="utf-8", newline="\n")
        (OUT / sec["file"]).write_text(guide_md(sec, intro), encoding="utf-8", newline="\n")
    else:
        (OUT / sec["file"]).write_text(page_md(sec["num"], sec["title"], sec["keywords"], sec["body"]), encoding="utf-8", newline="\n")

chapter_index = """---
title: 第 4 章 了解你的玩家
---

# 第 4 章 了解你的玩家

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 4 章。PDF 为扫描版，当前已完成初步 OCR 拆分，后续仍建议逐段人工校对并继续完善图表截图。

## 本章定位

本章讨论以玩家为中心的设计视角：玩家动机、人口统计分类、玩家贡献程度，以及避免用二元性思维误判目标玩家的方法。

## 原书内容整理

第 4 章内容已按原书小节拆分到侧边栏中的页面，便于逐节阅读和批注。

## 我的批注区

- 
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Wrote Chapter 4 pages to {OUT}")
print(f"pages={len(list(OUT.rglob('*.md')))}")
