while True:
    scr = input("Enter a score: ")
    try:
        s = float(scr)  # Пробуем преобразовать ввод в число
        if 0.0 <= s <= 10.0:  # Проверяем, находится ли число в диапазоне
            break  # Если всё хорошо, выходим из цикла
        else:
            print("Enter a score in the range 0.0 to 10.0!")
    except ValueError:
        print("Enter a digit, please!")
def computergrade(x):    
    if x>=0.9:
        print('A')
    elif  x>=0.8:
        print('B')
    elif  x>=0.7:
        print('C')    
    elif  x>=0.6:
        print('D')
    elif  x<0.6:
        print('F')
    print("Thank you for attending the class!")
computergrade(s)    

