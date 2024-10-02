import sys
input = sys.stdin.readline
N, K = map(int,input().split())
nation = []
for i in range(N):
    nation.append(list(map(int,input().split())))
res = sorted(nation, key = lambda x:(-x[1],-x[2],-x[3]))
idx = [res[i][0] for i in range(N)].index(K)
for i in range(N):
    if res[idx][1:] == res[i][1:]:
        print(i+1)
        break