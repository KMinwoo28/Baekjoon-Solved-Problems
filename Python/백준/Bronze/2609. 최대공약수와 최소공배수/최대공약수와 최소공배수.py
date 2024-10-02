a, b = map(int,input().split())
aa, bb = max(a,b), min(a,b)
while(bb!= 0):
    aa, bb = bb, aa%bb
print(aa)
print(a*b//aa)