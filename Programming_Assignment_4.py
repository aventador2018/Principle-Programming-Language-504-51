# Given a regular expression, construct a non-deterministic-finite-state that recognizes the set that this expression
# represents

# (0U1)(0U1)*00

def nond(str):
    result = ''
    if len(str) == 3 and str[-2:] == '00':
        result = 'Accepted'
    elif len(str) > 3 and str[-2:] == '00' and (str[1:-2].find('0') == -1 or str[1:-2].find('1') == -1):
        result = 'Accepted'
    else:
        result = 'Rejected'
    print(result)

nond('0')
nond('0000')
nond('01100')
nond('0001')
nond('1010100')
nond('010101000')