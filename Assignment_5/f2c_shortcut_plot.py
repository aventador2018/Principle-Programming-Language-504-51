import numpy as np
from matplotlib.pyplot import plot, show, xlabel, ylabel

def simpleC(F):
    C = (F - 30)/2
    return C

def exactC(F):
    C = (F - 30)*5/9
    return C

F = np.linspace(-20, 120, 141)
C1 = simpleC(F)
C2 = exactC(F)

plot(F, C1)
plot(F, C2)
xlabel('time (s)')
ylabel('height (m)')
show()