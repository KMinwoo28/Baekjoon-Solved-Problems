import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    one = list(map(int,input().split()))
    note1 = {}
    for i in range(N):
        note1[one[i]] = 0
    M = int(input())
    two = list(map(int,input().split()))
    for s in two:
        if s in note1:
            print(1)
        else:
            print(0)