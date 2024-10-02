import sys
import re
T = int(input())
cond = re.compile(r'(100+1+|01)+$')
for _ in range(T):
    code = sys.stdin.readline().rstrip()
    if cond.match(code):
        print('YES')
    else:
        print('NO')