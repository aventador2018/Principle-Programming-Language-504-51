class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def convert2Vec2D(self, other):
        if isinstance(other, (list, tuple)):
            return Vec2D(other[0], other[1])
        else:
            return other

    def __add__(self, other):
        other = self.convert2Vec2D(other)
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        other = self.convert2Vec2D(other)
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        other = self.convert2Vec2D(other)
        return self.x*other.x + self.y*other.y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __eq__(self, other):
        other = self.convert2Vec2D(other)
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __ne__(self, other):
        other = self.convert2Vec2D(other)
        return not self.__eq__(other) # reuse __eq__

u = Vec2D(-2, 4)
v = u + (1,1.5)

print v