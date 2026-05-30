from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "tmp_chapter04_figure_pages"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-04"
OUT.mkdir(parents=True, exist_ok=True)

# Coordinates are on 2.5x rendered pages. Crops include the figure and its caption only.
CROPS = [
    ("pdf_093.jpg", "figure-4-1-lara-croft-tomb-raider.png", (690, 1050, 1135, 1425)),
    ("pdf_094.jpg", "figure-4-2-heather-silent-hill-3.png", (645, 555, 1095, 930)),
    ("pdf_104.jpg", "figure-4-3-interest-rating-by-gender.png", (335, 330, 880, 860)),
]

made = []
for src_name, out_name, box in CROPS:
    img = Image.open(SRC / src_name).convert("RGB")
    crop = img.crop(box)
    out = OUT / out_name
    crop.save(out)
    made.append(out)
    print(out, crop.size)

font = ImageFont.load_default()
thumbs = []
for path in made:
    img = Image.open(path).convert("RGB")
    img.thumbnail((420, 420))
    canvas = Image.new("RGB", (460, 480), "white")
    canvas.paste(img, ((460 - img.width) // 2, 38))
    d = ImageDraw.Draw(canvas)
    d.text((10, 10), path.name, fill="black", font=font)
    thumbs.append(canvas)

contact = Image.new("RGB", (460 * len(thumbs), 480), "white")
for i, thumb in enumerate(thumbs):
    contact.paste(thumb, (i * 460, 0))
contact.save(ROOT / "tmp_chapter04_crops_contact.jpg", quality=92)
print(ROOT / "tmp_chapter04_crops_contact.jpg")
