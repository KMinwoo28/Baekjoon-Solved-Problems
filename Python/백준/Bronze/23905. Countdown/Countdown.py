import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N, K = map(int,input().split())
    numarray = list(map(int,input().split()))
    count = 0
    i = 0
    down = 0
    while i < N:
        if numarray[i] == K - down:
            if numarray[i] == 1:
                count += 1
                down = 0
            else:
                down += 1
        else:
            down = 0
            if numarray[i] == K:
                continue
        i += 1
    print(f"Case #{t+1}: {count}")