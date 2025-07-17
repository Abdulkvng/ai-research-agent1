#libraries

import requests
import bs4 import BeautifulSoup

#function to scrape website


def scrape_article(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    return "\n".join([p.text for p in paragraphs])

	
