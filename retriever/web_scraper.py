from bs4 import BeautifulSoup
import requests

def scrape_article(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (AI Research Agent)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return ""

    soup = BeautifulSoup(response.content, 'html.parser')

    # Optional: Remove scripts, styles, navs
    for tag in soup(["script", "style", "nav", "footer", "aside"]):
        tag.decompose()

    # Get text from <p> tags only
    paragraphs = soup.find_all('p')
    clean_text = "\n".join(p.get_text(strip=True) for p in paragraphs)

    return clean_text.strip()
