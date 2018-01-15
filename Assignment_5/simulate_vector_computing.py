import math
import numpy as np

x = [0, 2]
t = [1, 1.5]

a = np.array(x)
b = np.array(t)

result = []

def u(x):
    return math.sin(x)

def v(x):
    return math.cos(x)

def w(x):
    return math.exp(1/x)

def z(x, y):
    return x + y

for i in range(len(x)):
    x[i] = u(x[i])

for i in range(len(x)):
    x[i] = v(x[i])

for i in range(len(t)):
    t[i] = w(t[i])

for i in range(2):
    result.append(z(x[i], t[i]))

print result

def toVerify(a, b):
    return np.cos(np.sin(a)) + np.exp(1/b)

print toVerify(a, b)