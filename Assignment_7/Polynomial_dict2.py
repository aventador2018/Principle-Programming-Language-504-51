class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        s = 0
        for i in self.coeff:
            s += self.coeff[i]*x**i
        return s

    def __add__(self, other):
        # Start with the longest list and add in the other
        result_coeff = self.coeff.copy()
        for i in other.coeff:
            if i in result_coeff:
                result_coeff[i] = result_coeff[i] + other.coeff[i]
            else:
                result_coeff[i] = other.coeff[i]
        return Polynomial(result_coeff)

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        M = len(c) - 1
        N = len(d) - 1
        result_coeff = {}
        for i in c:
            for j in d:
                result_coeff[i + j] = c[i] * d[j]
        return Polynomial(result_coeff)

polynomial = Polynomial({1:1, 100:-3})
polynomial1 = Polynomial({20:1, 1:-1, 100:4})
print polynomial.__mul__(polynomial1).__call__(2)