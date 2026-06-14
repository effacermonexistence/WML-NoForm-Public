#!/usr/bin/env python3
"""Build a Gmail/email-ready rasterized PDF from a locked WML packet.

This preserves page order and visual layout while reducing size for direct email
attachment. It is intended for WML evidence packets after final visual approval.

Usage:
  python make_email_ready_pdf.py INPUT.pdf OUTPUT.pdf --dpi 100 --quality 70

Requires the Codex primary runtime dependencies: pypdf, reportlab, and pdftoppm.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from pypdf import PdfReader
from reportlab.pdfgen import canvas

DEFAULT_PDFTOPPM = "/Users/effacermonexistencecodex/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/pdftoppm"


def build_email_ready(input_pdf: Path, output_pdf: Path, dpi: int, quality: int, pdftoppm: str) -> None:
    input_pdf = input_pdf.expanduser().resolve()
    output_pdf = output_pdf.expanduser().resolve()
    if not input_pdf.exists():
        raise FileNotFoundError(input_pdf)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    tmp = Path(tempfile.mkdtemp(prefix="wml_email_ready_pages_"))
    try:
        prefix = str(tmp / "page")
        subprocess.run(
            [pdftoppm, "-jpeg", "-r", str(dpi), "-jpegopt", f"quality={quality}", str(input_pdf), prefix],
            check=True,
        )
        images = sorted(tmp.glob("page-*.jpg"))
        if not images:
            raise RuntimeError("pdftoppm did not produce raster pages")

        reader = PdfReader(str(input_pdf))
        c = canvas.Canvas(str(output_pdf), pageCompression=1)
        for idx, image_path in enumerate(images):
            media = reader.pages[idx].mediabox
            width = float(media.width)
            height = float(media.height)
            c.setPageSize((width, height))
            c.drawImage(str(image_path), 0, 0, width=width, height=height, preserveAspectRatio=False, mask="auto")
            c.showPage()
        c.save()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an email-ready WML PDF attachment.")
    parser.add_argument("input_pdf", type=Path)
    parser.add_argument("output_pdf", type=Path)
    parser.add_argument("--dpi", type=int, default=100)
    parser.add_argument("--quality", type=int, default=70)
    parser.add_argument("--pdftoppm", default=os.environ.get("PDFTOPPM", DEFAULT_PDFTOPPM))
    args = parser.parse_args()

    build_email_ready(args.input_pdf, args.output_pdf, args.dpi, args.quality, args.pdftoppm)
    size_mb = args.output_pdf.expanduser().resolve().stat().st_size / 1024 / 1024
    pages = len(PdfReader(str(args.output_pdf.expanduser().resolve())).pages)
    print(f"wrote={args.output_pdf}")
    print(f"pages={pages}")
    print(f"size_mb={size_mb:.2f}")


if __name__ == "__main__":
    main()
