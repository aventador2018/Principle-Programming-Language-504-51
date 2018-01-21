import sys
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]
infile = open(filename, 'r')

x = []
y = []

for line in infile:
    if line[0] != '#' and line[0] != '\n':
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
infile.close()

xarray = np.array(x)
yarray = np.array(y)

plt.plot(xarray, yarray, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.show()