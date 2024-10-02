import sys
input = sys.stdin.readline
while(True):
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    else:
        sang = {input():0 for _ in range(N)}
        count = 0
        sun = [input() for _ in range(M)]
        for s in sun:
           if s in sang:
               count += 1
        print(count)