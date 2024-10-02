import sys
input = sys.stdin.readline
T = int(input())
time = list(map(int,input().split()))
time.sort()
duration = []
for i in range(1,T+1):
    duration.append(sum(time[:i]))
print(sum(duration))