import sys
input = sys.stdin.readline
angle = [int(input()) for i in range(3)]
if sum(angle) != 180:
    print('Error')
else:
    if angle.count(60) == 3:
        print('Equilateral')
    elif len(set(angle)) == 2:
        print('Isosceles')
    else:
        print('Scalene')