a= 100
b= 100
N = int(input())
for _ in range(N):
    die1, die2 = map(int,input().split())
    if die1 < die2:
        a -= die2
    elif die1 > die2:
        b -= die1
print(a)
print(b)