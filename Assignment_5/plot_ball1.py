import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

v0 = 10
g = 9.81

def y(t):
    return v0*t-0.5*g*t**2

t = np.linspace(0, 2*v0/g, 21)
y = y(t)

plot(t, y)
xlabel('time (s)')
ylabel('height (m)')
show()