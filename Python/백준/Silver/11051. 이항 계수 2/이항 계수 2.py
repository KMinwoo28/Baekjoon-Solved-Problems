import sys
input = sys.stdin.readline
def fact(num):
    res = 1
    for i in range(num,0,-1):
        res *= i
    return res

N, K = map(int,input().split())
cal = fact(N)//(fact(N-K)*fact(K))
print(cal % 10007)