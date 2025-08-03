import fitz  # PyMuPDF
import requests
import tempfile

def extract_text_from_pdf_path(path):
    doc = fitz.open(path)
    text = "".join([page.get_text() for page in doc])
    return text

def extract_text_from_pdf_url(url):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(response.content)
        return extract_text_from_pdf_path(tmp.name)

