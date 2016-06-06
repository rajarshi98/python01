fname = raw_input("Enter file name: ")
fh = open(fname)
els = list()
word_els = list()


for line in fh:

	els=line.split()
	
	for word in els:
		word = word.lower()
		if word not in word_els:
			word_els.append(word)

print sorted(word_els)