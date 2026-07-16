import math

class shape:
    def area (self):
        pass

class Circle(shape):
    def __init__ (self,radius):
        self.radius = radius

    def area (self):
        return math.pi * self.radius **2

class Square(shape):
    def __init__ (self,side):
        self.side = side

    def area (self):
        return self.side * self.side

class Triangle(shape):
    def __init__ (self,base,height):
        self.base = base
        self.height = height

    def area (self):
        return 0.5 * self.base * self.height

circle = Circle(7)
square = Square(4)
triangle = Triangle(6,8)

print(f"Circle area: {circle.area()}")
print(f"Square area: {square.area()}")
print(f"Triangle area: {triangle.area()}")