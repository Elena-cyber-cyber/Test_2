class Dog:
    species = "Canis familiaris"
    info = "This is a dog class"
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Метод экземпляра класса   
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
mex = Dog("Mexx", 5)
print(mex)

