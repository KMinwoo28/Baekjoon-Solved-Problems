import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int,input().split()))
    res = 0 # total max value
    maxval = 0
    for i in range(N-1,-1,-1):
        if days[i] > maxval:
            maxval = days[i]
        else:
            res += maxval - days[i]
    print(res)