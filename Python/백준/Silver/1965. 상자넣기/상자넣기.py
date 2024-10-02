# 11053과 같은 문제.
import sys
input = sys.stdin.readline
n = int(input())
dp = [1]*n
A = list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))