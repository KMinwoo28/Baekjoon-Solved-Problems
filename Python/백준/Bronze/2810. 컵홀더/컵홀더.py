import sys
input = sys.stdin.readline
N = int(input())
seat = input().rstrip()
count = seat.count('LL')
if count <= 1:
    print(N)
else:
    print(N - count + 1)