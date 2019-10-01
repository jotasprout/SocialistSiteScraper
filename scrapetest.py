from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
        #html = urlopen('http://pythonscraping.com/pages/page1.html')
        #html = urlopen('https://thisfaqewihwg.com')
    except HTTPError as e:
        #print(e)
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle('http://pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')
else:
    print(title)
    
#except URLError as e:
#    print('The server could not be found!')
#else:
    #   print('It worked!')
#
#bs = BeautifulSoup(html.read(), 'lxml')
#print(html.read())
#print(bs.h1)