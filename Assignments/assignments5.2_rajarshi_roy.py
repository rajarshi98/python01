import urllib
import json

url=raw_input("Enter Url: ")
urlo=urllib.urlopen(url)
read=urlo.read()
load=json.loads(str(read))

counts=[]
colls=load["comments"]

for coll in colls:
	counts.append(coll["count"])

print sum(counts)