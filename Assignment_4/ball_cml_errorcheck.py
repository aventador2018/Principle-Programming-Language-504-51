import sys

g = 9.81
t = float(sys.argv[1])
v0 = float(sys.argv[2])
if t < 0 or t > 2*v0/g:
    print 'The parameter t you entered is invalid.'
    sys.exit(1)
y = v0*t - 0.5*g*t**2
print y