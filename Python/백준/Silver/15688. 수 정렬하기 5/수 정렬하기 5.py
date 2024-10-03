import sys
input = sys.stdin.readline
N = int(input())
numlist = [int(input()) for _ in range(N)]
numlist.sort()
for n in numlist:
    print(n)