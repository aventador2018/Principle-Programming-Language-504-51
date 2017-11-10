print "Exercise 1.1. Compute 1+1."
i = 1
j = 1

print i+j

print "Exercise 1.2. Write a Hello, World! program."
print "Hello, World!"

print "Exercise 1.3. Derive and compute a formula."
year = 10.0**9/(365*24*60*60)
print "%.1f years" %(year)

print "Exercise 1.4. Convert from meters to British length units."
meter = 640
inch = meter*100/2.54
foot = inch/12
yard = foot/3
mile = yard/1760

print "%.2f inches, %.2f feet, %.2f yards, %.4f miles" %(inch, foot, yard, mile)

print "Exercise 1.5. Compute the mass of various substances."
print 1000*7.8 #mass of iron
print 1000*0.0012 #mass of air
print 1000*0.67 #mass of gas
print 1000*0.9 #mass of ice
print 1000*1.03 #mass of the human body
print 1000*10.5 #mass of the human silver
print 1000*21.4 #mass of the human platinum


print "Exercise 1.6. Compute the growth of money in a bank."
print 1000*(1+0.05)**3

print "Exercise 1.7. Find error(s) in a program."
print "; is extra. The code did not import math package. I have corrected the code and the result is as follow:"
import math
x=1
print "sin(%g)=%g" %(x, math.sin(x))

print "Exercise 1.8. Type in program text."
from math import pi
h = 5.0 # height
b = 2.0 # base
r = 1.5 # radius
area_parallelogram = h*b
print 'The area of the parallelogram is %.3f' % area_parallelogram
area_square = b**2
print 'The area of the square is %g' % area_square
area_circle = pi*r**2
print 'The area of the circle is %.3f' % area_circle
volume_cone = 1.0/3*pi*r**2*h
print 'The volume of the cone is %.3f' % volume_cone

print "Exercise 1.9. Type in programs and debug them."
print "(a)Does sin2(x) + cos2(x) = 1?"
from math import sin, cos, pi
x = pi/4
val = sin(x)**2 + cos(x)**2
print val
print "(b)Work with the expressions for movement with constant acceleration:"
v0 = 3 #m/s
t = 1 #s
a = 2 #m/s**2
s = v0*t + 0.5*a*t**2
print s
print "(c)Verify these equations:"
a = 3.3
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a**2 + 2*a*b + b**2
eq2_sum = a**2 - 2*a*b + b**2
eq1_pow = (a + b)**2
eq2_pow = (a - b)**2
print 'First equation: %g = %g' %(eq1_sum, eq1_pow)
print 'Second equation: %g = %g' %(eq2_pow, eq2_pow)

print "Exercise 1.15. Find errors in the coding of formulas."
print "Since the value in the brakets has the highest computation priority, we need to make sure that that value is a float. So the following are correct answers:"
print "C = 21.0; F = 9.*(C/5.0) + 32; print F"
print "C = 21.0; F = 9.0*C/5.0 + 32; print F"
print "C = 21; F = (1./5)*9*C + 32; print F"

print "Exercise 1.16. Explain why a program does not work."
print "When C is calculated, A and B have not been initialized yet."