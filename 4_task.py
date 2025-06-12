def computepay (x, y) :
    return x * y
hrs = input("Enter Hours:")
rate = input("Enter rate:")
h = float(hrs)
r = float(rate)
pay = computepay(h,r)
if h <= 40 :
    print("Pay", pay)
elif h > 40 :
    print("Pay", 0.5 * r * (h - 40) + pay)
