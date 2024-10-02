import sys
input = sys.stdin.readline
i = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        if N % 2 == 1:
            print(f'{i}. odd {N//2}')
        else:
            print(f'{i}. even {N//2}')
    i += 1