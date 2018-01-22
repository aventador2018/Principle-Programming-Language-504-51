def read_stars(filename):
    infile = open(filename, 'r')
    data = infile.readlines()[1:]
    stars = {}
    for line in data:
        words = line.split()
        stars[' '.join(words[:-3])] = float(words[-1])
    infile.close()
    return stars

print read_stars('stars.dat')