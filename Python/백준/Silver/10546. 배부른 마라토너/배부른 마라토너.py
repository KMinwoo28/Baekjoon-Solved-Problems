import sys
input = sys.stdin.readline
N = int(input())
lst = {}
for _ in range(N):
    name = input().rstrip()
    if name in lst:
        lst[name] += 1
    else:
        lst[name] = 1
for _ in range(N-1):
    fin = input().rstrip()
    if lst[fin] >= 2:
        lst[fin] -= 1
    else:
        lst.pop(fin)
print(*lst.keys())