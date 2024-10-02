n, o = map(int,input().split())
yak = []
for i in range(1,n+1):
    if n % i == 0:
        yak.append(i)
if len(yak)<o:
    print(0)
else:
    print(yak[o-1])
    