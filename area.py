import math
class Circle:
    def __init__ (self,radius):
        self.radius = radius

    def area (self):
        return math.pi * self.radius **2

class Square:
    def __init__ (self,side):
        self.side = side

    def area (self):
        return self.side * self.side

class Triangle:
    def __init__ (self,base,height):
        self.base = base
        self.height = height

    def area (self):
        return 0.5 * self.base * self.height

Circle = Circle(7)
Square = Square(4)
Triangle = Triangle(6,8)

print(f"Circle area: {Circle.area()}")
print(f"Square area: {Square.area()}")
print(f"Triangle area: {Triangle.area()}")