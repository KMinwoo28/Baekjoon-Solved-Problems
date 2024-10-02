import re
T = int(input())
cond = re.compile('[ABCDEF]?A+F+C+[ABCDEF]?$')
for _ in range(T):
    code = input()
    if cond.match(code):
        print('Infected!')
    else:
        print('Good')