import sys
input = sys.stdin.readline

N, K = map(int,input().split())
numlist = [i for i in range(2,N+1)]
count = 0
while numlist:
    P = numlist[0]
    del numlist[0]
    count += 1
    if count == K:
        print(P)
        break
    mul = 2
    while P*mul <= max(numlist):
        if P*mul in numlist:
            numlist.remove(P*mul)
            count += 1
        if count == K:
            print(P*mul)
            sys.exit()
        mul += 1