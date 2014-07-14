

import urllib2

from bs4 import BeautifulSoup

try:
	html = urllib2.urlopen('http://cp-studio.tistory.com/127').read()
except urllib2.HTTPError, e:
	pass
except urllib2.URLError, e:
	pass
finally:
	print 1


#soup = BeautifulSoup(html)
