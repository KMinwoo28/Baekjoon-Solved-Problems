import sys
input = sys.stdin.readline
N, M = map(int,input().split())
Hear = {}
Both = {}
for i in range(N):
    Hear[input().rstrip()] = i
for k in range(M):
    See = input().rstrip()
    if See in Hear:
        Both[See] = k 
Both = sorted(Both.keys())
print(len(Both))
for s in Both:
    print(s)