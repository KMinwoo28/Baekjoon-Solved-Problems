import sys
input = sys.stdin.readline
N, M = map(int,input().split())
points = list(map(int,input().split()))
info = {}
for _ in range(M):
    stat = list(input().rstrip().split())
    info[stat[0]] = 0
    # Grade scores
    for i in range(1,len(stat)):
        if stat[i] == 'O':
            info[stat[0]] += points[i-1]
# Sort by highest points & Need to consider about Ties
result = sorted(info.items(), key = lambda x:(-x[1],int(x[0])))
print(result[0][0], result[0][1])  