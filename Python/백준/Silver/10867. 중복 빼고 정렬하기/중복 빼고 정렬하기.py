import sys
input = sys.stdin.readline
N = int(input())
numlist = list(set(map(int,input().split())))
numlist.sort()
print(*numlist)