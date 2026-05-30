from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-03"


def figure(rel_prefix: str, image: str, alt: str, caption: str) -> str:
    return (
        '<figure class="book-figure">\n'
        f'  <img src="{rel_prefix}/assets/book-images/game-design-fundamentals/chapter-03/{image}" alt="{alt}">\n'
        f'  <figcaption>{caption}</figcaption>\n'
        '</figure>'
    )


def apply(path: Path, replacements):
    text = path.read_text(encoding="utf-8")
    old = text
    for a, b in replacements:
        if a not in text:
            print(f"MISS: {path} :: {a[:80]!r}")
        text = text.replace(a, b)
    if text != old:
        path.write_text(text, encoding="utf-8", newline="\n")
        print("updated", path)

# root-level chapter pages use ../../../assets via rel_prefix ../../..
root_rel = "../../.."
# subsection pages under 03-02-classic-genres use ../../../../assets via rel_prefix ../../../..
sub_rel = "../../../.."

apply(CH / "03-01-what-is-genre.md", [
    (
        "随着这两个新型游戏平台的出现，这方面的游戏开发也得到了爆炸式的增长。像《粘粘世\n\n界》（如图3-1所示），就不能简单地划分到传统类别中的某一类中。",
        "随着这两个新型游戏平台的出现，这方面的游戏开发也得到了爆炸式的增长。像《粘粘世界》（如图3-1所示），就不能简单地划分到传统类别中的某一类中。\n\n" + figure(root_rel, "figure-3-1-world-of-goo.png", "图3-1 《粘粘世界》游戏中包含了建设、解谜以及不同寻常的物理机制", "图3-1　《粘粘世界》游戏中包含了建设、解谜以及不同寻常的物理机制")
    ),
    (
        "#### 子类型\n\n有时游戏分类是非常有用的，它可以将游\n\n戏划分为数个小型的集群或次类型，这样就能\n\n更好地让人理解游戏有哪些可玩性。像第一人\n\n称的射击类游戏，就有许多种子类型，如：竞\n\n技场类型，一种快速的多人竞赛模式（《军团\n\n要塞2》就是个典型的例子）；战术射击类型，\n\n利用潜行和有限的弹药来争取最大的战果；开\n\n放性的游戏类型，如《战地》系列；最后还有\n\n定轨射击类游戏，玩家的活动是受限制的，只\n\n图3-1《粘粘世界》游戏中包含了建设、解谜以\n\n能在一个画面内自动移动。同样，汽车赛车游\n\n及不同寻常的物理机制\n\n戏可以分组到提供作战模式和没有提供作战模式的类型中。",
        "#### 子类型\n\n有时游戏分类是非常有用的，它可以将游戏划分为数个小型的集群或次类型，这样就能更好地让人理解游戏有哪些可玩性。像第一人称的射击类游戏，就有许多种子类型，如：竞技场类型，一种快速的多人竞赛模式（《军团要塞2》就是个典型的例子）；战术射击类型，利用潜行和有限的弹药来争取最大的战果；开放性的游戏类型，如《战地》系列；最后还有定轨射击类游戏，玩家的活动是受限制的，只能在一个画面内自动移动。同样，汽车赛车游戏可以分组到提供作战模式和没有提供作战模式的类型中。"
    ),
    ("包括探和资源管理方面挑战", "包括探索和资源管理方面挑战"),
])

apply(CH / "03-02-classic-genres" / "03-02-01-shooters.md", [
    ("火。除了允许攻击的目标，武器很少会对其他东西造成伤害。", "除了允许攻击的目标，武器很少会对其他东西造成伤害。"),
    (
        "图3-2《王牌英雄》，一款多人的2D 射击游戏图3-3《孤岛危机3》，一款环境复杂的3D 射击游戏",
        figure(sub_rel, "figure-3-2-awesomenauts-2d-shooter.png", "图3-2 《王牌英雄》，一款多人的2D射击游戏", "图3-2　《王牌英雄》，一款多人的 2D 射击游戏") + "\n\n" + figure(sub_rel, "figure-3-3-crysis-3-3d-shooter.png", "图3-3 《孤岛危机3》，一款环境复杂的3D射击游戏", "图3-3　《孤岛危机3》，一款环境复杂的 3D 射击游戏")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-02-action-arcade.md", [
    (
        "图3-4《洞穴探险》，一款2D平台游戏\n\n图3-5《女孩》，一款卡通风格的格斗游戏",
        figure(sub_rel, "figure-3-4-spelunky-2d-platformer.png", "图3-4 《洞穴探险》，一款2D平台游戏", "图3-4　《洞穴探险》，一款 2D 平台游戏") + "\n\n" + figure(sub_rel, "figure-3-5-skullgirls-fighting-game.png", "图3-5 《骷髅女孩》，一款卡通风格的格斗游戏", "图3-5　《骷髅女孩》，一款卡通风格的格斗游戏")
    ),
    ("图3-5《女孩》，一款卡通风格的格斗游戏", "图3-5《骷髅女孩》，一款卡通风格的格斗游戏"),
])

apply(CH / "03-02-classic-genres" / "03-02-03-strategy.md", [
    (
        "图3-6《拿破仑：全面战争》，一款实时的策略游戏",
        figure(sub_rel, "figure-3-6-napoleon-total-war-strategy.png", "图3-6 《拿破仑：全面战争》，一款实时的策略游戏", "图3-6　《拿破仑：全面战争》，一款实时的策略游戏")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-04-role-playing.md", [
    (
        "图3-7《上古卷轴V：天际》，第一人称视角画面",
        figure(sub_rel, "figure-3-7-skyrim-first-person-rpg.png", "图3-7 《上古卷轴V：天际》，第一人称视角画面", "图3-7　《上古卷轴 V：天际》，第一人称视角画面")
    ),
    ("比大多数其他游戏\n\n力，但是在角色扮演游戏中", "比大多数其他游戏类型能发挥更丰富的作用。但是在角色扮演游戏中"),
])

apply(CH / "03-02-classic-genres" / "03-02-05-sports.md", [
    (
        "图3-8《实况足球2011》",
        figure(sub_rel, "figure-3-8-pro-evolution-soccer-2011.png", "图3-8 《实况足球2011》", "图3-8　《实况足球 2011》")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-06-vehicle-simulations.md", [
    (
        "图3-9《竞速飞驰4》的座舱视界",
        figure(sub_rel, "figure-3-9-speeding-flying-car-4-cockpit.png", "图3-9 《竞速飞驰4》的座舱视界", "图3-9　《竞速飞驰 4》的座舱视界")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-07-construction-management.md", [
    (
        "图3-10《开心农场》，一款基于浏览器并取得成功CMS游戏",
        figure(sub_rel, "figure-3-10-happy-farm-cms.png", "图3-10 《开心农场》，一款基于浏览器并取得成功的CMS游戏", "图3-10　《开心农场》，一款基于浏览器并取得成功的 CMS 游戏")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-08-adventure.md", [
    (
        "图3-11冒险游戏《暴雨》",
        figure(sub_rel, "figure-3-11-heavy-rain-adventure.png", "图3-11 冒险游戏《暴雨》", "图3-11　冒险游戏《暴雨》")
    ),
])

apply(CH / "03-02-classic-genres" / "03-02-09-puzzle.md", [
    (
        "图3-12游戏《割绳子：时光之旅》",
        figure(sub_rel, "figure-3-12-cut-the-rope-time-travel.png", "图3-12 游戏《割绳子：时光之旅》", "图3-12　游戏《割绳子：时光之旅》")
    ),
    ("发行量\n\n升。", "发行量上升。"),
])
