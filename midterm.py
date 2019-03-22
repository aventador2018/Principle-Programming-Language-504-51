# Given a Turing machine, find the output string produced by a given input string

import threading
from queue import Queue

input = ['BB010110BB', 'BB010000BB', 'BB000110BB']

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

q = Queue()

for element in input:
    q.put(element)

def threader():
    while True:
        element = q.get()
        turing(element)
        q.task_done()

for x in range(3):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

q.join()