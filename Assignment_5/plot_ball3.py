import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

user_input = raw_input("Please enter v0s: ")
v0s = np.array([int(i) for i in user_input.split(' ')])
g = 9.81

maxy = []

for v0 in v0s:
    def y(t):
        return v0 * t - 0.5 * g * t ** 2

    t = np.linspace(0, 2*v0/g, 21)
    y = y(t)

    maxy.append(max(y))

    plot(t, y)
    xlabel('time (s)')
    ylabel('height (m)')
show()

print 'The extents for different v0 are:'
for i in range(len(v0s)):
    print 'When v0 = %.1f, x is from 0 to %.1f, y is from 0 to %.2f' %(v0s[i], 2*v0s[i]/g, maxy[i])