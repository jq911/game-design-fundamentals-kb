from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-04"

men = CH / "04-02-demographics" / "04-02-01-men-and-women.md"
stat = CH / "04-04-binary-thinking" / "04-04-01-statistical-player-groups.md"

fig41 = """<figure markdown>
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-04/figure-4-1-lara-croft-tomb-raider.png" alt="图4-1 《古墓丽影》中的女主角劳拉" loading="lazy">
  <figcaption>图4-1 《古墓丽影》中的女主角劳拉</figcaption>
</figure>"""

fig42 = """<figure markdown>
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-04/figure-4-2-heather-silent-hill-3.png" alt="图4-2 《寂静岭3》中的女主海瑟" loading="lazy">
  <figcaption>图4-2 《寂静岭3》中的女主海瑟，看起来就像一位真实的女性</figcaption>
</figure>"""

fig43 = """<figure markdown>
  <img src="../../../assets/book-images/game-design-fundamentals/chapter-04/figure-4-3-interest-rating-by-gender.png" alt="图4-3 特定游戏的兴趣度等级" loading="lazy">
  <figcaption>图4-3 特定游戏的兴趣度等级：0～10</figcaption>
</figure>"""

text = men.read_text(encoding="utf-8")
text = text.replace("劳拉：克劳馥（见图4-1）", "劳拉·克劳馥（见图4-1）")
text = text.replace("图4-1《古墓丽影》中的女主角劳拉", fig41)
text = text.replace("RATMER\n\n了大量的传统意义上男性的行动、动作，因此男", "她做了大量的传统意义上男性的行动、动作，因此男")
text = text.replace("图4-2《寂静岭3》中的女主海瑟，看\n\n尤其是网络游戏设置了一些功能强大的自定义游\n\n起来就像一位真实的女性\n\n戏特征。", f"{fig42}\n\n尤其是网络游戏设置了一些功能强大的自定义游戏特征。")
text = text.replace("（自前只有对西方男女玩家群\n\n体的研究）", "（目前只有对西方男女玩家群体的研究）")
text = text.replace("（自前这种模式在很多手机\n\n游戏中仍然存在）", "（目前这种模式在很多手机游戏中仍然存在）")
text = text.replace("对胃- 的情况下", "对胃口的情况下")
text = text.replace("很天一批人", "很大一批人")
text = re.sub(r"\n{3,}", "\n\n", text)
men.write_text(text, encoding="utf-8", newline="\n")

text = stat.read_text(encoding="utf-8")
# Remove OCR fragments of chart labels/caption; preserve explanatory paragraphs around them.
chart_block = """女性数据

对特定游戏兴趣

男性数据

度的受访人数

兴趣等级为

6的男性人数

兴趣等级为

6的女性人数

10

图4-3

特定游戏的兴趣度等级：0～10"""
text = text.replace(chart_block, fig43)
text = text.replace("很天一批人", "很大一批人")
text = text.replace("图4-3说明了以上情况。", "图4-3说明了以上情况。")
text = re.sub(r"\n{3,}", "\n\n", text)
stat.write_text(text, encoding="utf-8", newline="\n")

train = CH / "04-06-exercises-training.md"
text = train.read_text(encoding="utf-8")
text = text.replace("BigFive", "Big Five")
text = text.replace("得到的测试结果是证实还是相于Jason VandenBerghe的假设，或是产生了一个不确定的\n\n结果。", "得到的测试结果是证实还是相反于 Jason VandenBerghe 的假设，或是产生了一个不确定的结果。")
text = text.replace("结果。\n\n帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary", "结果。\n\n#### 2. 选择一款游戏（也可以请朋友帮你选择一个游戏），并且在文档中记录下任何你认为包含的排除性元素（exclusionary")
text = text.replace("www.outofservice.com/\n\nbigfive", "www.outofservice.com/bigfive")
text = re.sub(r"\n{3,}", "\n\n", text)
train.write_text(text, encoding="utf-8", newline="\n")

print("Inserted Chapter 4 figures and cleaned nearby OCR text")
