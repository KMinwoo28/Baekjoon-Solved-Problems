a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
cor = False
for i in range(n0, 101):
    if a1*i + a0 <= c* i:
        continue
    else:
        break
else:
    cor = True
if cor:
    print(1)
else:
    print(0)