from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-08"
ASSET = "../../../../assets/book-images/game-design-fundamentals/chapter-08"

figs = {
    "图8-1": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-1-prince-of-persia-classic-2d.png", "《波斯王子经典版》——一款 2D 的滚屏游戏"),
    "图8-2": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-2-starcraft-terrain.png", "《星际争霸》中有多种高地和低谷地形"),
    "图8-3": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-3-need-for-speed-most-wanted-3d.png", "《极品飞车：最高通缉》——一款全 3D 游戏"),
    "图8-4": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-4-legacy-of-kain-material-spectral.png", "《凯恩的遗产：噬魂者》中同一位置的物质世界和鬼怪世界"),
    "图8-5": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-5-age-of-empires-scale.png", "在游戏《帝国时代》里建筑物只比人高一点儿"),
    "图8-6": ("08-03-dimensions-of-game-world/08-03-01-physical-dimension.md", "figure-8-6-spore-sphere-world.png", "游戏《孢子》部分设置在一个真实的球体上"),
    "图8-7": ("08-03-dimensions-of-game-world/08-03-02-time-dimension.md", "figure-8-7-settlers-irregular-time.png", "《工人物语：帝国的崛起》里活动用的时间不规则，但用户界面并没有计时器"),
    "图8-8": ("08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md", "figure-8-8-cleopatra-cultural-background.png", "《埃及艳后：尼罗河的女王》中的文化背景影响着屏幕上的每个东西"),
    "图8-9": ("08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md", "figure-8-9-grim-fandango-style.png", "《冥界狂想曲》把阿兹特克、装饰派艺术和墨西哥亡灵节的主题结合在了一起"),
    "图8-10": ("08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md", "figure-8-10-spec-ops-sandstorm-dubai.png", "《特种战线》中因沙尘暴而被摧毁的城市"),
    "图8-11": ("08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md", "figure-8-11-naruto-visual-style.png", "《火影》用一本漫画书的风格装饰了游戏中的现代日本建筑以及其他地方"),
    "图8-12": ("08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md", "figure-8-12-medieval-fantasy-example.png", "另一款仿中世纪的游戏：《幻魔霸主》"),
    "图8-13": ("08-03-dimensions-of-game-world/08-03-04-emotional-dimension.md", "figure-8-13-final-fantasy-aerith-death.png", "《最终幻想 VII》中的艾瑞丝之死"),
    "图8-14": ("08-03-dimensions-of-game-world/08-03-05-moral-dimension.md", "figure-8-14-americas-army-moral-perspective.png", "我们的部队捕获了一个自认为是我们其中一员的家伙"),
}

def fig_html(token, filename, caption):
    return f'''<figure class="book-figure">
  <img src="{ASSET}/{filename}" alt="{token} {caption}" loading="lazy">
  <figcaption>{token}　{caption}</figcaption>
</figure>'''

# Text cleanup across Chapter 8.
common_repls = {
    "自已": "自己",
    "进人": "进入",
    "自的": "目的",
    "成鲜明": "形成鲜明",
    "多天": "多大",
    "5，我应该": "5. 我应该",
    "王、王后和骑士。": "国际象棋的玩家初学时会把棋子看成国王、王后和骑士。",
    "游戏需要本身是真实的": "游戏世界本身需要是真实可信的",
    "现实世界重，一架": "现实世界中，一架",
    "并不重要，战斗机擅长": "并不重要；战斗机擅长",
    "游戏始级": "游戏始终",
    "行户走肉": "行尸走肉",
    "权利和控制": "权力和控制",
    "游戏者": "玩家",
    "进人整部": "进入整部",
    "消遭": "消遣",
    "愤概": "愤慨",
    "近几年来": "近年来",
    "应该把现实世界替换到游戏中的": "是否是现实世界被替换到游戏中的",
    "是不是现实世界替换到游戏中的": "是否是现实世界被替换到游戏中的",
    "什么是游戏世界中的人们所倚重的": "游戏世界中的人们倚重什么",
    "竞赛完成，赢得一场金融竞争": "竞赛取胜、赢得一场金融竞争",
}
for p in CH.rglob("*.md"):
    s = p.read_text(encoding="utf-8")
    for a, b in common_repls.items():
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8", newline="\n")

