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
        print('\nList of url in popular page ' + str(page) + ':\n')

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")

        listlink = []
        purelink = [] # List that contain no duplicate

        for link in soup.findAll('a',{'target' : '_blank'}):
            href = link.get('href')
            # listhref to ommit a non downloaded format
            listhref = list(href)
            if(listhref[0] == '/'):
                listlink.append(str(href))

        for link in listlink:
            if link not in purelink:
                purelink.append(link) # Make unique list

        for link in purelink:
            print('http://www.yify-torrent.org' + link + '\n')
        page += 1

trade_spider(5)
