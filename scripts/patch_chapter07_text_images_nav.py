from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH7 = ROOT / "docs" / "game-design-fundamentals" / "chapter-07"

FIG1 = '''<figure class="book-figure">
  <img src="../../../../assets/book-images/game-design-fundamentals/chapter-07/figure-7-1-grand-theft-auto-vice-city.png" alt="图7-1 《侠盗飞车之罪恶都市》就是受另外一种媒体（电视）启发的游戏">
  <figcaption>图7-1　《侠盗飞车之罪恶都市》就是受另外一种媒体（电视）启发的游戏</figcaption>
</figure>'''

FIG2 = '''<figure class="book-figure">
  <img src="../../../../assets/book-images/game-design-fundamentals/chapter-07/figure-7-2-puzzle-quest.png" alt="图7-2 益智之迷">
  <figcaption>图7-2　益智之迷</figcaption>
</figure>'''

repls = {
    "电视节自": "电视节目",
    "用儿句话": "用几句话",
    "飞行飞行迷": "飞行迷",
    "游戏一像LucasArts": "游戏——像 LucasArts",
    "抛开那些常见的精灵一巫师的组合": "抛开那些常见的精灵—巫师的组合",
    "有时候会尝试从游戏背景": "有时候你会尝试从游戏背景",
    "不必像“键踢腿，O键出拳”这样）": "（不必像“X 键踢腿，O 键出拳”这样）",
    "发行商用在游戏开发上的钱越多": "发行商用在游戏开发上的钱越多",
    "检测你的想法": "检验你的想法",
    "游戏需要本身是真实的": "游戏需要本身是真实的",
}

for p in CH7.rglob("*.md"):
    s = p.read_text(encoding="utf-8")
    for a, b in repls.items():
        s = s.replace(a, b)
    p.write_text(s, encoding="utf-8", newline="\n")

p1 = CH7 / "07-01-getting-an-idea" / "07-01-02-ideas-from-other-media.md"
s = p1.read_text(encoding="utf-8")
s = s.replace("图7-1《侠盗飞车之罪恶都市》就是受另外一种媒体（电视）启发的游戏", FIG1)
p1.write_text(s, encoding="utf-8", newline="\n")

p2 = CH7 / "07-02-from-idea-to-game-concept" / "07-02-02-genres-and-hybrids.md"
s = p2.read_text(encoding="utf-8")
s = s.replace("。DUZZLEEOUESTDwarven\n\n图7-2益智之迷\n\n", "。\n\n" + FIG2 + "\n\n")
s = s.replace("。DUZZLEEOUESTDwarven", "。\n\n" + FIG2)
s = s.replace("\n\n图7-2益智之迷\n\n", "\n\n" + FIG2 + "\n\n")
p2.write_text(s, encoding="utf-8", newline="\n")

# Improve exercise question line wrapping caused by OCR physical lines.
pq = CH7 / "07-05-exercises-questions.md"
s = pq.read_text(encoding="utf-8")
question_repls = {
    "#### 1. 写一份游戏概念方案：用几句话描述游戏的大致风格。如果你的游戏和其他游戏、电影、\n\n书籍或别的媒体包含相似的特征、动作或创意，可以参考它们。":
    "#### 1. 写一份游戏概念方案：用几句话描述游戏的大致风格。如果你的游戏和其他游戏、电影、书籍或别的媒体包含相似的特征、动作或创意，可以参考它们。",
    "#### 2. 考虑玩家是什么角色？玩家是否扮演成某个人物或事件，如果是这样一种模式，具体人\n\n物或事件是什么？是不是需要多名角色？如何利用玩家角色来帮助明确游戏可玩性？":
    "#### 2. 考虑玩家是什么角色？玩家是否扮演成某个人物或事件，如果是这样一种模式，具体人物或事件是什么？是不是需要多名角色？如何利用玩家角色来帮助明确游戏可玩性？",
    "#### 4. 该游戏可玩性的性质是什么？对其概括性描述。玩家将会遇到什么样的挑战？玩家可以\n\n采取什么样的动作通过关卡？":
    "#### 4. 该游戏可玩性的性质是什么？对其概括性描述。玩家将会遇到什么样的挑战？玩家可以采取什么样的动作通过关卡？",
    "#### 6. 游戏主要的屏幕显示模式是什么？游戏世界是如何通过屏幕呈现在玩家面前的？是否需\n\n要多个视角？":
    "#### 6. 游戏主要的屏幕显示模式是什么？游戏世界是如何通过屏幕呈现在玩家面前的？是否需要多个视角？",
    "#### 8. 这个游戏属于哪种游戏模式：竞争、合作、组队还是单人？如果游戏允许多名玩家参与，\n\n他们是在同一台设备上使用不同的控制进行操作，还是使用独立设备进行联网操作？":
    "#### 8. 这个游戏属于哪种游戏模式：竞争、合作、组队还是单人？如果游戏允许多名玩家参与，他们是在同一台设备上使用不同的控制进行操作，还是使用独立设备进行联网操作？",
    "#### 9. 游戏的亮点在哪里，为什么大家会玩这个游戏？目标玩家是哪些，他们区别于其他玩家\n\n的特征是什么？":
    "#### 9. 游戏的亮点在哪里，为什么大家会玩这个游戏？目标玩家是哪些，他们区别于其他玩家的特征是什么？",
}
for a, b in question_repls.items():
    s = s.replace(a, b)