# Patch the worst figure-interrupted passages with clean text + screenshot blocks.
p = CH / "08-03-dimensions-of-game-world" / "08-03-01-physical-dimension.md"
s = p.read_text(encoding="utf-8")
start = s.index("- 2D：")
end = s.index("#### 2. 大小")
replacement = f"""- **2D**：多亏了有手机和平板移动设备，世界上大多数的游戏仍旧是二维模式。这种模式在 2D 滚屏游戏里很引人注意，就像《波斯王子经典版》（如图8-1所示）。游戏中的王子可以横冲直撞、上下跳，但是不能向玩家方向移动（出屏幕方向），或者向玩家反方向移动（进屏幕方向）。当你考虑如何显示时，二维世界有一个很大的优势：二维世界直接对应显示器屏幕的两个维度，你不需要考虑如何向玩家传递深度的概念。另一方面，很多二维游戏仍然用三维硬件加速器来显示，使得物体看起来是三维的，即使游戏过程根本用不到三维。

{fig_html('图8-1', figs['图8-1'][1], figs['图8-1'][2])}

- **2.5D**：一般读作“两个半 D”。它主要出现在这样的游戏里：看起来是三维空间的，其实包含一系列重叠的二维图层。如《星际争霸》，这是一款经典的战争游戏，里面有高地和低谷，还有穿越障碍物和地面设备的飞机。玩家可以使物体很精确地在屏幕内水平移动。但是在纵向方面，物体必须在一个或者另一个平面上，平面中间什么都没有。飞行物不能在空中上下移动，它们只能在空气层里（如图8-2所示）。

- **3D**：真正意义上的三维。由于有 3D 硬件加速器和中介软件游戏引擎（如 Unity），现在的 3D 空间很容易实现。比起 2D 空间，它们能给玩家更真实的空间感觉（建筑物、洞穴、宇宙飞船等）。在 2D 空间里，玩家觉得是在旁观，而 3D 空间却使玩家感觉就像是身临其境。3D 空间对于车辆模拟和探索挑战型游戏非常有用，比如《极品飞车：最高通缉》（如图8-3所示）。现在为 PC 和游戏机设计的大部分大型游戏都使用 3D。

{fig_html('图8-2', figs['图8-2'][1], figs['图8-2'][2])}

{fig_html('图8-3', figs['图8-3'][1], figs['图8-3'][2])}

- **4D**：如果由于某些原因，你想采用 4D 空间，我们建议你把它作为 3D 的可选择版本来实现，而不是一个真正的 4D 空间。也就是说，创造两个（或多个）三维空间，使其看起来相似，但是会随着角色在其中移动而提供不同的经历。比如《凯恩的遗产》系列游戏，就包含两个 3D 世界：鬼怪领域和物质领域，两者有不同的游戏模式。它们两个的背景是相同的，但是物质世界是被白色灯光照亮的，而鬼怪世界则是蓝色灯光。在鬼怪世界里，建筑物是歪曲的（如图8-4所示）。两个领域中的可用操作不一样。看起来相似，但其实是用不同的规则统治的不同地方。在《指环王》的电影版本里，佛罗多戴上至尊魔戒时进入的世界，可以想象成现实世界的另一个可选版本，它与现实世界是重叠的，只是看起来不一样，行为上差别也很大。

{fig_html('图8-4', figs['图8-4'][1], figs['图8-4'][2])}

第一次考虑游戏空间的维度时，不要因为三维看起来更真实，或者最大限度地利用了机器硬件就立即假定它是三维的。就像设计其他东西一样，物理空间维度必须服务于游戏的娱乐价值，确保每个维度都能得到合理利用。《疯狂小旅鼠》（Lemmings）是一款非常不错的 2D 游戏，但是它的 3D 版本《疯狂小旅鼠 3D》却非常不成功，因为玩起来太难了。加入的第三维度不仅没能增添玩家的乐趣，反而起到了相反的作用。

"""
s = s[:start] + replacement + s[end:]
# Insert remaining physical-dimension figures at natural reference points.
s = s.replace("建筑物一般只比经过的人高出一点儿（如图8-5所示）。", "建筑物一般只比经过的人高出一点儿（如图8-5所示）。\n\n" + fig_html('图8-5', figs['图8-5'][1], figs['图8-5'][2]) + "\n\n")
s = s.replace("作为一个球体展示在屏幕上的（如图8-6所示）。", "作为一个球体展示在屏幕上的（如图8-6所示）。\n\n" + fig_html('图8-6', figs['图8-6'][1], figs['图8-6'][2]) + "\n\n")
s = re.sub(r"\n图8-[1-6][^\n]*(?:\n[^\n]*){0,2}", "\n", s)
p.write_text(s, encoding="utf-8", newline="\n")

