from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "ocr_pages" / "chapter10"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-10"
OUT.mkdir(parents=True, exist_ok=True)

# Crops from 2.5x rendered scanned pages. Coordinates are (left, top, right, bottom).
crops = [
    ("pdf_175.png", "figure-10-1-lotro-avatar-creation.png", (360, 980, 875, 1235)),
    ("pdf_180.png", "figure-10-2-cartoon-characters.png", (225, 610, 1035, 955)),
    ("pdf_184.png", "figure-10-3-mongolian-rider-concept-art.png", (55, 115, 430, 520)),
    ("pdf_184.png", "figure-10-4-edgar-model-sheet.png", (450, 125, 1115, 535)),
    ("pdf_186.png", "figure-10-5-power-golf-character-development.png", (330, 515, 940, 765)),
    ("pdf_189.png", "figure-10-6-zero-dimensional-character.png", (760, 600, 1115, 735)),
    ("pdf_189.png", "figure-10-7-one-dimensional-character.png", (235, 880, 1035, 1000)),
    ("pdf_189.png", "figure-10-8-two-dimensional-character.png", (230, 1325, 1030, 1455)),
    ("pdf_190.png", "figure-10-9-three-dimensional-character.png", (722, 300, 1110, 665)),
]

for src_name, out_name, box in crops:
    im = Image.open(SRC / src_name).crop(box)
    im = ImageOps.grayscale(im)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageOps.autocontrast(im, cutoff=1)
    im.save(OUT / out_name)
    print(out_name, im.size)
