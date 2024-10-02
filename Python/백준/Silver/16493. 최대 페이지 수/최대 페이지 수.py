# 0/1 Knapsack Problem
import sys
input = sys.stdin.readline
M, N = map(int,input().split()) # Max Weight, number of items
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
items = []
for _ in range(N):
    items.append(list(map(int,input().split()))) #(weight, benifit)
for i in range(1,N+1):
    for m in range(M+1):
        if items[i-1][0] <= m:
            if items[i-1][1] + dp[i-1][m - items[i-1][0]] >dp[i-1][m]:
                dp[i][m] = items[i-1][1] + dp[i-1][m - items[i-1][0]]
            else:
                dp[i][m] = dp[i-1][m]
        else:
            dp[i][m] = dp[i-1][m]
print(dp[N][M])