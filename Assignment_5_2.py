import numpy as np

# Domain parameters
L = 1.0 # Length of domain
NPOINTS = 5 # Number of points for discretisation
DT = 0.1 # delta_t timestep size
TN = 10.0 # t_n last time
h = float(L/(NPOINTS-1))
# Physical parameters
k = 1.0 # Conductivity
c = 2.0 # Heat capacity
rho = 5.0 # Density

r = (k*DT)/(c*rho*h*h)
# Assume all points start off with this value at time t=0
initial_value = 0.0
# Boundary conditions
left_bc = 0.0
right_bc = 100.0

A = np.zeros((NPOINTS, NPOINTS))
B = np.zeros((NPOINTS,1))
A[0, 0] = 1
A[NPOINTS - 1, NPOINTS - 1] = 1

#initiate the values for the matrix and the RHS
i = 1
while i < len(A) - 1:
    A[i, i-1] = r
    A[i, i] = -(2*r+1)
    A[i, i + 1] = r
    i = i + 1
B[0, 0] = left_bc
B[-1, -1] = right_bc

#print A, invA and RHS
invA = np.linalg.inv(A)
print(A)
print(invA)
print(B)

# start iterating
j = 0
while j < TN:
    k = 1
    u = np.dot(invA, B)
    while k < len(B) - 1:
        B[k] = -u[k]
        k = k + 1
    j = j + DT

print(u)