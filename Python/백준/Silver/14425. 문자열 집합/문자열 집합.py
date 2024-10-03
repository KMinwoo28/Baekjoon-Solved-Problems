import sys
input = sys.stdin.readline
N, M = map(int,input().split())
S = {input().rstrip(): 0 for i in range(N)}
for _ in range(M):
    test = input().rstrip()
    if test in S.keys():
        S[test] += 1
print(sum(S.values()))