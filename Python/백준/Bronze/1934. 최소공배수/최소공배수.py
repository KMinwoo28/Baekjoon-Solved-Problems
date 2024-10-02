T = int(input())
#유클리드 호제법 이용
for _ in range(T):
    a, b = map(int, input().split())
    aa, bb = a, b
    while aa%bb != 0:
        aa, bb = bb, aa%bb
    print(a*b//bb)