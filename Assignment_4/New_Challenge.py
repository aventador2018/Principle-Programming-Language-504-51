w = raw_input('Please input the word you want to count:')
i = 0
t = 0

infile = open('New_Challenge.txt', 'r')
lines = infile.readline()
file = lines.split()
for a in file:
    if a == w:
        i = i + 1
    t = t + 1
print w, i
print 'Total', t
infile.close()