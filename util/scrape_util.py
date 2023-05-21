from bs4 import BeautifulSoup
from . import html_util as html_util
import requests

# Remove HTML tags using BeautifulSoup
def scrape_article(url):
    soup = _get_soup(url)
    text = _get_text(soup)

    return html_util.sanitize_html_text(text)

def _get_soup(url):
    res = requests.get(url)
    html_page = res.content

    return BeautifulSoup(html_page, 'html.parser')

def _get_text(soup):
    return soup.find_all(text=True)
