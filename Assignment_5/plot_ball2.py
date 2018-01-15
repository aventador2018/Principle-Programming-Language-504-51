import sys
import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

user_input = raw_input("Please enter v0s: ")
v0s = np.array([int(i) for i in user_input.split(' ')])
g = 9.81

for v0 in v0s:
    def y(t):
        return v0 * t - 0.5 * g * t ** 2

    t = np.linspace(0, 2*v0/g, 21)
    y = y(t)

    plot(t, y)
    xlabel('time (s)')
    ylabel('height (m)')
show()