import fitz  # PyMuPDF
import requests
import tempfile
import os

def extract_text_from_pdf_path(path: str) -> str:
    """Extracts text from a local PDF file."""
    try:
        doc = fitz.open(path)
        return "\n".join(page.get_text() for page in doc)
    except Exception as e:
        print(f"❌ Failed to read PDF at {path}: {e}")
        return ""

def extract_text_from_pdf_url(url: str) -> str:
    """Downloads a remote PDF and extracts its text."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Error downloading PDF from {url}: {e}")
        return ""

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name

    try:
        text = extract_text_from_pdf_path(tmp_path)
    finally:
        os.remove(tmp_path)  # Clean up the temporary file

    return text
