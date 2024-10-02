n = int(input())
for _ in range(n):
    p = int(input())
    alist = []
    for i in range(p):
        c, a = map(str, input().split())
        alist.append([int(c),a])
    print(alist[alist.index(max(alist))][1])
        