from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-04"

REPL = {
    "自前": "目前",
    "自标": "目标",
    "自已": "自己",
    "进人": "进入",
    "加人": "加入",
    "投人": "投入",
    "JasonVandenBerghe": "Jason VandenBerghe",
    "BigFive": "Big Five",
    "bigfivepersonalitytest": "big five personality test",
    "Facebook": "Facebook",
    "Pinterest": "Pinterest",
    "AAA游戏": "AAA 游戏",
    "www.outofservice.com/\n\nbigfive": "www.outofservice.com/bigfive",
    "男孩和女孩": "男孩和女孩",
    "十儿岁的男孩": "十几岁的男孩",
    "想法儿乎相同": "想法几乎相同",
    "没有儿个人": "没有几个人",
    "天量已为人交的男性玩家": "大量已为人父的男性玩家",
    "一天玩儿次": "一天玩几次",
    "相于Jason VandenBerghe": "相反于 Jason VandenBerghe",
    "相于 Jason VandenBerghe": "相反于 Jason VandenBerghe",
}

for md in sorted(CH.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    for a, b in REPL.items():
        text = text.replace(a, b)
    # Remove standalone printed page numbers that slipped through OCR.
    text = re.sub(r"(?m)^\s*(7[0-9]|8[0-7])\s*$\n", "", text)
    # Join obvious OCR line breaks inside English/product names and URLs.
    text = text.replace("www.outofservice.com/\n\nbigfive", "www.outofservice.com/bigfive")
    text = re.sub(r"\n{3,}", "\n\n", text)
    md.write_text(text, encoding="utf-8", newline="\n")

# A few section-specific repairs visible during QA.
train = CH / "04-06-exercises-training.md"
text = train.read_text(encoding="utf-8")
text = text.replace("得到的测试结果是证实还是相于Jason VandenBerghe的假设，或是产生了一个不确定的\n\n结果。", "得到的测试结果是证实还是相反于 Jason VandenBerghe 的假设，或是产生了一个不确定的结果。")
text = text.replace("得到的测试结果是证实还是相于 Jason VandenBerghe的假设，或是产生了一个不确定的\n\n结果。", "得到的测试结果是证实还是相反于 Jason VandenBerghe 的假设，或是产生了一个不确定的结果。")
text = text.replace("得到的测试结果是证实还是相于 Jason VandenBerghe 的假设，或是产生了一个不确定的\n\n结果。", "得到的测试结果是证实还是相反于 Jason VandenBerghe 的假设，或是产生了一个不确定的结果。")
text = text.replace("结果。\n\n帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary", "结果。\n\n#### 2. 选择一款游戏（也可以请朋友帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary")
text = text.replace("结果。\n\n#### 2. 选择一款游戏（也可以请朋友帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary", "结果。\n\n#### 2. 选择一款游戏（也可以请朋友帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary")
text = re.sub(r"\n{3,}", "\n\n", text)
train.write_text(text, encoding="utf-8", newline="\n")

stat = CH / "04-04-binary-thinking" / "04-04-01-statistical-player-groups.md"
text = stat.read_text(encoding="utf-8")
text = text.replace("这只是一个假设的案例。在某些游戏中，重叠部分的范围是很小的，而那些不在重叠\n\n然而，值得注意的是，", "这只是一个假设的案例。在某些游戏中，重叠部分的范围是很小的。\n\n然而，值得注意的是，")
text = re.sub(r"\n{3,}", "\n\n", text)
stat.write_text(text, encoding="utf-8", newline="\n")

print("Applied final Chapter 4 OCR fixes")