# Other chapter figure insertions.
for token in ["图8-7", "图8-8", "图8-9", "图8-10", "图8-11", "图8-12", "图8-13", "图8-14"]:
    rel, filename, caption = figs[token]
    p = CH / rel
    s = p.read_text(encoding="utf-8")
    if filename not in s:
        # Insert after first textual reference to the figure.
        pattern = re.escape(f"（如{token}所示）")
        m = re.search(pattern, s)
        if m:
            insert_at = m.end()
            s = s[:insert_at] + "\n\n" + fig_html(token, filename, caption) + "\n\n" + s[insert_at:]
        else:
            s = s.replace(f"{token}", fig_html(token, filename, caption), 1)
    # Remove standalone OCR captions and nearby broken remnants if any remain.
    s = re.sub(rf"\n{token}[^\n]*(?:\n[^\n]*){{0,2}}", "\n", s)
    p.write_text(s, encoding="utf-8", newline="\n")

# Update TOC.
toc = ROOT / "docs" / "game-design-fundamentals" / "toc.md"
s = toc.read_text(encoding="utf-8")
s = s.replace("| 第 8 章 | 游戏世界 | 118 | 待整理 |", "| 第 8 章 | [游戏世界](chapter-08/index.md) | 118 | 已整理 |")
old = """## 第 8 章 游戏世界

- 8.1 什么是游戏世界 —— 118
- 8.2 游戏世界的目的 —— 119
- 8.3 游戏世界的维度 —— 120
- 8.4 现实主义 —— 138
- 8.5 本章总结 —— 139
- 8.6 设计练习——训练 —— 139
- 8.7 设计练习——习题 —— 140
"""
new = """## 第 8 章 游戏世界

| 小节 | 标题 | 页码 | 笔记 |
|---|---|---:|---|
| 8.1 | 什么是游戏世界 | 118 | [查看](chapter-08/08-01-what-is-game-world.md) |
| 8.2 | 游戏世界的目的 | 119 | [查看](chapter-08/08-02-purpose-of-game-world.md) |
| 8.3 | 游戏世界的维度 | 120 | [查看](chapter-08/08-03-dimensions-of-game-world.md) |
| 8.4 | 现实主义 | 138 | [查看](chapter-08/08-04-realism.md) |
| 8.5 | 本章总结 | 139 | [查看](chapter-08/08-05-summary.md) |
| 8.6 | 设计练习——训练 | 139 | [查看](chapter-08/08-06-exercises-training.md) |
| 8.7 | 设计练习——习题 | 140 | [查看](chapter-08/08-07-exercises-questions.md) |
"""
if old not in s:
    raise SystemExit("TOC Chapter 8 block not found")
s = s.replace(old, new)
toc.write_text(s, encoding="utf-8", newline="\n")

# Update mkdocs nav by adding Chapter 8 after Chapter 7.
mk = ROOT / "mkdocs.yml"
s = mk.read_text(encoding="utf-8")
if "第 8 章 游戏世界:" not in s:
    marker = "          - 7.5 设计练习：习题: game-design-fundamentals/chapter-07/07-05-exercises-questions.md\n"
    ch8_nav = marker + """      - 第 8 章 游戏世界:
          - 章节导览: game-design-fundamentals/chapter-08/index.md
          - 8.1 什么是游戏世界: game-design-fundamentals/chapter-08/08-01-what-is-game-world.md
          - 8.2 游戏世界的目的: game-design-fundamentals/chapter-08/08-02-purpose-of-game-world.md
          - 8.3 游戏世界的维度:
              - 导览: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world.md
              - 8.3.1 物理维度: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world/08-03-01-physical-dimension.md
              - 8.3.2 时间维度: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world/08-03-02-time-dimension.md
              - 8.3.3 环境维度: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world/08-03-03-environmental-dimension.md
              - 8.3.4 感情维度: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world/08-03-04-emotional-dimension.md
              - 8.3.5 道德维度: game-design-fundamentals/chapter-08/08-03-dimensions-of-game-world/08-03-05-moral-dimension.md
          - 8.4 现实主义: game-design-fundamentals/chapter-08/08-04-realism.md
          - 8.5 本章总结: game-design-fundamentals/chapter-08/08-05-summary.md
          - 8.6 设计练习：训练: game-design-fundamentals/chapter-08/08-06-exercises-training.md
          - 8.7 设计练习：习题: game-design-fundamentals/chapter-08/08-07-exercises-questions.md
"""
    if marker not in s:
        raise SystemExit("mkdocs chapter 7 tail not found")
    s = s.replace(marker, ch8_nav)
mk.write_text(s, encoding="utf-8", newline="\n")

print("Patched Chapter 8 text, images, toc, and nav")
