from bs4 import BeautifulSoup

def get_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser").get_text()
    return sanitize_html_text(soup)

def sanitize_html_text(text):
    output = ''

    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    
    return _remove_extra_whitespace(output)

def _remove_extra_whitespace(text):
    cleaned_text = ' '.join(word for word in text.split() if word)
    return cleaned_text