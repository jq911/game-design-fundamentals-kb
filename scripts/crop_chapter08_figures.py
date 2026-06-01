from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "ocr_pages" / "chapter08"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-08"
OUT.mkdir(parents=True, exist_ok=True)

# Crops from 2.5x rendered scanned pages. Coordinates are (left, top, right, bottom).
crops = [
    ("pdf_139.png", "figure-8-1-prince-of-persia-classic-2d.png", (690, 885, 1165, 1095)),
    ("pdf_140.png", "figure-8-2-starcraft-terrain.png", (70, 410, 535, 720)),
    ("pdf_140.png", "figure-8-3-need-for-speed-most-wanted-3d.png", (565, 405, 1110, 735)),
    ("pdf_140.png", "figure-8-4-legacy-of-kain-material-spectral.png", (710, 805, 1138, 1325)),
    ("pdf_142.png", "figure-8-5-age-of-empires-scale.png", (585, 190, 1125, 510)),
    ("pdf_143.png", "figure-8-6-spore-sphere-world.png", (245, 480, 970, 875)),
    ("pdf_145.png", "figure-8-7-settlers-irregular-time.png", (210, 185, 940, 590)),
    ("pdf_146.png", "figure-8-8-cleopatra-cultural-background.png", (245, 890, 920, 1305)),
    ("pdf_147.png", "figure-8-9-grim-fandango-style.png", (300, 775, 890, 1210)),
    ("pdf_148.png", "figure-8-10-spec-ops-sandstorm-dubai.png", (245, 825, 865, 1125)),
    ("pdf_149.png", "figure-8-11-naruto-visual-style.png", (245, 1185, 1110, 1465)),
    ("pdf_151.png", "figure-8-12-medieval-fantasy-example.png", (340, 120, 965, 555)),
    ("pdf_153.png", "figure-8-13-final-fantasy-aerith-death.png", (720, 205, 1135, 515)),
    ("pdf_156.png", "figure-8-14-americas-army-moral-perspective.png", (320, 345, 900, 745)),
]

for src_name, out_name, box in crops:
    im = Image.open(SRC / src_name).crop(box)
    im = ImageOps.grayscale(im)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageOps.autocontrast(im, cutoff=1)
    im.save(OUT / out_name)
    print(out_name, im.size)
