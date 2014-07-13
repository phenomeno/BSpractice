import urllib2

html = urllib2.urlopen('http://collections.lacma.org/node/233751').read()


from bs4 import BeautifulSoup
soup = BeautifulSoup(html)



#grab img
x = soup.select('div#content > div > div > div > div > img')	
x1 = x[0]
img = x1['src']
"""

#grab title
y = soup.select('div#content > h1')
y1= y[0]
title = y1.string


#grab artist name
z = soup.select('div#content > div > div > div > h2 > div > a')
z1 = z[0]
artist = z1.string

#grab date
a = soup.select('div#content > div > div.group-right')
date = a[0].contents[25]
datelist = str(date) 
datelist = datelist.split(',',1)

location = datelist[0]
date = datelist[1]




#find almanac data
inddate = date.split('-',1)
firstdate = inddate[0]
seconddate = inddate[1]

html2 = urllib2.urlopen('http://www.memoirstream.com/rhmorris/memoirs/memoirs'+firstdate+'.html')

soup2 = BeautifulSoup(html2)

#grab world data
"""

# 1. open the file w/ write mode (img.html)

f = open('img.html', 'w')


# 2. put "<img src=blah blah />" in to the file
f.write('<img src="' + img +'"/>')
f.write('<p>'+ title +'</p>')
f.write ('<p>' + artist + '</p>')
f.write('<p>' + location +'</p>')
f.write('<p>'+ date +'</p>')


# 3. close the file

f.close



