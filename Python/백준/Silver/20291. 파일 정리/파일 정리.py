import sys
input = sys.stdin.readline
flist = {}
N = int(input())
for _ in range(N):
    file, extension = map(str,input().rstrip().split('.'))
    if extension in flist:
        flist[extension] += 1
    else:
        flist[extension] = 1
res = sorted(flist.items())
for s in res:
    print(*s)  