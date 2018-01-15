import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

def h(x):
    return (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2)

n = 41
dx = 8. / (n - 1)

x = [-4 + i * dx for i in range(n)]
y = [h(i) for i in x]

plot(x, y)
xlabel('x')
ylabel('y')
show()