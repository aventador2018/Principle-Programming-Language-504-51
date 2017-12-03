print "Exercise 3.1. Write a Fahreheit-Celsius conversion function."

def C(F):
    C = 5.0/9*(F-32.0)
    return '{:0.2f}'.format(C)

print C(70)
print ""

print "Exercise 3.2. Write the program in Exer. 2.12 as a function."
def s(M):
    s = 0; k = 1;
    while k < M:
        s += 1.0/k
        k = k + 1
    return s

print s(3)
print ""

print "Exercise 3.6. Write some simple functions."
def hw1():
    return "Hello, World!"

def hw2():
    print "Hello, World!"

def hw3(a, b):
    print a + ',' + b

print hw1()
hw2()
hw3('Hello ', 'World!')
print ""

print "Exercise 3.8. Implement a Gaussian function."
import math
def gauss(x, m=0, s=1):
    y = (1/(math.sqrt(2*math.pi)*s))*math.exp((-1.0/2)*((x-m)/s)**2)
    return y

i = -5
while i <= 5:
    print gauss(i)
    i = i + 0.1
print ""

print "Exercise 3.22. Write a sort function for a list of 4-tuples."
data = [
('Alpha Centauri A', 4.3, 0.26, 1.56),
('Alpha Centauri B', 4.3, 0.077, 0.45),
('Alpha Centauri C', 4.2, 0.00001, 0.00006),
("Barnard's Star", 6.0, 0.00004, 0.0005),
('Wolf 359', 7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
('Sirius A', 8.6, 1.00, 23.6),
('Sirius B', 8.6, 0.001, 0.003),
('Ross 154', 9.4, 0.00002, 0.0005),
]

def mysorta(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        return 0

def mysortb(a, b):
    if a[2] < b[2]:
        return -1
    elif a[2] > b[2]:
        return 1
    else:
        return 0

def mysortc(a, b):
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    else:
        return 0
byDistance = sorted(data, mysorta)
byBrightness = sorted(data, mysortb)
byLuminosity = sorted(data, mysortc)
print "Sort by distance:"
print byDistance
print "Sort by apparent brightness"
print byBrightness
print "Sort by luminosity"
print byLuminosity
print ""
print "star name versus distance:"
for x in byDistance:
    print x[0], x[1]
print ""
print "star name versus apparent brightness:"
for x in byBrightness:
    print x[0], x[2]
print ""
print "star name versus luminosity:"
for x in byLuminosity:
    print x[0], x[3]