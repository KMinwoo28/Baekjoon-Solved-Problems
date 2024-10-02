# Another Approach
import sys
input = sys.stdin.readline
N = int(input())
l = input().rstrip().split('*')
f, r = l[0], l[1]
for _ in range(N):
    t = input().rstrip()
    if t[:len(f)] == f and t[-len(r):] == r and len("".join(l)) <= len(t):
        print('DA')
    else:
        print('NE')