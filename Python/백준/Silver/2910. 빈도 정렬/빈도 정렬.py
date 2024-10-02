import sys
input = sys.stdin.readline
N, C = map(int,input().split())
msg = list(map(int,input().split()))
freq = {}
Imfast = 0
for s in msg:
    if s in freq:
        freq[s][0] += 1
    else:
        freq[s] = [1 ,Imfast]
        Imfast += 1
res = sorted(freq.items(),key = lambda x:(-x[1][0],x[1][1]))
for r in res:
    for i in range(r[1][0]) :
        print(r[0], end = ' ') 