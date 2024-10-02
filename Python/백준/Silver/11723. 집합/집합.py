import sys
input = sys.stdin.readline

S = set()
M = int(input())
for _ in range(M):
    req = input().strip().split()
    if len(req) == 1:
        if req[0] == 'all':
            S = set(i for i in range(1,21))
        else:
            S = set()
    else:
        order, value = req[0], req[1]
        value = int(value)
        if order == 'add':
            S.add(value)
        elif order == 'remove':
            S.discard(value)
        elif order == 'check':
            print(1 if value in S else 0)
        elif order == 'toggle':
            S.discard(value) if value in S else S.add(value)