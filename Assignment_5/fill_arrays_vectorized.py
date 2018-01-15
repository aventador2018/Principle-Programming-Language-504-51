import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

def h(x):
    return (1/np.sqrt(2*np.pi))*np.exp(-0.5*x**2)

x = np.linspace(-4, 4, 41)
y = h(x)

plot(x, y)
xlabel('x')
ylabel('y')
show()