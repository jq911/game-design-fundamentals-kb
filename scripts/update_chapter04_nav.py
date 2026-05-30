from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
MKDOCS = ROOT / "mkdocs.yml"

chapter4 = """      - 第 4 章 了解你的玩家:
          - 章节导览: game-design-fundamentals/chapter-04/index.md
          - 4.1 VandenBerghe 的 5 种游戏领域:
              - 导览: game-design-fundamentals/chapter-04/04-01-vandenberghe-five-domains.md
              - 4.1.1 五因素模型: game-design-fundamentals/chapter-04/04-01-vandenberghe-five-domains/04-01-01-five-factor-model.md
              - 4.1.2 5种游戏领域: game-design-fundamentals/chapter-04/04-01-vandenberghe-five-domains/04-01-02-five-game-domains.md
              - 4.1.3 另一个领域：讲故事的态度: game-design-fundamentals/chapter-04/04-01-vandenberghe-five-domains/04-01-03-story-attitude.md
          - 4.2 人口统计分类:
              - 导览: game-design-fundamentals/chapter-04/04-02-demographics.md
              - 4.2.1 男人和女人: game-design-fundamentals/chapter-04/04-02-demographics/04-02-01-men-and-women.md
              - 4.2.2 男孩和女孩: game-design-fundamentals/chapter-04/04-02-demographics/04-02-02-boys-and-girls.md
              - 4.2.3 女孩的游戏: game-design-fundamentals/chapter-04/04-02-demographics/04-02-03-games-for-girls.md
          - 4.3 玩家贡献: game-design-fundamentals/chapter-04/04-03-player-dedication.md
          - 4.4 二元性思维的危害:
              - 导览: game-design-fundamentals/chapter-04/04-04-binary-thinking.md
              - 4.4.1 从统计学角度研究玩家群体: game-design-fundamentals/chapter-04/04-04-binary-thinking/04-04-01-statistical-player-groups.md
              - 4.4.2 致力于包容性，而不是普遍性: game-design-fundamentals/chapter-04/04-04-binary-thinking/04-04-02-inclusiveness-not-universality.md
          - 4.5 本章总结: game-design-fundamentals/chapter-04/04-05-summary.md
          - 4.6 设计练习：训练: game-design-fundamentals/chapter-04/04-06-exercises-training.md
          - 4.7 设计练习：习题: game-design-fundamentals/chapter-04/04-07-exercises-questions.md
"""

text = MKDOCS.read_text(encoding="utf-8")
if "      - 第 4 章 了解你的玩家:" in text:
    print("Chapter 4 nav already present")
else:
    marker = "          - 3.5 设计练习：习题: game-design-fundamentals/chapter-03/03-05-exercises-questions.md\n"
    if marker not in text:
        raise SystemExit("Cannot find Chapter 3 nav end marker")
    text = text.replace(marker, marker + chapter4)
    MKDOCS.write_text(text, encoding="utf-8", newline="\n")
    print("Inserted Chapter 4 nav")
