# Using Deque
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
Q = deque()
for _ in range(T):
    com = input().rstrip()
    if com.split()[0] == 'push':
        Q.append(int(com.split()[1]))
    elif com.split()[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif com.split()[0] == 'size':
        print(len(Q))
    elif com.split()[0] == 'empty':
        print(1 if len(Q) == 0 else 0)
    elif com.split()[0] == 'front':
        print(-1 if len(Q) == 0 else Q[0])
    elif com.split()[0] == 'back':
        print(-1 if len(Q) == 0 else Q[-1])