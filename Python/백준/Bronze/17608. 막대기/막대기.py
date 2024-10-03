import sys
input = sys.stdin.readline
N = int(input())
stack = [int(input()) for _ in range(N)]
highest = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > highest:
        count += 1
        highest = stack[i]
print(count)