import sys
input = sys.stdin.readline
ball = [1,0,0]
M = int(input())
for _ in range(M):
    a, b = map(int,input().split())
    ball[a-1], ball[b-1] = ball[b-1], ball[a-1]
print(ball.index(1) + 1)