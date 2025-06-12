def things():
    print('Hello!')
    print('Great!')
things()
big = max('Hello world')
print(big)
print(float(99)/100)
i = 42
print(type(i))
def greet(lang):
    if lang =='es':
        return('Hola')
    elif lang == 'fr':
        return('Bonjour')
    else:
       return('Hello')
n = input('Tell me your name: ')
print(greet(n))
def addtwo(a,b):
    added = a + b
    return added
m = input('Tell me the first number: ')
g = input('Tell me the second number: ')
k = int(m)
l = int(g)
kola = addtwo(k,l)
print(f"The sum of your numbers is: {kola}")

