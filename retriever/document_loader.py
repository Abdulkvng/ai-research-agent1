
import fitz  # PyMuPDF

def load_pdf_text(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)
