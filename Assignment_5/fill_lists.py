import math
from matplotlib.pyplot import plot, show, xlabel, ylabel

def h(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*x**2)

i = -4
xlist = []
while i <= 4:
    xlist.append(i)
    i = i + 0.25
hlist = [h(x) for x in xlist]

plot(xlist, hlist)
xlabel('x')
ylabel('h')
show()