import sys
input = sys.stdin.readline
L, P = map(int,input().split())
party = L*P
est = list(map(int,input().split()))
for i in range(5):
    est[i] = est[i] - party
print(*est)