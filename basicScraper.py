from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from logger import log


def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        log(e) 
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        log(e)
        return None
    return title

