import sys
input = sys.stdin.readline
N, M = map(int,input().split())
sitelist = {}
for _ in range(N):
    site, pw = map(str,input().split())
    sitelist[site] = pw
for _ in range(M):
    print(sitelist[input().rstrip()])
