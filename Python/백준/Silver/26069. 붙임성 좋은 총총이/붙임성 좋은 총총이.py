import sys
input = sys.stdin.readline
dance = {}
dp = 1
N = int(input())
for _ in range(N):
    meet = list(map(str,input().rstrip().split()))
    if 'ChongChong' in meet:
        s = meet.index('ChongChong')
        if meet[1-s] not in dance:
            dance[meet[1-s]] = 0
            dp += 1
    else:
        if meet[0] in dance:
            if meet[1] not in dance:
                dance[meet[1]] = 0
                dp += 1
        elif meet[1] in dance:
            if meet[0] not in dance:
                dance[meet[0]] = 0
                dp += 1
print(dp)