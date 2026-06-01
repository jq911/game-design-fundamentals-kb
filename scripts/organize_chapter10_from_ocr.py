from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
RAW = ROOT / "ocr_pages" / "chapter10_raw.md"
OUT = ROOT / "docs" / "game-design-fundamentals" / "chapter-10"
OUT.mkdir(parents=True, exist_ok=True)

raw_lines = RAW.read_text(encoding="utf-8").splitlines()

PAGES = [
    ("index.md", "第 10 章 角色开发"),
    ("10-01-character-design-goals.md", "10.1 角色设计的目标"),
    ("10-02-player-task-model.md", "10.2 玩家和任务模型之间的关系"),
    ("10-03-visual-appearance.md", "10.3 视觉外表"),
    ("10-04-character-depth.md", "10.4 创作角色的深度"),
    ("10-05-audio-design.md", "10.5 音频设计"),
    ("10-06-summary.md", "10.6 本章总结"),
    ("10-07-exercises-training.md", "10.7 设计练习：训练"),
    ("10-08-exercises-questions.md", "10.8 设计练习：习题"),
]

RANGES = {
    "10-01-character-design-goals.md": (33, 104),
    "10-02-player-task-model.md": (105, 314),
    "10-03-visual-appearance.md": (315, 818),
    "10-04-character-depth.md": (819, 1276),
    "10-05-audio-design.md": (1277, 1448),
    "10-06-summary.md": (1449, 1460),
    "10-07-exercises-training.md": (1461, 1512),
    "10-08-exercises-questions.md": (1513, len(raw_lines)),
}

SUBHEADINGS = {
    "10.2.1玩家设计的化身角色": "### 10.2.1 玩家设计的化身角色",
    "10.2.2指定化身和非指定化身": "### 10.2.2 指定化身和非指定化身",
    "10.2.3不同控制机制的效果": "### 10.2.3 不同控制机制的效果",
    "10.2.4设计你自己的化身角色": "### 10.2.4 设计你自己的化身角色",
    "10.3.1角色身体类型": "### 10.3.1 角色身体类型",
    "10.3.2衣着、武器、标志性物品和名字": "### 10.3.2 衣着、武器、标志性物品和名字",
    "10.3.3": "### 10.3.3 调色板",
    "10.3.4同伴": "### 10.3.4 同伴",
    "10.3.5": "### 10.3.5 其他视觉设计资源",
    "10.4.1作用、态度和价值": "### 10.4.1 作用、态度和价值",
    "10.4.2属性": "### 10.4.2 属性",
    "10.4.3人物维度": "### 10.4.3 人物维度",
    "10.4.4角色成长": "### 10.4.4 角色成长",
    "10.4.5人物原型": "### 10.4.5 人物原型",
    "10.5.1音效和音乐": "### 10.5.1 音效和音乐",
    "10.5.2声音和语言": "### 10.5.2 声音和语言",
}

