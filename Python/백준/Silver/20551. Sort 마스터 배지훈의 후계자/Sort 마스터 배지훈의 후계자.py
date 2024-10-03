import sys
input = sys.stdin.readline
M, N = map(int,input().split())
A = [int(input()) for _ in range(M)]
A.sort()
D = {}
for i in range(M):
    if A[i] not in D:
        D[A[i]] = i
for _ in range(N):
    target = int(input())
    if target in D:
        print(D[target])
    else:
        print(-1)