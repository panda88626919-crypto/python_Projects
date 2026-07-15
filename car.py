class car:

    def __init__ (self,color,milesge):
        self.color = color
        self.mileage = milesge

    def __str__ (self):
        return (f"The {self.color} is {self.mileage} miles")

blue = car("blue",20000)
red = car("red",30000)

print(blue)
print(blue)