import numpy as np

class Integrate1D(object):

    def __init__(self, function=None):

        """
        Assumes that function is a function of a single variable
        """
        self._function = function   


    def rectangle_integrate(self, a=None, b=None, n=None):        

       
        """
        Numerically integrates self._function from a to b, using n
        rectangles.  We assume that the function is continuous within
        this interval.
        """

        sum_of_rectangles = 0.0
        h = float( (b-a) / n )

        x = a
        while x < b:

            sum_of_rectangles += self._function(x) * h

            x += h 

        return sum_of_rectangles

if __name__ == "__main__":


    # Simple test of the class

    A = 0.0
    B = np.pi
    N = 1.0E3

    def test_f1(x):
        return x*x

    my_intclass = Integrate1D(function=test_f1)

    result = my_intclass.rectangle_integrate(a=A, b=B, n=N)
    print('result: ' + str(result))
