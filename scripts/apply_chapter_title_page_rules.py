from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
BOOK = ROOT / "docs" / "game-design-fundamentals"

# 1. Book landing page: remove “阅读路径” and “当前整理状态”.
book_index = BOOK / "index.md"
text = book_index.read_text(encoding="utf-8")
text = re.sub(r"\n## 阅读路径\n.*?(?=\n## 当前整理状态\n)", "\n", text, flags=re.S)
text = re.sub(r"\n## 当前整理状态\n.*?(?=\n!!! note|\Z)", "\n", text, flags=re.S)
text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
book_index.write_text(text, encoding="utf-8", newline="\n")

# 2-4. Chapter title pages: only “本章定位” and “复习线索” as content sections.
chapter_data = {
    "chapter-01/index.md": {
        "title": "第 1 章 游戏和电子游戏",
        "position": "在正式讨论游戏设计之前，本章先回答三个基础问题：\n\n1. 什么是游戏，它和玩具、智力谜题有什么区别？\n2. 电子游戏相对传统游戏带来了哪些变化？\n3. 游戏为什么能让人觉得有趣，以及游戏还能承担哪些严肃用途？",
        "review": [
            "**游戏的四个基础元素**：玩 / 操作、假想、目标、规则。",
            "**可玩性的核心结构**：挑战 + 玩家可采取的动作。",
            "**电子游戏的媒介优势**：规则可隐藏、节奏可由计算机控制、世界可被视听呈现、可引入人工智能。",
            "**娱乐性不是单一概念**：可玩性、美学、沉浸、情感、故事、风险、探索、学习、创造、角色扮演、社交都可以贡献乐趣。",
            "**严肃游戏**：游戏也可以用于教育、培训、模拟、说服、健康和个人成长。",
        ],
    },
    "chapter-02/index.md": {
        "title": "第 2 章 游戏的设计与开发",
        "position": "本章从游戏设计的工作方式开始，介绍以玩家为中心的设计观、电子游戏的关键组成、游戏结构、开发阶段、设计团队、设计文档，以及游戏设计者需要具备的能力。",
        "review": [
            "**以玩家为中心**：设计不是只表达设计者意图，而是持续判断玩家会如何理解、行动和反馈。",
            "**关键组成**：核心机制、用户界面、交互模型、视角、游戏模式共同决定玩家体验。",
            "**开发过程**：概念、原型、制作、测试和迭代是反复收敛的过程。",
            "**团队协作**：设计者需要和程序、美术、音频、制作、测试等角色共享语言。",
            "**设计文档**：文档的价值在于沟通、记录决策和支撑迭代，而不是形式本身。",
        ],
    },
    "chapter-03/index.md": {
        "title": "第 3 章 游戏类别",
        "position": "本章介绍电子游戏类别的定义、类别与挑战的关系，以及经典游戏类别（射击、动作、策略、角色扮演、体育、模拟、冒险、解谜等）的基本特征。",
        "review": [
            "**类别是玩家预期**：游戏类别帮助玩家快速理解核心体验，但不应该限制设计想象。",
            "**类别与挑战相关**：不同类别通常强调不同类型的挑战、节奏和操作方式。",
            "**经典类别**：射击、动作、策略、角色扮演、体育、模拟、冒险、解谜等各有常见结构。",
            "**混合类别**：现代游戏常把多个类别的机制组合在一起，形成复合体验。",
            "**设计判断**：选择类别时要关注目标玩家、核心玩法和市场沟通，而不是只贴标签。",
        ],
    },
    "chapter-04/index.md": {
        "title": "第 4 章 了解你的玩家",
        "position": "本章讨论以玩家为中心的设计视角：玩家动机、人口统计分类、玩家贡献程度，以及避免用二元性思维误判目标玩家的方法。",
        "review": [
            "**玩家动机**：VandenBerghe 的 5 种游戏领域提供了一种理解玩家偏好的心理学视角。",
            "**人口统计不是刻板印象**：年龄、性别等分类可以提供线索，但不能替代真实玩家研究。",
            "**玩家贡献程度**：休闲玩家和高投入玩家对时间、金钱、难度和社交的期待可能不同。",
            "**避免二元思维**：不要把玩家简单分成男性/女性、核心/休闲等对立阵营。",
            "**包容性设计**：重点不是讨好所有人，而是减少不必要的排除性元素。",
        ],
    },
}

START = "<!-- chapter-pager:start -->"
END = "<!-- chapter-pager:end -->"

def extract_pagers(text: str):
    blocks = re.findall(rf"{re.escape(START)}.*?{re.escape(END)}", text, flags=re.S)
    top = blocks[0].strip() if blocks else ""
    bottom = blocks[-1].strip() if len(blocks) > 1 else ""
    return top, bottom

for rel, data in chapter_data.items():
    path = BOOK / rel
    original = path.read_text(encoding="utf-8")
    top, bottom = extract_pagers(original)
    title = data["title"]
    review = "\n".join(f"- {item}" for item in data["review"])
    parts = ["---", f"title: {title}", "---", ""]
    if top:
        parts += [top, ""]
    parts += [
        f"# {title}",
        "",
        "## 本章定位",
        "",
        data["position"],
        "",
        "## 复习线索",
        "",
        review,
        "",
    ]
    if bottom:
        parts += [bottom, ""]
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8", newline="\n")

print("Applied book and chapter title page rules")
