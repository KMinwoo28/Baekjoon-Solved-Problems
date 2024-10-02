import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    wearlst = {}
    for _ in range(N):
        wear = list(input().rstrip().split())
        if wear[1] in wearlst:
            wearlst[wear[1]] += 1
        else:
            wearlst[wear[1]] = 2
    days = 1
    for s in wearlst.values():
        days *= s
    print(days - 1) #알몸상태 제외