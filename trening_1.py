while True:
    hrs = input("Enter Hours:")
    try:
        h = float(hrs)
        break
    except ValueError:
        print("Enter a number, please!")
    
while True:
    rate = input("Enter rate:")
    try:
        r = float(rate)
        break
    except ValueError:
        print("Enter a number, please!") 
   
pay = h * r
if pay <= 40 :
    print("Pay: ", pay)
elif pay > 40 :
    print("Pay:", 0.5 * r * (h - 40) + pay)
  


