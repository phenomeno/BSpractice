# 1. find website links
# 2. get photo url

import urllib2

html = urllib2.urlopen('http://cp-studio.tistory.com/544').read()


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)




imgs = soup.findAll('span', {'class':"imageblock"})

u = []

for img in imgs:
	y=img.findAll(["img"])
	z=y[0]
	u.append(z['src'])
	

f = open('imggrab.html', 'w')


for link in u:
	f.write('<img src="' + link + '"/>')
	
