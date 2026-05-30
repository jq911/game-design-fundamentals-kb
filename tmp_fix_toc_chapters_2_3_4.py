from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
TOC = ROOT / "docs" / "game-design-fundamentals" / "toc.md"

text = TOC.read_text(encoding="utf-8")

replacements = {
    "| 第 2 章 | 游戏的设计与开发 | 28 | 待整理 |": "| 第 2 章 | [游戏的设计与开发](chapter-02/index.md) | 28 | 已整理 |",
    "| 第 3 章 | 游戏类别 | 60 | 待整理 |": "| 第 3 章 | [游戏类别](chapter-03/index.md) | 60 | 已整理 |",
    "| 第 4 章 | 了解你的玩家 | 69 | 待整理 |": "| 第 4 章 | [了解你的玩家](chapter-04/index.md) | 69 | 已整理 |",
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"Missing summary row: {old}")
    text = text.replace(old, new)

blocks = {
    """## 第 2 章 游戏的设计与开发

- 2.1 走近游戏设计 —— 28
- 2.2 电子游戏的关键组成 —— 33
- 2.3 电子游戏的结构 —— 36
- 2.4 游戏开发过程中的各个阶段 —— 40
- 2.5 游戏设计团队 —— 48
- 2.6 游戏设计文档 —— 50
- 2.7 剖析游戏设计者 —— 55
- 2.8 本章总结 —— 58
- 2.9 设计练习——训练 —— 58
- 2.10 设计练习——习题 —— 59
""": """## 第 2 章 游戏的设计与开发

| 小节 | 标题 | 页码 | 笔记 |
|---|---|---:|---|
| 2.1 | 走近游戏设计 | 28 | [查看](chapter-02/02-01-approaching-game-design.md) |
| 2.2 | 电子游戏的关键组成 | 33 | [查看](chapter-02/02-02-key-components.md) |
| 2.3 | 电子游戏的结构 | 36 | [查看](chapter-02/02-03-video-game-structure.md) |
| 2.4 | 游戏开发过程中的各个阶段 | 40 | [查看](chapter-02/02-04-development-stages.md) |
| 2.5 | 游戏设计团队 | 48 | [查看](chapter-02/02-05-game-design-team.md) |
| 2.6 | 游戏设计文档 | 50 | [查看](chapter-02/02-06-design-documents.md) |
| 2.7 | 剖析游戏设计者 | 55 | [查看](chapter-02/02-07-anatomy-of-game-designer.md) |
| 2.8 | 本章总结 | 58 | [查看](chapter-02/02-08-summary.md) |
| 2.9 | 设计练习——训练 | 58 | [查看](chapter-02/02-09-exercises-training.md) |
| 2.10 | 设计练习——习题 | 59 | [查看](chapter-02/02-10-exercises-questions.md) |
""",
    """## 第 3 章 游戏类别

- 3.1 什么是游戏类别 —— 60
- 3.2 经典的游戏类别 —— 61
- 3.3 本章总结 —— 67
- 3.4 设计练习——训练 —— 68
- 3.5 设计练习——习题 —— 68
""": """## 第 3 章 游戏类别

| 小节 | 标题 | 页码 | 笔记 |
|---|---|---:|---|
| 3.1 | 什么是游戏类别 | 60 | [查看](chapter-03/03-01-what-is-genre.md) |
| 3.2 | 经典的游戏类别 | 61 | [查看](chapter-03/03-02-classic-genres.md) |
| 3.3 | 本章总结 | 67 | [查看](chapter-03/03-03-summary.md) |
| 3.4 | 设计练习——训练 | 68 | [查看](chapter-03/03-04-exercises-training.md) |
| 3.5 | 设计练习——习题 | 68 | [查看](chapter-03/03-05-exercises-questions.md) |
""",
    """## 第 4 章 了解你的玩家

- 4.1 VandenBerghe 的 5 种游戏领域 —— 69
- 4.2 人口统计分类 —— 71
- 4.3 玩家贡献 —— 82
- 4.4 二元性思维的危害 —— 84
- 4.5 本章总结 —— 86
- 4.6 设计练习——训练 —— 86
- 4.7 设计练习——习题 —— 87
""": """## 第 4 章 了解你的玩家

| 小节 | 标题 | 页码 | 笔记 |
|---|---|---:|---|
| 4.1 | VandenBerghe 的 5 种游戏领域 | 69 | [查看](chapter-04/04-01-vandenberghe-five-domains.md) |
| 4.2 | 人口统计分类 | 71 | [查看](chapter-04/04-02-demographics.md) |
| 4.3 | 玩家贡献 | 82 | [查看](chapter-04/04-03-player-dedication.md) |
| 4.4 | 二元性思维的危害 | 84 | [查看](chapter-04/04-04-binary-thinking.md) |
| 4.5 | 本章总结 | 86 | [查看](chapter-04/04-05-summary.md) |
| 4.6 | 设计练习——训练 | 86 | [查看](chapter-04/04-06-exercises-training.md) |
| 4.7 | 设计练习——习题 | 87 | [查看](chapter-04/04-07-exercises-questions.md) |
""",
}
for old, new in blocks.items():
    if old not in text:
        raise SystemExit("Missing chapter block starting: " + old.splitlines()[0])
    text = text.replace(old, new)

TOC.write_text(text, encoding="utf-8", newline="\n")
print(f"Updated {TOC}")
