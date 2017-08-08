from bs4 import BeautifulSoup
import urllib2 
import requests
import pyspeedtest

url = "http://tvshows4mobile.com/"
show = ""
show_name = "Orange Is The New Black"
season = "Season 03"



def get_soup_object(url):
	content = urllib2.urlopen(url)
	soup = BeautifulSoup(content, 'html.parser')
	return soup

soup = get_soup_object(url)

#Passes first page of website.
for div in soup.find_all("div", class_="series_set"):
	a = div.find_all('a')
	x = a[0].get('href')
	if x[len(x)-1]=='m':
		show = x

#Chooses show form list
soup = get_soup_object(show)
z = ''
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==show_name):
		show = a[0]['href']

#opens shows link
soup = get_soup_object(show)
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==season):
		show = a[0]['href']

#collects all
soup = get_soup_object(show)
all_episodes_link = ''

for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	all_episodes_link += str(a[0].get('href')) + " "

#go to next page if there
for div in soup.find_all("div", class_="pagination"):
	a = div.find_all('a')
	show +=  str(a[0].get('href')) + " "

for pages in show.split():
	soup = get_soup_object(pages)

	for div in soup.find_all("div", class_="data"):
		a = div.find_all('a')
		all_episodes_link += str(a[0].get('href')) + " "
			
for episodes in x.split():
	soup = get_soup_object(episodes)
	
	for div in soup.find_all("div", class_="data"):
		a = div.find_all('a')
		if a[0].string[len(a[0].string)-1]=='4' :
			episode_link =  a[0]['href']
	print episode_link

file_name = 'trial_video.mp4' 
rsp = urllib2.urlopen(episode_link)
meta = rsp.info()
x = float(meta.getheaders("Content-Length")[0])
x/=(1000**2)
print "File size: {:0.2f} MB".format(x)


'''

with open(file_name,'wb') as f:
    f.write(rsp.read())
    rsp.close()
'''