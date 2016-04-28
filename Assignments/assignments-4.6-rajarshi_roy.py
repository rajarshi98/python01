def computepay(h,r):

	grosspay = h * r
	try :
			h = float(hrs)
			r = float(rate)
	except : 
		return "Please Enter a Number! "
	if h <= 40 :
		return "Your Paycheck " + str(grosspay)
	else :
		grosspay = r * 40 + (r * 1.5 * (h - 40))
		return "Your Paycheck plus overtime is " + str(grosspay)

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter PayRate: ")
h = float(hrs)
r = float(rate)

print computepay(h, r)