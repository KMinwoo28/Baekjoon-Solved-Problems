import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort(reverse = True)
b.sort()
sum = 0
for i in range(N):
    sum += a[i]*b[i]
print(sum)