pq.write_text(s, encoding="utf-8", newline="\n")

# Update TOC Chapter 7 status and links.
toc = ROOT / "docs" / "game-design-fundamentals" / "toc.md"
s = toc.read_text(encoding="utf-8")
s = s.replace("| 第 7 章 | 游戏概念 | 107 | 待整理 |", "| 第 7 章 | [游戏概念](chapter-07/index.md) | 107 | 已整理 |")
old = """## 第 7 章 游戏概念

- 7.1 获得一个创意 —— 107
- 7.2 从创意到游戏概念 —— 111
- 7.3 本章总结 —— 116
- 7.4 设计练习——训练 —— 116
- 7.5 设计练习——习题 —— 117
"""
new = """## 第 7 章 游戏概念

| 小节 | 标题 | 页码 | 笔记 |
|---|---|---:|---|
| 7.1 | 获得一个创意 | 107 | [查看](chapter-07/07-01-getting-an-idea.md) |
| 7.2 | 从创意到游戏概念 | 111 | [查看](chapter-07/07-02-from-idea-to-game-concept.md) |
| 7.3 | 本章总结 | 116 | [查看](chapter-07/07-03-summary.md) |
| 7.4 | 设计练习——训练 | 116 | [查看](chapter-07/07-04-exercises-training.md) |
| 7.5 | 设计练习——习题 | 117 | [查看](chapter-07/07-05-exercises-questions.md) |
"""
if old not in s:
    raise SystemExit("TOC Chapter 7 block not found")
s = s.replace(old, new)
toc.write_text(s, encoding="utf-8", newline="\n")

# Update mkdocs nav by appending Chapter 7 after Chapter 6 block (currently at nav end).
mk = ROOT / "mkdocs.yml"
s = mk.read_text(encoding="utf-8")
old_end = """          - 6.4 本章总结: game-design-fundamentals/chapter-06/06-04-summary.md
          - 6.5 设计练习：习题: game-design-fundamentals/chapter-06/06-05-exercises-questions.md
"""
ch7_nav = """          - 6.4 本章总结: game-design-fundamentals/chapter-06/06-04-summary.md
          - 6.5 设计练习：习题: game-design-fundamentals/chapter-06/06-05-exercises-questions.md
      - 第 7 章 游戏概念:
          - 章节导览: game-design-fundamentals/chapter-07/index.md
          - 7.1 获得一个创意:
              - 导览: game-design-fundamentals/chapter-07/07-01-getting-an-idea.md
              - 7.1.1 梦想着梦想: game-design-fundamentals/chapter-07/07-01-getting-an-idea/07-01-01-dreaming-dreams.md
              - 7.1.2 来自其他媒体的游戏创意: game-design-fundamentals/chapter-07/07-01-getting-an-idea/07-01-02-ideas-from-other-media.md
              - 7.1.3 来自其他游戏的游戏创意: game-design-fundamentals/chapter-07/07-01-getting-an-idea/07-01-03-ideas-from-other-games.md
              - 7.1.4 如何进行头脑风暴: game-design-fundamentals/chapter-07/07-01-getting-an-idea/07-01-04-brainstorming.md
              - 7.1.5 和其他人交流你的梦想: game-design-fundamentals/chapter-07/07-01-getting-an-idea/07-01-05-communicating-your-dream.md
          - 7.2 从创意到游戏概念:
              - 导览: game-design-fundamentals/chapter-07/07-02-from-idea-to-game-concept.md
              - 7.2.1 玩家的角色: game-design-fundamentals/chapter-07/07-02-from-idea-to-game-concept/07-02-01-player-role.md
              - 7.2.2 游戏类型和混合体: game-design-fundamentals/chapter-07/07-02-from-idea-to-game-concept/07-02-02-genres-and-hybrids.md
              - 7.2.3 定义你的目标人群: game-design-fundamentals/chapter-07/07-02-from-idea-to-game-concept/07-02-03-defining-target-audience.md
              - 7.2.4 游戏进度考虑: game-design-fundamentals/chapter-07/07-02-from-idea-to-game-concept/07-02-04-progression-considerations.md
          - 7.3 本章总结: game-design-fundamentals/chapter-07/07-03-summary.md
          - 7.4 设计练习：训练: game-design-fundamentals/chapter-07/07-04-exercises-training.md
          - 7.5 设计练习：习题: game-design-fundamentals/chapter-07/07-05-exercises-questions.md
"""
if "第 7 章 游戏概念:" not in s:
    if old_end not in s:
        raise SystemExit("mkdocs chapter 6 tail not found")
    s = s.replace(old_end, ch7_nav)
mk.write_text(s, encoding="utf-8", newline="\n")

print("Patched Chapter 7 text/images/toc/nav")
