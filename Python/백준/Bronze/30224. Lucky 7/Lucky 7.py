import sys
input = sys.stdin.readline
N = int(input())
if '7' not in str(N):
    print(0) if N % 7 != 0 else print(1)
else:
    print(2) if N % 7 != 0 else print(3)