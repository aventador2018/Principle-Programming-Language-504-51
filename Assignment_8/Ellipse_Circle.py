class Eclipse:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return pi*self.a*self.b

    def circumference(self):
        return 2*pi*self.b + 4*(self.a - self.b)

class Circle(Eclipse):
    def __init__(self, R):
        self.a = R
        self.b = R

from math import *

circle = Circle(3)
print circle.area()
print circle.circumference()