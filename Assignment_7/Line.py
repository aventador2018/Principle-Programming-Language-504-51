class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def value(self, x):
        x0, y0 = self.p1
        x1, y1 = self.p2
        a = (y1 - y0) / float(x1 - x0)
        b = y0 - a * x0
        return a*x + b

line = Line((0,0), (3,5))
print line.value(0.2)