import sys
input = sys.stdin.readline
T = int(input())
cord = []
for _ in range(T):
    cord.append(list(map(int,input().split())))
cord = sorted(cord, key = lambda x:(x[0],x[1]))
for s in cord:
    print(*s)