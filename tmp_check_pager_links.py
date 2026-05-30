from pathlib import Path
import re
import posixpath

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
DOCS = ROOT / "docs"
BASE = "/game-design-fundamentals-kb/"
issues = []


def clean_url_for_md(md: Path) -> str:
    rel = md.relative_to(DOCS).as_posix()
    if rel.endswith("/index.md"):
        return BASE + rel[:-len("index.md")]
    return BASE + rel[:-3] + "/"

valid = {clean_url_for_md(p).rstrip("/") for p in DOCS.rglob("*.md")}

chapter_files = sorted((DOCS / "game-design-fundamentals").glob("chapter-*/*.md")) + sorted((DOCS / "game-design-fundamentals").glob("chapter-*/*/*.md"))
for md in chapter_files:
    base_url = clean_url_for_md(md)
    text = md.read_text(encoding="utf-8")
    for m in re.finditer(r'class="chapter-pager__button[^"]*" href="([^"]+)"', text):
        href = m.group(1)
        # Clean MkDocs URLs end in '/', so raw relative links resolve from the current page URL directory.
        resolved = posixpath.normpath(posixpath.join(base_url, href)).rstrip('/')
        if resolved not in valid:
            issues.append((str(md.relative_to(ROOT)), href, resolved))

print(f"pager link issues={len(issues)}")
for issue in issues[:100]:
    print(issue)
