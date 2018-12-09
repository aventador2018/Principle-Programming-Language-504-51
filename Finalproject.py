import numpy as np

A = np.zeros((2, 2))
B = np.zeros((2, 1))

#Assign coeffiencts
A[0,0] = -1
A[0, 1] = 0.4
A[1, 0] = 0.6
A[1, 1] = -0.9
B[0] = -0.6
B[1] = -0.2

#Calculate inverse and then perform dot product
inv = np.linalg.inv(A)
print(np.dot(np.linalg.inv(A),B))

# Directly solve for pc and pe
solve = np.linalg.solve(A, B)
print(solve)