import sys
input = sys.stdin.readline
fi = [0]*45
fi[0] = fi[1] = 1
for i in range(2,45):
    fi[i] = fi[i-1] +fi[i-2]
T = int(input())
for _ in range(T):
    res = []
    n = int(input())
    for i in range(44, -1, -1):
        if n >= fi[i]:
            n -= fi[i]
            res.append(fi[i])
        if n == 0:
            break
    res.sort()    
    print(*res)