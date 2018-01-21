def read_densities(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        densities[line[:11].rstrip()] = float(line[12:].rstrip())
    infile.close()
    return densities

densities = read_densities('densities.dat')
print densities