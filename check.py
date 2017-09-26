import urllib2
from bs4 import BeautifulSoup

name = "Lost"

url="http://www.imdb.com/"

r = urllib2.urlopen(url)
info = r.read()
print type(info)
print info