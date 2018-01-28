class Line:
    def __init__(self, p1, p2):
        if isinstance(p1, (tuple, list)) and isinstance(p2, (float, int)):
            # p1 is a point and p2 is slope
            self.a = p2
            self.b = p1[1] - p2 * p1[0]
        elif isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
            self.a = (p2[1] - p1[1])/float(p2[0] - p1[0])
            self.b = p1[1] - self.a * p1[0]
        elif isinstance(p1, (float, int)) and isinstance(p2, (float, int)):
            self.a = p1
            self.b = p2

    def value(self, x):
        return self.a*x + self.b

line = Line((0,0), (3,5))
print line.value(0.5)

line1 = Line((1,1), 1)
print line1.value(0.5)

line2 = Line(1, 2)
print line2.value(0.5)