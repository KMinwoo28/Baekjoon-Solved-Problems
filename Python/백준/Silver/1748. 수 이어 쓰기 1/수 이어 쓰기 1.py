from math import log10
N = int(input())
hap = 0
for i in range(int(log10(N))):
    hap += (10**(i+1)-10**i) * (i+1)
hap += (N-10**(int(log10(N)))+1)*(int(log10(N))+1)
print(hap)