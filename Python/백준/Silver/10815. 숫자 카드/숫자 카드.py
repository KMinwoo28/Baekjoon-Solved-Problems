import sys
input = sys.stdin.readline
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))
D = {i:0 for i in cards}
for c in checks:
    if c not in D:
        print(0, end=' ')
    else:
        print(1, end=' ')