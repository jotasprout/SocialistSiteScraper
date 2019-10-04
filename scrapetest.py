from urllib.request import urlopen
from urllib.error import HTTPError # Page is not found
from urllib.error import URLError # Server is not found

from bs4 import BeautifulSoup

# Function to seek title and provide error checking
def getTitle(url):
    try:
        html = urlopen(url)
        #html = urlopen('http://pythonscraping.com/pages/page1.html')
        #html = urlopen('https://thisfaqewihwg.com')
    except HTTPError as e:
        print(e)
        return None # Return null, break, or some other 'Plan B'
    except URLError as e:
        print('The server could not be found, dude.')
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        #return None
        print('Tag was not found.')
    return title

# Use getTitle and commands for each possible outcome

title = getTitle('https://roxorsoxor.com/prezplaypro/index.html')

if title == None:
    print('Title could not be found. Or, at least, there is no H1 tag in the body')
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