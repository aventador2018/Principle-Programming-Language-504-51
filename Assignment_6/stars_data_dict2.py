def read_stars(filename):
    infile = open(filename, 'r')
    data = infile.readlines()[1:]
    stars = {}
    for line in data:
        words = line.split()
        stars[' '.join(words[:-3])] = {
            'Distance (light-years)': words[-3],
            'Apparent Brightness': words[-2],
            'Luminosity': float(words[-1])
        }
    infile.close()
    return stars

print read_stars('stars.dat')