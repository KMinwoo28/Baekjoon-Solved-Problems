import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif order[0] == 'top':
        print(stack[-1]) if len(stack) != 0 else print(-1)