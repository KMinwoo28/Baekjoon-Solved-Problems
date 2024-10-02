import sys
input = sys.stdin.readline
N = int(input())
av = {}
for _ in range(N):
    name, InOut = input().rstrip().split()
    if InOut == 'enter':
        av[name] = True
    elif InOut == 'leave':
        av.pop(name)
res = sorted(av.keys(),reverse = True)
for r in res:
    print(r)