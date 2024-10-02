import sys
input = sys.stdin.readline
A, B = map(list,input().split())
res = 0
newB = []
for b in B:
    newB.append(int(b))
for i in range(len(A)):
    res += int(A[i])*sum(newB)
print(res)