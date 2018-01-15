import numpy as np

def f(x):
    return x**3 + x*np.exp(x) + 1

v = np.array((2, 3, -1))
first = np.zeros(3)
for x in range(3):
    first[x] = f(v[x])

print first
print f(v)