import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp1, dp2 = [1]*N, [1]*N # Ascending & Descending
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dp1[i] = dp1[i-1] + 1
    if arr[i] >= arr[i-1]:
        dp2[i] = dp2[i-1] + 1 
print(max(max(dp1), max(dp2)))