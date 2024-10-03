import sys
input = sys.stdin.readline
total = int(input())
N = int(input())
sum = 0
for i in range(N):
    a, b = map(int,input().split())
    sum += a*b
print('Yes') if total == sum else print('No')