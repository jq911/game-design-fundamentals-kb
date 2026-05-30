from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "ocr_pages" / "chapter07"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-07"
OUT.mkdir(parents=True, exist_ok=True)

# Coordinates are on 2.5x rendered OCR images (1224 x 1644).
# Keep only the source figure + full caption, avoiding surrounding paragraphs/page headers.
crops = [
    ("pdf_127.png", "figure-7-1-grand-theft-auto-vice-city.png", (252, 1018, 1048, 1512)),
    ("pdf_133.png", "figure-7-2-puzzle-quest.png", (290, 630, 950, 1200)),
]

for src, name, box in crops:
    im = Image.open(SRC / src).crop(box)
    im = ImageOps.grayscale(im)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageOps.autocontrast(im, cutoff=1)
    im.save(OUT / name)
    print(OUT / name, im.size)
