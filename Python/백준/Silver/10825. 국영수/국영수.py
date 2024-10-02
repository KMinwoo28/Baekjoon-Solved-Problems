import sys
input = sys.stdin.readline
N = int(input())
student = []
for _ in range(N):
    student.append(list(input().split()))
res = sorted(student, key = lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for s in res:
    print(s[0])