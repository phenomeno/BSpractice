#-*- coding: utf-8 -*-


# 1. find website links
# 2. get photo url

import urllib2

html = urllib2.urlopen('http://cp-studio.tistory.com/544').read()


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)

#3. grab the blog title

title = soup.select('div.titleWrap > h2 > a')
title= title[0]
title1= title.string
title1 = title1.encode('utf-8')

#4. grab images 
imgs = soup.findAll('span', {'class':"imageblock"})

u = []

for img in imgs:
	y=img.findAll(["img"])
	z=y[0]
	u.append(z['src'])
	
	
#5. add title	

f = open('imggrab.html', 'w')
f.write('<p>' + title1 + '</p>')



#6. add images
for link in u:
	f.write('<b><img src="' + link + '"/></b>')
	
f.close
