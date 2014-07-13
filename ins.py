import urllib2

html = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_United_States_insurance_companies').read()


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)




for x in soup.select('div#mw-content-text > ul > li > a'):
	
	print x['title']
	
	a = 'http://en.wikipedia.org' + x['href']
	
	html2 = urllib2.urlopen(a).read()
	
	soup2 = BeautifulSoup(html2)
	
	
	x = soup2.select('#mw-content-text > ul > li > a')
	
	
	co = x[0]
	
	print co['href']
	
	
	

