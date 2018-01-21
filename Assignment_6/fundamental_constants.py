def readfile():
    constants = {}
    file = []
    infile = open('constants.txt', 'r')
    lines = infile.readlines()[2:]
    for line in lines:
        constants[line[0:26].rstrip()] = line[27:45].rstrip()
    infile.close()

    return constants

print readfile()