T = int(input())
for _ in range(T):
    car = int(input())
    n = int(input())
    for i in range(n):
        a, b = map(int,input().split())
        car += a*b
    print(car)