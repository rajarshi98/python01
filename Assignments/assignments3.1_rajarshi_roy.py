hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter PayRate: ")
r = float(rate)
grosspay = h * r
if h <= 40 :
    print grosspay
else:
     grosspay = r * 40 + (r * 1.5 * (h - 40))

     print grosspay