import sys
input = sys.stdin.readline
def power(base, exp, re):
    if exp == 1:
        return base % re
    if exp == 0:
        return 1
    base2 = power(base, exp//2, re)
    if exp % 2 == 0:
        return ((base2 % re) * (base2 % re)) % re
    else:
        return ((((base2 % re) * (base2 % re)) % re) * (base % re)) % re
A, X, re = map(int,input().split())
print(power(A,X,re))