# top-down approach
import sys
input = sys.stdin.readline
a, b = map(int,input().split())
res = 1
while b != a:
    res += 1
    tmp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    if tmp == b:
        print(-1)
        break
else:
    print(res)