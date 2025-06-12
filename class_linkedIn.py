import random
class Dog:
    info = "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking voice."
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I am avive!")
        self.lucky_number = random.randint(1,10)
    def bark(self):
        return (f"Wolf! My name is {self.name} and I am {self.age} years old. My lucky number is {self.lucky_number}")    
dog1 = Dog("Fido",4)
print(dog1.lucky_number)
dog2 = Dog("Buddy",6)
print(dog1.lucky_number)
print(dog1.name)
print(dog2.name)
print(dog1.bark())
print(dog2.bark())
class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side ** 2
square1 = Square(5)
print(square1.area())            


