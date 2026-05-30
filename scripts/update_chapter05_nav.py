from pathlib import Path

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
MKDOCS = ROOT / "mkdocs.yml"

chapter5 = """      - 第 5 章 了解你的游戏设备:
          - 章节导览: game-design-fundamentals/chapter-05/index.md
          - 5.1 家用游戏机:
              - 导览: game-design-fundamentals/chapter-05/05-01-home-game-consoles.md
              - 5.1.1 典型用法: game-design-fundamentals/chapter-05/05-01-home-game-consoles/05-01-01-typical-usage.md
              - 5.1.2 输入设备: game-design-fundamentals/chapter-05/05-01-home-game-consoles/05-01-02-input-devices.md
              - 5.1.3 业务考虑: game-design-fundamentals/chapter-05/05-01-home-game-consoles/05-01-03-business-considerations.md
          - 5.2 个人计算机:
              - 导览: game-design-fundamentals/chapter-05/05-02-personal-computers.md
              - 5.2.1 典型用法: game-design-fundamentals/chapter-05/05-02-personal-computers/05-02-01-typical-usage.md
              - 5.2.2 输入设备: game-design-fundamentals/chapter-05/05-02-personal-computers/05-02-02-input-devices.md
              - 5.2.3 业务考虑: game-design-fundamentals/chapter-05/05-02-personal-computers/05-02-03-business-considerations.md
          - 5.3 便携设备:
              - 导览: game-design-fundamentals/chapter-05/05-03-portable-devices.md
              - 5.3.1 典型用法: game-design-fundamentals/chapter-05/05-03-portable-devices/05-03-01-typical-usage.md
              - 5.3.2 输入设备: game-design-fundamentals/chapter-05/05-03-portable-devices/05-03-02-input-devices.md
              - 5.3.3 专用游戏手持设备: game-design-fundamentals/chapter-05/05-03-portable-devices/05-03-03-dedicated-handhelds.md
              - 5.3.4 手机和无线设备: game-design-fundamentals/chapter-05/05-03-portable-devices/05-03-04-mobile-and-wireless-devices.md
          - 5.4 其他设备: game-design-fundamentals/chapter-05/05-04-other-devices.md
          - 5.5 本章总结: game-design-fundamentals/chapter-05/05-05-summary.md
          - 5.6 设计练习：训练: game-design-fundamentals/chapter-05/05-06-exercises-training.md
"""

text = MKDOCS.read_text(encoding="utf-8")
if "      - 第 5 章 了解你的游戏设备:" in text:
    print("Chapter 5 nav already present")
else:
    marker = "          - 4.7 设计练习：习题: game-design-fundamentals/chapter-04/04-07-exercises-questions.md\n"
    if marker not in text:
        raise SystemExit("Cannot find Chapter 4 nav end marker")
    text = text.replace(marker, marker + chapter5)
    MKDOCS.write_text(text, encoding="utf-8", newline="\n")
    print("Inserted Chapter 5 nav")
