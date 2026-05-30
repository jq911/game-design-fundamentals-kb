from pathlib import Path

import fitz
from rapidocr_onnxruntime import RapidOCR

ROOT = Path(r"C:\Users\jiaqiang03\lobsterai\project\game-design-fundamentals-kb")
PDF = Path(r"C:\Users\jiaqiang03\Desktop\游戏设计基础原书第3版.pdf")
OUT_DIR = ROOT / "ocr_pages" / "chapter05"
OUT_MD = ROOT / "ocr_pages" / "chapter05_raw.md"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Chapter 5 printed pp. 88-95 maps to PDF pages 107-114 because printed page = PDF page - 19.
START_PDF, END_PDF = 107, 114
PRINTED_OFFSET = 19

ocr = RapidOCR()
doc = fitz.open(PDF)
sections = []

for pdf_page in range(START_PDF, END_PDF + 1):
    page = doc[pdf_page - 1]
    img_path = OUT_DIR / f"pdf_{pdf_page:03d}.png"
    pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False)
    pix.save(img_path)

    result, _ = ocr(str(img_path))
    rows = []
    for item in result or []:
        box, text, score = item
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]
        rows.append({
            "x": min(xs),
            "y": min(ys),
            "text": text.strip(),
            "score": float(score),
        })
    rows.sort(key=lambda r: (round(r["y"] / 18) * 18, r["x"]))
    text_lines = [r["text"] for r in rows if r["text"]]
    printed = pdf_page - PRINTED_OFFSET
    sections.append((pdf_page, printed, text_lines))

with OUT_MD.open("w", encoding="utf-8", newline="\n") as f:
    f.write("# 第 5 章 OCR 原始文本\n\n")
    f.write(f"> 来源：`{PDF}`。PDF 为扫描版，以下为 OCR 初稿，需人工校对。\n\n")
    for pdf_page, printed, lines in sections:
        f.write(f"## 书内页 {printed} / PDF 页 {pdf_page}\n\n")
        for line in lines:
            f.write(line + "\n\n")

print(OUT_MD)
