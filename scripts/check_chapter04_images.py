from pathlib import Path
from PIL import Image
import hashlib
import json
import re

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
IMG_DIR = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-04"
MD_FILES = [
    ROOT / "docs" / "game-design-fundamentals" / "chapter-04" / "04-02-demographics" / "04-02-01-men-and-women.md",
    ROOT / "docs" / "game-design-fundamentals" / "chapter-04" / "04-04-binary-thinking" / "04-04-01-statistical-player-groups.md",
]
EXPECTED = [
    "figure-4-1-lara-croft-tomb-raider.png",
    "figure-4-2-heather-silent-hill-3.png",
    "figure-4-3-interest-rating-by-gender.png",
]

rows = []
issues = []

for name in EXPECTED:
    path = IMG_DIR / name
    item = {"file": str(path.relative_to(ROOT)), "exists": path.exists()}
    if not path.exists():
        issues.append(f"missing: {path}")
        rows.append(item)
        continue
    data = path.read_bytes()
    item["bytes"] = len(data)
    item["sha256_12"] = hashlib.sha256(data).hexdigest()[:12]
    try:
        with Image.open(path) as im:
            item["format"] = im.format
            item["mode"] = im.mode
            item["size"] = list(im.size)
            im.verify()
        with Image.open(path) as im:
            im.load()
            item["load_ok"] = True
    except Exception as e:
        item["load_ok"] = False
        item["error"] = repr(e)
        issues.append(f"invalid image: {path}: {e!r}")
    if item.get("format") != "PNG":
        issues.append(f"not png: {path}: {item.get('format')}")
    w, h = item.get("size", [0, 0])
    if w < 200 or h < 150:
        issues.append(f"too small: {path}: {w}x{h}")
    rows.append(item)

refs = []
for md in MD_FILES:
    text = md.read_text(encoding="utf-8")
    for m in re.finditer(r'<img\s+[^>]*src="([^"]+)"[^>]*alt="([^"]*)"', text):
        refs.append({
            "markdown": str(md.relative_to(ROOT)),
            "src": m.group(1),
            "alt": m.group(2),
        })

for name in EXPECTED:
    if not any(name in ref["src"] for ref in refs):
        issues.append(f"not referenced in markdown: {name}")

report = {
    "image_dir": str(IMG_DIR),
    "images": rows,
    "markdown_refs": refs,
    "issues": issues,
}

out_json = ROOT / "tmp_chapter04_image_integrity.json"
out_md = ROOT / "tmp_chapter04_image_integrity_report.md"
out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

lines = ["# Chapter 04 Image Integrity Report", "", f"- images checked: {len(rows)}", f"- markdown refs found: {len(refs)}", f"- issues: {len(issues)}", ""]
for item in rows:
    lines.append(f"- `{item['file']}`")
    lines.append(f"  - exists: {item.get('exists')}")
    if item.get("exists"):
        lines.append(f"  - size: {item.get('size')}")
        lines.append(f"  - bytes: {item.get('bytes')}")
        lines.append(f"  - format/mode: {item.get('format')} / {item.get('mode')}")
        lines.append(f"  - load_ok: {item.get('load_ok')}")
        lines.append(f"  - sha256_12: {item.get('sha256_12')}")
    lines.append("")
if issues:
    lines.append("## Issues")
    lines.extend(f"- {issue}" for issue in issues)
else:
    lines.append("No file integrity or markdown-reference issues found.")

out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(out_md)
print("issues=", len(issues))
for item in rows:
    print(item)
