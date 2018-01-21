import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

infile = open('xy.dat', 'r')
x = []
y = []

for line in infile:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))

infile.close()

xarray = np.array(x)
yarray = np.array(y)

plot(xarray, yarray)
xlabel('x')
ylabel('y')
show()