fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1  # Отступ внутри цикла
print('Line Count: ', count)  # Без отступа — это за пределами цикла
