N = int(input())
dp = [0] * 21 # 그 해에 남아있는 벌레의 수
dp[0] = 1
dp[1] = 1
for i in range(2, 21):
    dp[i] = dp[i-1] * 2
    if i % 2 == 0:
        dp[i] -= dp[i-4] + dp[i-5]
print(dp[N])