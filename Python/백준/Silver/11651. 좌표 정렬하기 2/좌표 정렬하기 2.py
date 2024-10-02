import sys
input = sys.stdin.readline
N = int(input())
points = {i:list(map(int,input().split())) for i in range(N)}
res = sorted(points.values(), key = lambda x:(x[1],x[0]))
for r in res:
    print(*r)