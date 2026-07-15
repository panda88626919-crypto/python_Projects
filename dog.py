from os import name


class Dog :

    species = "Canis familiaris"

    def __init__ (self,name,age,sound):
        self.name = name
        self.age = age
        self.sound = sound

    def description(self):
        return f"{self.name} is {self.age} years old"

    def __str__ (self):
        return (f"{self.name} says {self.sound}")

buddy = Dog("buddy", 9,"Woof")
leo = Dog("leo", 4,"Woof")

print(leo.description())
print(buddy)
