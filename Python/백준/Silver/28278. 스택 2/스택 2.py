import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    order = list(map(int,input().split()))
    if order[0] == 1:
        stack.append(order[1])
    elif order[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif order[0] == 3:
        print(len(stack))
    elif order[0] == 4:
        print(1) if len(stack) == 0 else print(0)
    elif order[0] == 5:
        print(stack[-1]) if len(stack) != 0 else print(-1)