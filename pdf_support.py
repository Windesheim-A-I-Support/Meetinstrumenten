import fitz  # PyMuPDF
import logging
from pathlib import Path

log = logging.getLogger(__name__)

def extract_pdf_text(pdf_path: Path) -> str:
    """Extract full text from a PDF file."""
    doc = fitz.open(pdf_path)
    text_pages = []
    for page in doc:
        txt = page.get_text("text")
        text_pages.append(txt)
    return "\n\n".join(text_pages)

def find_pdf_files(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.pdf"))

def main():
    # ... existing Excel loading code ...

    # 1️⃣ Detect PDF files
    pdfs = find_pdf_files(DOCUMENTS_DIR)
    log.info("Found %d PDF(s) for text extraction", len(pdfs))

    pdf_texts = {}
    for pdf in pdfs:
        try:
            log.info("Reading PDF: %s", pdf.name)
            text = extract_pdf_text(pdf)
            pdf_texts[pdf.name] = text
        except Exception as e:
            log.error("Failed to extract %s: %s", pdf.name, e)

    # 2️⃣ Example: Save each as .txt for later NLP
    (OUTPUT_DIR / "pdf_texts").mkdir(exist_ok=True)
    for name, text in pdf_texts.items():
        fn = OUTPUT_DIR / "pdf_texts" / (Path(name).stem + ".txt")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(text)
        log.info("✔ Saved extracted text to %s", fn)

    # pdf_texts now available for clustering & analysis