FIGURES = {
    "图10-1《指环王Online》为玩家创建他们自己的化身提供了很多选项": '''<figure class="book-figure">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-1-lotro-avatar-creation.png" alt="图10-1 《指环王 Online》为玩家创建自己的化身提供选项" loading="lazy">
  <figcaption>图10-1　《指环王 Online》为玩家创建自己的化身提供选项</figcaption>
</figure>''',
    "图10-2电子游戏和其他媒介上的一些卡通角色": '''<figure class="book-figure">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-2-cartoon-characters.png" alt="图10-2 电子游戏和其他媒介上的一些卡通角色" loading="lazy">
  <figcaption>图10-2　电子游戏和其他媒介上的一些卡通角色</figcaption>
</figure>''',
    "图10-3一个虚构的蒙古女骑手的概念艺术": '''<figure class="book-figure book-figure--narrow">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-3-mongolian-rider-concept-art.png" alt="图10-3 一个虚构的蒙古女骑手的概念艺术" loading="lazy">
  <figcaption>图10-3　一个虚构的蒙古女骑手的概念艺术</figcaption>
</figure>''',
    "图10-4游戏《人生如戏》中的人物埃德加的模型板": '''<figure class="book-figure">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-4-edgar-model-sheet.png" alt="图10-4 游戏《人生如戏》中的人物埃德加的模型板" loading="lazy">
  <figcaption>图10-4　游戏《人生如戏》中的人物埃德加的模型板</figcaption>
</figure>''',
    "图10-5《力量高尔夫》是一款包含了真实角色开发的运动游戏": '''<figure class="book-figure">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-5-power-golf-character-development.png" alt="图10-5 《力量高尔夫》是一款包含真实角色开发的运动游戏" loading="lazy">
  <figcaption>图10-5　《力量高尔夫》是一款包含真实角色开发的运动游戏</figcaption>
</figure>''',
    "图10-6": '''<figure class="book-figure book-figure--narrow">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-6-zero-dimensional-character.png" alt="图10-6 零维度角色的感情状态" loading="lazy">
  <figcaption>图10-6　零维度角色只有离散的感情状态</figcaption>
</figure>''',
    "图10-7一维角色的感情状态是一个会随时间变化的单一变量": '''<figure class="book-figure book-figure--narrow">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-7-one-dimensional-character.png" alt="图10-7 一维角色的感情状态是随时间变化的单一变量" loading="lazy">
  <figcaption>图10-7　一维角色的感情状态是随时间变化的单一变量</figcaption>
</figure>''',
    "图10-8二维角色有多个且相互不冲突的感情状态": '''<figure class="book-figure book-figure--narrow">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-8-two-dimensional-character.png" alt="图10-8 二维角色有多个且相互不冲突的感情状态" loading="lazy">
  <figcaption>图10-8　二维角色有多个且相互不冲突的感情状态</figcaption>
</figure>''',
    "图10-9": '''<figure class="book-figure book-figure--narrow">
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-10/figure-10-9-three-dimensional-character.png" alt="图10-9 三维角色可能拥有相互冲突的感情状态" loading="lazy">
  <figcaption>图10-9　三维角色可能拥有相互冲突的感情状态，并产生前后矛盾的行为</figcaption>
</figure>''',
}

REPL = {
    "一一": "——",
    "自已": "自己",
    "充许": "允许",
    "深人": "深入",
    "衣看": "衣着",
    "鑫笨": "笨拙",
    "增恨": "憎恨",
    "避好": "嗜好",
    "丑脑": "丑陋",
    "血握": "血腥",
    "方不得已": "万不得已",
    "本王化": "本地化",
    "打栗子": "松鼠库克倒霉的一天",
    "ArctumsMengsk": "Arcturus Mengsk",
    "JimRaynor": "Jim Raynor",
    "WilliamVaughan": "William Vaughan",
    "GeorgeMaestri": "George Maestri",
    "KarenCollins": "Karen Collins",
    "FredericWertham": "Frederic Wertham",
    "StevenPoole": "Steven Poole",
    "CarlJung": "Carl Jung",
    "BjornHurri": "Bjorn Hurri",
    "characterizationattribute": "characterization attribute",
    "statusattribute": "status attribute",
    "HitPoint": "Hit Point",
    "Hero'sJourney": "Hero's Journey",
    "conceptart": "concept art",
    "modelsheet": "model sheet",
    "3dsMax": "3ds Max",
    "art-drivencharacterdesign": "art-driven character design",
    "Maxis小组": "Maxis 小组",
}

SKIP_EXACT = {
    "第10章", "角色开发", "角色设计的目标", "玩家和任务模型之间的关系", "视觉外表",
    "创作角色的深度", "音频设计", "本章总结", "训练", "设计练习", "一习题",
    "调色板", "其他视觉设计资源", "VTadikkawieethis", "Seq. 12", "Page 4", "Edgar", "Clean-Up Modcel",
}


def clean(s: str) -> str:
    s = s.strip()
    for a, b in REPL.items():
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s


def should_skip(s: str) -> bool:
    if not s:
        return True
    if s in FIGURES:
        return False
    if s in SKIP_EXACT:
        return True
    if s.startswith("## 书内页") or s.startswith("第10章角色开发"):
        return True
    if re.fullmatch(r"\d+", s) or re.fullmatch(r"\d+游戏设计基础", s) or s == "游戏设计基础":
        return True
    if re.fullmatch(r"10\.[12358]", s):
        return True
    if s.startswith(("?", "e美国", "日本最具影响力", "VTadikkawieethis", "aldtoit", "aaxrighu", "图（由")):
        return True
    if re.match(r"^图10-[23456789]", s):
        return True
    return False


