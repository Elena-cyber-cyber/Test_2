class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def __str__(self):
        return f"{self.name} is {self.age} years old and {self.name}'s color is {self.coat_color}"
    def speak(self,sound):
        return f"{self.name} barks: {sound}"
class JackRusselTerrier(Dog):
    def speak(self,sound="Arf"):
        return super().speak(sound)
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass
miles =JackRusselTerrier("Miles",4,"brown")
jim = Bulldog("Jim", 5, "yellow")
print(miles)
print(miles.speak("Wow"))


 
