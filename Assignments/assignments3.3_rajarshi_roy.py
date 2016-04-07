s = raw_input("Enter Score: ")
score = float(s)
if score > 1.0 :
        print "value out of range"
elif 1.0 >= score >= 0.9:
        print "A"
elif .9 > score >=.8:
        print "B"
elif .8 > score >=.7:
        print "D"    
elif .7 > score >=.6:
        print "D"
else:
    print "Error"