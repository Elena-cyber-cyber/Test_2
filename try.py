smallest = 0
largest = 0
num = input('Enter a number:')
try:
  const = (int(num))
except:
  print("An exception occurred, please, enter a number")
if const > largest:
    const = largest
if const < smallest:
    const = smallest
print(smallest, largest)    
    
