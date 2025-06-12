largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
        
    try:
        num_1 = int(num)
    except ValueError:
        print("Invalid input")
        continue
        
if largest is  None or num_1 > largest:
    largest = num_1
    
if smallest is None or num_1 < smallest:
    smallest = num_1
    
print("Maximum is ", largest)
print("Minimum is ", smallest)
