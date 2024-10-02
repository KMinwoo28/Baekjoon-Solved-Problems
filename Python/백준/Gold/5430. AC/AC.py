import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    order = list(input())
    N = int(input())
    numlist = deque(input().rstrip()[1:-1].split(','))
    if N == 0:
        numlist = []
    Rcount = 0
    for o in order:
        if o == 'R':
            Rcount += 1
        elif o == 'D':
            if len(numlist) < 1:
                print('error')
                break
            else:
                if Rcount % 2 == 0:
                    numlist.popleft()
                else:
                    numlist.pop()
    else:
        if Rcount % 2 == 1:
            numlist.reverse()
        print('['+','.join(numlist)+']')