from pathlib import Path
from PIL import Image, ImageDraw

root = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
out = root / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-03"
files = sorted(out.glob("figure-3-*.png"), key=lambda p: int(p.name.split("-")[2]))
thumbs = []
for p in files:
    im = Image.open(p).convert("RGB")
    im.thumbnail((360, 260))
    canvas = Image.new("RGB", (380, 310), "white")
    d = ImageDraw.Draw(canvas)
    d.text((10, 8), p.name, fill=(0, 0, 0))
    canvas.paste(im, (10, 40))
    thumbs.append(canvas)

cols = 3
rows = (len(thumbs) + cols - 1) // cols
sheet = Image.new("RGB", (cols * 380, rows * 310), (245, 245, 245))
for i, t in enumerate(thumbs):
    sheet.paste(t, ((i % cols) * 380, (i // cols) * 310))

path = root / "tmp_chapter03_crops_contact.jpg"
sheet.save(path, quality=92)
print(path)
