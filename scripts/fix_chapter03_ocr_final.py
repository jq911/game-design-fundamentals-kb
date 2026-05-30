from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-03"


def replace(path: Path, old: str, new: str):
    text = path.read_text(encoding="utf-8")
    if old not in text:
        print(f"MISS: {path} :: {old[:90]!r}")
        return
    path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")
    print("fixed", path)

# 3.1 OCR: “探索”缺字。
replace(
    CH / "03-01-what-is-genre.md",
    "游戏中有包括探和资源管理方面挑战的高级别的回合制模式",
    "游戏中有包括探索和资源管理方面挑战的高级别的回合制模式",
)

# 3.2.3 图 3-6 浮动图片打断句子，改为先放图，再接后文。
replace(
    CH / "03-02-classic-genres" / "03-02-03-strategy.md",
    "挑战。有时也会加入经济和探索挑战来延迟游戏时间，丰富游戏类型（如图3-6所示）。游戏进行一段时间之后，还会出现实体对抗",
    "挑战。有时也会加入经济和探索挑战来延迟游戏时间，丰富游戏类型（如图3-6所示）。\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-6-napoleon-total-war-strategy.png\" alt=\"图3-6 《拿破仑：全面战争》，一款实时的策略游戏\">\n  <figcaption>图3-6　《拿破仑：全面战争》，一款实时的策略游戏</figcaption>\n</figure>\n\n游戏进行一段时间之后，还会出现实体对抗",
)
replace(
    CH / "03-02-classic-genres" / "03-02-03-strategy.md",
    "游戏。例如，西洋跳棋（国际跳棋）就是\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-6-napoleon-total-war-strategy.png\" alt=\"图3-6 《拿破仑：全面战争》，一款实时的策略游戏\">\n  <figcaption>图3-6　《拿破仑：全面战争》，一款实时的策略游戏</figcaption>\n</figure>\n\n一个抽象的战争游戏；",
    "游戏。例如，西洋跳棋（国际跳棋）就是一个抽象的战争游戏；",
)

# 3.2.4 补回 OCR 漏掉的 RPG 说明句。
replace(
    CH / "03-02-classic-genres" / "03-02-04-role-playing.md",
    "角色扮演游戏（RPG）允许玩家以更广的方式与游戏世界进行交互，比大多数其他游戏类型能发挥更丰富的作用。但是在角色扮演游戏中，玩家通过经验和选择希望培养哪一项特殊的技能来获得它们。",
    "角色扮演游戏（RPG）允许玩家以更广的方式与游戏世界进行交互，比大多数其他游戏类型能发挥更丰富的作用。角色扮演游戏允许玩家体验现实中不可能实现的某些东西：从一个普通人到一个具有惊人能量的超级英雄的成长的感觉。很多游戏都立即提供给玩家这种能力，但是在角色扮演游戏中，玩家通过经验和选择希望培养哪一项特殊的技能来获得它们。",
)

# 3.2.5 修正破折号 OCR，并把图 3-8 移到引用句后。
replace(
    CH / "03-02-classic-genres" / "03-02-05-sports.md",
    "一个非常令人愉快的一而且有利可图的——产品线。",
    "一个非常令人愉快的——而且有利可图的——产品线。",
)
replace(
    CH / "03-02-classic-genres" / "03-02-05-sports.md",
    "接进行对比（如图3-8所示）。当然，并不是所有体育游戏都是极端现实主义的。有的，比如说Electronic Arts公司的怀旧\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-8-pro-evolution-soccer-2011.png\" alt=\"图3-8 《实况足球2011》\">\n  <figcaption>图3-8　《实况足球 2011》</figcaption>\n</figure>\n\nSega Genesis游戏",
    "接进行对比（如图3-8所示）。\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-8-pro-evolution-soccer-2011.png\" alt=\"图3-8 《实况足球2011》\">\n  <figcaption>图3-8　《实况足球 2011》</figcaption>\n</figure>\n\n当然，并不是所有体育游戏都是极端现实主义的。有的，比如说Electronic Arts公司的怀旧 Sega Genesis游戏",
)

# 3.2.6 图 3-9 移到引用句后，避免打断“试图再现”。
replace(
    CH / "03-02-classic-genres" / "03-02-06-vehicle-simulations.md",
    "控制一个机器差不多。如果你在设计一个虚拟的交通工具",
    "控制一个机器差不多。\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-9-speeding-flying-car-4-cockpit.png\" alt=\"图3-9 《竞速飞驰4》的座舱视界\">\n  <figcaption>图3-9　《竞速飞驰 4》的座舱视界</figcaption>\n</figure>\n\n如果你在设计一个虚拟的交通工具",
)
replace(
    CH / "03-02-classic-genres" / "03-02-06-vehicle-simulations.md",
    "有组织的竞赛模拟试图\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-9-speeding-flying-car-4-cockpit.png\" alt=\"图3-9 《竞速飞驰4》的座舱视界\">\n  <figcaption>图3-9　《竞速飞驰 4》的座舱视界</figcaption>\n</figure>\n\n再现在已经存在的赛事",
    "有组织的竞赛模拟试图再现在已经存在的赛事",
)

# 3.2.8 图 3-11 移到引用句后。
replace(
    CH / "03-02-classic-genres" / "03-02-08-adventure.md",
    "一个虚构的独立人物、一个主角、故事的主角。虽然角色扮演游戏和冒险游戏都拥有这种品质，\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-11-heavy-rain-adventure.png\" alt=\"图3-11 冒险游戏《暴雨》\">\n  <figcaption>图3-11　冒险游戏《暴雨》</figcaption>\n</figure>\n\n但RPG游戏通常提供",
    "一个虚构的独立人物、一个主角、故事的主角。\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-11-heavy-rain-adventure.png\" alt=\"图3-11 冒险游戏《暴雨》\">\n  <figcaption>图3-11　冒险游戏《暴雨》</figcaption>\n</figure>\n\n虽然角色扮演游戏和冒险游戏都拥有这种品质，但RPG游戏通常提供",
)

# 3.2.9 图 3-12 移到引用句后，修正“追求”断裂。
replace(
    CH / "03-02-classic-genres" / "03-02-09-puzzle.md",
    "示）是两个例外，它们只需试错就可以通过。而寻找隐藏物品的游戏可以算作解谜游戏",
    "示）是两个例外，它们只需试错就可以通过。\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-12-cut-the-rope-time-travel.png\" alt=\"图3-12 游戏《割绳子：时光之旅》\">\n  <figcaption>图3-12　游戏《割绳子：时光之旅》</figcaption>\n</figure>\n\n而寻找隐藏物品的游戏可以算作解谜游戏",
)
replace(
    CH / "03-02-classic-genres" / "03-02-09-puzzle.md",
    "它们是休闲游戏的主要类型，而且也不用去过于追\n\n<figure class=\"book-figure\">\n  <img src=\"../../../../assets/book-images/game-design-fundamentals/chapter-03/figure-3-12-cut-the-rope-time-travel.png\" alt=\"图3-12 游戏《割绳子：时光之旅》\">\n  <figcaption>图3-12　游戏《割绳子：时光之旅》</figcaption>\n</figure>\n\n求娱乐性和成功。",
    "它们是休闲游戏的主要类型，而且也不用去过于追求娱乐性和成功。",
)
