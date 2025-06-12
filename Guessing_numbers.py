import random
import time
print('Привет! Добро пожаловать в игру угадай число! Я загадаю число между 1 и 100!')
time.sleep(3) 
print('Я загадываю число... ')
time.sleep(2)      
guess = int(input('Скажи число: '))
correct_number = random.randint(1,100)
guess_count = 1
while guess != correct_number:
    time.sleep(2)      
    guess_count += 1
    if guess > correct_number:
        guess =int(input('Неправильно. Загадай меньшее число: '))
    else:
        guess =int(input('Неправильно. Загадай большее число: '))       
print('Ты угадал!')
print(f"Количество попыток: {guess_count}")
                     
                     
                  
