from bs4 import BeautifulSoup
import urllib2 
import requests
import pyspeedtest
import string
import sys
import os
import errno
import requests
import commands

def get_soup_object(url):
	try:
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		content = urllib2.urlopen(req)
		soup = BeautifulSoup(content, 'html.parser')
		return soup
	except Exception as e:
		print "No TV series found with {0} name!!!".format(show_name)
		sys.exit()

def download_episode(episode_link,episode_no):
	file_name = show_name+" "+season+"-"+str(episode_no)
	if not os.path.exists(file_name):
		req = urllib2.Request(episode_link, headers={'User-Agent' : "Magic Browser"}) 
		rsp = urllib2.urlopen(req)
		meta = rsp.info()
		total_length = float(meta.getheaders("Content-Length")[0])
		file_size_MB = total_length/(1000**2)
		print "\nFile size: {:0.2f} MB".format(file_size_MB)
		#download_speed = float(commands.getstatusoutput("pyspeedtest | grep Download | cut -d ' ' -f 3")[1])
		#print "Download speed(MBps): ",download_speed/8
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

def get_url():
	url = "http://tvshows4mobile.com/"	
	if show_name[0].lower() in ('a','b','c'):
		url+='a'
	elif show_name[0].lower() in ('d','e','f'):
		url+='d'
	elif show_name[0].lower() in ('g','h','i'):
		url+='g'
	elif show_name[0].lower() in ('j','k','l'):
		url+='j'
	elif show_name[0].lower() in ('m','n','o'):
		url+='m'
	elif show_name[0].lower() in ('p','q','r'):
		url+='p'
	elif show_name[0].lower() in ('s','t','u'):
		url+='s'
	elif show_name[0].lower() in ('v','w','x'):
		url+='v'
	else:
		url+=y
	return url	
	
show = ""
show_name = raw_input("Enter the show name: ")
show_name = string.capwords(show_name)
season = "Season "
try:
  season_no = str(input("Enter season no: "))
  if len(season_no) == 1:
    season+='0'
    season+=season_no
  else:
    season+=season_no
  episode_no = input("Enter episode to start download from: ")  
except Exception as e:
  print "ERROR!!! Enter value of int type only."
  sys.exit()


soup = get_soup_object(get_url())
#Chooses show from list
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==show_name):
		show = a[0]['href']

#opens shows link
soup = get_soup_object(show)
season_found = False
for div in soup.find_all("div", class_="data"):
	a = div.find_all('a')
	if (a[0].string==season):
		show = a[0]['href']
		season_found = True	

if not season_found :
	print "No such season found of {0}!!!".format(show_name)
	sys.exit()

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

all_episodes_link = all_episodes_link.split()
all_episodes_link.reverse()
all_episodes_link = all_episodes_link[episode_no-1:]

for episodes in all_episodes_link:
	soup = get_soup_object(episodes)
	
	for div in soup.find_all("div", class_="data"):
		a = div.find_all('a')
		if a[0].string[len(a[0].string)-1]=='4' :
			episode_link =  a[0]['href']
			download_episode(episode_link,episode_no)
			episode_no+=1

print "\nAll Downloads completed!! Enjoy!!"	
