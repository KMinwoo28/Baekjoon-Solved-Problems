import sys
input = sys.stdin.readline
from collections import deque
D = deque()
N = int(input())
for _ in range(N):
    order = list(input().rstrip().split())
    if order[0] == '1':
        D.appendleft(order[1])
    elif order[0] == '2':
        D.append(order[1])
    elif order[0] == '3':
        print(D.popleft() if len(D) != 0 else -1)
    elif order[0] == '4':
        print(D.pop() if len(D) != 0 else -1)
    elif order[0] == '5':
        print(len(D))
    elif order[0] == '6':
        print(1 if len(D) == 0 else 0)
    elif order[0] == '7': 
        print(D[0] if len(D) != 0 else -1)
    elif order[0] == '8':
        print(D[-1] if len(D) != 0 else -1)