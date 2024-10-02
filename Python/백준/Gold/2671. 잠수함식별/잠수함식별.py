import re
cond = re.compile('(100+1+|01)+$')
signal = input()
if cond.match(signal):
    print('SUBMARINE')
else:
    print('NOISE')