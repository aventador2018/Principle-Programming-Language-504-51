import numpy as np

#Establish the constant variables
Qa = 0 #200
ca = 0 #2
Wsmoker = 1000
Wgrill = 2000
Qd = 100
Qb = 0 #50
cb = 0 #2
Qc = 150
E13 = 25
E34 = 50
E24 = 25

#Equations
# 0 = Wsmoker + Qa*ca - Qa*c1 + E13(c3 - c1) => (-Qa-E13)*c1 + 0*c2 - E13*c3 + 0*c4 = -Wsmoker - Qa*ca
# 0 = Qb*cb + (Qa - Qd)*c4 - Qc*c2 + E24(c4 - c2) => 0*c1 - (Qc + E24)*c2 + 0*c3 + (Qa-Qd+E24)*c4 = -Qb*cb
# 0 = Wgrill + Qa*c1 + E13*(c1 - c3) + E34*(c4 - c3) - Qa*c3 => (Qa+E13)*c1 + 0*c2 - (E13+E34+Qa)*c3 + E34*c4 = -Wgrill
# 0 = Qa*c3 - Qa*c4 + E34*(c3 - c4) + E24*(c2 - c4) => 0*c1 + E24*c2 + (E34+Qa)*c3 - (Qa+E34+E24)*c4 = 0

A = np.zeros((4, 4))
B = np.zeros((4, 1))
print(A)
print(B)

#Assign coeffiencts
A[0,0] = (-Qa-E13)
A[0, 2] = -E13
B[0, 0] = -Wsmoker - Qa*ca
A[1, 1] = -Qc - E24
A[1, 3] = Qa - Qd + E24
B[1, 0] = -Qb*cb
A[2, 0] = Qa+E13
A[2, 2] = E13 + E34 + Qa
A[2, 3] = E34
B[2, 0] = -Wgrill
A[3, 1] = E24
A[3, 2] = E34 + Qa
A[3, 3] = -Qa - E34 - E24

print(A)
print(B)

c = np.linalg.solve(A, B)
print(c)