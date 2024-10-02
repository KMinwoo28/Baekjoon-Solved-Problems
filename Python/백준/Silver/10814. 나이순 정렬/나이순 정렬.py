import sys
input = sys.stdin.readline
N = int(input())
members = {i:list(input().rstrip().split()) for i in range(N)}
res = sorted(members.items(),key = lambda x:(int(x[1][0]),x[0]))
for s in res:
    print(*s[1])