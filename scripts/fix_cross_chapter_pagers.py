from pathlib import Path
import posixpath
import re
import yaml

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
START = "<!-- chapter-pager:start -->"
END = "<!-- chapter-pager:end -->"

with MKDOCS.open("r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

pages = []

def walk(node):
    if isinstance(node, str):
        pages.append(node)
    elif isinstance(node, list):
        for item in node:
            walk(item)
    elif isinstance(node, dict):
        for _title, child in node.items():
            walk(child)

walk(cfg.get("nav", []))
# Work only on the book chapter pages, in exact nav order.
pages = [p for p in pages if p.startswith("game-design-fundamentals/chapter-")]

missing = [p for p in pages if not (DOCS / p).exists()]
if missing:
    raise SystemExit("Missing nav files:\n" + "\n".join(missing))


def page_url(path: str) -> str:
    if path.endswith("/index.md"):
        return path[:-len("index.md")]
    if path.endswith(".md"):
        return path[:-3] + "/"
    return path


def rel_link(src: str, dst: str) -> str:
    src_dir = page_url(src)
    if not src_dir.endswith("/"):
        src_dir = posixpath.dirname(src_dir) + "/"
    return posixpath.relpath(page_url(dst), start=src_dir).replace("\\", "/")


def button(kind: str, target: str | None, current: str) -> str:
    label = "上一页" if kind == "prev" else "下一页"
    if not target:
        return f'<span class="chapter-pager__button chapter-pager__button--{kind} chapter-pager__button--disabled"><span class="chapter-pager__label">{label}</span></span>'
    return f'<a class="chapter-pager__button chapter-pager__button--{kind}" href="{rel_link(current, target)}"><span class="chapter-pager__label">{label}</span></a>'


def pager(current: str, prev_page: str | None, next_page: str | None, pos: str) -> str:
    return f"""{START}

<div class="chapter-pager chapter-pager--{pos}">
{button('prev', prev_page, current)}
{button('next', next_page, current)}
</div>

{END}"""


def strip_pagers(text: str) -> str:
    return re.sub(rf"\n*{re.escape(START)}.*?{re.escape(END)}\n*", "\n\n", text, flags=re.S).strip() + "\n"


def insert_pagers(text: str, current: str, prev_page: str | None, next_page: str | None) -> str:
    text = strip_pagers(text)
    top = pager(current, prev_page, next_page, "top")
    bottom = pager(current, prev_page, next_page, "bottom")
    m = re.search(r"(?m)^# .+\n", text)
    if m:
        text = text[:m.start()].rstrip() + "\n\n" + top + "\n\n" + text[m.start():].lstrip()
    else:
        text = top + "\n\n" + text
    marker = "\n## 我的批注区"
    if marker in text:
        before, after = text.split(marker, 1)
        return before.rstrip() + "\n\n" + bottom + "\n\n" + marker.lstrip("\n") + after
    return text.rstrip() + "\n\n" + bottom + "\n"

for i, current in enumerate(pages):
    prev_page = pages[i - 1] if i > 0 else None
    next_page = pages[i + 1] if i + 1 < len(pages) else None
    path = DOCS / current
    text = path.read_text(encoding="utf-8")
    path.write_text(insert_pagers(text, current, prev_page, next_page), encoding="utf-8", newline="\n")

print(f"Updated pagers across {len(pages)} chapter pages")
print("first:", pages[0], "next=", pages[1] if len(pages) > 1 else None)
print("last:", pages[-1], "prev=", pages[-2] if len(pages) > 1 else None)
