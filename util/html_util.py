from bs4 import BeautifulSoup

# Remove HTML tags using BeautifulSoup
def get_text_from_html(html):
    return BeautifulSoup(html, "html.parser").get_text()