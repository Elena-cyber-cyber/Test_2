far = input("Enter a number: ")
try:
    mar = int(far)
    celsium = (mar -32) * 5/9.0
    print(celsium)
except:
    print("Enter a valid number: ")
    
