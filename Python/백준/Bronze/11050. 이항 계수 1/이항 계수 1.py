import sys
input = sys.stdin.readline
def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)

N, K = map(int, input().split())
print(fact(N)//(fact(N-K)*fact(K)))