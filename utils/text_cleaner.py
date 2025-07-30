
import re

def clean_text(text: str) -> str:
    """
    Cleans raw text by removing extra whitespace, non-printable characters,
    and excessive newlines.
    """
    # Remove extra spaces and newlines
    text = re.sub(r'\s+', ' ', text)

    # Remove non-printable characters
    text = ''.join(c for c in text if c.isprintable())

    return text.strip()
