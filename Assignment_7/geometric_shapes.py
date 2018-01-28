class Rectangle:
    def __init__(self, W, H, x0, y0):
        self.W = W
        self.H = H
        self.x0 = x0
        self.y0 = y0

    def area(self):
        return self.W*self.H

    def circumference(self):
        return self.W*2+self.H*2


class Triangle:
    def __init__(self, x0, y0, x1, y1, x2, y2):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def area(self):
        return 0.5*abs(self.x1*self.y2 - self.x2*self.y1 - self.x0*self.y2 + self.x2*self.y0 + self.x0*self.y0 - self.x1*self.y0)

    def circumference(self):
        return sqrt((self.x0-self.x1)**2+(self.y0-self.y1)**2) + sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2) + sqrt((self.x0-self.x2)**2+(self.y0-self.y2)**2)

from math import *
rectangle = Rectangle(2, 3, 0, 0)
print 'Lower left corner: ', rectangle.x0, ',', rectangle.y0
print 'Area: ', rectangle.area()
print 'Circumference: ', rectangle.circumference()

triangle = Triangle(0, 0, 2, 2, 4, 0)
print 'Area: ', triangle.area()
print 'Circumference: ', triangle.circumference()