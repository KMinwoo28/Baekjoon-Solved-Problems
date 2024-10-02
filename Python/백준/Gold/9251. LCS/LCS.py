import sys
input = sys.stdin.readline
def LCS(X,Y):
    m = len(X)
    n = len(Y)
    dp = [[None]*(n+1) for i in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

arr1 = input().rstrip()
arr2 = input().rstrip()
print(LCS(arr1,arr2))