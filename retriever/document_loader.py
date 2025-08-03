from retriever.pdf_loader import extract_text_from_pdf_url, extract_text_from_pdf_path
from retriever.web_scraper import scrape_article
import os



def load_document(input_type: str, path_or_url: str) -> str:
    if input_type == "web":
        return scrape_article(path_or_url)

    if input_type == "pdf":
        if path_or_url.startswith("http"):
            print(f"🔗 Downloading remote PDF: {path_or_url}")
            return extract_text_from_pdf_url(path_or_url)
        elif os.path.exists(path_or_url):
            print(f"📄 Loading local PDF: {path_or_url}")
            return extract_text_from_pdf_path(path_or_url)
        else:
            print(f"❌ Path does not exist: {path_or_url}")
            raise FileNotFoundError("PDF path is invalid or URL is unreachable.")

    raise ValueError("Invalid input type. Must be 'web' or 'pdf'.")

