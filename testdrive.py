import Integrate1D

def main():

    X0 = 1.0
    XN = 2.0
    NUM_RECT = 10

    currentResult = 100

    results = []

    print('n', '     h', '       integral', '          error')

    # Construct an instance of the Integrate1D class
    intobject = Integrate1D.Integrate1D(function=myfunction)

    # Perform integration with rectangles
    result = intobject.rectangle_integrate(a=X0, b=XN, n=NUM_RECT)
    results.append(result)

    print(str(NUM_RECT)+'     '+str(float((XN-X0)/NUM_RECT))+'     '+str(result)+'     '+str(7/3-result))

    while(True):
        NUM_RECT = NUM_RECT*10
        currentResult = intobject.rectangle_integrate(a=X0, b=XN, n=NUM_RECT)
        print(str(NUM_RECT) + '     ' + str(float((XN - X0) / NUM_RECT)) + '     ' + str(currentResult) + '     ' + str(7/3 - currentResult))
        if(abs(currentResult - results[-1]) <= 1.0E-06):
            break
        else:
            results.append(currentResult)


def myfunction(x):

    return x*x


if __name__=="__main__":

    main()
