print "Exercise 2.1. Make a Fahreheit-Celsius conversion table"
F = 0
while F<=100:
    C = 5*(F-32)/9.0
    print "%d %.3f" %(F, C)
    F = F+10
print ""

print "Exercise 2.2. Write an approximate Fahrenheit-Celsius conversion table."
F = 0
while F<=100:
    C = 5*(F-32)/9.0
    C1 = (F-30)/2.0
    print "%d %.3f %.3f" %(F, C, C1)
    F = F+10
print ""

print "Exercise 2.3. Generate odd numbers."
n = 10
i = 0
while i<=n:
    if i%2 == 1:
        print i
    i = i+1
print ""

print "Exercise 2.4. Store odd numbers in a list."
n = 10
i = 0
lista = []
while i<=n:
    if i%2 == 1:
        lista.append(i)
    i = i+1
print lista

print "Exercise 2.5. Generate odd numbers by a list comprehension."
n = 11
print [i for i in range(n+1) if i%2==1]
print ""

print "Exercise 2.6. Make a table of function values."
v0 = 1
g = 9.81
n = 11
t = 0
while t<=2*v0/g:
    y = v0*t-0.5*g*t**2
    print "%.3f %.3f" %(t, y)
    t = t+2*v0/g/11
print ""

print "Exercise 2.7. Store numbers in lists."
v0 = 1
g = 9.81
n = 11
t = 0
listt = []
listy = []
while t<=2*v0/g:
    listt.append('{:0.3f}'.format(t))
    listy.append('{:0.3f}'.format(v0*t-0.5*g*t**2))
    t = t+2*v0/g/11
print zip(listt,listy)
print ""

print "Exercise 2.8. Work with a list."
a = [2, 3, 5, 7, 11, 13]
print "Old list:"
for e in a:
    print e
p = 17
a.append(p)
print "New list:"
for e in a:
    print e
print ""

print "Exercise 2.9. Simulate operations on lists by hand."
a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c
b[0] = -1
d = [e+1 for e in a]
print d
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-3:]
print "c = a+b = [1, 3, 5, 7, 11, 13, 17]"
print "d = [1+1, 3+1, 5+1, 7+1, 11+1]"
print "b[0] = -1, so 0 is appended to [1+1, 3+1, 5+1, 7+1, 11+1], b[-1] = 17, so 18 is appended to [1+1, 3+1, 5+1, 7+1, 11+1, 0]"
print "d[-2:] = [0, 18]"
print ""

print "Exercise 2.10. Generate equally spaced coordinates."
coordinates = []
x = 0
h = 0.01
i = 0
while i <= 100:
    x = 1 + i*h
    coordinates.append('{:0.2f}'.format(x))
    i = i + 1
print coordinates
print ""

print "Exercise 2.11. Use a list comprehension to solve Exer. 2.10."
x = 0
h = 0.01
i = 0
print ['{:0.2f}'.format(1 + i*h) for i in range(100)]
print ""

print "Exercise 2.12. Compute a mathematical sum."
print "The program has an infinite loop. K should increase each time. 1 should be 1.0."
s = 0; k = 1; M = 100
while k < M:
    s += 1.0/k
    k = k + 1
print s
print ""

print "Exercise 2.13. Use a for loop in Exer. 2.12."
s = 0; M = 100
for k in range(1, 100):
    s += 1.0 / k
print s
print ""

print "Exercise 2.21. Store data in lists in Exercise 2.2."
f = 0
F = []
C = []
C_approx = []
while f<=100:
    c = 5*(f-32)/9.0
    c1 = (f-30)/2.0
    F.append(f)
    C.append(float('{:0.3f}'.format(c)))
    C_approx.append(c1)
    f = f+10
newlist = [F, C, C_approx]
for i in range(len(F)):
    print "%d %.3f %d" %(F[i], C[i], C_approx[i])

print "Exercise 2.27. Explore what zero can be on a computer."
eps = 1.0
while 1.0 != 1.0 + eps:
    print '...............', eps
    eps = eps/2.0
print 'final eps:', eps
print "The first line assigns 1.0 to variable eps"
print "The loop first determines whether 1.0 is equal to 1.0 + eps. If not, the loop will be executed. It will print out ............... eps and then let eps devide by 2.0"
print "The loop will keep going until eps is small enough that 1.0 = 1.0 + eps"
print "The last line prints out the final eps value"
print "1.0 in python is not always 1, there could be some numbers after the point. For example: 1.00000000000000000003. So If eps is small enough, 1.0 = 1.0 + eps could be true."
print ""
print "I would say, this is not caused by python. This is the nature of computer."