def flush_para(out, para):
    if para:
        text = "".join(para).strip()
        text = text.replace(" ，", "，").replace(" 。", "。")
        out.append(text)
        para.clear()


def normalize(lines, fname):
    out, para = [], []
    for raw in lines:
        s = clean(raw)
        if should_skip(s):
            continue
        if s in FIGURES:
            flush_para(out, para)
            out.append(FIGURES[s])
            continue
        if s in SUBHEADINGS:
            flush_para(out, para)
            out.append(SUBHEADINGS[s])
            continue
        if s == "10.4包":
            continue
        if s.startswith("设计点拨：") or s.startswith("无态度的酷"):
            flush_para(out, para)
            out.append("#### " + s)
            continue
        if fname == "10-03-visual-appearance.md" and re.fullmatch(r"[123]\..+", s):
            flush_para(out, para)
            out.append("#### " + s)
            continue
        if s.startswith("口"):
            flush_para(out, para)
            out.append("- " + s[1:].strip())
            continue
        if fname.startswith("10-0") and re.match(r"^\d+\.", s):
            flush_para(out, para)
            out.append(s)
            continue
        para.append(s)
        if s.endswith(("。", "？", "！", "）", "”")) and len("".join(para)) > 50:
            flush_para(out, para)
    flush_para(out, para)
    return out


def fm(title):
    return f"---\ntitle: {title}\n---\n\n"


def pager(current):
    files = [x[0] for x in PAGES]
    i = files.index(current)
    prev = "../chapter-09/09-07-exercises-questions" if i == 0 else files[i-1].replace(".md", "")
    nxt = files[i+1].replace(".md", "") if i + 1 < len(files) else None
    def block(pos):
        lines = ["<!-- chapter-pager:start -->", "", f'<div class="chapter-pager chapter-pager--{pos}">']
        if prev:
            lines.append(f'<a class="chapter-pager__button chapter-pager__button--prev" href="{prev}"><span class="chapter-pager__label">上一页</span></a>')
        if nxt:
            lines.append(f'<a class="chapter-pager__button chapter-pager__button--next" href="{nxt}"><span class="chapter-pager__label">下一页</span></a>')
        lines.extend(["</div>", "", "<!-- chapter-pager:end -->"])
        return "\n".join(lines)
    return block("top"), block("bottom")

# Chapter title page: only allowed content sections are 本章定位 and 复习线索.
top, bottom = pager("index.md")
index = fm("第 10 章 角色开发") + top + "\n\n# 第 10 章 角色开发\n\n## 本章定位\n\n本章讨论如何设计令人信服、可识别且能承载游戏体验的角色。重点从化身与玩家关系、视觉外表、角色深度、属性与成长，以及音效、音乐和语言等方面，说明角色如何服务于可玩性、叙事和商业识别。\n\n## 复习线索\n\n- 好角色应当吸引人、可信，并能让玩家理解或认同其在游戏世界中的位置。\n- 化身设计需要处理玩家自定义、指定化身、控制机制和玩家投射之间的关系。\n- 视觉外表包括身体类型、衣着、武器、标志性物品、名字、调色板与同伴等识别要素。\n- 故事驱动角色设计关注角色的作用、态度、价值、属性、维度、成长与人物原型。\n- 音频设计通过音效、音乐主题、声音、词汇、语法、口音和说话风格进一步定义角色。\n\n" + bottom + "\n"
(OUT / "index.md").write_text(index, encoding="utf-8", newline="\n")

for fname, title in PAGES[1:]:
    start, end = RANGES[fname]
    body_lines = normalize(raw_lines[start-1:end], fname)
    top, bottom = pager(fname)
    text = fm(title) + top + f"\n\n# {title}\n\n"
    text += "> 来源：私人资料库 OCR 整理，摘自《游戏设计基础（原书第 3 版）》第 10 章。PDF 为扫描版，文字已做轻度校正，仍建议以后逐段人工复核。\n\n"
    text += "## 原书内容整理\n\n" + "\n\n".join(body_lines).strip() + "\n\n"
    text += bottom + "\n\n## 我的批注区\n\n-\n"
    (OUT / fname).write_text(text, encoding="utf-8", newline="\n")

print(OUT)
