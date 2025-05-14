from abs import Shape, SolidShape
from managers import FigureManager
from math import sqrt

fm = FigureManager()

@fm.add_figure('circle')
class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius**2
    def perimetr(self): return 2 * 3.14 * self.radius

@fm.add_figure('triangle')
class Triangle(Shape):
    def __init__(self, side): self.side = side
    def area(self): return (sqrt(3) / 4) * self.side**2
    def perimetr(self): return self.side * 3

@fm.add_figure('square')
class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self): return self.width * self.height
    def perimetr(self): return 2 * (self.width + self.height)

@fm.add_figure('cube')
class Cube(SolidShape):
    def __init__(self, side): self.side = side
    def area(self): return 6 * self.side**2
    def perimetr(self): return 12 * self.side
    def volume(self): return self.side**3
