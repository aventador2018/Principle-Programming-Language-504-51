import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

def f(x, t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

t = 0
x = np.linspace(-4, 4, 41)
y = f(x, t)

plot(x, y)
show()