from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter09_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-09"
OUT.mkdir(parents=True, exist_ok=True)

text = RAW.read_text(encoding="utf-8")

lines = []
for line in text.splitlines():
    s = line.strip()
    if not s:
        lines.append("")
        continue
    if s.startswith("# 第 9 章 OCR 原始文本") or s.startswith("> 来源"):
        continue
    if re.match(r"^## 书内页 .* / PDF 页 .*$", s):
        lines.append("")
        continue
    if re.match(r"^\d+\s*游戏设计基础$", s):
        continue
    if re.match(r"^游戏设计基础\s*\d+$", s):
        continue
    if re.match(r"^第9章\s*创造型和表现型玩法\s*\d*$", s) or re.match(r"^第9章.*创造型和表现型玩法.*$", s):
        continue
    if s in {"第9章", "创造型和表现型玩法", "游戏设计基础"}:
        continue
    if re.match(r"^\d{1,3}\s*$", s):
        continue
    lines.append(s)

clean = "\n".join(lines)
clean = re.sub(r"\n{3,}", "\n\n", clean)

replacements = {
    "自已": "自己",
    "充许": "允许",
    "深人": "深入",
    "眼晴": "眼睛",
    "自前": "目前",
    "儿种": "几种",
    "儿乎": "几乎",
    "儿小时": "几小时",
    "较天地": "较大地",
    "作彝": "作弊",
    "辩别": "辨别",
    "自标": "目标",
    "天人物": "大人物",
    "陷易受攻击": "陷入易受攻击",
    "掷般子": "掷骰子",
    "魔法\n\n和体质": "魔力\n\n和体质",
    "《Mi朋友》": "《Mii 朋友》",
    "潼没": "湮没",
    "《蒙华弹珠》": "《梦幻弹珠》",
    "沙箱模型": "沙盒模式",
    "Gamasutradeveloper": "Gamasutra Developer",
    "JasonRohrer": "Jason Rohrer",
    "AdobePremiere": "Adobe Premiere",
    "RichardRouse": "Richard Rouse",
    "avatarselection": "avatar selection",
    "avatarcustomization": "avatar customization",
    "avatarconstruction": "avatar construction",
    "functionalattribute": "functional attribute",
    "statusattribute": "status attribute",
    "sandboxmode": "sandbox mode",
    "freeform-creativeplay": "freeform creative play",
    "NPC“客户”": "NPC“客户”",
    "一一": "——",
    "—一": "——",
    "9.1自定义型玩法": "9.1 自定义型玩法",
    "9.1.1个性表达的形式": "9.1.1 个性表达的形式",
    "9.1.2了解属性": "9.1.2 了解属性",
    "9.1.3功能属性": "9.1.3 功能属性",
    "9.1.4装饰属性": "9.1.4 装饰属性",
    "9.2\n\n创造型玩法": "9.2 创造型玩法",
    "9.2.1受限的创造型玩法": "9.2.1 受限的创造型玩法",
    "9.2.2自由创造型玩法和沙盒模式": "9.2.2 自由创造型玩法和沙盒模式",
    "9.3其他的表达形式": "9.3 其他的表达形式",
    "9.3.1角色扮演": "9.3.1 角色扮演",
    "9.3.2故事叙述": "9.3.2 故事叙述",
    "9.4\n\n游戏修改": "9.4 游戏修改",
    "9.4.1关卡编辑器": "9.4.1 关卡编辑器",
    "9.4.2机器人": "9.4.2 机器人",
    "9.5本章总结": "9.5 本章总结",
    "9.6设计练习——训练": "9.6 设计练习——训练",
    "9.7设计练习——习题": "9.7 设计练习——习题",
    "1.受经济限制的玩法": "1. 受经济限制的玩法",
    "2.按照物理标准创造": "2. 按照物理标准创造",
    "3.按照美学标准创造": "3. 按照美学标准创造",
}
for a, b in replacements.items():
    clean = clean.replace(a, b)
clean = re.sub(r"\n{3,}", "\n\n", clean).strip()

