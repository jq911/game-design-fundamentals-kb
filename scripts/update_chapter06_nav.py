from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
MKDOCS = ROOT / "mkdocs.yml"

chapter6 = """      - 第 6 章 通过游戏来盈利:
          - 章节导览: game-design-fundamentals/chapter-06/index.md
          - 6.1 直接支付模式:
              - 导览: game-design-fundamentals/chapter-06/06-01-direct-payment-models.md
              - 6.1.1 零售模式: game-design-fundamentals/chapter-06/06-01-direct-payment-models/06-01-01-retail-model.md
              - 6.1.2 网络销售: game-design-fundamentals/chapter-06/06-01-direct-payment-models/06-01-02-online-sales.md
              - 6.1.3 基于订购的交易模式: game-design-fundamentals/chapter-06/06-01-direct-payment-models/06-01-03-subscription-model.md
              - 6.1.4 章节销售模式: game-design-fundamentals/chapter-06/06-01-direct-payment-models/06-01-04-episodic-sales.md
              - 6.1.5 众筹: game-design-fundamentals/chapter-06/06-01-direct-payment-models/06-01-05-crowdfunding.md
          - 6.2 间接盈利模式:
              - 导览: game-design-fundamentals/chapter-06/06-02-indirect-revenue-models.md
              - 6.2.1 免费增值游戏: game-design-fundamentals/chapter-06/06-02-indirect-revenue-models/06-02-01-freemium-games.md
              - 6.2.2 免费游戏模式: game-design-fundamentals/chapter-06/06-02-indirect-revenue-models/06-02-02-free-to-play-model.md
              - 6.2.3 广告与赞助: game-design-fundamentals/chapter-06/06-02-indirect-revenue-models/06-02-03-advertising-and-sponsorship.md
              - 6.2.4 命题游戏: game-design-fundamentals/chapter-06/06-02-indirect-revenue-models/06-02-04-commissioned-games.md
          - 6.3 世界游戏市场:
              - 导览: game-design-fundamentals/chapter-06/06-03-world-game-markets.md
              - 6.3.1 传统游戏市场: game-design-fundamentals/chapter-06/06-03-world-game-markets/06-03-01-traditional-markets.md
              - 6.3.2 新兴市场: game-design-fundamentals/chapter-06/06-03-world-game-markets/06-03-02-emerging-markets.md
          - 6.4 本章总结: game-design-fundamentals/chapter-06/06-04-summary.md
          - 6.5 设计练习：习题: game-design-fundamentals/chapter-06/06-05-exercises-questions.md
"""

text = MKDOCS.read_text(encoding="utf-8")
if "      - 第 6 章 通过游戏来盈利:" in text:
    print("Chapter 6 nav already present")
else:
    marker = "          - 5.6 设计练习：训练: game-design-fundamentals/chapter-05/05-06-exercises-training.md\n"
    if marker not in text:
        raise SystemExit("Cannot find Chapter 5 nav end marker")
    text = text.replace(marker, marker + chapter6)
    MKDOCS.write_text(text, encoding="utf-8", newline="\n")
    print("Inserted Chapter 6 nav")
