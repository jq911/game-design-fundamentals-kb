from pathlib import Path
import posixpath
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-04"

order = [
    ("index.md", "第 4 章导览"),
    ("04-01-vandenberghe-five-domains.md", "4.1 VandenBerghe 的 5 种游戏领域"),
    ("04-01-vandenberghe-five-domains/04-01-01-five-factor-model.md", "4.1.1 五因素模型"),
    ("04-01-vandenberghe-five-domains/04-01-02-five-game-domains.md", "4.1.2 5种游戏领域"),
    ("04-01-vandenberghe-five-domains/04-01-03-story-attitude.md", "4.1.3 另一个领域：讲故事的态度"),
    ("04-02-demographics.md", "4.2 人口统计分类"),
    ("04-02-demographics/04-02-01-men-and-women.md", "4.2.1 男人和女人"),
    ("04-02-demographics/04-02-02-boys-and-girls.md", "4.2.2 男孩和女孩"),
    ("04-02-demographics/04-02-03-games-for-girls.md", "4.2.3 女孩的游戏"),
    ("04-03-player-dedication.md", "4.3 玩家贡献"),
    ("04-04-binary-thinking.md", "4.4 二元性思维的危害"),
    ("04-04-binary-thinking/04-04-01-statistical-player-groups.md", "4.4.1 从统计学角度研究玩家群体"),
    ("04-04-binary-thinking/04-04-02-inclusiveness-not-universality.md", "4.4.2 致力于包容性，而不是普遍性"),
    ("04-05-summary.md", "4.5 本章总结"),
    ("04-06-exercises-training.md", "4.6 设计练习：训练"),
    ("04-07-exercises-questions.md", "4.7 设计练习：习题"),
]

START = "<!-- chapter-pager:start -->"
END = "<!-- chapter-pager:end -->"

def page_url(path: str) -> str:
    if path == "index.md":
        return "./"
    if path.endswith("/index.md"):
        return path[:-len("index.md")]
    if path.endswith(".md"):
        return path[:-3] + "/"
    return path


def rel_link(src: str, dst: str) -> str:
    src_url_dir = page_url(src)
    if not src_url_dir.endswith("/"):
        src_url_dir = posixpath.dirname(src_url_dir) + "/"
    dst_url = page_url(dst)
    return posixpath.relpath(dst_url, start=src_url_dir).replace("\\", "/")


def button(kind: str, target, current_path: str) -> str:
    label = "上一页" if kind == "prev" else "下一页"
    if not target:
        return f'<span class="chapter-pager__button chapter-pager__button--{kind} chapter-pager__button--disabled"><span class="chapter-pager__label">{label}</span></span>'
    path, _title = target
    href = rel_link(current_path, path)
    return f'<a class="chapter-pager__button chapter-pager__button--{kind}" href="{href}"><span class="chapter-pager__label">{label}</span></a>'


def pager(idx: int, position: str) -> str:
    current_path, _ = order[idx]
    prev_target = order[idx - 1] if idx > 0 else None
    next_target = order[idx + 1] if idx + 1 < len(order) else None
    return f"""{START}

<div class="chapter-pager chapter-pager--{position}">
{button('prev', prev_target, current_path)}
{button('next', next_target, current_path)}
</div>

{END}"""


def strip_existing(text: str) -> str:
    return re.sub(rf"\n*{re.escape(START)}.*?{re.escape(END)}\n*", "\n\n", text, flags=re.S).rstrip() + "\n"


def insert_pagers(text: str, idx: int) -> str:
    text = strip_existing(text)
    top_block = pager(idx, "top")
    bottom_block = pager(idx, "bottom")
    heading_match = re.search(r"(?m)^# .+\n", text)
    if heading_match:
        insert_at = heading_match.start()
        text = text[:insert_at].rstrip() + "\n\n" + top_block + "\n\n" + text[insert_at:].lstrip()
    notes_marker = "\n## 我的批注区"
    if notes_marker in text:
        before, after = text.split(notes_marker, 1)
        return before.rstrip() + "\n\n" + bottom_block + "\n\n" + notes_marker.lstrip("\n") + after
    return text.rstrip() + "\n\n" + bottom_block + "\n"

for idx, (path, _title) in enumerate(order):
    file_path = CH / path
    if not file_path.exists():
        raise FileNotFoundError(file_path)
    text = file_path.read_text(encoding="utf-8")
    file_path.write_text(insert_pagers(text, idx), encoding="utf-8", newline="\n")

print(f"Updated {len(order)} chapter 4 pages with previous/next pager")
