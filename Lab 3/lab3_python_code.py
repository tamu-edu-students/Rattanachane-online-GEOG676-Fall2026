
# create class
class Shape():
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * self.radius * self.radius
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area(self):
        return 0.5 * self.base * self.height

# read txt file
def open(r'C:\Rattanachane-online-GEOG676-Fall2026\Lab3\shape.txt')
lines = file.readlines()
file.close()

for line in lines:
    linesplit(',')
    shape = components[0]

    if shape == 'Rectangle':
        rect = Rectangle(components[1], components[2])
        print('Area of Rectangle:', rect.getArea())
    elif shape == 'Circle':
        circ = Circle(components[1])
        print('Area of Circle:', circ.getArea())
    elif shape == 'Triangle':
        tri = Triangle(components[1], components[2])
        print('Area of Triangle:', tri.getArea())
    else:
        pass