import sys
input = sys.stdin.readline
N = int(input())
place = [i for i in range(1,N+1)]
est = []
for _ in range(N):
    est.append(int(input()))
est.sort()
complain = 0 
for i in range(N):
    complain += abs(est[i]-place[i])
print(complain)  