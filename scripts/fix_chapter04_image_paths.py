from pathlib import Path
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
CH = ROOT / "docs" / "game-design-fundamentals" / "chapter-04"

for md in sorted(CH.rglob("*.md")):
    text = md.read_text(encoding="utf-8")
    # MkDocs Material clean URLs render each Markdown file as its own directory,
    # so raw HTML image links need one more ../ than the filesystem parent depth.
    depth_from_docs = len(md.relative_to(ROOT / "docs").parts)
    prefix = "../" * depth_from_docs
    new = re.sub(
        r'src="(?:\.\./)+assets/book-images/game-design-fundamentals/chapter-04/',
        f'src="{prefix}assets/book-images/game-design-fundamentals/chapter-04/',
        text,
    )
    if new != text:
        md.write_text(new, encoding="utf-8", newline="\n")
        print(f"fixed {md.relative_to(ROOT)} -> prefix {prefix}")
