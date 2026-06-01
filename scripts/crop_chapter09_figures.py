from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "ocr_pages" / "chapter09"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-09"
OUT.mkdir(parents=True, exist_ok=True)

# Crops from 2.5x rendered scanned pages. Coordinates are (left, top, right, bottom).
crops = [
    ("pdf_166.png", "figure-9-1-rollercoaster-tycoon-track-designer.png", (305, 870, 925, 1225), None),
    # Crop only the figure body. The printed caption is supplied by Markdown figcaption.
    ("pdf_168.png", "figure-9-2-draw-something.png", (745, 430, 1125, 910), (58, 225, 138, 345)),
]

for src_name, out_name, box, blur_box in crops:
    im = Image.open(SRC / src_name).crop(box)
    if blur_box:
        region = im.crop(blur_box).filter(ImageFilter.GaussianBlur(radius=16))
        im.paste(region, blur_box)
    im = ImageOps.grayscale(im)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageOps.autocontrast(im, cutoff=1)
    im.save(OUT / out_name)
    print(out_name, im.size)
