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
	
"""
x = imgs[0]
y = x.findAll(["img"])
z= y[0]
print z['src']



for img in imgs:
	print img.a['href'].split("imgurl=")[1]

for x in soup.select('div#mw-content-text > ul > li > a'):
	
	print x['title']
	
	a = 'http://en.wikipedia.org' + x['href']
	
	html2 = urllib2.urlopen(a).read()
	
	soup2 = BeautifulSoup(html2)
	
	
	x = soup2.select('#mw-content-text > ul > li > a')
	
	
	co = x[0]
	
	print co['href']
	
"""
	
# 3. display photo url
# 4. add titles
	
	

