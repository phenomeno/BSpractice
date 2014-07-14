#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

l = []

def link(x):	#generates links based on ending number
	
	a = "http://cp-studio.tistory.com/" + str(x)
	l.append(a)
	

u = []
def img(x):		#pulls pictures
	
	try:
		html = urllib2.urlopen(x).read()
	except urllib2.HTTPError, e:
		pass
	except urllib2.URLError, e:
		pass
	finally:
		return ''
	
	soup = BeautifulSoup(html)
	imgs = soup.findAll('span', {'class':"imageblock"})
	for img in imgs:
		y = img.findAll(["img"])	#since it's a tag we have the extra brackets
		z = y[0]
	u.append(z['src'])
	
	
t = []
def title(x):	#grabs title

	try:
		html = urllib2.urlopen(x).read()
	except urllib2.HTTPError, e:
		pass
	except urllib2.URLError, e:
		pass
	finally:
		return ''
	
	soup = BeautifulSoup(html)
	
	title = soup.select('div.titleWrap > h2 > a')
	title = title[0]
	title1 = title.string
	t.append(title1)
	
	
	
def add(x,z):	# add to blog title to website
	y = x.encode('utf-8')
	f = open('/Users/Lee/test/BSpractice/imggrab.html', 'w')
	f.write('<meta charset=\"utf-8\">')
	f.write('<p>' + y + '</p>')
	
	for w in z:
		f.write('<img src="' + w + '"/>')
	f.close
	


#testing
"""
for x in range(124,125):
	link(x)
	l = l[0]
	img(l)
	title(l)
	t = t[0]
	print t
	title_add(t)
	img_add(u)
	l = []
	u = []
	t = []
	

"""
for x in range(122,123):
	link(x)
	l=l[0]
	img(l)
	if len(u)==0:
		print '1'
	title(l)
	if len(t)==0:
		print '2'
	else:
		t=t[0]
		add(t, u)
	l = []
	u = []
	t = []
	
	
	
"""	
link(128)
l = l[0]
print l
html = urllib2.urlopen(l).read()
soup = BeautifulSoup(html)
soup.findAll("div")
	
	
"""
