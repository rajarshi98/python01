name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
import re
handle = open(name)
for line in handle:
	line = line.rstrip()
	if re.search('^From:', line) :
		print name 

		
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hold=dict()
for line in handle :
	fline = line.split()
    hh=fline[5]
    hrlst=wh.split(:)
	hr=hrlist[0]
    hold(hr)=hold.get(hr,0)+1
	for line in name ('^From:', line) :
		
        t=hold.items()
		t.sort()
	for k, v in t:
	print k,v

