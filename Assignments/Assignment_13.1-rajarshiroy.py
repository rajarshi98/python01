import urllib
from BeautifulSoup import *

url=raw_input("Enter - ")
html=urllib.urlopen(url).read()
bsoup=BeautifulSoup(html)


numlist = bsoup('span')
nl = []

for i in numlist:
	nl.append(int(i.text))


print sum(nl)