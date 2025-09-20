"""
Batch convert all PDFs in the current directory to PNG images.

Output directory: ./png (created if it doesn't exist)
Dependency: PyMuPDF (install with: pip install pymupdf)
"""

from pathlib import Path
import sys

try:
    import fitz  # PyMuPDF
except Exception as exc:  # pragma: no cover
    print("[ERROR] PyMuPDF not installed. Install with: pip install pymupdf", file=sys.stderr)
    raise


def convert_pdf_to_png(pdf_path: Path, output_dir: Path, zoom: float = 2.0) -> int:
    """Convert a single PDF to PNGs (one per page). Returns number of pages converted."""
    pages_converted = 0
    with fitz.open(pdf_path) as doc:
        for page_index in range(doc.page_count):
            page = doc.load_page(page_index)
            matrix = fitz.Matrix(zoom, zoom)  # scale (2.0 ~= 144 DPI)
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            out_file = output_dir / f"{pdf_path.stem}_p{page_index + 1}.png"
            pix.save(out_file.as_posix())
            pages_converted += 1
    return pages_converted


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    out_dir = base_dir / "png"
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(base_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"[INFO] No PDFs found in {base_dir}")
        return 0

    total_pages = 0
    for pdf in pdf_files:
        try:
            print(f"[INFO] Converting: {pdf.name}")
            pages = convert_pdf_to_png(pdf, out_dir, zoom=2.0)
            print(f"[OK]   {pdf.name} -> {pages} page(s) saved to ./png")
            total_pages += pages
        except Exception as e:  # pragma: no cover
            print(f"[FAIL] {pdf.name}: {e}", file=sys.stderr)

    print(f"[DONE] Converted {len(pdf_files)} PDF(s), {total_pages} page(s) total.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
