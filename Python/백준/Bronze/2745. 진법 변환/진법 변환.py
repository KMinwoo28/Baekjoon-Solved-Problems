LOC = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
val = [i for i in range(len(LOC))]
N , B = input().split()
N = list(N)
res = 0
for i in range(len(N)):
    res += val[LOC.index(N[i])]*(int(B)**(len(N)-i-1))
print(res)