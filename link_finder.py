import os
from html.parser import HTMLParser
from urllib import parse
from general import *

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called
    def handle_starttag(self, tag, attrs):
        # Search other link
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        # Gather all heading tag for SEO purposes
        if tag == 'h1' or tag == 'h2'or tag == 'h3':
            for (attribute, value) in attrs:
                data = '' + tag + ' ||| ' + value
                if attribute == 'title':
                    if not os.path.exists('heading.txt'):
                        write_file('heading.txt', data)
                    else:
                        append_to_file('heading.txt', data)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
