import sys
input = sys.stdin.readline
while True:
    tri = list(map(int,input().split()))
    if tri.count(0) == 3:
        break
    else:
        copied = tri[::]
        copied.remove(max(tri))
        if  max(tri) >= sum(copied):
            print('Invalid')
        elif len(list(set(tri))) == 1:
            print('Equilateral')
        elif len(list(set(tri))) == 2:
            print('Isosceles')
        else:
            print('Scalene')