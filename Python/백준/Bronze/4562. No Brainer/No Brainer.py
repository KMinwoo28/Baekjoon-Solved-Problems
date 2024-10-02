import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    X, Y = map(int,input().split())
    if X < Y:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')