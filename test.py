
#should be a wbsite
html = open('./test.html', 'r').read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)


print soup.title.string

print soup.a.string


print soup.a['href']

print soup.find_all('a')


for x in soup.find_all('a'):
	print x.string
	
	
print soup.find_all(


print a[0].contents[25]
#this grabs an item out of a list if a[0] is presented as a dirty list