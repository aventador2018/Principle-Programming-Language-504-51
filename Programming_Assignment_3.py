# Given the state tables off  non-deterministic-finite-state automaton and a string, decide whether the string is
# recognized by the automaton.

def nond(str):
    result = ''
    if str.find('1') == -1:
        result = 'Accepted'
    elif (str[-2:] == '01' or str[-2:] == '11') and str[:-2].find('1') == -1:
        result = 'Accepted'
    else:
        result = 'Rejected'
    print(result)

nond('0000')
nond('0110')
nond('0001')
nond('1010101')
nond('010101011')