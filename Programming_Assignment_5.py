# Given a Turing machine, find the output string produced by a given input string

import time

input = 'BB010110BB'

def turing(str):
    str = list(str)
    state = 0
    i = 2
    while (i < 10):
        if state == 0:
            if str[i] == '0':
                i = i + 1
                continue
            elif str[i] == '1':
                state = 1
                i = i + 1
                continue
            else:
                state = 3
                i = i + 1
                break
        elif state == 1:
            if str[i] == '0':
                state = 0
                i = i + 1
                continue
            elif str[i] == '1':
                state = 2
                str[i] = '0'
                i = i - 1
                continue
            else:
                state = 3
                i = i + 1
                break
        elif state == 2:
            if str[i] == '1':
                state = 3
                str[i] = '0'
                i = i + 1
                break
            else:
                break
    str = "".join(str)
    print(str)

start = time.time()

turing(input)

print('Entire job took:', format(time.time() - start, '0.10f'))