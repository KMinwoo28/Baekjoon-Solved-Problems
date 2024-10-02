N = int(input())
dp = [0] * 91
dp[0] = 1 # Starts at 1
dp[1] = 1 # Should be '10'
# 하나씩 해보면, 개수는 피보나치를 따른다.
for i in range(2, N):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[N-1])