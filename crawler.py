from bs4 import BeautifulSoup
import urllib2 
import requests
import pyspeedtest
import sys
import os
import errno
import requests
import commands

url = "http://tvshows4mobile.com/"
show = ""
show_name = "Narcos"
season = "Season 02"
episode_no = 1

def get_soup_object(url):
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	content = urllib2.urlopen(req)
	soup = BeautifulSoup(content, 'html.parser')
	return soup


def download_episode(episode_link,episode_no):
	file_name = show_name+" "+season+"-"+str(episode_no)
	if not os.path.exists(file_name):
		req = urllib2.Request(episode_link, headers={'User-Agent' : "Magic Browser"}) 
		rsp = urllib2.urlopen(req)
		meta = rsp.info()
		total_length = float(meta.getheaders("Content-Length")[0])
		file_size_MB = total_length/(1000**2)
		print "File size: {:0.2f} MB".format(file_size_MB)
		download_speed = float(commands.getstatusoutput("pyspeedtest | grep Download | cut -d ' ' -f 3")[1])
		print "Download speed(MBps): ",download_speed/8
		print "Downloading %s"%file_name
		with open(file_name,'wb') as f:
			dl = 0
			total_length = int(total_length)
			response = requests.get(episode_link, stream=True)
			total_length = response.headers.get('content-length')
			dl = 0
			total_length = int(total_length)
			for data in response.iter_content(chunk_size=512):
				dl += len(data)
				f.write(data)
				done = int(50 * dl / total_length)
				sys.stdout.write("\r[%s%s] %s%% completed" % ('=' * done, ' ' * (50-done), done*2))    
				sys.stdout.flush()
	else:
		print "{0} already exists downloading next episode.".format(file_name)

	
soup = get_soup_object(url)

#Passes first page of website.
for div in soup.find_all("div", class_="series_set"):
	a = div.find_all('a')
	x = a[0].get('href')
	if x[len(x)-1]=='m':
		show = x
		print show

#Chooses show form list
soup = get_soup_object(show)
z = ''
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==show_name):
		show = a[0]['href']
		print show

#opens shows link
soup = get_soup_object(show)
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==season):
		show = a[0]['href']
		print show

#collects all
soup = get_soup_object(show)
all_episodes_link = ''

#go to next page if there
for div in soup.find_all("div", class_="pagination"):
	show+=" "
	a = div.find_all('a')
	show +=  str(a[0].get('href'))

total_show_pages = show.split()

#collects download link from all the pages
for show_page in total_show_pages:
	soup = get_soup_object(show_page)
	for div in soup.find_all("div", class_="data"):
		a = div.find_all('a')
		all_episodes_link += str(a[0].get('href')) + " "
	
for episodes in all_episodes_link.split():
	soup = get_soup_object(episodes)
	
	for div in soup.find_all("div", class_="data"):
		a = div.find_all('a')
		if a[0].string[len(a[0].string)-1]=='4' :
			episode_link =  a[0]['href']
			download_episode(episode_link,episode_no)
			episode_no+=1

print "All Downloads completed!! Enjoy!!"			
