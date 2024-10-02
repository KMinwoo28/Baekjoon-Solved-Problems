import sys
input = sys.stdin.readline
while True:
    line = list(map(int,input().split()))
    line.sort()
    if line.count(0) == 3:
        break
    if line[0]**2 + line[1]**2 == line[2]**2:
        print('right')
    else:
        print('wrong')