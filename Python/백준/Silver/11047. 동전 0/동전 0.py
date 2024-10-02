N, K = map(int,input().split())
clist = []
for _ in range(N):
    clist.append(int(input()))
cList = clist[::-1]
coincount = 0
for i in range(N):
    coincount += K // cList[i]
    K = K % cList[i]
print(coincount)