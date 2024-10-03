import sys
input = sys.stdin.readline
N, L = map(int,input().split())
fruit = list(map(int,input().split()))
fruit.sort()
for h in fruit:
    if L >= h:
        L += 1
    else:
        break
print(L)