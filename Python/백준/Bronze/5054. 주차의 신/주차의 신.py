T = int(input())
for _ in range(T):
    N = int(input())
    loc = sorted(list(map(int,input().split())))
    dis = 0
    for i in range(N):
        dis += abs(loc[i-1] - loc[i])
    print(dis)