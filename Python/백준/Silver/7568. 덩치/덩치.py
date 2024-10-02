import sys
input = sys.stdin.readline

N = int(input())
thick = [list(map(int,input().split())) for lst in range(N)]
rank = []
for person in thick:
    r = 1
    for s in thick:
        if s[0] > person[0] and s[1] > person[1]:
            r += 1
    rank.append(r)
print(*rank)