import requests
from bs4 import BeautifulSoup

def trade_spider(max):
    page = 1
    while page <= max :
        if(page == 1) :
            url = 'http://www.yify-torrent.org/popular.html'
            print(url)
        else :
            url = 'http://www.yify-torrent.org/popular-' + str(page) + '.html'
            print(url)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a',{'target' : '_blank'}):
            href = link.get('href')
            listhref = list(href)
            if(listhref[0] == '/'):
                print('http://www.yify-torrent.org' + href)
        page += 1

trade_spider(1)
