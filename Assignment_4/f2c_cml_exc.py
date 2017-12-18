import sys

try:
    F = float(sys.argv[1])
except:
    print 'You forgot to input a parameter'
    sys.exit(1)
C = 5.0/9*(F-32.0)
print "Celsius: %.2f" %(C)