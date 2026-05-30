from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
PDF = Path(r"C:\Users\jiaqiang03\Desktop\游戏设计基础原书第3版.pdf")
OUT = ROOT / "tmp_chapter04_figure_pages"
OUT.mkdir(parents=True, exist_ok=True)

# Chapter 4 figures: 4-1 printed p.74/PDF 93, 4-2 printed p.75/PDF 94, 4-3 printed p.85/PDF 104.
pages = [93, 94, 104]
scale = 2.5

doc = fitz.open(PDF)
rendered = []
for pdf_page in pages:
    page = doc[pdf_page - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    out = OUT / f"pdf_{pdf_page:03d}.jpg"
    pix.save(out)
    rendered.append(out)
    print(out, pix.width, pix.height)

# Contact/grid previews for crop calibration.
font = ImageFont.load_default()
thumbs = []
for path in rendered:
    img = Image.open(path).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for x in range(0, w, 100):
        draw.line([(x, 0), (x, h)], fill=(255, 0, 0), width=1)
        draw.text((x + 3, 5), str(x), fill=(255, 0, 0), font=font)
    for y in range(0, h, 100):
        draw.line([(0, y), (w, y)], fill=(255, 0, 0), width=1)
        draw.text((5, y + 3), str(y), fill=(255, 0, 0), font=font)
    img.thumbnail((520, 720))
    canvas = Image.new("RGB", (540, 760), "white")
    canvas.paste(img, ((540 - img.width) // 2, 30))
    d = ImageDraw.Draw(canvas)
    d.text((10, 8), path.name, fill="black", font=font)
    thumbs.append(canvas)

contact = Image.new("RGB", (540 * len(thumbs), 760), "white")
for i, thumb in enumerate(thumbs):
    contact.paste(thumb, (i * 540, 0))
contact.save(OUT / "contact_grid.jpg", quality=92)
print(OUT / "contact_grid.jpg")
