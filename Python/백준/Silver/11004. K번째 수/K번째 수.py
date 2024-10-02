import sys
input = sys.stdin.readline
N, K = map(int,input().split())
numdic = {}
for i,k in enumerate(list(map(int,input().split()))):
    numdic[i] = k
res = sorted(numdic.items(),key = lambda x:x[1])
print(res[K-1][1])