while True:
    line = input('>')
    if len(line) >'0' and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('I got it!')
##total = 0
##for itervar in[3,41,12,9,74,15]:
##    total = total + itervar
##print("Amount: ", total)
##largest = None
##print("Initial: ", largest)
##for itervar in [3, 41,34,56,67,7,9]:
##    if largest is None or itervar > largest:
##        largest = itervar
##    print("Loop",itervar,largest)
##print("The largest number is:", largest)
##def min(values):
##    smallest = None
##    for value in values:
##        if smallest is None or value<smallest:
##            smallest = value
##    return smallest
##my_list = [3, 41,34,56,67,7,9]
##print(min(my_list))
##count = 0
##total = 0
##largest = None
##smallest = None
##while True:
##    num = input('Tell me a number а your choice: ')
##    if num == 'done':
##       break
##    try:
##        num_1 =int(num)
##    except ValueError:
##        print("Invalid input")
##        continue
##    if largest is None or num_1 > largest:
##        largest = num_1
##    
##    if smallest is None or num_1 < smallest:
##        smallest = num_1    
##    count = count +1
##    total = total + num_1
##print(count,total,largest,smallest)   
    


