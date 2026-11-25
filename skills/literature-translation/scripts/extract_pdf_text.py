#!/usr/bin/env python3
"""Extract full text page-by-page from an academic PDF for translation & table extraction."""

import argparse
import os
import subprocess
import sys


def extract_with_pypdf(pdf_path: str) -> list[str]:
    from pypdf import PdfReader  # type: ignore

    reader = PdfReader(pdf_path)
    return [page.extract_text() or "" for page in reader.pages]


def extract_with_pymupdf(pdf_path: str) -> list[str]:
    import fitz  # type: ignore

    doc = fitz.open(pdf_path)
    return [page.get_text("text") or "" for page in doc]


def extract_with_pdftotext(pdf_path: str) -> list[str]:
    out = subprocess.check_output(["pdftotext", pdf_path, "-"]).decode("utf-8", errors="replace")
    return out.split("\x0c")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract full text page-by-page from a PDF.")
    parser.add_argument("pdf_path", help="Absolute path to input PDF")
    parser.add_argument("output_txt", help="Absolute path to output UTF-8 text file")
    args = parser.parse_args()

    if not os.path.isfile(args.pdf_path):
        print(f"Error: PDF not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    pages: list[str] | None = None
    used_backend = ""
    for name, fn in [
        ("pymupdf", extract_with_pymupdf),
        ("pypdf", extract_with_pypdf),
        ("pdftotext", extract_with_pdftotext),
    ]:
        try:
            pages = fn(args.pdf_path)
            used_backend = name
            break
        except Exception:
            continue

    if pages is None:
        print("Error: Neither pymupdf, pypdf, nor pdftotext is available.", file=sys.stderr)
        sys.exit(2)

    os.makedirs(os.path.dirname(os.path.abspath(args.output_txt)), exist_ok=True)
    with open(args.output_txt, "w", encoding="utf-8") as f:
        for idx, text in enumerate(pages, start=1):
            f.write(f"\n--- PAGE {idx} ---\n")
            f.write(text.strip() + "\n")

    print(f"Extracted {len(pages)} pages using {used_backend} -> {args.output_txt}")


if __name__ == "__main__":
    main()
