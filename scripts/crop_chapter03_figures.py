from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
SRC = ROOT / "tmp_chapter03_figure_pages"
OUT = ROOT / "docs" / "assets" / "book-images" / "game-design-fundamentals" / "chapter-03"
OUT.mkdir(parents=True, exist_ok=True)

# Coordinates are for source pages rendered at 2.5x, about 1224x1642/1644.
# QA target: complete figure + original caption, no surrounding paragraph/header/footer text.
crops = [
    ("pdf_080.jpg", "figure-3-1-world-of-goo.png", (600, 395, 1060, 830)),
    ("pdf_081.jpg", "figure-3-2-awesomenauts-2d-shooter.png", (95, 970, 590, 1325)),
    ("pdf_081.jpg", "figure-3-3-crysis-3-3d-shooter.png", (585, 970, 1085, 1325)),
    ("pdf_082.jpg", "figure-3-4-spelunky-2d-platformer.png", (95, 970, 590, 1325)),
    ("pdf_082.jpg", "figure-3-5-skullgirls-fighting-game.png", (585, 970, 1085, 1325)),
    ("pdf_083.jpg", "figure-3-6-napoleon-total-war-strategy.png", (645, 170, 1110, 515)),
    ("pdf_083.jpg", "figure-3-7-skyrim-first-person-rpg.png", (650, 875, 1115, 1215)),
    ("pdf_084.jpg", "figure-3-8-pro-evolution-soccer-2011.png", (640, 430, 1100, 765)),
    ("pdf_084.jpg", "figure-3-9-speeding-flying-car-4-cockpit.png", (660, 1205, 1120, 1495)),
    ("pdf_085.jpg", "figure-3-10-happy-farm-cms.png", (350, 535, 965, 1015)),
    ("pdf_085.jpg", "figure-3-11-heavy-rain-adventure.png", (690, 1115, 1165, 1460)),
    ("pdf_086.jpg", "figure-3-12-cut-the-rope-time-travel.png", (735, 455, 1120, 955)),
]

for src, name, box in crops:
    im = Image.open(SRC / src).crop(box)
    im = ImageOps.grayscale(im)
    im = ImageEnhance.Contrast(im).enhance(1.08)
    im = ImageOps.autocontrast(im, cutoff=1)
    im.save(OUT / name)
    print(OUT / name, im.size)
