import sys
input = sys.stdin.readline
N = int(input())
line = list(map(int,input().split()))
stack = []
received = 1
while line:
    if line[0] == received:
        line.pop(0)
        received += 1
    else:
        stack.append(line.pop(0))
    while stack:
        if stack[-1] == received:
            stack.pop()
            received += 1
        else:
            break
print('Nice' if not stack else 'Sad')