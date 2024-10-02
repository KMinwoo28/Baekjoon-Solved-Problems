import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * N
dp[0] = float(input())
for i in range(1, N):
    tmp = float(input())
    if tmp < dp[i-1] *tmp:
        dp[i] = dp[i-1]* tmp
    else:
        dp[i] = tmp
print('%.3f'  %max(dp))    