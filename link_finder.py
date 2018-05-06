from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    
    # Constructor
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # Handle starting tag in HTML Parser
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    # Getter for links
    def page_links(self):
        return self.links

    # Error exception
    def error(self, message):
        pass
