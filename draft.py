#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

l = []

def link(x):	#generates links based on ending number
	a = "http://cp-studio.tistory.com/" + str(x)
	l.append(a)
	

def imggtr(x):		#pulls pictures and blog title
	html = urllib2.urlopen(x).read()
	soup = BeautifulSoup(html)
	
	
	## grab the images
	
	imgs = soup.findAll('span', {'class':"imageblock"})
	
	u = []
	
	for img in imgs:
		y = img.findAll(["img"])	#since it's a tag we have the extra brackets
		z = y[0]
		u.append(z['src'])
		
		if u == []:
			print 'True'
			break
			
		else:
			
		
			print 'False'
			## grab the blog title
	
			title = soup.select('div.titleWrap > h2 > a')
			title = title[0]
			title1 = title.string
			title1 = title1.encode('utf-8')
	
	
	
			## add to blog title to website
		
			f = open('/Users/Lee/test/BSpractice/imggrab.html', 'w')
			f.write('<meta charset=\"utf-8\">')
			f.write('<p>' + title1 + '</p>')
		
			## add images to website
	
			for x in u:
				f.write('<img src="' + x + '"/>')
	
				f.close
	


#testing

for x in [123]:
	link(x)

for x in l:
	imggtr(x)