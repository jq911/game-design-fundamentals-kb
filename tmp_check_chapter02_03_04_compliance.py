from pathlib import Path
import json
import posixpath
import re
import subprocess
import sys

import yaml
from PIL import Image

ROOT = Path.cwd()
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"
CHAPTERS = ["chapter-02", "chapter-03", "chapter-04"]
START = "<!-- chapter-pager:start -->"

issues = []

def add(kind: str, path: Path, msg: str):
    issues.append({"kind": kind, "path": str(path).replace("\\", "/"), "msg": msg})

cfg = yaml.safe_load(MKDOCS.read_text(encoding="utf-8"))
nav_pages = []

def walk(node):
    if isinstance(node, str):
        nav_pages.append(node)
    elif isinstance(node, list):
        for item in node:
            walk(item)
    elif isinstance(node, dict):
        for child in node.values():
            walk(child)

walk(cfg.get("nav", []))
nav_set = set(nav_pages)

for chapter in CHAPTERS:
    chapter_root = DOCS / "game-design-fundamentals" / chapter
    files = sorted(chapter_root.rglob("*.md"))
    if not files:
        add("missing", chapter_root, "chapter directory has no Markdown files")
        continue

    for f in files:
        rel = f.relative_to(DOCS).as_posix()
        if rel not in nav_set:
            add("nav", f, "Markdown file is not included in mkdocs.yml nav")

    idx = chapter_root / "index.md"
    if not idx.exists():
        add("chapter-index", idx, "missing chapter index.md")
    else:
        s = idx.read_text(encoding="utf-8")
        heads = [h.strip() for h in re.findall(r"(?m)^##\s+(.+)$", s)]
        if heads != ["本章定位", "复习线索"]:
            add("chapter-index", idx, f"chapter title page sections are {heads}, expected ['本章定位', '复习线索']")
        for bad in ["## 原书内容整理", "## 我的批注区", "阅读提示", "子小节目录", "本节开篇"]:
            if bad in s:
                add("chapter-index", idx, f"forbidden/invalid content found: {bad}")

    for f in files:
        s = f.read_text(encoding="utf-8")
        rel = f.relative_to(DOCS).as_posix()
        page_url = rel[:-len("index.md")] if rel.endswith("/index.md") else rel[:-3] + "/"
        base = page_url if page_url.endswith("/") else posixpath.dirname(page_url) + "/"

        for bad in ["阅读提示", "子小节目录", "本节开篇"]:
            if bad in s:
                add("forbidden-block", f, f"contains forbidden block/text: {bad}")

        if f.name != "index.md":
            if "## 原书内容整理" not in s:
                add("regular-page", f, "regular page missing ## 原书内容整理")
            if "## 我的批注区" not in s:
                add("regular-page", f, "regular page missing ## 我的批注区")

        pager_count = s.count(START)
        if pager_count != 2:
            add("pager", f, f"expected 2 pager blocks, found {pager_count}")

        first_h1 = re.search(r"(?m)^#\s+", s)
        if START in s and first_h1 and s.find(START) > first_h1.start():
            add("pager", f, "top pager appears after H1")

        if f.name != "index.md" and "## 我的批注区" in s:
            bottom_pager = s.rfind(START)
            comments = s.find("## 我的批注区")
            if bottom_pager > comments:
                add("pager", f, "bottom pager appears after ## 我的批注区")

        for m in re.finditer(r'<img\s+[^>]*src="([^"]+)"', s):
            src = m.group(1)
            if src.startswith(("http://", "https://", "/")):
                continue
            norm = posixpath.normpath(posixpath.join(base, src))
            target = DOCS / norm
            if not target.exists():
                add("image-path", f, f"image src does not resolve under MkDocs clean URL: {src} -> {norm}")

        for pat in ["## 书内页", "PDF 页", "Cuotee", "阅读路径", "当前整理状态"]:
            if pat in s:
                add("artifact", f, f"suspicious leftover: {pat}")

        for line_no, line in enumerate(s.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith(("图2-", "图3-", "图4-", "表2-", "表3-", "表4-")) and "<figcaption>" not in stripped:
                add("caption-leftover", f, f"line {line_no}: standalone figure/table caption remains: {stripped[:120]}")

for chapter in CHAPTERS:
    imgdir = DOCS / "assets" / "book-images" / "game-design-fundamentals" / chapter
    if imgdir.exists():
        for img in sorted(imgdir.glob("*.png")):
            try:
                im = Image.open(img)
                w, h = im.size
                if w < 180 or h < 120:
                    add("image-size", img, f"image is very small: {w}x{h}")
            except Exception as e:
                add("image-open", img, f"cannot open image: {e}")

report = ROOT / "tmp_chapter02_03_04_compliance_report.json"
report.write_text(json.dumps(issues, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"compliance issues={len(issues)}")
for issue in issues:
    print(f"[{issue['kind']}] {issue['path']}: {issue['msg']}")
print(f"report={report}")
