hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
pay = h * r
if pay <= 40 :
    print(pay)
elif pay > 40 :
    print(1.5 * r * (h - 40) + pay)
