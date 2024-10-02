from math import ceil
N = int(input())
first = ceil(N/2)
last = (N//2)
for i in range(1,N+1):
    print(('* '*first).rstrip())
    print(' *'*last)