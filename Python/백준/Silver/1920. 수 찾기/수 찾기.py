import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int,input().split()))
M = int(input())
finding = list(map(int,input().split()))
numdict = {}
for n in nums:
    numdict[n] = 0
for m in finding:
    if m in numdict:
        print(1)
    else:
        print(0)