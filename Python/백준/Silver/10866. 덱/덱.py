import sys
input = sys.stdin.readline
from collections import deque

D = deque()
N = int(input())
for _ in range(N):
    order = list(input().rstrip().split())
    if order[0] == 'push_front':
        D.appendleft(order[1])
    elif order[0] == 'push_back':
        D.append(order[1])
    elif order[0] == 'pop_front':
        print(D.popleft() if len(D) != 0 else -1)
    elif order[0] == 'pop_back':
        print(D.pop() if len(D) != 0 else -1)
    elif order[0] == 'size':
        print(len(D))
    elif order[0] == 'empty':
        print(1 if len(D) == 0 else 0)
    elif order[0] == 'front':
        print(D[0] if len(D) != 0 else -1)
    elif order[0] == 'back':
        print(D[-1] if len(D) != 0 else -1)  