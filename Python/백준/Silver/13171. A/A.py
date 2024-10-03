import sys
input = sys.stdin.readline
big = 10**9 + 7
def power(base, exp):
    if exp == 1:
        return base
    if exp == 0:
        return 1
    base2 = power(base, exp//2)
    if exp % 2 == 0:
        return ((base2 % big) * (base2 % big)) % big
    else:
        return ((((base2 % big) * (base2 % big)) % big) * (base % big)) % big
A = int(input())
X = int(input())
print(power(A,X))