sections = [
    {"num":"9.1","title":"自定义型玩法","file":"09-01-customization-gameplay.md","keywords":"自定义型玩法、化身、属性、功能属性、装饰属性"},
    {"num":"9.2","title":"创造型玩法","file":"09-02-creative-gameplay.md","keywords":"创造型玩法、受限创造、自由创造、沙盒模式、分享"},
    {"num":"9.3","title":"其他的表达形式","file":"09-03-other-expressive-forms.md","keywords":"表达形式、角色扮演、故事叙述、化身、玩家创作"},
    {"num":"9.4","title":"游戏修改","file":"09-04-game-modifications.md","keywords":"游戏修改、mods、关卡编辑器、机器人、玩家工具"},
    {"num":"9.5","title":"本章总结","file":"09-05-summary.md","keywords":"总结、自我表达、创造型玩法、游戏修改"},
    {"num":"9.6","title":"设计练习——训练","file":"09-06-exercises-training.md","keywords":"训练题、属性、创造型玩法、美学规则"},
    {"num":"9.7","title":"设计练习——习题","file":"09-07-exercises-questions.md","keywords":"习题、自定义、创造型玩法、角色扮演、游戏修改"},
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

ASSET = "../../../assets/book-images/game-design-fundamentals/chapter-09"

def fig_html(token, filename, caption):
    return f'''<figure class="book-figure">
  <img src="{ASSET}/{filename}" alt="{token} {caption}" loading="lazy">
  <figcaption>{token}　{caption}</figcaption>
</figure>'''

figs = {
    "图9-1": ("figure-9-1-rollercoaster-tycoon-track-designer.png", "《过山车大亨 2》的过山车跑道设计界面"),
    "图9-2": ("figure-9-2-draw-something.png", "《你画我猜》"),
}


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
        if line.startswith(("图9-", "表9-")):
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
        if re.match(r"^\d+[,.，、]\s*", line) or re.match(r"^\d+\.\s+", line):
            flush()
            blocks.append(line)
            continue
        if re.match(r"^9\.\d+\.\d+\s+", line):
            flush()
            blocks.append(line)
            continue
        if line.startswith(("提", "开发实例：", "允许mods存在的危险")):
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
    body = join_ocr_lines(body.strip())
    body = body.replace("提如果玩家选择人物或设置属性会影响游戏，那么你必须对玩家做出合理的说明。", "提示：如果玩家选择人物或设置属性会影响游戏，那么你必须对玩家做出合理的说明。")
    body = body.replace("提育碧（Ubisoft）出品的《想象：时装设计师》实施固定规则机制，但这样做的后果", "提示：育碧（Ubisoft）出品的《想象：时装设计师》实施固定规则机制，但这样做的后果")
    body = re.sub(r"(?m)^提示：(.+)$", r"#### 提示：\1", body)
    body = re.sub(r"(?m)^开发实例：(.+)$", r"#### 开发实例：\1", body)
    body = re.sub(r"(?m)^允许mods存在的危险$", r"#### 允许 mods 存在的危险", body)
    body = re.sub(r"(?m)^(9\.\d+\.\d+)\s+(.+)$", r"### \1 \2", body)
    body = re.sub(r"(?m)^(\d+)\.\s+([^\d\n].*)$", r"#### \1. \2", body)
    body = body.replace("图9-1《过山车大亨2》的过山车跑道设计界面", fig_html("图9-1", *figs["图9-1"]))
    body = body.replace("图9-2《你画我猜》", fig_html("图9-2", *figs["图9-2"]))
    # If OCR caption spacing differs, remove leftovers after insertion.
    body = re.sub(r"\n图9-[12][^\n]*", "\n", body)
    body = body.replace("《过山车大亨2》", "《过山车大亨 2》")
    body = body.replace("《半条命2》", "《半条命 2》")
    body = body.replace("《雷神之锤3：竞技场》", "《雷神之锤 3：竞技场》")
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def page_md(num, title, keywords, body):
    body = normalize_body(body)
    return f"""---
title: {num} {title}
---

# {num} {title}

> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 9 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。
> 关键词：{keywords}

## 原书内容整理

{body}

## 我的批注区

-
"""

for sec in sections:
    (OUT / sec["file"]).write_text(page_md(sec["num"], sec["title"], sec["keywords"], sec["body"]), encoding="utf-8", newline="\n")

chapter_index = """---
title: 第 9 章 创造型和表现型玩法
---

# 第 9 章 创造型和表现型玩法

## 本章定位

本章讨论玩家如何在游戏中表达自我与创造内容：从化身选择、定制和构造，到受限创造、自由创造、角色扮演、故事叙述，以及通过关卡编辑器、mods 和机器人扩展游戏本身。

## 复习线索

- 自定义型玩法让玩家通过化身选择、化身定制和化身构造表达个性。
- 属性可以分成功能属性和装饰属性；前者影响核心机制，后者主要影响外观和身份表达。
- 创造型玩法可以受经济、物理或美学规则限制，也可以以沙盒模式提供更自由的工具体验。
- 角色扮演和故事叙述是非物质建造型的表达形式，依赖化身表现、对话、截图、视频或文本记录等系统支持。
- 游戏修改、关卡编辑器和机器人把部分设计能力交给玩家，但也带来内容风险、工具质量和知识产权问题。
"""
(OUT / "index.md").write_text(chapter_index, encoding="utf-8", newline="\n")

print(f"Generated {len(list(OUT.rglob('*.md')))} markdown files in {OUT}")
