N = int(input())
remainder = 0
for _ in range(N):
    a, b = map(int,input().split())
    remainder += b % a
print(remainder)